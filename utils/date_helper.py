from datetime import datetime, timedelta


class DateHelper:

    @staticmethod
    def get_delivery_date(days_from_now=1):
        return (datetime.now() + timedelta(days=days_from_now)).strftime("%d.%m.%Y")