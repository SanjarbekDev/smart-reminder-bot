from datetime import datetime
import pytz



class livetime:
    def __init__(self,time_zone:str) -> None:
        self.time_zone=time_zone

    def get_time(self)->list:
        time_uts=pytz.timezone(self.time_zone)
        dt=datetime.now(time_uts)
        return list(dt.strftime('%Y %m %d %w %H:%M %S').split())

    def get_sql_format(self):
        time_uts=pytz.timezone(self.time_zone)
        dt=datetime.now(time_uts)
        return dt.strftime("%d-%m")

    def show_time_zone():
        return pytz.all_timezones[260:310]



