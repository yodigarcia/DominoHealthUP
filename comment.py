class DocNote:
    def __init__(self,comment1,date):
        self.__pubid = ''
        self.__comment1=comment1
        self.__date=date

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
