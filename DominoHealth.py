from flask import Flask, render_template, request, url_for, redirect, session, flash
from ChronicIllness import BloodPressure, BloodGlucose, Weight, Information
from wtforms import Form, StringField, PasswordField, RadioField, IntegerField, TextAreaField, validators, FloatField ,SelectField,TextAreaField,BooleanField
from wtforms.fields.html5 import DateField
from datetime import datetime 
from Account import Account
from Schedule import Schedule
from Patient import Patient
from water import Water
from water2 import Water2
from water3 import Water3
from water4 import Water4
from Food_Select import Food_Select
from Food_1 import Food
from comment import DocNote
from Calories_Graph import Calories
from feedback import Feedback1
import firebase_admin
from firebase_admin import credentials, db
import json


#<!--- yodi --->
#red = credentials.Certificate(r"C:\Users\yodigarcia\PycharmProjects\DominoHealth (testing)\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
#default_app = firebase_admin.initialize_app(cred, {
#   'databaseURL': 'https://dominohealth.firebaseio.com'})
# cred = credentials.Certificate(r"C:\Users\yodigarcia\PycharmProjects\DominoHealth (testing)\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# default_app = firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://dominohealth.firebaseio.com'})


#<!--- kiahzuo desktop --->
#cred = credentials.Certificate(r'C:\Users\kiah zuo\PycharmProjects\DominoHealth-master\DominoHealth-master\cred\dominohealth-firebase-adminsdk-anpr6-1509e334db.json')
#default_app = firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dominohealth.firebaseio.com'})


#<!--- kheehing desktop --->
# cred = credentials.Certificate(r"C:\Users\lightcreaater\Documents\GitHub\DominoHealth\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# <!--- kheehing laptop --->
cred = credentials.Certificate(r"C:\Users\kheehing\Documents\GitHub\DominoHealthUP\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
#<!--- kheehing school desktop --->
# cred = credentials.Certificate(r"C:\Users\171723R\Documents\GitHub\DominoHealth\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://dominohealth.firebaseio.com'})

#<!--- matthew laptop --->
# cred = credentials.Certificate(r"C:\Users\matth\Documents\GitHub\DominoHealth\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# default_app = firebase_admin.initialize_app(cred, {
#       'databaseURL': 'https://dominohealth.firebaseio.com'})


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


class Staff(Form):
    username = StringField('', [validators.DataRequired()])
    password = PasswordField('', [validators.DataRequired()])


class Patients(Form):
    firstname = StringField('First Name ')
    lastname = StringField('Last Name ')
    gender = RadioField('Gender ', choices=[('male', 'Male'), ('female', 'Female')])
    contact = IntegerField('Contact ', [validators.NumberRange(min=8, message='Invalid number provided')])
    nric = StringField('NRIC ')
    contact = IntegerField('Contact ', [validators.NumberRange(min=8, max=8, message='Invalid number provided')])
    nric = IntegerField('NRIC ')
    address = StringField('Address ')
    zip = IntegerField('Zip')
    date_o_birth = DateField('Date of Birth ', format='%Y-%m-%d')
    admission_date = DateField('Admission Date ', format='%Y-%m-%d')


class Schedules(Form):
    fullname = StringField('')
    gender = RadioField('Gender ', choices=[('Male', 'Male'), ('Female', 'Female')])
    contact = IntegerField('Contact ', [validators.NumberRange(min=8, message='Invalid number provided')])
    nric = StringField('NRIC ')
    contact = IntegerField('Contact ', [validators.NumberRange(min=8, max=8, message='Invalid number provided')])
    nric = IntegerField('NRIC ')
    address = StringField('Address ')
    date_o_birth = DateField('Date of Birth ', format='%Y-%m-%d')
    condition = TextAreaField('')
    scheduledate = DateField('Schedule Checkup ', format='%Y-%m-%d')
    contactname = StringField('')
    email = StringField('')
    # emergency = IntegerField('', [validators.NumberRange(min=8, max=8, message='Invalid number provided')])

class Fud_Select(Form):
    my_food_order = SelectField(u'Steamed Rice',
                           choices=[('-', '-'), ('1 Steamed Rice', '1 Serving (~295 cal)'), ('2 Steamed Rice', '2 Servings (~590 cal)'),
                                    ('3 Steamed Rice', '3 Servings (~885 cal)')])

    my_food_order2 = SelectField(u'Vegetable Porridge',
                           choices=[('-', '-'), ('1 Porridge', '1 Serving (~240 Cal)'), ('2 Porridge', '2 Servings (~480 cal)'),
                                    ('3 Porridge', '3 Servings (~720 cal)')])

    my_food_order3 = SelectField(u'Mixed Rice(Beef)',
                           choices=[('-', '-'), ('1 Mixed Rice', '1 Serving (~390 cal)'), ('2 Mixed Rice', '2 Servings (~780 cal)'),
                                    ('3 Mixed Rice', '3 Servings (~1,170 cal)')])

    my_food_order4 = SelectField(u'Vegetable Fusilli',
                                 choices=[('-', '-'), ('1 Vegetable Fusilli', '1 Serving (~345 cal)'), ('2 Vegetable Fusilli', '2 Servings (~690 cal)'),
                                          ('3 Vegetable Fusilli', '3 Servings (~1,035 cal)')])

    my_food_order5 = SelectField(u'Mixed Fruit Yogurt',
                                 choices=[('-', '-'), ('1 Mixed Fruit Yogurt', '1 Serving (~218 cal)'), ('2 Mixed Fruit Yogurt', '2 Servings (~436 cal)'),
                                          ('3 Mixed Fruit Yogurt', '3 Servings (~654 cal)')])

    my_food_order6 = SelectField(u'Mushroom Soup',
                                 choices=[('-', '-'), ('1 Mushroom Soup', '1 Serving (~110 cal)'), ('2 Mushroom Soup', '2 Servings (~220 cal)'),
                                          ('3 Mushroom Soup', '3 Servings (~330 cal)')])

    my_food_order7 = SelectField(u'Yogurt Special',
                                 choices=[('-', '-'), ('1 Yogurt Special', '1 Serving (~145 cal)'), ('2 Yogurt Specials', '2 Servings (~290 cal)'),
                                          ('3 Yogurt Specials', '3 Servings (~345 cal)')])

    my_food_order8 = SelectField(u'Steamed Salmon',
                                 choices=[('-', '-'), ('1 Steamed Salmon', '1 Serving (~436 cal)'), ('2 Steamed Salmon', '2 Servings (~872 cal)')])

    my_food_order9 = SelectField(u'Salad & Eggs',
                                 choices=[('-', '-'), ('1 Salad & Eggs', '1 Serving (~238 cal)'), ('2 Salad & Eggs', '2 Servings (~476 cal)'),
                                          ('3 Salad & Eggs', '3 Servings (~714 cal)')])

    my_food_order10 = SelectField(u'Breakfast Set',
                                 choices=[('-', '-'), ('1 Breakfast Set', '1 Serving (~550 cal)'), ('2 Breakfast Set', '2 Servings (~1,100 cal)'),
                                          ('3 Breakfast Set', '3 Servings (~1,650 cal)')])

    my_food_order11 = SelectField(u'Vegetables & Rice',
                                 choices=[('-', '-'), ('1 Vegetables & Rice', '1 Serving (~320 cal)'), ('2 Vegetables & Rice', '2 Servings (~640 cal)'),
                                          ('3 Vegetables & Rice', '3 Servings (~960 cal)')])

    my_food_order12 = SelectField(u'Breakfast Omelette',
                                  choices=[('-', '-'), ('1 Omelette', '1 Serving (~140 cal)'), ('2 Omelette', '2 Servings (~280 cal)'),
                                           ('3 Omelette', '3 Servings (~400 cal)')])

@app.context_processor
def utility_processor():
    def test():
        currentuser = root.child('loggedin').get()
        list = []

        for pubid in currentuser:    #-L2cm2FcD-Pb_LUpP6Zf

            logged = currentuser[pubid]

            if logged['currentuser'] != '':
                current = Account(logged['currentuser'], logged['currentuser'])
                current.set_pubid(pubid)
                print(current.get_pubid())
                list.append(current)
        
        return currentuser['-L2d1-A6J4Sp57T354Dm']['currentuser'][1:]

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


@app.route('/profile', methods=["GET", "POST"])
def profile():
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
        return redirect(url_for('profile'))

    return render_template('profile.html', form=form)


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    form = Schedules(request.form)
    if request.method == "POST" and form.validate():
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

        schd = Schedule(fullname, gender, contact, address, date_o_birth, nric, condition, email, scheduledate, emgname)

        schd_db = root.child('Checkup')
        schd_db.push({
            'fullname': schd.get_fullname(),
            'gender': schd.get_gender(),
            'emergencycontact': schd.get_mobile(),
            'address': schd.get_address(),
            'dateofbirth': schd.get_dateobirth(),
            'nric': schd.get_nric(),
            'condition': schd.get_condition(),
            'email': schd.get_email(),
            'scheduledate': schd.get_schedule(),
            'emergencycontactname': schd.get_emgname()
         })
        return redirect(url_for('schedule'))

    return render_template('schedule.html', form=form)


@app.route('/patientdb')
def patientdb():
    booked = root.child('Checkup').get()
    list = []

    for pubid in booked:

        bookedpatients = booked[pubid]

        if bookedpatients['fullname'] != '':
            bookedpatient = Schedule(bookedpatients['fullname'], bookedpatients['gender'], bookedpatients['emergencycontact'], bookedpatients['address'],
                                     bookedpatients['dateofbirth'], bookedpatients['nric'], bookedpatients['condition'],
                                     bookedpatients['email'], bookedpatients['scheduledate'],bookedpatients['emergencycontactname'])
            bookedpatient.set_pubid(pubid)
            print(bookedpatient.get_pubid())
            list.append(bookedpatient)

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

        schd = Schedule(fullname, gender, contact, address, date_o_birth, nric, condition, email, scheduledate, emgname)

        schd_db = root.child('Checkup/' + id)
        schd_db.set({
            'fullname': schd.get_fullname(),
            'gender': schd.get_gender(),
            'emergencycontact': schd.get_mobile(),
            'address': schd.get_address(),
            'dateofbirth': schd.get_dateobirth(),
            'nric': schd.get_nric(),
            'condition': schd.get_condition(),
            'email': schd.get_email(),
            'scheduledate': schd.get_schedule(),
            'emergencycontactname': schd.get_emgname()
        })
        flash('Updated successfully', 'success')
        return redirect(url_for('home'))

    else:
        url = 'Checkup/'+id
        bookedpatients = root.child(url).get()

        if bookedpatients['fullname'] != '':
            bookedpatient = Schedule(bookedpatients['fullname'], bookedpatients['gender'], bookedpatients['emergencycontact'], bookedpatients['address'],
                                     bookedpatients['dateofbirth'], bookedpatients['nric'], bookedpatients['condition'],
                                     bookedpatients['email'], bookedpatients['scheduledate'],bookedpatients['emergencycontactname'])

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

        return render_template('updatepatient.html', form=form)


@app.route('/profile_page')
def ProfilePage():
    return render_template('profile_page.html')

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


@app.route('/patientdb')
def Patientdb():
    return render_template('patientdb.html')


@app.route('/layout')
def layout():
    return render_template('layout.html')


class Aft_dis(Form):
    nric = StringField("")
    status = RadioField("",choices=[(0,'0%'),(10,'10%'),(20,'20%'),(30,'30%'),(40,'40%'),(50,'50%'),(60,'60%'),(70,'70%'),(80,'80%'),(90,'90%'),(100,'100%')])
    eye_problem = TextAreaField("Are you experiencing any problems?<small>&nbsp;if yes please state</small>")
    medication = TextAreaField("Do you have any problems with your medication?<small>&nbsp;if yes please state</small>")
    others = TextAreaField("Do you have any other enquires ?")

@app.route('/after_discharge', methods=["GET", "POST"])
def after_discharge_():
    form = Aft_dis(request.form)
    if request.method == "POST":
        nric = form.nric.data
        status = form.status.data
        eye_problem = form.eye_problem.data
        medication = form.medication.data
        others = form.others.data  
        currentuser = root.child('loggedin').get()
        info = Information(nric,status,problem,medication,others)
        info_db = root.child(currentuser['-L2d1-A6J4Sp57T354Dm']['currentuser'][1:]).child("outpatient")
        if nric != None:
            info_db.push({
                'nric': info.get_informationzero(),
                'status': info.get_informationone(),
                'problem': info.get_informationtwo(),
                'medication': info.get_informationthree(),
                'others': info.get_informationfour(),
            })
        return redirect(url_for('after_discharge_'))

    return render_template('after_discharge.html', form = form)


class BloodA(Form):
    month = IntegerField("Month", [validators.NumberRange(min=1, max=12, message='Invalid month')])
    day = IntegerField("Day", [validators.NumberRange(min=1, max=31, message='Invalid day')])
    blood_glucose = FloatField("Blood Glucose")
    blood_pressure = FloatField("Blood Pressure")
    weight = FloatField("Weight")
    text_doc = StringField("Text")

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


@app.route('/fud', methods= ["GET", "POST"])
def fud():
    form = Fud_Select(request.form)
    if request.method == "POST":
        food_quantity = form.my_food_order.data
        food_quantity2 = form.my_food_order2.data
        food_quantity3 = form.my_food_order3.data
        food_quantity4 = form.my_food_order4.data
        food_quantity5 = form.my_food_order5.data
        food_quantity6 = form.my_food_order6.data
        food_quantity7 = form.my_food_order7.data
        food_quantity8 = form.my_food_order8.data
        food_quantity9 = form.my_food_order9.data
        food_quantity10 = form.my_food_order10.data
        food_quantity11 = form.my_food_order11.data
        food_quantity12 = form.my_food_order12.data

        food_q = Food_Select(food_quantity, food_quantity2, food_quantity3, food_quantity4, food_quantity5, food_quantity6,
                             food_quantity7, food_quantity8, food_quantity9, food_quantity10, food_quantity11, food_quantity12)

        food_q_db = root.child('food_quantity')
        food_q_db.push({
            "food_queue": food_q.get_food_quantity(),
            "food_queue2": food_q.get_food_quantity2(),
            "food_queue3": food_q.get_food_quantity3(),
            "food_queue4": food_q.get_food_quantity4(),
            "food_queue5": food_q.get_food_quantity5(),
            "food_queue6": food_q.get_food_quantity6(),
            "food_queue7": food_q.get_food_quantity7(),
            "food_queue8": food_q.get_food_quantity8(),
            "food_queue9": food_q.get_food_quantity9(),
            "food_queue10": food_q.get_food_quantity10(),
            "food_queue11": food_q.get_food_quantity11(),
            "food_queue12": food_q.get_food_quantity12(),
        })

    return render_template('Fud.html', form=form)

@app.route('/food_info')
def food_info():
    return render_template('Food_Information.html')


@app.route('/events')
def events_page():
    return render_template('Events.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
