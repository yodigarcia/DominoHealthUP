class DocNote:
    def __init__(self,name,comment1,date,date2):
        self.__pubid = ''
        self.__name=name
        self.__comment1=comment1
        self.__date2=date2
        self.__date=date

    def set_name(self,name):
        self.__name=name

    def return_name(self):
        return self.__name

    def get_comment1(self):
        return self.__comment1

    def set_comment1(self,comment1):
        self.__comment1=comment1

    def get_commentdate(self):
        return self.__date

    def set_commentdate(self,date):
        self.__date=date


    def get_pubid(self):
        return self.__pubid

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def set_discharge(self,date2):
        self.__date2=date2

    def get_discharge(self):
        return self.__date2
