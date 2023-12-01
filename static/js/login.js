import { initializeApp } from "https://www.gstatic.com/firebasejs/10.5.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.5.2/firebase-analytics.js";


const firebaseConfig = {
    apiKey: "AIzaSyCrdIo19D3-Eg88rxaQXYsGKK16Nx7QHDg",
    authDomain: "carrental-2bd8f.firebaseapp.com",
    projectId: "carrental-2bd8f",
    storageBucket: "carrental-2bd8f.appspot.com",
    messagingSenderId: "915249307434",
    appId: "1:915249307434:web:76ef5838ebe19e01070853",
    measurementId: "G-P957WW9XQS"
};
firebase.initializeApp(firebaseConfig);

function sendOTP() {
    var phoneNumber = document.getElementById('number').value;
    console.log('phonenumbers=====',phoneNumber);
    // Configure application verifier for reCAPTCHA
    var appVerifier = new firebase.auth.RecaptchaVerifier('recaptcha-container');
    firebase.auth().signInWithPhoneNumber(phoneNumber, appVerifier)
        .then(function (confirmationResult) {
            // SMS sent. Prompt user to type the code from the message
            var otp = prompt("Please enter the OTP sent to your phone:");
            if (otp != null) {
                confirmationResult.confirm(otp).then(function (result) {
                    // User signed in successfully.
                    var user = result.user;
                    window.location.href = "/home"; // Redirect to home page
                }).catch(function (error) {
                    // User couldn't sign in (bad verification code?)
                    alert(error.message);
                });
            }
        }).catch(function (error) {
            // Error; SMS not sent
            alert(error.message);
        });
}
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Stop the form from submitting traditionally
        sendOTP(); // Call your sendOTP function
    });
});