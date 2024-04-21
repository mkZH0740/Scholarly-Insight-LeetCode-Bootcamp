// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAnalytics } from 'firebase/analytics';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCRLDN4-YCHn2-c2Mq4nIrx8DcqqCaKEwQ",
    authDomain: "scholarly-insight-f7377.firebaseapp.com",
    projectId: "scholarly-insight-f7377",
    storageBucket: "scholarly-insight-f7377.appspot.com",
    messagingSenderId: "884841530999",
    appId: "1:884841530999:web:c45f4112f2dc21b1d46872",
    measurementId: "G-5L2HY86XLJ"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
const analytics = getAnalytics(app);
const auth = getAuth(app);
const firestore = getFirestore(app);

// Export the services for use in other parts of your application
export { app, analytics, auth, firestore };
