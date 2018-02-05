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
function round(value, decimals) {
	return Number(Math.round(value+'e'+decimals)+'e-'+decimals);
}
//==================================================================
	//Diabetes blood pressure
	var bp_list_sys= [];
	var bp_list_dia= [];
	function sbp_list(){
		if(bp_list_sys != null){
			for (var i = 0; i < bp_list_sys.length; i ++ ){
				return bp_list_sys[i]+',';
			}	
		}else if(bp_list == null){
			return {x: new Date(0,0,0), y: 0}
		};
	};
	function dbp_list(){
		if(bp_list_dia != null){
			for (var i = 0; i < bp_list_dia.length; i ++ ){
				return bp_list_dia[i]+','
			}	
		}else if(bp_list == null){
			return {x: new Date(0,0,0), y: 0}
		};
	};
	var Diabetes_bp =  firebase.database().ref().child("Diabetes_bp");
	Diabetes_bp.on("child_added", snap => {
		var bp_day = (snap.child("day").val());
		var bp_month = (snap.child("month").val());
		var bp_sys = (snap.child("systolic").val());
		var bp_dia = (snap.child("diastolic").val());
		var  list_bp_sys = [];
		list_bp_sys.push(bp_sys);
		var  list_bp_dia = [];
		list_bp_dia.push(bp_dia);
		var list_bp_day = [];
		list_bp_day.push(bp_day);
		var list_bp_month = [];
		list_bp_month.push(bp_month);
		// bp_list_sys.push('xValueFormatString: "Year ####",');
		// bp_list_dia.push('xValueFormatString: "Year ####",');
		for (var i = 0; i < list_bp_sys.length; i ++ ){
				var systolic = {
				x: new Date(2018,list_bp_month[i] , list_bp_day[i]), y: list_bp_sys[i]
				};
			bp_list_sys.push(systolic);
		};
		for (var i = 0; i < list_bp_dia.length; i ++ ){
			var diastolic = {
			x: new Date(2018,list_bp_month[i] , list_bp_day[i]), y: list_bp_dia[i]
			};
		bp_list_dia.push(diastolic);
	};
	});

	//Diabetes blood glucose
	var bg_list= [];
	function rbg_list(){
		if(bg_list != null){
			for (var i = 0; i < bg_list.length; i ++ ){
				return bg_list[i]+','
			};
		}else if(bg_list == null){
			return {x: new Date(0,0,0), y: 0};
		};
	};
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
		
	//Diabetes bmi
	var bmi_list= [];
	function rbg_list(){
		if(bmi_list != null){
			for (var i = 0; i < bmi_list.length; i ++ ){
				return bmi_list[i]+','
			}	
		}else if(bmi_list == null){
			return {x: new Date(0,0,0), y: 0}
		};
	};
	var Diabetes_bmi =  firebase.database().ref().child("Diabetes_bmi");
	Diabetes_bmi.on("child_added", snap => {
		var bmi_day = (snap.child("day").val());
		var bmi_month = (snap.child("month").val());
		var bmi = (snap.child("bmi").val());
		var  list_bmi = [];
		list_bmi.push(bmi);
		var list_bmi_day = [];
		list_bmi_day.push(bmi_day);
		var list_bmi_month = [];
		list_bmi_month.push(bmi_month);	
		for (var i = 0; i < list_bmi.length; i ++ ){
			  var Blood_bmi = {
				  x: new Date(2018,list_bmi_month[i] , list_bmi_day[i]), y: list_bmi[i]
				};
			  bmi_list.push(Blood_bmi);
			};
		});

// Graph 1
function show_chart() {
	var cip_blood_chart = new CanvasJS.Chart("cip_blood_chart", {
	animationEnabled: true,
	theme: "light2",
	axisY:{
		includeZero: false,
	},
	axisX:{
		valueFormatString:  "D MMM",
		gridColor: "Silver",
	},
	legend:{
		cursor:"pointer",
		verticalAlign: "bottom",
		dockInsidePlotArea: true,
	},
	toolTip:{
		shared:true,
		borderColor: "black",
		contentFormatter: function (e) {
			var content = " ";
			var systolic_val = " ";
			var diastolic_val = " ";
			for (var i = 0; i < e.entries.length; i++) {
				if(i ==0){
					content += "<span style='color:blue;'>"+  e.entries[i].dataSeries.name + " " + "<strong>" + e.entries[i].dataPoint.y + "</strong></span><br>";
					systolic_val = e.entries[i].dataPoint.y ;
				}if(i == 1){
					content += e.entries[i].dataSeries.name + " " + "<strong>" + e.entries[i].dataPoint.y + "</strong><br>";
					diastolic_val = e.entries[i].dataPoint.y;
					if(systolic_val >= 140 && diastolic_val < 90){
						content += "<span class='bp_graph_red'> Isolated Systolic Hypertension </span>";
					}else if(systolic_val < 90 || diastolic_val <= 60){
						content += "<span class='bp_graph_blue'> Low Blood Pressure </span>";
					}else if(systolic_val <= 130 && diastolic_val <= 80){
						content += "<span class='bp_graph_green'> Ideal Blood Pressure </span>";
					}else if(systolic_val <= 140 && diastolic_val <= 90){
						content += "<span class='bp_graph_yellow'> Pre-High Blood Pressure </span>";
					}else if(systolic_val <= 159 && diastolic_val <= 99){
						content += "<span class='bp_graph_red'> Grade 1 Hypertension </span>";
					}else if(systolic_val > 159 || diastolic_val > 99){
						content += "<span class='bp_graph_red'> Grade 2 Hypertension </span>";
					}else{
						content += "<span class='bp_graph_red'> See a Doctor Now </span>";
					}
				}
			}
			return content;
		}
	},  
	data: [{
		type: "spline",
		showInLegend: true,
		color: "blue",
		name: "Systolic",
		dataPoints: bp_list_sys
	},{
		type: "spline",
		showInLegend: true,
		color: "black",
		name: "Diastolic",
		dataPoints: bp_list_dia
}]
});
// Graph 2
var cip_blood_glucose_chart = new CanvasJS.Chart("cip_blood_glucose_chart", {
	animationEnabled: true,
	theme: "light2",
	axisY:{
		includeZero: false
	},
	toolTip:{
		shared:true,
		contentFormatter: function (e) {
			var content = '';
			for (var i = 0; i < e.entries.length; i++) {
				content += e.entries[i].dataPoint.y + ' mmol/L <br>';
				y = e.entries[i].dataPoint.y
				if(y>11){
					content += "<span class='bp_graph_red'> Diabetic </span>";
				}else{
					content += "<span class='bp_graph_green'> Normal </span>";
				}
			}
			return content;
		}
	},
	axisY: {
		suffix: "mmol/L",
		stripLines: [{
			startValue:16,
			endValue:11,
			labelAutoFit: true, 
			label: "Diabetes",
			color:'red',
			labelFontColor: "black",
			labelBackgroundColor: "transparent",
			opacity: .1
		},{
			startValue:16,
			endValue:99,
			color: "red",
			opacity: .1
		},{
			startValue:11,
			endValue:0,
			labelAutoFit: true, 
			label: "Normal",
			color:'white',
			labelFontColor: "black",
			labelBackgroundColor: "transparent"
		},
	]
	},
	axisX:{
		valueFormatString: "DD MMM",
	},
	data: [{
		type: "spline",
		dataPoints:	bg_list,
		color: "black",
	}]
});
// Graaph 3
var cip_bmi_chart = new CanvasJS.Chart("cip_bmi_chart", {
	animationEnabled: true,
	theme: "light2",
	axisY:{
		includeZero: false,
		stripLines:[{                
				startValue:25,
				endValue:18.5,
				label:'Normal',
				color:'green',
				labelFontColor: "black",
				labelBackgroundColor: "transparent",
				labelFontFamily: "Open Sans",
				opacity: .1,
				thickness:3
			},{                
				startValue:18.5,
				endValue:1,
				label:'UnderWeight',
				color:'red',
				labelFontColor: "black",
				labelBackgroundColor: "transparent",
				opacity: .1,
				thickness:3
			},{                
				startValue:30,
				endValue:25,
				label:'OverWeight',
				color:'yellow',
				labelFontColor: "black",
				labelBackgroundColor: "transparent",
				opacity: .1,
				thickness:3
			},{                
				startValue:40,
				endValue:30,
				label:'Obese',
				color:'red',
				labelFontColor: "black",
				labelBackgroundColor: "transparent",
				opacity: .1,
				thickness:3
			},{                
				startValue:40,
				endValue:45,
				label:'Clinically Obese',
				color:'black',
				labelFontColor: "black",
				labelBackgroundColor: "transparent",
				opacity: .1,
				thickness:3
			}
		],
	},
	toolTip:{
		shared:true,
		contentFormatter: function (e) {
			var content = '';
			for (var i = 0; i < e.entries.length; i++) {
				var yax = e.entries[i].dataPoint.y
				yax = round(yax, 2)
				content += "BMI:" + yax + '<br>';
				if(yax<18.5){
					content += "<span class='bp_graph_red'> UnderWeight </span>";
				}else if(yax<24.9){
					content += "<span class='bp_graph_green'> Normal </span>";
				}else if(yax<29.9){
					content += "<span class='bp_graph_yellow'> Overweight </span>";
				}else if(yax<39.9){
					content += "<span class='bp_graph_red'> Obese </span>";
				}else{				
				content += "<span class='bp_graph_red'> Clinically Obese </span>";
				}
			}
			return content;
		}
	},
	axisX:{
		valueFormatString: "DD MMM",
	},
	data: [{
		type: "spline",
		dataPoints: bmi_list,
		color: "black",
	}]
});
cip_blood_chart.render();
cip_blood_glucose_chart.render();
cip_bmi_chart.render();
}
