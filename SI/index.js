import {getAuth, signInWithEmailAndPassword ,createUserWithEmailAndPassword} from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js"
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js"

const firebaseConfig = {
    apiKey: "AIzaSyCQP4HDrOEL7fjf7_C__X5g0qfDEU2ECMU",
    authDomain: "scholarly-insight-b75ae.firebaseapp.com",
    projectId: "scholarly-insight-b75ae",
    storageBucket: "scholarly-insight-b75ae.appspot.com",
    messagingSenderId: "72406004118",
    appId: "1:72406004118:web:07a8cee13814b07976adb7",
    measurementId: "G-87HM1N5KXZ"
  };
  
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const database = firebase.database();


function register()  {  // To be called by HTML
    // Add the element IDs    
    email = document.getElementById('email').value;
    password = document.getElementById('password').value;
    name = document.getElementById('name').value;



    createUserWithEmailAndPassword(auth,email,password)
    .then((userCredential)  => {
        const user = userCredential.user;

        var database_ref= database.ref()

        var user_data = {email:email,
                        name:name,
                    last_login:Date.now()}
        database_ref.child('users/' + user.uid).set(user_data);

        alert('User Created')


    }).catch((error) => {
        // Firebase errors
        var error_code = error.code;
        var error_message = error.message;
        alert(error_message);
    });
}


function login(){

    email = document.getElementById('email').value;
    password = document.getElementById('password').value;

    auth.signInWithEmailAndPassword(email,password)
    .then(function(){
        var user = auth.currentUser
        var database_ref= database.ref()

        var user_data = {last_login:Date.now()}
        
        
        database_ref.child('users/' + user.uid).update(user_data)

        alert('User Created')
    }).catch(function(error){
        // Firebase errors
        var error_code = error.code
        var error_message = error.message
        alert(error_message)
    });

}