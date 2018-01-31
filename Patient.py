from Person import Person

class Patient(Person):
    def __init__(self, firstname, lastname, gender, contact, address, zip, dateobirth, admissiondate, nric):
        Person.__init__(self, gender, contact, address, dateobirth, nric)
        self.__fname = firstname
        self.__lname = lastname
        self.__zip = zip
        self.__admissiondate = admissiondate
        self.__pubid = ''

    def get_pubid(self):
        return self.__pubid

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_zip(self):
        return self.__zip

    def get_admissiondate(self):
        return self.__admissiondate



