

class Feedback1:

    def __init__(self,name1,feed1,feed2,feed3,date):
        self.__pubid = ''
        self.__feed1=feed1
        self.__feed2=feed2
        self.__name1=name1
        self.__feed3=feed3
        self.__date=date

    def get_date(self):
        return self.__date

    def set_date(self,date):
        self.__date=date

    def get_pubid(self):
        return self.__pubid

    def set_pubid(self, pubid):
        self.__pubid = pubid


    def set_feed3(self,feed3):
        self.__feed3=feed3

    def get_feed3(self):
        return self.__feed3


    def set_name1(self,name1):
        self.__name1=name1

    def get_name1(self):
        return self.__name1

    def set_feed1(self,feed1):
        self.__feed1=feed1

    def get_feed1(self):
        return self.__feed1

    def set_feed2(self,feed2):
        self.__feed2=feed2

    def get_feed2(self):
        return self.__feed2


