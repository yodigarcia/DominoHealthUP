from flask import Flask, render_template, request, url_for, redirect, session, flash
from ChronicIllness import BloodPressure, BloodGlucose, Weight
from wtforms import Form, StringField, PasswordField, RadioField, IntegerField, TextAreaField, validators, FloatField, SelectField, DateTimeField
from wtforms.fields.html5 import DateField, DateTimeLocalField
from wtforms_components import TimeField
from datetime import datetime 
from Account import Account
from Schedule import Schedule
from Patient import Patient
from water import Water
from water2 import Water2
from water3 import Water3
from water4 import Water4
from Food_1 import Food
from comment import DocNote
from Calories_Graph import Calories
from feedback import Feedback1
import firebase_admin
from firebase_admin import credentials, db
import json


#<!--- yodi --->
cred = credentials.Certificate(r"C:\Users\yodigarcia\PycharmProjects\DominoHealth (testing)\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
default_app = firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://dominohealth.firebaseio.com'})

#<!--- kiahzuo desktop --->
# cred = credentials.Certificate(r'C:\Users\kiah zuo\PycharmProjects\DominoHealth-master\DominoHealth-master\cred\dominohealth-firebase-adminsdk-anpr6-1509e334db.json')
# default_app = firebase_admin.initialize_app(cred, {
#      'databaseURL': 'https://dominohealth.firebaseio.com'})
#cred = credentials.Certificate(r'C:\Users\kiah zuo\PycharmProjects\DominoHealth-master\DominoHealth-master\cred\dominohealth-firebase-adminsdk-anpr6-1509e334db.json')
#default_app = firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dominohealth.firebaseio.com'})

#<!--- kheehing desktop --->
# cred = credentials.Certificate(r"C:\Users\lightcreaater\Documents\GitHub\DominoHealth\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
#<!--- kheehing laptop --->
# cred = credentials.Certificate(r"C:\Users\kheehing\Documents\GitHub\DominoHealth\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
#<!--- kheehing school desktop --->
# cred = credentials.Certificate(r"C:\Users\171723R\Documents\GitHub\DominoHealth\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# default_app = firebase_admin.initialize_app(cred, {
    # 'databaseURL': 'https://dominohealth.firebaseio.com'})

#<!--- matthew laptop --->
# cred = credentials.Certificate(r"C:\Users\matth\Documents\GitHub\DominoHealth\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# default_app = firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dominohealth.firebaseio.com'})


app = Flask(__name__)
root = db.reference()


class Fooder(Form):
    quantity = StringField("")

class Caloriess(Form):
    time = StringField("")
    calories = StringField("")

class Waterer4(Form):
    water41 = SelectField(u'Morning',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water42 = SelectField(u'Noon',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water43 = SelectField(u'Night',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water44 = StringField("Date of Intake")
    name4=StringField("Name")


class DocComment(Form):
    comment1=StringField("")
    date= StringField("")


class Feedbacker(Form):
    feed1=StringField("")
    feed2=StringField("")
    name1=StringField("")
    feed3=SelectField(u'Service Rating',
                          choices=[('Bad', 'Bad'), ('Normal', 'Normal'), ('Good', 'Good'),
                                   ])


class Waterer(Form):
    water = SelectField(u'Morning',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water2 = SelectField(u'Noon',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water3 = SelectField(u'Night',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    note1= StringField("Note")
    note2= TextAreaField("Questions")
    pain1 = SelectField(u'Morning',
                         choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '),
                                  ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                  ('3', 'Close to unbearable (Painful even when on pain killers) '),
                                  ('4', 'Unbearable (Unbearable pain even on painkillers)')])
    pain2 = SelectField(u'Noon',
                         choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '),
                                  ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                  ('3', 'Close to unbearable (Painful even when on pain killers) '),
                                  ('4', 'Unbearable (Unbearable pain even on painkillers)')])
    pain3 = SelectField(u'Night',
                         choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '),
                                  ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                  ('3', 'Close to unbearable (Painful even when on pain killers) '),
                                  ('4', 'Unbearable (Unbearable pain even on painkillers)')])


class Waterer2(Form):
    water21 = SelectField(u'Morning',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water22 = SelectField(u'Noon',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water23 = SelectField(u'Night',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water24 = StringField("Note")
    pain21 = SelectField(u'Morning',
                          choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '), ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                   ('3', 'Close to unbearable (Painful even when on pain killers) '), ('4', 'Unbearable (Unbearable pain even on painkillers)')])
    pain22 =SelectField(u'Noon',
                          choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '), ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                   ('3', 'Close to unbearable (Painful even when on pain killers) '), ('4', 'Unbearable (Unbearable pain even on painkillers)')])
    pain23 = SelectField(u'Night',
                          choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '), ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                   ('3', 'Close to unbearable (Painful even when on pain killers) '), ('4', 'Unbearable (Unbearable pain even on painkillers)')])


class Waterer3(Form):
    water31 = SelectField(u'Morning',
                          choices=[('Water Intake Inadequate. Drink at least 600ML', 'Low'), ('600', 'Normal'),
                                   ('Drink Lesser Abit', 'High ')])
    water32 = SelectField(u'Noon',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water33 = SelectField(u'Night',
                          choices=[('0', '0/4 Jug (0ML)'), ('300', '1/4 Jug (300ML)'), ('600', '1/2 Jug (600ML)'),
                                   ('900', '3/4 Jug ( 900ML) '), ('1200', '1 Jug(1200ML)')])
    water34 = StringField("Note")
    pain31 = SelectField(u'Morning',
                         choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '),
                                  ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                  ('3', 'Close to unbearable (Painful even when on pain killers) '),
                                  ('4', 'Unbearable (Unbearable pain even on painkillers)')])
    pain32 = SelectField(u'Noon',
                         choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '),
                                  ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                  ('3', 'Close to unbearable (Painful even when on pain killers) '),
                                  ('4', 'Unbearable (Unbearable pain even on painkillers)')])
    pain33 = SelectField(u'Night',
                         choices=[('0', 'No Pain ( 0 Pain Felt)'), ('1', 'Slight Pain (Bearable without pain killers '),
                                  ('2', 'Moderate Pain (Requires Pain Killer to be bearable)'),
                                  ('3', 'Close to unbearable (Painful even when on pain killers) '),
                                  ('4', 'Unbearable (Unbearable pain even on painkillers)')])


class BloodA(Form):
    month = IntegerField("Month", [validators.NumberRange(min=1, max=12, message='Invalid month')])
    day = IntegerField("Day", [validators.NumberRange(min=1, max=31, message='Invalid day')])
    blood_glucose = FloatField("Blood Glucose")
    blood_pressure = FloatField("Blood Pressure")
    weight = FloatField("Weight")
    text_doc = StringField("Text")


class Staff(Form):
    username = StringField('', [validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired()])

class Patients(Form):
    firstname = StringField('First Name ')
    lastname = StringField('Last Name ')
    gender = RadioField('Gender ', choices=[('Male', 'Male'), ('Female', 'Female')])
    contact = IntegerField('Contact ', [validators.NumberRange(min=8, message='Invalid number provided')])
    nric = StringField('NRIC ')
    address = StringField('Address ')
    zip = IntegerField('Zip')
    date_o_birth = DateField('Date of Birth ', format='%Y-%m-%d')
    admission_date = DateField('Admission Date ', format='%Y-%m-%d')


class Schedules(Form):
    fullname = StringField('')
    gender = RadioField('Gender ', choices=[('Male', 'Male'), ('Female', 'Female')])
    contact = IntegerField('Contact ', [validators.NumberRange(min=8, message='Invalid number provided')])
    nric = StringField('NRIC ')
    address = StringField('Address ')
    date_o_birth = DateField('Date of Birth ', format='%Y-%m-%d')
    condition = TextAreaField('')
    scheduledate = DateField('Schedule Checkup ')
    test = TimeField('Time ', format='%H:%M')
    contactname = StringField('')
    email = StringField('')
    emergency = IntegerField('', [validators.NumberRange(min=8, message='Invalid number provided')])
    doctoravail = DateField('', format='%Y-%m-%d')

@app.context_processor
def utility_processor():
    def test():
        currentuser = root.child('loggedin').get()
        return currentuser['-L2d1-A6J4Sp57T354Dm']['currentuser']

    return dict(test=test)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = Staff(request.form)

    if request.method == "POST" and form.validate():
        user = form.username.data
        passw = form.password.data

        loggedin_db = root.child('loggedin/-L2d1-A6J4Sp57T354Dm')
        loggedin_db.set({
            'currentuser': form.username.data
        })

        if user[0] == 'P' and passw == 'patient':  # harcoded username and password
            session['logged_in'] = True  # this is to set a session to indicate the user is login into the system.
            session['usertype'] = 'Patient'
            return redirect(url_for('home'))

        elif user[0] == 'S' and passw == 'staff':
            session['logged_in'] = True 
            session['usertype'] = 'Doctor'
            return redirect(url_for('doctorselect'))
        
        else:
            error = 'Invalid login'
            flash(error, 'danger')
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')

    loggedin_db = root.child('loggedin/-L2d1-A6J4Sp57T354Dm')
    loggedin_db.set({
        'currentuser' : ''
    })

    return redirect(url_for('login'))


@app.route('/register', methods=["GET", "POST"])
def register():
    form = Patients(request.form)
    if request.method == "POST" and form.validate():
        fname = form.firstname.data
        lname = form.lastname.data
        gender = form.gender.data
        address = form.address.data
        contact = form.contact.data
        zip = form.zip.data
        nric = form.nric.data
        date_o_birth = str(form.date_o_birth.data)
        admission_date = str(form.admission_date.data)

        pdb = Patient(fname, lname, gender, contact, address, zip, date_o_birth, admission_date, nric)

        pdb_db = root.child('Patient_Information')
        pdb_db.push({
            'firstname': pdb.get_fname(),
            'lastname': pdb.get_lname(),
            'gender': pdb.get_gender(),
            'address': pdb.get_address(),
            'contact': pdb.get_mobile(),
            'zip': pdb.get_zip(),
            'dateofbirth': pdb.get_dateobirth(),
            'admission date': pdb.get_admissiondate(),
            'nric': pdb.get_nric()
         })
        return redirect(url_for('register'))

    return render_template('register.html', form=form)


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    form = Schedules(request.form)
    if request.method == "POST":
        fullname = form.fullname.data
        gender = form.gender.data
        contact = form.contact.data
        address = form.address.data
        date_o_birth = str(form.date_o_birth.data)
        nric = form.nric.data
        condition = form.condition.data
        email = form.email.data
        emgname = form.contactname.data
        scheduledate = str(form.scheduledate.data)
        emergency = form.emergency.data
        time = str(form.test.data)

        schd = Schedule(fullname, gender, contact, address, date_o_birth, nric, condition, email, scheduledate, emgname, emergency, time)

        schd_db = root.child('Checkup')
        schd_db.push({
            'fullname': schd.get_fullname(),
            'gender': schd.get_gender(),
            'contact': schd.get_mobile(),
            'address': schd.get_address(),
            'dateofbirth': schd.get_dateobirth(),
            'nric': schd.get_nric(),
            'condition': schd.get_condition(),
            'email': schd.get_email(),
            'scheduledate': schd.get_schedule(),
            'emergencycontactname': schd.get_emgname(),
            'emergencycontact': schd.get_emergency(),
            'time': schd.get_time()
         })
        return redirect(url_for('schedule'))

    return render_template('schedule.html', form=form)

@app.route('/patientsdatabase')
def patientsdb():
    patients = root.child('Patient_Information').get()
    list = []

    for ids in patients:
        patientsinfo = patients[ids]
        if patientsinfo['firstname']:
            patientinfo = Patient(patientsinfo['firstname'], patientsinfo['lastname'], patientsinfo['gender'], patientsinfo['contact'],
                                  patientsinfo['address'], patientsinfo['zip'],  patientsinfo['dateofbirth'], patientsinfo['admission date'],
                                  patientsinfo['nric'])
            patientinfo.set_pubid(ids)
            print(patientinfo.get_pubid)
            list.append(patientinfo)
    print(list)
    return render_template('patientsdb.html', patientsdb=list)

@app.route('/patientdb')
def patientdb():
    booked = root.child('Checkup').get()
    list = []
    name = []

    for pubid in booked:

        bookedpatients = booked[pubid]

        if bookedpatients['fullname']:
            bookedpatient = Schedule(bookedpatients['fullname'], bookedpatients['gender'], bookedpatients['contact'], bookedpatients['address'],
                                     bookedpatients['dateofbirth'], bookedpatients['nric'], bookedpatients['condition'],
                                     bookedpatients['email'], bookedpatients['scheduledate'],bookedpatients['emergencycontactname'],
                                     bookedpatients['emergencycontact'], bookedpatients['time'])
            bookedpatient.set_pubid(pubid)
            print(bookedpatient.get_pubid())
            name.append(bookedpatient.get_fullname())
            name.sort()
        for i in name:
            if bookedpatients['fullname'] == i:
                print(name)
                list.append(bookedpatient)
            else:
                continue

    return render_template('patientdb.html', booked=list)


@app.route('/update/<string:id>/', methods=["GET","POST"])
def update_patient(id):
    form = Schedules(request.form)
    if request.method == "POST":
        fullname = form.fullname.data
        gender = form.gender.data
        contact = form.contact.data
        address = form.address.data
        date_o_birth = str(form.date_o_birth.data)
        nric = form.nric.data
        condition = form.condition.data
        email = form.email.data
        emgname = form.contactname.data
        scheduledate = str(form.scheduledate.data)
        emergency = str(form.emergency.data)
        time = str(form.test.data)

        schd = Schedule(fullname, gender, contact, address, date_o_birth, nric, condition, email, scheduledate, emgname, emergency, time)

        schd_db = root.child('Checkup/' + id)
        schd_db.set({
            'fullname': schd.get_fullname(),
            'gender': schd.get_gender(),
            'contact': schd.get_mobile(),
            'address': schd.get_address(),
            'dateofbirth': schd.get_dateobirth(),
            'nric': schd.get_nric(),
            'condition': schd.get_condition(),
            'email': schd.get_email(),
            'scheduledate': schd.get_schedule(),
            'emergencycontactname': schd.get_emgname(),
            'emergencycontact': schd.get_emergency(),
            'time': schd.get_time()
        })
        flash('Updated successfully', 'success')
        return redirect(url_for('patientdb'))

    else:
        url = 'Checkup/'+id
        bookedpatients = root.child(url).get()

        if bookedpatients['fullname'] != '':
            bookedpatient = Schedule(bookedpatients['fullname'], bookedpatients['gender'], bookedpatients['contact'], bookedpatients['address'],
                                     bookedpatients['dateofbirth'], bookedpatients['nric'], bookedpatients['condition'],
                                     bookedpatients['email'], bookedpatients['scheduledate'],bookedpatients['emergencycontactname'], 
                                     bookedpatients['emergencycontact'], bookedpatients['time'])

            bookedpatient.set_pubid(id)
            form.fullname.data = bookedpatient.get_fullname()
            form.gender.data = bookedpatient.get_gender()
            form.contact.data = bookedpatient.get_mobile()
            form.address.data = bookedpatient.get_address()
            form.date_o_birth.data = datetime.strptime(bookedpatient.get_dateobirth(), '%Y-%m-%d')
            form.nric.data = bookedpatient.get_nric()
            form.condition.data = bookedpatient.get_condition()
            form.email.data = bookedpatient.get_email()
            form.scheduledate.data = datetime.strptime(bookedpatient.get_schedule(), '%Y-%m-%d')
            form.contactname.data = bookedpatient.get_emgname()
            form.emergency.data = bookedpatient.get_emergency()
            form.test.data = datetime.strptime(bookedpatient.get_time(), '%H:%M:%S')

        return render_template('updatepatient.html', form=form)

# Kiahzuo

@app.route('/viewfeedback')
def viewfeedback():
    feedback = root.child('feedback').get()
    list =[]

    for pubid in feedback:

        eachfeedback= feedback[pubid]

        if eachfeedback['name1'] !="":
            feedbackpatient=Feedback1(eachfeedback['name1'],eachfeedback['feed1'],eachfeedback['feed2'],eachfeedback['feed3'])
            feedbackpatient.set_pubid(pubid)
            print(feedbackpatient.get_pubid())
            list.append(feedbackpatient)

    return render_template('feedbackview.html', feedback=list)


@app.route('/selfprofile')
def selfprofile():
    water4 = root.child('long').get()
    list = []
    comment=root.child('Doc1').get()
    list2=[]

    for pubid in water4:
        waterdata= water4[pubid]

        if waterdata['water44'] != " ":
            waterdatapatient=Water4(waterdata['water44'],waterdata['water41'],waterdata['water42'],waterdata['water43'],waterdata['name4'])
            waterdatapatient.set_pubid(pubid)
            print(waterdatapatient.get_pubid())
            list.append(waterdatapatient)

    for pubid in comment:
        commentdata= comment[pubid]

        if commentdata['DocComment'] != " ":
                commentdatapatient=DocNote(commentdata['DocComment'],commentdata['Date'])
                commentdatapatient.set_pubid(pubid)
                print(commentdatapatient.get_pubid())
                list2.append(commentdatapatient)

    return render_template('selfprofile.html',comment=list2 ,water4= list)


@app.route('/docupdate')
def docprofile():
    return render_template('docupdate.html')


@app.route('/docprofile', methods=["GET", "POST"])
def docupdate():
    form = DocComment(request.form)
    if request.method == "POST":
        comment = form.comment1.data
        date= form.date.data

        dc = DocNote(comment,date)

        dc_db = root.child("Doc1")
        dc_db.push({
            'DocComment': dc.get_comment1() ,"Date":dc.get_commentdate()
        })

    comment=root.child('Doc1').get()
    list2=[]

    water4 = root.child('long').get()
    list = []

    for pubid in comment:
        commentdata= comment[pubid]

        if commentdata['DocComment'] != " ":
                commentdatapatient=DocNote(commentdata['DocComment'],commentdata['Date'])
                commentdatapatient.set_pubid(pubid)
                print(commentdatapatient.get_pubid())
                list2.append(commentdatapatient)

    for pubid in water4:

        waterdata = water4[pubid]

        if waterdata['water44'] != " ":
            waterdatapatient=Water4(waterdata['water44'],waterdata['water41'],waterdata['water42'],waterdata['water43'],waterdata['name4'])
            waterdatapatient.set_pubid(pubid)
            print(waterdatapatient.get_pubid())
            list.append(waterdatapatient)

    return render_template('docprofile.html',form=form ,comment=list2,water4= list)


@app.route('/doctorselect')
def doctorselect():
    return render_template('doctorselect.html')


@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')


@app.route('/wiki')
def Wiki():
    return render_template('wiki.html')


@app.route('/select')
def select():
    return render_template('select.html')


@app.route('/updatelong/<string:id>/', methods=['GET', 'POST'])
def update_publication(id):
    form = Waterer4(request.form)
    if request.method == 'POST':
            morning=form.water41.data
            afternoon=form.water43.data
            night=form.water42.data
            date=form.water44.data
            name=form.name4.data

            longupdate = Water4(morning,afternoon,night,date,name)
            longupdate_db = root.child('long/' + id)

            longupdate_db.set({
                "water41":longupdate.get_water43(),
                "water42":longupdate.get_water42(),
                "water43":longupdate.get_water41(),
                "water44":longupdate.get_water44(),
                "name4":longupdate.get_name4()
            })

            flash('Magazine Updated Sucessfully.', 'success')

            return redirect(url_for('selfprofile'))

    else:
        url = 'long/'+id
        waterdata = root.child(url).get()

        if waterdata['name4'] != " ":
            waterdatapatient = Water4(waterdata['water43'], waterdata['water41'], waterdata['water42'],
                                          waterdata['water44'], waterdata['name4'])
            waterdatapatient.set_pubid(id)
            form.water44.data=waterdatapatient.get_water44()
            form.water43.data=waterdatapatient.get_water43()
            form.water42.data=waterdatapatient.get_water42()
            form.water41.data=waterdatapatient.get_water41()
            form.name4.data=waterdatapatient.get_name4()

        return render_template('updatelong.html',form=form)


#comment deletion
@app.route('/delete_comment/<string:id>',methods=['POST'])
def delete_comment(id):
    dc_db = root.child('Doc1/'+id)
    dc_db.delete()

    return redirect(url_for('docupdate'))


#tracker long
@app.route('/delete_publication/<string:id>', methods=['POST'])
def delete_publication(id):
    mag_db = root.child('long/' + id)
    mag_db.delete()

    return redirect(url_for('selfprofile'))


@app.route('/trackerlong', methods=["GET","POST"])
def longterm():
    form = Waterer4(request.form)
    if request.method=="POST":
        cloud=form.water41.data
        cloud2=form.water42.data
        cloud3=form.water43.data
        cloud4=form.water44.data
        cloud5=form.name4.data

        cloud10=Water4(cloud,cloud2,cloud3,cloud4,cloud5)

        cloud_db = root.child('long')
        cloud_db.push({
            "water41":cloud10.get_water41(),
            "water42":cloud10.get_water42(),
            "water43":cloud10.get_water43(),
            "water44":cloud10.get_water44(),
            "name4":cloud10.get_name4()
        })
    return render_template('longterm.html', form=form)


@app.route('/feedbackpage', methods=["GET","POST"])
def feedback():
    form = Feedbacker(request.form)
    if request.method=="POST":
        earth = form.feed1.data
        earth1= form.feed2.data
        earth2= form.name1.data
        earth3=form.feed3.data

        earth10= Feedback1(earth,earth1,earth2,earth3)

        water_db = root.child('feedback')
        water_db.push({
            'feed1': earth10.get_feed1(),
            "feed2": earth10.get_feed2(),
            "name1": earth10.get_name1(),
            "feed3": earth10.get_feed3()
        })
    return render_template('feedback.html', form=form)


@app.route('/tracker', methods=["GET", "POST"])
def tracker():
    form = Waterer(request.form)
    if request.method=="POST":
        fire = form.water.data
        fire2= form.water2.data
        fire3= form.water3.data

        fire6= form.note1.data
        fire7= form.note2.data
        fire8 = form.pain1.data
        fire9 = form.pain2.data
        fire11 = form.pain3.data

        fire10= Water(fire,fire2,fire3,fire6,fire7,fire8,fire9,fire11)

        water_db = root.child('water')
        water_db.push({
            'Water': fire10.get_water(),
            "Water2": fire10.get_water2(),
            "Water3": fire10.get_water3(),
            "Note1": fire10.get_note1(),
            "Note2": fire10.get_note2(),
            "Pain1": fire10.get_pain1(),
            "Pain2": fire10.get_pain2(),
            "Pain3": fire10.get_pain3()
        })
    return render_template('tracker.html',form=form)


@app.route('/tracker2', methods=["GET", "POST"])
def tracker2():
    form= Waterer2(request.form)
    if request.method == "POST":
        grass = form.water21.data
        grass2= form.water22.data
        grass3= form.water23.data
        grass4=form.water24.data
        grass5 = form.pain21.data
        grass6 = form.pain22.data
        grass7 = form.pain23.data

        grass10=Water2(grass, grass2, grass3, grass4, grass5, grass6, grass7)
        grass_db = root.child('water2')
        grass_db.push({
            "Water21": grass10.getwater21(),
            "Water22": grass10.getwater22(),
            "Water23": grass10.getwater23(),
            "Water24": grass10.getwater24(),
            "Pain21" : grass10.getpain21(),
            "Pain22" : grass10.getpain22(),
            "Pain23" : grass10.getpain23()
        })
    return render_template('tracker2.html', form=form)


@app.route('/After_discharge', methods=["GET", "POST"])
def after_discharge():
    return render_template('after_discharge.html')


@app.route('/chronic_illness', methods=["GET", "POST"])
def chronic_illness_():
    form = BloodA(request.form)
    if request.method == "POST" and form.validate():
        month = form.month.data
        month = month-1 
        day = form.day.data
        blood_pressure = form.blood_pressure.data
        blood_glucose = form.blood_glucose.data
        weight = form.weight.data
        bg = BloodGlucose(month, day, blood_glucose)
        bp = BloodPressure(month, day, blood_pressure)
        weight = Weight(month, day, weight)

        bp_db = root.child('Diabetes_bp')
        bg_db = root.child('Diabetes_bg')
        weight_db = root.child('Diabetes_weight')
        if blood_pressure != None:
            bp_db.push({
                'month': bp.get_month(),
                'day': bp.get_day(),
                'blood pressure': bp.get_blood_pressure(),
            })
        elif blood_glucose != None:
            bg_db.push({
                'month': bg.get_month(),
                'day': bg.get_day(),
                'blood glucose': bg.get_blood_glucose(),
            })
        elif weight != None:
            weight_db.push({
                'month': weight.get_month(),
                'day': weight.get_day(),
                'weight': weight.get_weight(),
            })
        return redirect(url_for('chronic_illness_'))

    bp = root.child('Diabetes_bp').get()
    bg = root.child('Diabetes_bg').get()
    wi = root.child('Diabetes_weight').get()
    list_bg = []
    list_bp = []
    list_wi = []

    try:
        for data in bp:
            i = bp[data]
            if 'blood pressure' in i:
                if i['blood pressure'] != None:
                    db_data = BloodPressure(i['month'], i['day'], i['blood pressure'])
                    db_data.set_data(data)
                    # print(db_data.get_data())
                    list_bp.append(db_data)
        for data in bg:
            j = bg[data]
            if 'blood glucose' in j:
                if j['blood glucose'] != None:
                    db_data = BloodGlucose(j['month'], j['day'], j['blood glucose'])
                    db_data.set_data(data)
                    # print(db_data.get_data())
                    list_bg.append(db_data)
        for data in wi:
            k = wi[data]
            if 'weight' in k:
                if k['weight'] != None:
                    db_data = Weight(k['month'], k['day'], k['weight'])
                    db_data.set_data(data)
                    # print(db_data.get_data())
                    list_wi.append(db_data)
    except:
        TypeError

    return render_template('Chronic_illness_patient.html', form=form, bp=list_bp, bg=list_bg,wi=list_wi)


@app.route('/chronic_illness_s')
def chronic_illness():
    form = BloodA(request.form)
    if request.method == "POST" and form.validate():
        month = form.month.data
        month = month-1 
        day = form.day.data
        blood_pressure = form.blood_pressure.data
        blood_glucose = form.blood_glucose.data
        weight = form.weight.data
        bg = BloodGlucose(month, day, blood_glucose)
        bp = BloodPressure(month, day, blood_pressure)
        weight = Weight(month, day, weight)

        bp_db = root.child('Diabetes_bp')
        bg_db = root.child('Diabetes_bg')
        weight_db = root.child('Diabetes_weight')
        if blood_pressure != None:
            bp_db.push({
                'month': bp.get_month(),
                'day': bp.get_day(),
                'blood pressure': bp.get_blood_pressure(),
            })
        elif blood_glucose != None:
            bg_db.push({
                'month': bg.get_month(),
                'day': bg.get_day(),
                'blood glucose': bg.get_blood_glucose(),
            })
        elif weight != None:
            weight_db.push({
                'month': weight.get_month(),
                'day': weight.get_day(),
                'weight': weight.get_weight(),
            })
        return redirect(url_for('chronic_illness_s'))

    bp = root.child('Diabetes_bp').get()
    bg = root.child('Diabetes_bg').get()
    wi = root.child('Diabetes_weight').get()
    list_bg = []
    list_bp = []
    list_wi = []

    try:
        for data in bp:
            i = bp[data]
            if 'blood pressure' in i:
                if i['blood pressure'] != None:
                    db_data = BloodPressure(i['month'], i['day'], i['blood pressure'])
                    db_data.set_data(data)
                    # print(db_data.get_data())
                    list_bp.append(db_data)
        for data in bg:
            j = bg[data]
            if 'blood glucose' in j:
                if j['blood glucose'] != None:
                    db_data = BloodGlucose(j['month'], j['day'], j['blood glucose'])
                    db_data.set_data(data)
                    # print(db_data.get_data())
                    list_bg.append(db_data)
        for data in wi:
            k = wi[data]
            if 'weight' in k:
                if k['weight'] != None:
                    db_data = Weight(k['month'], k['day'], k['weight'])
                    db_data.set_data(data)
                    # print(db_data.get_data())
                    list_wi.append(db_data)
    except:
        TypeError

    return render_template('Chronic_illness_staff.html', form=form, bp=list_bp, bg=list_bg,wi=list_wi)


@app.route('/menu', methods=["GET", "POST"])
def food():
    form = Fooder(request.form)
    if request.method == "POST":
        quantity = form.quantity.data

        send = Food(quantity)
        send_db = root.child('selected')
        send_db.push({
            "Steamed_Rice": send.get_quantity(),
        })

    return render_template('food.html', form = form)


@app.route('/Food_Health', methods= ["GET", "POST"])
def Food_Health():
    form = Caloriess(request.form)
    if request.method == "POST":
        time = form.time.data
        calories = form.calories.data

        calories = Calories(time, calories)

        calories_db = root.child('Calories')
        calories_db.push({
            "time": calories.get_time(),
            "calories": calories.get_calories(),
        })

    calories = root.child('Calories').get()
    list = []

    for pubid in calories:
        timecalories = calories[pubid]

        if timecalories['time'] != '':
            timecaloriespatient = Calories(timecalories["calories"], timecalories["time"])
            timecaloriespatient.set_pubid(pubid)
            print(timecaloriespatient.get_pubid())
            list.append(timecaloriespatient)

    return render_template("Food_Health.html", form=form, calories=list)


@app.route('/fud')
def fud():
    return render_template('Fud.html')


@app.route('/events')
def events_page():
    return render_template('Events.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)




