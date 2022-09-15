from datetime import datetime, timedelta, date


class Time:
    _FORMAT = '%Y-%m-%d'
    _INQUIRE_LIMIT_DAYS = 60

    @classmethod
    def _parse_date(cls, date_, format_=None):
        if not date_:
            return date.today()
        elif isinstance(date_, date):
            return date_
        elif isinstance(date_, datetime):
            return datetime.date()
        elif isinstance(date_, str):
            return datetime.strptime(date_, format_ or cls._FORMAT).date()
        raise Exception('Error')

    @classmethod
    def middle_time(cls, start_date, end_date=None):
        start_on = cls._parse_date(date_=start_date)
        end_on = cls._parse_date(date_=end_date)
        if end_on < start_on:
            raise ValueError('結束日期必須大於開始日期')
        interval = end_on - start_on
        days = interval.days
        if days > cls._INQUIRE_LIMIT_DAYS:
            raise ValueError(f'間距必須小於{cls._INQUIRE_LIMIT_DAYS}')
        return [start_on + timedelta(days=day) for day in range(days + 1)]


if __name__ == '__main__':
    print(Time.middle_time('2022-6-1'))
