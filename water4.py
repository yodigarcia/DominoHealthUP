
class Water4:
    def __init__(self,water41,water42,water43,water44,name4):
        self.__pubid = ''
        self.__water41=water41
        self.__water42=water42
        self.__water43=water43
        self.__water44=water44
        self.__name4=name4

    def set_name4(self,name4):
        self.__name4=name4

    def get_name4(self):
        return self.__name4

    def get_pubid(self):
        return self.__pubid

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def get_water41(self):
        return self.__water41

    def get_water42(self):
        return self.__water42

    def get_water43(self):
        return self.__water43

    def get_water44(self):
        return self.__water44

    def set_water41(self,water41):
        self.__water41=water41

    def set_water42(self,water42):
        self.__water42=water42

    def set_water43(self,water43):
        self.__water43=water43

    def set_water44(self,water44):
        self.__water44=water44

    def sum_intake(self):
        return self.__water41+self.__water42+self.__water43


