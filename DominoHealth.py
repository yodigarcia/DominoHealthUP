from flask import Flask, render_template, request, url_for, redirect, session, flash
from wtforms import Form, StringField, PasswordField, RadioField, IntegerField, TextAreaField, validators, FloatField ,SelectField,TextAreaField,BooleanField
from wtforms.fields.html5 import DateField
from wtforms_components import TimeField
from firebase_admin import credentials, db
from datetime import datetime
import firebase_admin
import json
from ChronicIllness import BloodPressure, BloodGlucose, Bmi, Information, Date
from Food_Select import Food_Select
from feedback import Feedback1
from Schedule import Schedule
from Account import Account
from Patient import Patient
from comment import DocNote
from water2 import Water2
from water3 import Water3
from water4 import Water4
from Food_1 import Food
from water import Water
from Timedb import Timedb
from events_submissions import event_submissions


#<!--- yodi --->
# cred = credentials.Certificate(r"C:\Users\yodigarcia\Downloads\DominoHealthUP\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# default_app = firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://dominohealth.firebaseio.com'})


#<!--- kiahzuo desktop --->

cred = credentials.Certificate(r'C:\Users\kiah zuo\PycharmProjects\DominoHealth-master\DominoHealth-master\cred\dominohealth-firebase-adminsdk-anpr6-1509e334db.json')
default_app = firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://dominohealth.firebaseio.com'})

# cred = credentials.Certificate(r'C:\Users\kiah zuo\PycharmProjects\DominoHealth-master\DominoHealth-master\cred\dominohealth-firebase-adminsdk-anpr6-1509e334db.json')
# default_app = firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://dominohealth.firebaseio.com'})

#<!--- kheehing desktop --->
# cred = credentials.Certificate(r"C:\Users\lightcreaater\Documents\GitHub\DominoHealthUP\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# <!--- kheehing laptop --->
# cred = credentials.Certificate(r"C:\Users\kheehing\Documents\GitHub\DominoHealthUP\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# default_app = firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dominohealth.firebaseio.com'})

#<!--- matthew laptop --->
# cred = credentials.Certificate(r"C:\Users\matth\Documents\GitHub\DominoHealthUP\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
# default_app = firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://dominohealth.firebaseio.com'})

#<!--- matthew laptop 2 --->
#cred = credentials.Certificate(r"C:\Users\matth\Documents\GitHub\DominoHealthUP\cred\dominohealth-firebase-adminsdk-anpr6-8fddaeda58.json")
#default_app = firebase_admin.initialize_app(cred, {
#      'databaseURL': 'https://dominohealth.firebaseio.com'})

app = Flask(__name__)
root = db.reference()

@app.context_processor
def utility_processor():
    def test():
        currentuser = root.child('loggedin').get() 
        return currentuser['-L2d1-A6J4Sp57T354Dm']['currentuser']

    return dict(test=test)

####################################################################################################
####################################################################################################
####################################################################################################
# --- MATTHEW CLASS ---
class Fooder(Form):
    quantity = StringField("")

class Caloriess(Form):
    time = StringField("")
    calories = StringField("")

class Fud_Select(Form):
    name = TextAreaField('Enter Your Name:')

    time = SelectField(u'Time',choices=[('', '-'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')])

    my_food_order = SelectField(u'Steamed Rice',
                                 choices=[(0, '-'), (295, '1 Serving (~295 cal)'), (590, '2 Servings (~590 cal)'),
                                          (885, '3 Servings (~885 cal)')])

    my_food_order2 = SelectField(u'Vegetable Porridge',
                                 choices=[(0, '-'), (240, '1 Serving (~240 Cal)'), (480, '2 Servings (~480 cal)'),
                                          (720, '3 Servings (~720 cal)')])

    my_food_order3 = SelectField(u'Mixed Rice(Beef)',
                                 choices=[(0, '-'), (390, '1 Serving (~390 cal)'), (780, '2 Servings (~780 cal)'),
                                    (1170, '3 Servings (~1,170 cal)')])

    my_food_order4 = SelectField(u'Vegetable Fusilli',
                                 choices=[(0, '-'), (345, '1 Serving (~345 cal)'), (690, '2 Servings (~690 cal)'),
                                          (1035, '3 Servings (~1,035 cal)')])

    my_food_order5 = SelectField(u'Mixed Fruit Yogurt',
                                 choices=[(0, '-'), (218, '1 Serving (~218 cal)'), (436, '2 Servings (~436 cal)'),
                                          (654, '3 Servings (~654 cal)')])

    my_food_order6 = SelectField(u'Mushroom Soup',
                                 choices=[(0, '-'), (110, '1 Serving (~110 cal)'), (220, '2 Servings (~220 cal)'),
                                          (330, '3 Servings (~330 cal)')])

    my_food_order7 = SelectField(u'Yogurt Special',
                                 choices=[(0, '-'), (145, '1 Serving (~145 cal)'), (290, '2 Servings (~290 cal)'),
                                          (345, '3 Servings (~345 cal)')])

    my_food_order8 = SelectField(u'Steamed Salmon',
                                 choices=[(0, '-'), (436, '1 Serving (~436 cal)'), (872, '2 Servings (~872 cal)')])

    my_food_order9 = SelectField(u'Salad & Eggs',
                                 choices=[(0, '-'), (238, '1 Serving (~238 cal)'), (476, '2 Servings (~476 cal)'),
                                          (714, '3 Servings (~714 cal)')])

    my_food_order10 = SelectField(u'Breakfast Set',
                                 choices=[(0, '-'), (550, '1 Serving (~550 cal)'), (1100, '2 Servings (~1,100 cal)'),
                                          (1650, '3 Servings (~1,650 cal)')])

    my_food_order11 = SelectField(u'Vegetables & Rice',
                                 choices=[(0, '-'), (320, '1 Serving (~320 cal)'), (640, '2 Servings (~640 cal)'),
                                          (960, '3 Servings (~960 cal)')])

    my_food_order12 = SelectField(u'Breakfast Omelette',
                                  choices=[(0, '-'), (140, '1 Serving (~140 cal)'), (280, '2 Servings (~280 cal)'),
                                           (400, '3 Servings (~400 cal)')])

####################################################################################################
######################################## MATTHEW APP ROUTE #########################################
@app.route('/food_info')
def food_info():
    return render_template('Food_Information.html')

@app.route('/fud', methods= ["GET", "POST"])
def fud():
    form = Fud_Select(request.form)
    if request.method == "POST":
        name = form.name.data
        f_time = form.time.data
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

        food_q = Food_Select(name, f_time, food_quantity, food_quantity2, food_quantity3, food_quantity4, food_quantity5, food_quantity6,
                             food_quantity7, food_quantity8, food_quantity9, food_quantity10, food_quantity11, food_quantity12)

        food_q_db = root.child('food_quantity')
        food_q_db.push({
            "f_name": food_q.get_name(),
            "f_time": food_q.get_f_time(),
            "Steamed Rice": food_q.get_food_quantity(),
            "Vegetable Porridge": food_q.get_food_quantity2(),
            "Mixed Rice": food_q.get_food_quantity3(),
            "Vegetable Fusilli": food_q.get_food_quantity4(),
            "Mixed Fruit Yogurt": food_q.get_food_quantity5(),
            "Mushroom Soup": food_q.get_food_quantity6(),
            "Yogurt Special": food_q.get_food_quantity7(),
            "Steamed Salmon": food_q.get_food_quantity8(),
            "Salad & Eggs": food_q.get_food_quantity9(),
            "Breakfast Set": food_q.get_food_quantity10(),
            "Vegetables & Rice": food_q.get_food_quantity11(),
            "Breakfast Omelette": food_q.get_food_quantity12(),
            "totalcal" : food_q.getTotalcalorie(),
        })

        return redirect(url_for("fud"))

    return render_template('Fud.html', form=form, list1=list)

@app.route('/CalIntake')
def calintake():
    ref = db.reference('food_quantity')
    food_q = ref.get()

    return render_template('Your_Calorie_Intake.html', food_q = food_q )

@app.route('/delete/<food_q>')

def delete(food_q):
    root.child('food_quantity').child(food_q).delete()
    return redirect(url_for('calintake'))

@app.route('/menu', methods=["GET", "POST"])
def food():

    return render_template('food.html')

####################################################################################################
####################################################################################################
####################################################################################################
# --- KIAH ZUO CLASS ---
class Waterer(Form):
    water = TextAreaField("Symptoms")
    water2 = TextAreaField("General Information")
    water3 = TextAreaField("Is Surgery Required for my instance")
    note1= TextAreaField("What are the different type of diabetes")
    note2= TextAreaField("What are some myths about diabetes")
    pain1 = TextAreaField("How long do I need to stay in the hospital")

class Waterer4(Form):
    water41 = SelectField(u'Morning',
                          choices=[(0, '0/4 Jug (0ML)'), (300, '1/4 Jug (300ML)'), (600, '1/2 Jug (600ML)'),
                                   (900, '3/4 Jug ( 900ML) '), (1200, '1 Jug(1200ML)')])
    water42 = SelectField(u'Noon',
                          choices=[(0, '0/4 Jug (0ML)'), (300, '1/4 Jug (300ML)'), (600, '1/2 Jug (600ML)'),
                                   (900, '3/4 Jug ( 900ML) '), (1200, '1 Jug(1200ML)')])
    water43 = SelectField(u'Night',
                          choices=[(0, '0/4 Jug (0ML)'), (300, '1/4 Jug (300ML)'), (600, '1/2 Jug (600ML)'),
                                   (900, '3/4 Jug ( 900ML) '), (1200, '1 Jug(1200ML)')])
    water44 = DateField('Date of Intake ', format='%Y-%m-%d')
    name4=StringField("Name")

class DocComment(Form):
    name=StringField("Patient Name")
    comment1=TextAreaField("Comment")
    date= DateField('Date ', format='%Y-%m-%d')
    date2 = DateField('Estimated date of discharge ', format='%Y-%m-%d')

class Feedbacker(Form):
    feed1=TextAreaField("")
    feed2=SelectField(u'Pain Level',
                          choices=[('1', '1 (Little to no pain )'), ('2', '2 ( Slight pain but bearable )'), ('3', '3 ( Moderate Pain '),('4','4 ( Painful and needs attention )'),('5','Overwhelming Pain')

                                   ])
    name1=StringField("")
    feed3=SelectField(u'Status',
                          choices=[('Refill Jug', 'Require Refilling Of Water'), ('Require Food', 'Need some food'), ('Patient requires clarification regarding Medication', 'Require clarification regarding medication')
                              , ("Require assistance to the toilet","Need help going to the toilet ")
                                   ])
    date = DateField('Date ', format='%Y-%m-%d')

####################################################################################################
######################################## KIAH ZUO APP ROUTE ########################################
@app.route('/viewfeedback')
def viewfeedback():
    feedback = root.child('feedback').get()
    list =[]

    for pubid in feedback:

        eachfeedback= feedback[pubid]

        if eachfeedback['name1'] !="":
            feedbackpatient=Feedback1(eachfeedback['name1'],eachfeedback['feed1'],eachfeedback['feed2'],eachfeedback['feed3'],eachfeedback['date'])
            feedbackpatient.set_pubid(pubid)
            print(feedbackpatient.get_pubid())
            list.append(feedbackpatient)

    return render_template('feedbackview.html', feedback=list)
#patient view own self charting
@app.route('/selfprofile')
def selfprofile():
    water4 = root.child('long').get()
    list = []
    comment=root.child('Doc1').get()
    list2=[]

    for pubid in water4:
        waterdata= water4[pubid]

        if waterdata['water44'] != " ":
            waterdatapatient=Water4(waterdata['water41'],waterdata['water42'],waterdata['water43'],waterdata['water44'],waterdata['name4'])
            waterdatapatient.set_pubid(pubid)
            print(waterdatapatient.get_pubid())
            list.append(waterdatapatient)

    for pubid in comment:
        commentdata = comment[pubid]

        if commentdata['DocComment'] != " ":
            commentdatapatient = DocNote(commentdata['Name'], commentdata['DocComment'], commentdata['Date'],
                                         commentdata['Discharge'])
            commentdatapatient.set_pubid(pubid)
            print(commentdatapatient.get_pubid())
            list2.append(commentdatapatient)

    return render_template('selfprofile.html',comment=list2 ,water4= list)



#view patient input and add doc comment
@app.route('/docprofile', methods=["GET", "POST"])
def docupdate():
    form = DocComment(request.form)
    if request.method == "POST":
        comment = form.comment1.data
        date= str(form.date.data)
        name=form.name.data
        discharge=str(form.date2.data)


        dc = DocNote(name,comment,date,discharge)

        dc_db = root.child("Doc1")
        dc_db.push({
            "Name": dc.return_name(),'DocComment': dc.get_comment1() ,"Date":dc.get_commentdate() ,"Discharge":dc.get_discharge()
        })

    comment=root.child('Doc1').get()
    list2=[]


    water4 = root.child('long').get()
    list = []

    for pubid in comment:
        commentdata= comment[pubid]

        if commentdata['DocComment'] != " ":
                commentdatapatient=DocNote(commentdata['Name'],commentdata['DocComment'],commentdata['Date'],commentdata['Discharge'])
                commentdatapatient.set_pubid(pubid)
                print(commentdatapatient.get_pubid())
                list2.append(commentdatapatient)

    for pubid in water4:

        waterdata = water4[pubid]
        waterdata= water4[pubid]

        if waterdata['water44'] != " ":
            waterdatapatient=Water4(waterdata['water41'],waterdata['water42'],waterdata['water43'],waterdata['water44'],waterdata['name4'])
            waterdatapatient.set_pubid(pubid)
            print(waterdatapatient.get_pubid())
            list.append(waterdatapatient)

    return render_template('docprofile.html',form=form ,comment=list2,water4= list)



@app.route('/doctorselect')
def doctorselect():
    return render_template('doctorselect.html')


@app.route('/diabetesedit')
def diabetesedit():
    water = root.child('water').get()
    list = []

    for pubid in water:

        admindata = water[pubid]

        if admindata['Note1'] != " ":
            admindatapage = Water(admindata['Water'], admindata['Water2'], admindata['Water3'], admindata['Note1'],
                                  admindata['Pain1'], admindata['Note2'])
            admindatapage.set_pubid(pubid)
            print(admindatapage.get_pubid())
            list.append(admindatapage)

    return render_template('diabetes.html', water=list)


# allow admin to edit the wiki
@app.route('/editwiki')
def diabetes():
    water = root.child('water').get()
    list = []

    for pubid in water:

        admindata=water[pubid]

        if admindata['Note1'] != " ":
            admindatapage=Water(admindata['Water'],admindata['Water2'],admindata['Water3'],admindata['Note1'],admindata['Pain1'],admindata['Note2'])
            admindatapage.set_pubid(pubid)
            print(admindatapage.get_pubid())
            list.append(admindatapage)

    return render_template('diabetesedit.html', water=list)

#going to the wiki page
@app.route('/wiki')
def Wiki():
    return render_template('wiki.html')

#go to the patient select page
@app.route('/select')
def select():
    return render_template('select.html')


#allow admin to add stuff to the wiki
@app.route('/adminwiki', methods=["GET", "POST"])
def tracker():
    form = Waterer(request.form)
    if request.method=="POST":
        fire = form.water.data
        fire2= form.water2.data
        fire3= form.water3.data

        fire6= form.note1.data
        fire7= form.note2.data
        fire8 = form.pain1.data


        fire10= Water(fire,fire2,fire3,fire6,fire7,fire8)

        water_db = root.child('water')
        water_db.push({
            'Water': fire10.get_water(),
            "Water2": fire10.get_water2(),
            "Water3": fire10.get_water3(),
            "Note1": fire10.get_note1(),
            "Note2": fire10.get_note2(),
            "Pain1": fire10.get_pain1(),

        })
    return render_template('tracker.html',form=form)

# update wiki
@app.route('/updatewiki/<string:id>/', methods=['GET','POST'])
def update_wiki(id):
    form=Waterer(request.form)
    if request.method=='POST':
        general=form.water2.data
        symptoms=form.water.data
        surgery=form.water3.data
        types=form.note1.data
        longtermeffect=form.pain1.data
        stay=form.note2.data

        wikiupdate=Water(symptoms,general,surgery,types,stay,longtermeffect)
        wikiupdate_db= root.child('water/'+id)

        wikiupdate_db.set({
            "Water2":wikiupdate.get_water2(),
            "Water":wikiupdate.get_water(),
            "Water3":wikiupdate.get_water3(),
            "Note1":wikiupdate.get_note1(),
            "Pain1":wikiupdate.get_pain1(),
            'Note2':wikiupdate.get_note2(),
        })

        flash('Magazine Updated Sucessfully.', 'success')

        return redirect(url_for('diabetes'))
    else:
        url = 'water/'+id
        wikidata=root.child(url).get()

        if wikidata['Water'] != " ":
            wikiadmin= Water(wikidata['Water'],wikidata['Water2'],wikidata['Water3'],wikidata['Note1'],wikidata['Note2'],wikidata['Pain1'])
            wikiadmin.set_pubid((id))
            form.water2.data=wikiadmin.get_water2()
            form.water.data=wikiadmin.get_water()
            form.water3.data=wikiadmin.get_water3()
            form.note1.data=wikiadmin.get_note1()
            form.pain1.data=wikiadmin.get_pain1()
            form.note2.data=wikiadmin.get_note2()

        return render_template('updatewiki.html',form=form)


# Update the user intake
@app.route('/updatelong/<string:id>/', methods=['GET', 'POST'])
def update_publication(id):
    form = Waterer4(request.form)
    if request.method == 'POST':
            morning=form.water41.data
            afternoon=form.water42.data
            night=form.water43.data
            date=str(form.water44.data)
            name=form.name4.data

            longupdate = Water4(morning,afternoon,night,date,name)
            longupdate_db = root.child('long/' + id)

            longupdate_db.set({
                "water41":longupdate.get_water41(),
                "water42":longupdate.get_water42(),
                "water43":longupdate.get_water43(),
                "water44":longupdate.get_water44(),
                "name4":longupdate.get_name4()

            })

            flash('Magazine Updated Sucessfully.', 'success')

            return redirect(url_for('selfprofile'))

    else:
        url = 'long/'+id
        waterdata = root.child(url).get()

        if waterdata['name4'] != " ":
            waterdatapatient = Water4(waterdata['water41'], waterdata['water42'], waterdata['water43'],
                                          waterdata['water44'], waterdata['name4'])
            waterdatapatient.set_pubid(id)
            form.water44.data=datetime.strptime(waterdatapatient.get_water44(), '%Y-%m-%d')
            form.water43.data=waterdatapatient.get_water43()
            form.water42.data=waterdatapatient.get_water42()
            form.water41.data=waterdatapatient.get_water41()
            form.name4.data=waterdatapatient.get_name4()

        return render_template('updatelong.html',form=form)


#doctor comment deletion
@app.route('/delete_comment/<string:id>',methods=['POST'])
def delete_comment(id):
    dc_db = root.child('Doc1/'+id)
    dc_db.delete()

    return redirect(url_for('docupdate'))


#Self charting Deletion
@app.route('/delete_publication/<string:id>', methods=['POST'])
def delete_publication(id):
    mag_db = root.child('long/' + id)
    mag_db.delete()

    return redirect(url_for('selfprofile'))

#Input for self tracker
@app.route('/trackerlong', methods=["GET","POST"])
def longterm():
    form = Waterer4(request.form)
    if request.method=="POST":
        cloud=form.water41.data
        cloud2=form.water42.data
        cloud3=form.water43.data
        cloud4=str(form.water44.data)
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

# feed back page for users to push
@app.route('/feedbackpage', methods=["GET","POST"])
def feedback():
    form = Feedbacker(request.form)
    if request.method=="POST":
        earth = form.feed1.data
        earth1= form.feed2.data
        earth2= form.name1.data
        earth3=form.feed3.data
        date=str(form.date.data)


        earth10= Feedback1(earth,earth1,earth2,earth3,date)

        water_db = root.child('feedback')
        water_db.push({
            'feed1': earth10.get_feed1(),
            "feed2": earth10.get_feed2(),
            "name1": earth10.get_name1(),
            "feed3": earth10.get_feed3(),
            "date":earth10.get_date()
        })
    return render_template('feedback.html', form=form)

####################################################################################################
####################################################################################################
####################################################################################################
# --- YODI CLASSS ---
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
    scheduledate = DateField('Schedule Checkup ', format='%Y-%m-%d')
    contactname = StringField('')
    email = StringField('')
    emergency = IntegerField('', [validators.NumberRange(min=8, message='Invalid number provided')])
    time = TimeField('', format='%H:%M')

####################################################################################################
########################################## YODI APP ROUTE ##########################################
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
        nric = form.nric.data.upper()
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
        time = str(form.time.data)

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


@app.route('/patientdb')
def patientdb():
    booked = root.child('Checkup').get()
    list = []

    for pubid in booked:

        bookedpatients = booked[pubid]

        if bookedpatients['fullname']:
            bookedpatient = Schedule(bookedpatients['fullname'], bookedpatients['gender'], bookedpatients['contact'], bookedpatients['address'],
                                     bookedpatients['dateofbirth'], bookedpatients['nric'], bookedpatients['condition'],
                                     bookedpatients['email'], bookedpatients['scheduledate'],bookedpatients['emergencycontactname'], 
                                     bookedpatients['emergencycontact'], bookedpatients['time'])

            bookedpatient.set_pubid(pubid)
            print(bookedpatient.get_pubid())
            list.append(bookedpatient)

    return render_template('patientdb.html', booked=list)


@app.route('/updatesched/<string:id>/', methods=["GET","POST"])
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
        emergency = form.emergency.data
        time = str(form.time.data)

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
            bookedpatient = Schedule(bookedpatients['fullname'], bookedpatients['gender'], bookedpatients['contact'], 
                                     bookedpatients['address'], bookedpatients['dateofbirth'], bookedpatients['nric'], 
                                     bookedpatients['condition'], bookedpatients['email'], bookedpatients['scheduledate'],
                                     bookedpatients['emergencycontactname'],bookedpatients['emergencycontact'], bookedpatients['time'])

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
            form.time.data = datetime.strptime(bookedpatient.get_time(), '%H:%M:%S')

        return render_template('updatepatient.html', form=form)


@app.route('/patientsdatabase')
def patientsdb():
    patientdata = root.child('Patient_Information').get()
    list = []

    for pubid in patientdata:

        patient = patientdata[pubid]

        if patient['firstname']:
            patientsdata = Patient(patient['firstname'], patient['lastname'], patient['gender'], 
                                   patient['contact'], patient['address'], patient['zip'], 
                                   patient['dateofbirth'], patient['admission date'], patient['nric'])

            patientsdata.set_pubid(pubid)
            print(patientsdata.get_pubid())
            list.append(patientsdata)

    return render_template('patientsdb.html', patient=list)


@app.route('/updateinfo/<string:id>/', methods=["GET","POST"])
def update_patientinfo(id):
    form = Patients(request.form)
    if request.method == "POST" and form.validate():
        fname = form.firstname.data
        lname = form.lastname.data
        gender = form.gender.data
        address = form.address.data
        contact = form.contact.data
        zip = form.zip.data
        nric = form.nric.data.upper()
        date_o_birth = str(form.date_o_birth.data)
        admission_date = str(form.admission_date.data)

        pdb = Patient(fname, lname, gender, contact, address, zip, date_o_birth, admission_date, nric)

        pdb_db = root.child('Patient_Information/'+ id)
        pdb_db.set({
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
        flash('Updated successfully', 'success')
        return redirect(url_for('patientsdb'))
    else:
        url = 'Patient_Information/'+id
        patient = root.child(url).get()

        if patient['firstname']:
            patientsdata = Patient(patient['firstname'], patient['lastname'], patient['gender'], 
                                   patient['contact'], patient['address'], patient['zip'], 
                                   patient['dateofbirth'], patient['admission date'], patient['nric'])
            patientsdata.set_pubid(id)
            form.firstname.data = patientsdata.get_fname()
            form.lastname.data = patientsdata.get_lname()
            form.gender.data = patientsdata.get_gender()
            form.address.data = patientsdata.get_gender()
            form.contact.data = patientsdata.get_mobile()
            form.zip.data = patientsdata.get_zip()
            form.nric.data = patientsdata.get_nric()
            form.date_o_birth.data = datetime.strptime(patientsdata.get_dateobirth(), '%Y-%m-%d')
            form.admission_date.data = datetime.strptime(patientsdata.get_admissiondate(), '%Y-%m-%d')

        return render_template('updateinfo.html', form=form)

####################################################################################################
####################################################################################################
####################################################################################################
# --- GARETH ClASS---
class EventForms(Form):
    title = StringField('Event Title')
    location = StringField('Event Location')
    date = StringField('Event Date and time')
    time = SelectField('', choices=[('', 'Select'), ('6:00', '6:00'), ('6.30', '6.30'),
                                                ('7:00', '7:00'), ('7:30', '7:30'), ('8:00', '8:00'), ('8:30', '8:30'),
                                                ('9:00', '9:00'), ('9:30', '9:30'), ('10:00', '10:00'),
                                                ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'),
                                                ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'),
                                                ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'),
                                                ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'),
                                                ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'),
                                                ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'),
                                                ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'),
                                                ('21:00', '21:00')], default='')
    description = TextAreaField('Event Description')
####################################################################################################
######################################### Gareth APP ROUTE #########################################
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/events', methods=["GET", "POST"])
def events():
    form = EventForms(request.form)
    if request.method == "POST":
        title = form.title.data
        location = form.location.data
        date = form.date.data
        time = form.time.data
        desc = form.description.data
        es = event_submissions(title, location, date, time, desc)

        event_form = root.child('Event_Data')
        event_form.push({
            'title': es.get_event_title(),
            'location': es.get_event_location(),
            'date': es.get_event_date(),
            'time': es.get_event_time(),
            'desc': es.get_event_desc(),
        })
        return redirect(url_for('events'))

    try:
        ev = root.child('Event_Data').get()
        list_ev = []
        for data in ev:
            i = ev[data]
            if i['title']:
                ev_data = event_submissions(i['title'], i['location'], i['date'], i['time'], i['desc'])
                ev_data.set_data(data)
                list_ev.append(ev_data)

    except:
        TypeError

    return render_template('Events.html', form=form)
####################################################################################################
####################################################################################################
####################################################################################################
# --- KHEE HING  CLASS---
class Aft_dis(Form):
    nric = StringField("", [validators.Regexp("^[STFG]\d{7}[A-Z]$" ,message = "Wrong NRIC format")])
    status = RadioField("",choices=[('0 - 33','0% - 33%'),('34 - 66','34% - 66'),('67 -  99','67% - 99%')])
    
    eye_bv = BooleanField('Blurred vision')
    eye_sp = BooleanField('Spots or lines in your vision')
    eye_we = BooleanField('Watery eyes')
    eye_ed = BooleanField('Eye discomfort')
    eye_lo = BooleanField('Loss of vision')
    
    kiney_sw = BooleanField('Swelling of the hands, feet, and face')
    kiney_wg = BooleanField('Weight gain from edema')
    kiney_id = BooleanField('Itching and/or drowsiness. (This can occur with end stage kidney disease)')
    
    heart_brain_so = BooleanField('Shortness of breath')
    heart_brain_ff = BooleanField('Feeling faint')
    heart_brain_fd = BooleanField('Feeling dizzy')
    heart_brain_sw = BooleanField('Sweating')
    heart_brain_n = BooleanField('Nausea')
    heart_brain_cp = BooleanField('Chest pain or pressure')
    heart_brain_sj = BooleanField('Pain in the shoulders, jaw, and left arm')
    
    feet_ = BooleanField('any of the symptoms above')
    
    nerves_bp = BooleanField('Burning pain')
    nerves_n = BooleanField('Numbness')
    nerves_to = BooleanField('Tingling or loss of feeling in the feet or lower legs')
    nerves_cd = BooleanField('Constipation and diarrhea')
    nerves_pw = BooleanField('Problems with sexual function')

    neuropathy_pn = BooleanField('Peripheral neuropathy: damage to the peripheral nervous system')
    neuropathy_at = BooleanField('Autonomic Type I: damage to the nerves of internal organs')
    neuropathy_gm = BooleanField('Gastroparesis: movement of food through the stomach slows or stops')
    neuropathy_ph = BooleanField('Postural hypotension: drop in blood pressure due to change in body position')
    neuropathy_ud = BooleanField('Uncontrolled diarrhea')

    medication = TextAreaField("Do you have any problems with your medication?<small>&nbsp;if yes please state</small>")
    others = TextAreaField("Do you have any other enquires ?")

class BloodA(Form):
    month = IntegerField("Month", [validators.NumberRange(min=1, max=12, message='Invalid month')])
    day = IntegerField("Day", [validators.NumberRange(min=1, max=31, message='Invalid day')])
    blood_glucose = FloatField("Blood Glucose (mmol/L)")
    systolic = IntegerField("Systolic")
    diastolic = IntegerField("Diastolic")
    weight = FloatField("Weight (KG)")
    height = FloatField("Height (M)")
    text_doc = StringField("Text")

####################################################################################################
######################################## KHEE HING APP ROUTE #######################################
@app.route('/add', methods=["GET", "POST"])
def after_discharge_display():
    form = Aft_dis(request.form)
    bmi = root.child('outpatient').get()
    list = []
    try:
        for data in bmi:
            i = bmi[data]
            if 'nric' in i:
                if i['nric']:
                    bmi_data = Information( i['nric'], i['status'], 
                                            i['eye_bv'], i['eye_sp'], i['eye_we'], i['eye_ed'], i['eye_lo'], 
                                            i['kiney_sw'], i['kiney_wg'], i['kiney_id'], 
                                            i['heart_brain_so'], i['heart_brain_ff'], i['heart_brain_fd'], i['heart_brain_sw'], i['heart_brain_n'], i['heart_brain_cp'], i['heart_brain_sj'], 
                                            i['feet_'], 
                                            i['nerves_bp'], i['nerves_n'], i['nerves_to'], i['nerves_cd'], i['nerves_pw'], 
                                            i['neuropathy_pn'], i['neuropathy_at'], i['neuropathy_gm'], i['neuropathy_ph'], i['neuropathy_ud'],
                                            i['medication'], i['others'])
                    # bmi_data.set_data(data)
                    # list.append(bmi_data)
                    # if 'eye_bv' == True:
                    # bmi_data = Information(i['eye_bv'])
                    bmi_data.set_data(data)
                    list.append(bmi_data)
                    
    except:
        TypeError
    return render_template('After_discharge_display.html', bmi = list)

@app.route('/after_discharge', methods=["GET", "POST"])
def after_discharge():
    form = Aft_dis(request.form)
    if request.method == "POST" and form.validate():
        nric = form.nric.data
        status = form.status.data

        eye_bv = form.eye_bv.data
        eye_sp = form.eye_sp.data
        eye_we = form.eye_we.data
        eye_ed = form.eye_ed.data
        eye_lo = form.eye_lo.data

        kiney_sw = form.kiney_sw.data
        kiney_wg = form.kiney_wg.data
        kiney_id = form.kiney_id.data

        heart_brain_so = form.heart_brain_so.data
        heart_brain_ff = form.heart_brain_ff.data
        heart_brain_fd = form.heart_brain_fd.data
        heart_brain_sw = form.heart_brain_sw.data
        heart_brain_n = form.heart_brain_n.data
        heart_brain_cp = form.heart_brain_cp.data
        heart_brain_sj = form.heart_brain_sj.data

        feet_ = form.feet_.data

        nerves_bp = form.nerves_bp.data
        nerves_n = form.nerves_n.data
        nerves_to = form.nerves_to.data
        nerves_cd = form.nerves_cd.data
        nerves_pw = form.nerves_pw.data

        neuropathy_pn = form.neuropathy_pn.data
        neuropathy_at = form.neuropathy_at.data
        neuropathy_gm = form.neuropathy_gm.data
        neuropathy_ph = form.neuropathy_ph.data
        neuropathy_ud = form.neuropathy_ud.data

        medication = form.medication.data
        others = form.others.data  
        currentuser = root.child('loggedin').get()
        info = Information( nric, status, 
                            eye_bv, eye_sp, eye_we, eye_ed, eye_lo,
                            kiney_sw, kiney_wg, kiney_id,
                            heart_brain_so, heart_brain_ff, heart_brain_fd, heart_brain_sw, heart_brain_n, heart_brain_cp, heart_brain_sj,
                            feet_,
                            nerves_bp, nerves_n, nerves_to, nerves_cd, nerves_pw,
                            neuropathy_pn, neuropathy_at, neuropathy_gm, neuropathy_ph, neuropathy_ud,
                            medication, others)
        info_db = root.child("outpatient")
        if nric :
            info_db.push({
                'nric': info.get_nric(),
                'status': info.get_status(),
                'eye_bv': info.get_eye_bv(),
                'eye_sp': info.get_eye_sp(),
                'eye_we': info.get_eye_we(),
                'eye_ed': info.get_eye_ed(),
                'eye_lo': info.get_eye_lo(),

                'kiney_sw': info.get_kiney_sw(),
                'kiney_wg': info.get_kiney_wg(),
                'kiney_id': info.get_kiney_id(),

                'heart_brain_so': info.get_heart_brain_so(),
                'heart_brain_ff': info.get_heart_brain_ff(),
                'heart_brain_fd': info.get_heart_brain_fd(),
                'heart_brain_sw': info.get_heart_brain_sw(),
                'heart_brain_n': info.get_heart_brain_n(),
                'heart_brain_cp': info.get_heart_brain_cp(),
                'heart_brain_sj': info.get_heart_brain_sj(),

                'feet_': info.get_feet_(),

                'nerves_bp': info.get_nerves_bp(),
                'nerves_n': info.get_nerves_n(),
                'nerves_to': info.get_nerves_to(),
                'nerves_cd': info.get_nerves_cd(),
                'nerves_pw': info.get_nerves_pw(),

                'neuropathy_pn': info.get_neuropathy_pn(),
                'neuropathy_at': info.get_neuropathy_at(),
                'neuropathy_gm': info.get_neuropathy_gm(),
                'neuropathy_ph': info.get_neuropathy_ph(),
                'neuropathy_ud': info.get_neuropathy_ud(),

                'medication': info.get_medication(),
                'others': info.get_others(),
            })
        return redirect(url_for('after_discharge'))

    return render_template('After_discharge.html', form = form)

@app.route('/chronic_illness', methods=["GET", "POST"])
def chronic_illness_():
    form = BloodA(request.form)
    if request.method == "POST" and form.validate():
        month = form.month.data
        month -= 1 
        day = form.day.data
        systolic = form.systolic.data
        diastolic = form.diastolic.data
        blood_glucose = form.blood_glucose.data
        weight = form.weight.data
        height = form.height.data
        bg = BloodGlucose(month, day, blood_glucose)
        bp = BloodPressure(month, day, systolic, diastolic)
        bmi = Bmi(month, day, weight, height)

        bp_db = root.child('Diabetes_bp')
        bg_db = root.child('Diabetes_bg')
        bmi_db = root.child('Diabetes_bmi')

        if diastolic and systolic:
            bp_db.push({
                'month': bp.get_month(),
                'day': bp.get_day(),
                'systolic': bp.get_systolic(),
                'diastolic': bp.get_diastolic(),
            })
        elif blood_glucose:
            bg_db.push({
                'month': bg.get_month(),
                'day': bg.get_day(),
                'blood glucose': bg.get_blood_glucose(),
            })
        elif weight and height:
            bmi_db.push({
                'day': bmi.get_day(),
                'month': bmi.get_month(),
                'weight': bmi.get_weight(),
                'height': bmi.get_height(),
                'bmi': bmi.get_bmi(),
            })
        return redirect(url_for('chronic_illness_'))

    bp = root.child('Diabetes_bp').get()
    bg = root.child('Diabetes_bg').get()
    bmi = root.child('Diabetes_bmi').get()

    list_bg = []
    list_bp = []
    list_bmi = []
    
    try:
        for data in bp:
            i = bp[data]
            if 'systolic' and 'diastolic' in i:
                if i['systolic'] and i['diastolic']:
                    db_data = BloodPressure(i['month'], i['day'], i['systolic'],i['diastolic'])
                    db_data.set_data(data)
                    list_bp.append(db_data)
        for data in bg:
            j = bg[data]
            if 'blood glucose' in j:
                if j['blood glucose']:
                    db_data = BloodGlucose(j['month'], j['day'], j['blood glucose'])
                    db_data.set_data(data)
                    list_bg.append(db_data)
        for data in bmi:
            k = bmi[data]
            if 'weight' and 'height' in k:
                if k['bmi']:
                    db_data = Bmi(k['month'], k['day'], k['weight'], k['height'])
                    db_data.set_data(data)
                    list_bmi.append(db_data)
    except:
        TypeError

    return render_template('Chronic_illness_patient.html', form=form, bp=list_bp, bg=list_bg, bmi=list_bmi)

###**  #######  ##    #  ####    **###
###**  #        # #   #  #   #   **###
###**  #####    #  #  #  #    #  **###
###**  #        #   # #  #   #   **###
###**  #######  #    ##  ####    **###
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
