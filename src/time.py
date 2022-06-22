from datetime import datetime, timedelta


class Time:
    today = str(datetime.now().date())

    @classmethod
    def middle_time(cls, start_date=today, end_date=today):
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        date_list = list()
        if end < start:
            raise ValueError('結束日期必須大於開始日期')
        for middle in range((end - start).days):
            if middle == 0:
                continue
            date_list.append(start.date() + timedelta(days=middle))
        # days = [start.date() + timedelta(days=middle) for middle in range((end - start).days +1)]
        return date_list


if __name__ == '__main__':
    print(Time.middle_time('2021-1-1', '2021-1-4'))
