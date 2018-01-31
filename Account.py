class Account:

    def __init__(self, username, password):
        self.__pubid = ''
        self.__username = username
        self.__password = password

    def get_pubid(self):
        return self.__pubid

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def set_user(self, user):
        self.__username = user

    def set_passw(self, passw):
        self.__password = passw
