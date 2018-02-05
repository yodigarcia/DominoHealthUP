class event_submissions:
    def __init__(self, event_title, event_location, event_date, event_time, event_desc):
        self.__data = ''
        self.__event_title = event_title
        self.__event_location = event_location
        self.__event_date = event_date
        self.__event_time = event_time
        self.__event_desc = event_desc

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_event_title(self, event_title):
        self.__event_title = event_title

    def get_event_title(self):
        return self.__event_title

    def set_event_location(self, event_location):
        self.__event_location = event_location

    def get_event_location(self):
        return self.__event_location

    def set_event_date(self, event_date):
        self.__event_date = event_date

    def get_event_date(self):
        return self.__event_date

    def set_event_time(self, event_time):
        self.__event_time = event_time

    def get_event_time(self):
        return self.__event_time

    def set_event_desc(self, event_desc):
        self.__event_desc = event_desc

    def get_event_desc(self):
        return self.__event_desc