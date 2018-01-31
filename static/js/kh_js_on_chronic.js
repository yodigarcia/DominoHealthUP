//navbar content
var nd = document.getElementById("diabetes_navbar")
var nh = document.getElementById("hypertension_navbar")
//diabetes content
var du = document.getElementById("diabetes_understanding_content");
var dt = document.getElementById("diabetes_treatment_content");
var dm = document.getElementById("diabetes_medication_content");
var de = document.getElementById("diabetes_exercise_content");
var dd = document.getElementById("diabetes_dental_content");
var ds = document.getElementById("diabetes_sexual_content");
var dp = document.getElementById("diabetes_pregnancy_content");
//hypertension content
var hu = document.getElementById("hypertension_understanding_content");
var ht = document.getElementById("hypertension_treatment_content");
var hm = document.getElementById("hypertension_medication_content");
//graph content
var dbp = document.getElementById("CIP_blood");
var dgl = document.getElementById("CIP_glucose");
var dw = document.getElementById("CIP_weight");

function navbar_none(){
    nd.style.display = "none";
    nh.style.display = "none";
    diabetes_none();
    hypertension_none();
}
function td_nvbr() {
    nh.style.display = "none";
    nd.style.display = "block";
    dbp.style.display = "block";
    dgl.style.display = "block";
    dw.style.display = "block";
    diabetes_none();
    hypertension_none();
}
function toggle_hypertension_navbar() {
    nd.style.display = "none";
    nh.style.display = "block";
    dbp.style.display = "none";
    dgl.style.display = "none";
    dw.style.display = "none";
    diabetes_none();
    hypertension_none();
}
function diabetes_none(){
        du.style.display = "none";
        dt.style.display = "none";
        dm.style.display = "none";
        de.style.display = "none";
        dd.style.display = "none";
        ds.style.display = "none";
        dp.style.display = "none";
}
function toggle_diabetes_understanding() {
        du.style.display = "block";
        dt.style.display = "none";
        dm.style.display = "none";
        de.style.display = "none";
        dd.style.display = "none";
        ds.style.display = "none";
        dp.style.display = "none";
}

function toggle_diabetes_treatment() {
        du.style.display = "none";
        dt.style.display = "block";
        dm.style.display = "none";
        de.style.display = "none";
        dd.style.display = "none";
        ds.style.display = "none";
        dp.style.display = "none";
}

function toggle_diabetes_medication() {
        du.style.display = "none";
        dt.style.display = "none";
        dm.style.display = "block";
        de.style.display = "none";
        dd.style.display = "none";
        ds.style.display = "none";
        dp.style.display = "none";
}

function toggle_diabetes_exercise() {
    du.style.display = "none";
    dt.style.display = "none";
    dm.style.display = "none";
    de.style.display = "block";
    dd.style.display = "none";
    ds.style.display = "none";
    dp.style.display = "none";
}

function toggle_diabetes_dental() {
    du.style.display = "none";
    dt.style.display = "none";
    dm.style.display = "none";
    de.style.display = "none";
    dd.style.display = "block";
    ds.style.display = "none";
    dp.style.display = "none";
}

function toggle_diabetes_sexual() {
        du.style.display = "none";
        dt.style.display = "none";
        dm.style.display = "none";
        de.style.display = "none";
        dd.style.display = "none";
        ds.style.display = "block";
        dp.style.display = "none";
}

function toggle_diabetes_pregnancy() {
        du.style.display = "none";
        dt.style.display = "none";
        dm.style.display = "none";
        de.style.display = "none";
        dd.style.display = "none";
        ds.style.display = "none";
        dp.style.display = "block";
}

function hypertension_none(){
        hu.style.display = "none";
        hm.style.display = "none";
        ht.style.display = "none";
}

function toggle_hypertension_understanding() {
        hu.style.display = "block";
        hm.style.display = "none";
        ht.style.display = "none";
}
function toggle_hypertension_medication() {
        hu.style.display = "none";
        hm.style.display = "block";
        ht.style.display = "none";
}
function toggle_hypertension_treatment() {
        hu.style.display = "none";
        hm.style.display = "none";
        ht.style.display = "block";
}

//reset function
function clearInp() {
document.getElementsByTagName("input").value = "";
}