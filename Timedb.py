class Timedb:

    def __init__(self, date, opening, close):
        self.__date = date
        self.__open = opening
        self.__close = close
        self.__id = ""

    def get_date(self):
        return self.__date

    def get_open(self):
        return self.__open

    def get_close(self):
        return self.__close

    def get_id(self):
        return self.__id
        
    def set_id(self, id):
        self.__id = id

