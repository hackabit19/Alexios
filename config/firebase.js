import firebase from 'firebase';

const firebaseConfig = {
    apiKey: "AIzaSyCKKfQqxSFDeyKq_1sD9NJ2E142EEbX59A",
    authDomain: "alexios-4f5ac.firebaseapp.com",
    databaseURL: "https://alexios-4f5ac.firebaseio.com",
    projectId: "alexios-4f5ac",
    storageBucket: "alexios-4f5ac.appspot.com",
    messagingSenderId: "877478050151",
    appId: "1:877478050151:web:6ec822c3b29b66441257c2",
    measurementId: "G-28SRLJ8N3Y"
}

let Firebase = firebase.initializeApp(firebaseConfig);
export default Firebase;