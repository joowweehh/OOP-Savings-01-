class Statement():
    def __init__(self,month,week,dates,amount):
        self.__month = month
        self.__week = week
        self.__dates = dates
        self.__amount = amount

    def get_month(self):
        return self.__month
    def get_week(self):
        return self.__week
    def get_dates(self):
        return self.__dates
    def get_amount(self):
        return self.__amount

    def set_month(self,month):
        self.__month = month
    def set_week(self,week):
        self.__week = week
    def set_dates(self,dates):
        self.__dates = dates
    def set_amount(self,amount):
        self.__amount = amount
