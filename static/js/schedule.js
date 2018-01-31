// Initialize Firebase
var config = {
	apiKey: "AIzaSyCqk7saUxrniqmu914PiyznojPxVLnikc4",
	authDomain: "dominohealth.firebaseapp.com",
	databaseURL: "https://dominohealth.firebaseio.com",
	projectId: "dominohealth",
	storageBucket: "dominohealth.appspot.com",
	messagingSenderId: "1024600628682"
};
firebase.initializeApp(config);

var patientsdb = firebase.database().ref().child("Patient_Information");
patientsdb.on("child_added", snap => {
    for( i=0; i < patientsdb.length ; i++ ) {
    console.log(patientsdb);
}});
