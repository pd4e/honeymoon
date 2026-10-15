from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class AgeCalculator:
    def __init__(self, birth_date, gender, start_date):
        # 성별 정보에 따라 출생년도 접두사 결정
        prefix = "19" if gender in ["1", "2", "5", "6"] else "20"
        birth_year = int(prefix + birth_date[:2])
        self.birth_date = datetime.strptime(str(birth_year) + birth_date[2:], '%Y%m%d')
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')

    def calculate_age(self):
        age = self.start_date.year - self.birth_date.year
        m = self.start_date.month - self.birth_date.month
        d = self.start_date.day - self.birth_date.day

        # 만 나이 계산
        full_age = age
        if m < 0 or (m == 0 and d < 0):
            full_age -= 1

        # print(full_age)
        # 보험 나이 계산
        insu_age = full_age

        # 6개월 후의 날짜 계산
        # half_year_later = self.birth_date + timedelta(days=365*full_age + 190)
        half_year_later = self.birth_date + relativedelta(years=full_age, months=6)

        print(self.birth_date, half_year_later, self.start_date, full_age)
        # 대조일이 6개월 후의 날짜보다 크거나 같으면 보험 나이에 1을 더함
        if self.start_date >= half_year_later:
            insu_age += 1

        return insu_age
