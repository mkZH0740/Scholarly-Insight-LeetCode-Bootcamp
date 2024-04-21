// components/HomePage.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function HomePage() {
    const navigate = useNavigate();
    
    return (
        <div style={{ textAlign: 'center', padding: '50px' }}>
        <h1>Welcome to Scholarly Insight</h1>
        <p>Click the button below to search for articles.</p>
        <button
            onClick={() => navigate('/search')}
            style={{ padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
        >
            Search Articles
        </button>
        <button
            onClick={() => navigate('/forum')}
            style={{ padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
        >
            Forum
        </button>
        </div>
        //add a button to navigate to the forum page
        
    );

}

export default HomePage;
