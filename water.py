class Water:

    def __init__(self,water,water2,water3,note1,note2,pain1):
        self.__pubid = ''
        self.__water=water
        self.__water2=water2
        self.__water3=water3
        self.__note1=note1
        self.__note2=note2
        self.__pain1 = pain1

    def get_pubid(self):
        return self.__pubid

    def set_pubid(self, pubid):
        self.__pubid = pubid


    def set_water(self,water):
        self.__water=water

    def get_water(self):
        return self.__water

    def set_water2(self,water2):
        self.__water2=water2

    def get_water2(self):
        return self.__water2

    def set_water3(self,water3):
        self.__water=water3

    def get_water3(self):
        return self.__water3



    def set_note1(self,note1):
        self.__note1=note1

    def get_note1(self):
        return self.__note1

    def set_note2(self,note2):
        self.__note2=note2

    def get_note2(self):
        return self.__note2

    def set_pain1(self,pain1):
        self.__pain1=pain1

    def get_pain1(self):
        return self.__pain1


