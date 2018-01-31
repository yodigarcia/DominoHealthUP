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
//firebase
//==================================================================
	//Diabetes blood pressure
	var bp_list= [];
	function rbp_list(){
		if(bp_list != null){
			for (var i = 0; i < bp_list.length; i ++ ){
				return bp_list[i]+','
			}	
		}else if(bp_list == null){
			return {x: new Date(0,0,0), y: 0}
		}
	}
	var Diabetes_bp =  firebase.database().ref().child("Diabetes_bp");
	Diabetes_bp.on("child_added", snap => {
		var bp_day = (snap.child("day").val());
		var bp_month = (snap.child("month").val());
		var bp_bp = (snap.child("blood pressure").val());
		var  list_bp_bp = [];
		list_bp_bp.push(bp_bp);
		var list_bp_day = [];
		list_bp_day.push(bp_day);
		var list_bp_month = [];
		list_bp_month.push(bp_month);
		for (var i = 0; i < list_bp_bp.length; i ++ ){
			//   window.console.log(list_bp_bp[i]);
			//   window.console.log(list_bp_day[i]);
			//   window.console.log(list_bp_month[i]);
			  var Blood_Pressure = {
				  x: new Date(2018,list_bp_month[i] , list_bp_day[i]), y: list_bp_bp[i]
				};
			  bp_list.push(Blood_Pressure);
			//   window.console.log(Blood_Pressure);
			};
		});

	//Diabetes blood glucose
	var bg_list= [];
	function rbg_list(){
		if(bg_list != null){
			for (var i = 0; i < bg_list.length; i ++ ){
				return bg_list[i]+','
			}	
		}else if(bg_list == null){
			return {x: new Date(0,0,0), y: 0}
		}
	}
	var Diabetes_bg =  firebase.database().ref().child("Diabetes_bg");
	Diabetes_bg.on("child_added", snap => {
		var bg_day = (snap.child("day").val());
		var bg_month = (snap.child("month").val());
		var bg_bg = (snap.child("blood glucose").val());
		var  list_bg_bg = [];
		list_bg_bg.push(bg_bg);
		var list_bg_day = [];
		list_bg_day.push(bg_day);
		var list_bg_month = [];
		list_bg_month.push(bg_month);
		for (var i = 0; i < list_bg_bg.length; i ++ ){
			  var Blood_Glucose = {
				  x: new Date(2018,list_bg_month[i] , list_bg_day[i]), y: list_bg_bg[i]
				};
			  bg_list.push(Blood_Glucose);
			};
		});
		
	//Diabetes weight
	var weight_list= [];
	function rbg_list(){
		if(weight_list != null){
			for (var i = 0; i < weight_list.length; i ++ ){
				return weight_list[i]+','
			}	
		}else if(weight_list == null){
			return {x: new Date(0,0,0), y: 0}
		}
	}
	var Diabetes_weight =  firebase.database().ref().child("Diabetes_weight");
	Diabetes_weight.on("child_added", snap => {
		var weight_day = (snap.child("day").val());
		var weight_month = (snap.child("month").val());
		var weight = (snap.child("weight").val());
		var  list_weight = [];
		list_weight.push(weight);
		var list_weight_day = [];
		list_weight_day.push(weight_day);
		var list_weight_month = [];
		list_weight_month.push(weight_month);
		for (var i = 0; i < list_weight.length; i ++ ){
			  var Blood_Weight = {
				  x: new Date(2018,list_weight_month[i] , list_weight_day[i]), y: list_weight[i]
				};
			  weight_list.push(Blood_Weight);
			};
		});

// Graph 1
function show_chart() {
	var cip_blood_chart = new CanvasJS.Chart("cip_blood_chart", {
		animationEnabled: true,
	theme: "light2",
	axisY:{
		includeZero: false
	},
	data: [{
		type: "spline",
		dataPoints: bp_list
	}]
});
// Graph 2
var cip_blood_glucose_chart = new CanvasJS.Chart("cip_blood_glucose_chart", {
	animationEnabled: true,
	theme: "light2",
	axisY:{
		includeZero: false
	},
	data: [{
		type: "spline",
		dataPoints:	bg_list
	}]
});
// Graaph 3
var cip_weight_chart = new CanvasJS.Chart("cip_weight_chart", {
	animationEnabled: true,
	theme: "light2",
	axisY:{
		includeZero: false
	},
	data: [{
		type: "spline",
		dataPoints: weight_list
	}]
});
cip_blood_chart.render();
cip_blood_glucose_chart.render();
cip_weight_chart.render();
}