import React from 'react';
import { auth } from '../../firebaseConfig';

const SignOut = () => {
  return (
    auth.currentUser && (
      <button onClick={() => auth.signOut()}>登出</button>
    )
  );
};

export default SignOut;
