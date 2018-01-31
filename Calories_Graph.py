class Calories:
    def __init__(self, time, calories):
        self.__pubid = ''
        self.time = time
        self.calories = calories

    def get_pubid(self):
        return self.__pubid

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_calories(self, calories):
        self.calories = calories

    def get_calories(self):
        return self.calories
