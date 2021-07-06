class Date:
    @staticmethod
    def is_date_valid(date_string):
        year,month,day=map(int,date_string.split('-'))
        return month <=12 and day <=31
