# For the Graph
class Date:
    def __init__(self, month, day):
        self.__month = month
        self.__day = day
        self.__data = ''

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_day(self):
        return self.__day

    def set_day(self, day):
        self.__day = day

    def get_month(self):
        return self.__month

    def set_month(self, month):
        self.__month = month


class BloodPressure(Date):
    def __init__(self, month, day, blood_pressure):
        super().__init__(month, day)
        self.__blood_pressure = blood_pressure

    def get_blood_pressure(self):
            return self.__blood_pressure

    def set_blood_pressure(self, blood_pressure):
            self.__blood_pressure = blood_pressure


class BloodGlucose(Date):
    def __init__(self, month, day, blood_glucose):
        super().__init__(month, day)
        self.__blood_glucose = blood_glucose

    def get_blood_glucose(self):
        return self.__blood_glucose

    def set_blood_glucose(self, blood_glucose):
        self.__blood_glucose = blood_glucose


class Weight(Date):
    def __init__(self,month , day, weight):
        super().__init__(month,day)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

class Information():
    def __init__(self, zero, one, two, three, four):
        self.__informationzero = zero
        self.__informationone = one
        self.__informationtwo = two
        self.__informationthree = three
        self.__informationfour = four
        
    def get_informationzero(self):
        return self.__informationzero
    def set_informationzero(self,informationzero):
        self.__informationzero = informationzero
        
    def get_informationone(self):
        return self.__informationone
    def set_information1(self,informationone):
        self.__informationone = informationone
        
    def get_informationtwo(self):
        return self.__informationtwo
    def set_informationtwo(self,informationtwo):
        self.__informationtwo = informationtwo
        
    def get_informationthree(self):
        return self.__informationthree
    def set_informationthree(self,informationthree):
        self.__informationthree = informationthree
        
    def get_informationfour(self):
        return self.__informationfour
    def set_informationfour(self,informationfour):
        self.__informationfour = informationfour