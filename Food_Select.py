
class Food_Select:
    def __init__(self, food_quantity, food_quantity2, food_quantity3, food_quantity4,
                 food_quantity5, food_quantity6, food_quantity7, food_quantity8, food_quantity9,
                 food_quantity10, food_quantity11, food_quantity12):
        self.__pubid = ''
        self.__food_quantity = food_quantity
        self.__food_quantity2 = food_quantity2
        self.__food_quantity3 = food_quantity3
        self.__food_quantity4 = food_quantity4
        self.__food_quantity5 = food_quantity5
        self.__food_quantity6 = food_quantity6
        self.__food_quantity7 = food_quantity7
        self.__food_quantity8 = food_quantity8
        self.__food_quantity9 = food_quantity9
        self.__food_quantity10 = food_quantity10
        self.__food_quantity11 = food_quantity11
        self.__food_quantity12 = food_quantity12

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def get_pubid(self):
        return self.__pubid


    def set_food_quantity(self,food_quantity):
        self.__food_quantity = food_quantity

    def get_food_quantity(self):
        return self.__food_quantity


    def set_food_quantity2(self,food_quantity2):
        self.__food_quantity2 = food_quantity2

    def get_food_quantity2(self):
        return self.__food_quantity2


    def set_food_quantity3(self,food_quantity3):
        self.__food_quantity3 = food_quantity3

    def get_food_quantity3(self):
        return self.__food_quantity3


    def set_food_quantity4(self,food_quantity4):
        self.__food_quantity4 = food_quantity4

    def get_food_quantity4(self):
        return self.__food_quantity4


    def set_food_quantity5(self,food_quantity5):
        self.__food_quantity5 = food_quantity5

    def get_food_quantity5(self):
        return self.__food_quantity5


    def set_food_quantity6(self,food_quantity6):
        self.__food_quantity6 = food_quantity6

    def get_food_quantity6(self):
        return self.__food_quantity6


    def set_food_quantity7(self,food_quantity7):
        self.__food_quantity7 = food_quantity7

    def get_food_quantity7(self):
        return self.__food_quantity7


    def set_food_quantity8(self,food_quantity8):
        self.__food_quantity8 = food_quantity8

    def get_food_quantity8(self):
        return self.__food_quantity8


    def set_food_quantity9(self,food_quantity9):
        self.__food_quantity9 = food_quantity9

    def get_food_quantity9(self):
        return self.__food_quantity9


    def set_food_quantity10(self,food_quantity10):
        self.__food_quantity10 = food_quantity10

    def get_food_quantity10(self):
        return self.__food_quantity10


    def set_food_quantity11(self,food_quantity11):
        self.__food_quantity11 = food_quantity11

    def get_food_quantity11(self):
        return self.__food_quantity11

    def set_food_quantity12(self,food_quantity12):
        self.__food_quantity12 = food_quantity12

    def get_food_quantity12(self):
        return self.__food_quantity12

    def set_total_calories(self, total_calories):
        self.__total_calories = total_calories

    def get_total_calories(self):
        total_calories = self.__food_quantity() + self.__food_quantity2() + self.__food_quantity3() + self.__food_quantity4() + self.__food_quantity5() + self.__food_quantity6() + self.__food_quantity7() + self.__food_quantity8() + self.__food_quantity9() + self.__food_quantity10() + self.__food_quantity11() + self.__food_quantity12()
        return int(total_calories)
