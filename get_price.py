from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from get_insu_info import AgeCalculator
import json
import pandas as pd
import os

def get_price(self, amounts):
    try:
    # 보험나이 구하기
        age_calculator = AgeCalculator(amounts[2][:6], amounts[2][7], amounts[0])
        personal_info = [age_calculator.calculate_age(), 1 if amounts[2][7] in ['1', '3', '5', '7'] else 2]
        #QMessageBox.information(self, '알림', '70세 이상 보험료가 존재하지 않습니다.')
        print(personal_info)
        # 나이가 70세 이상인 경우
        if personal_info[0] >= 70:
            QMessageBox.information(self, '알림', '70세 이상은 가입할 수 없습니다. ')
            return

    except ValueError:
        QMessageBox.information(self, '알림', '생년월일을 확인 해주세요.')

    # 현재 스크립트 파일이 있는 폴더 경로를 가져옵니다.
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # meritz_price.json 파일의 경로를 생성합니다.
    json_file_path = os.path.join(current_directory, 'meritz_price.json')

    # json 파일을 읽어옵니다.
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    start_date = datetime.strptime(amounts[0], '%Y-%m-%d')
    end_date = datetime.strptime(amounts[1], '%Y-%m-%d')
    # print(start_date, end_date)
    term_day = end_date - start_date

    # print(term_day, personal_info1[0], personal_info2[0])
    if 46 <= term_day.days + 1 <= 60:
        filtered_df1 = df[(df['plan_title'] == 'M0-2') &
                          (df['term_day'] == 60) &
                          (df['sex'] == personal_info[1]) &
                          (df['age'] == personal_info[0])]

    elif 61 <= term_day.days + 1 <= 90:
        filtered_df1 = df[(df['plan_title'] == 'M0-2') &
                          (df['term_day'] == 90) &
                          (df['sex'] == personal_info[1]) &
                          (df['age'] == personal_info[0])]

    else :
        filtered_df1 = df[(df['plan_title'] == 'M0-2') &
                         (df['term_day'] == term_day.days + 1) &
                         (df['sex'] == personal_info[1]) &
                         (df['age'] == personal_info[0])]

    if not filtered_df1.empty:
        price = filtered_df1.iloc[0]['price']
        return price
    else:
        QMessageBox.information(self, '알림', '보험료 계산에 문제가 있습니다.')
        return