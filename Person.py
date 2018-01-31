class Person:

    def __init__(self, gender, contact, address, dateobirth, nric):
        self.__gender = gender
        self.__mobile = contact
        self.__address = address
        self.__nric = nric
        self.__dateobirth = dateobirth

    def get_gender(self):
        return self.__gender

    def get_mobile(self):
        return self.__mobile

    def get_address(self):
        return self.__address

    def get_dateobirth(self):
        return self.__dateobirth

    def get_nric(self):
        return self.__nric
