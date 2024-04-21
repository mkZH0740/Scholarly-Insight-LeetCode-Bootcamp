import React, { useState } from 'react';
import { auth } from '../../firebaseConfig';
import { useNavigate } from 'react-router-dom'; // Import useNavigate instead of useHistory

const SignUp = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate(); // Create navigate function

  const handleSignUp = async (event) => {
    event.preventDefault();
    setError(null); // Reset error message
    try {
      await auth.createUserWithEmailAndPassword(email, password);
      // Registration successful, navigate to the homepage or show a success message
      navigate('/home'); // Replace '/home' with your home route
    } catch (error) {
      setError(error.message); // Display error message
    }
  };

  return (
    <div>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSignUp}>
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default SignUp;
