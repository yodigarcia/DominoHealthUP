from Person import Person

class Schedule(Person):

    def __init__(self, fullname, gender, contact, address, dateobirth, nric, condition, email, scheduledate, emgname):
        Person.__init__(self, gender, contact, address, dateobirth, nric)
        self.__pubid = ''
        self.__fullname = fullname
        self.__condition = condition
        self.__email = email
        self.__scheduledate = scheduledate
        self.__emgname = emgname

    def get_pubid(self):
        return self.__pubid

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def get_emgname(self):
        return self.__emgname

    def get_schedule(self):
        return self.__scheduledate

    def get_fullname(self):
        return self.__fullname

    def get_condition(self):
        return self.__condition

    def get_email(self):
        return self.__email


