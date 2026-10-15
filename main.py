from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QKeySequence
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import pandas as pd
from main_w import Ui_MainWindow
from create_pdf import create_pdf
import re
import win32com.client
from get_price import get_price
from qt_material import apply_stylesheet


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        apply_stylesheet(self, theme='dark_yellow.xml', css_file='style.css')
        self.setWindowTitle("허니문 리조트 : 메리츠 여행자 보험 가입 증서 관리")
        self.open_btn.clicked.connect(self.load_transaction_data)
        # self.open_tobe_btn.setVisible(False)
        self.split_excel_btn.clicked.connect(self.export_excel)
        self.open_tobe_btn.clicked.connect(self.load_tobe_data)
        self.cal_price_btn.clicked.connect(self.cal_price)
        self.pdf_btn.clicked.connect(self.create_pdf)
        # self.excel_edit.setStyleSheet("QLineEdit:!focus { color: #ccc; }")
        self.progress_bar.setStyleSheet("QProgressBar { color: #ccc; }")
        self.list_table.setColumnWidth(0, 100)
        self.list_table.setColumnWidth(1, 120)
        self.list_table.setColumnWidth(2, 100)
        self.list_table.setColumnWidth(3, 100)
        self.list_table.setColumnWidth(4, 130)
        self.list_table.setColumnWidth(5, 300)
        self.progress_bar.setVisible(False)
        self.title.setProperty('class', 'title')
        return

    def load_transaction_data(self):
        # 파일 대화상자 열기
        file_name = QFileDialog.getOpenFileName(self, 'Select File', '', 'Excel Files (*.xlsx)')

        # 확장자를 제외한 파일명 가져오기
        self.excel_edit.setText(file_name[0])

        try:
            # 데이터프레임에 엑셀 데이터 넣기
            df = pd.read_excel(file_name[0], sheet_name=0, header=0)
            if df.empty or df.iloc[0].isnull().all():
                QMessageBox.information(self, '오류', '데이터가 없습니다.')
            else:
                # 특정 열 데이터 가져오기 (첫행이 빈칸으로 되어 있으면 안됨)
                selected_columns = ['한글이름', '영문이름', '출발일', '도착일', '주민등록번호', '여행상품']

                # 필요한 필드만 가져옴
                selected_df = df[selected_columns].copy()

                # 한글이름 분리
                selected_df['한글이름'] = selected_df['한글이름'].str.split('/')

                # 날짜에서 시간 제거
                selected_df['출발일'] = pd.to_datetime(selected_df['출발일'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
                selected_df['도착일'] = pd.to_datetime(selected_df['도착일'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')

                # 영문이름 분리
                split_names = selected_df['영문이름'].str.split('/')

        except Exception as e:
            QMessageBox.information(self, '오류', f'데이터 불러오기에 실패했습니다. \n엑셀파일 첫행 확인 후 재시도 \n{str(e)}')

        # 이름을 합치는 함수 정의
        def combine_names(names):
            if len(names) == 4:
                return [names[0].strip() + ' ' + re.sub(r'\s', '', names[1].strip()),
                        names[2].strip() + ' ' + re.sub(r'\s', '', names[3].strip())]
            elif len(names) == 2:
                formatted_names = []
                for name in names:
                    parts = name.strip().split()
                    if len(parts) == 1:
                        # 이름이 하나만 있는 경우 그대로 사용
                        formatted_names.append(parts[0])
                    elif len(parts) == 2:
                        # 이름이 붙어 있는 경우
                        formatted_names.append(f"{parts[0]} {parts[1]}")
                    else:
                        # 이름에 공백이 있는 경우
                        formatted_names.append(f"{parts[0]} {parts[1]}{parts[-1]}")
                return formatted_names
            else:

                return ['확인필요-----' + names[0].strip(), names[1].strip() + ' ' + names[2].strip()]

        # 이름을 합친 결과를 새로운 열에 저장
        selected_df['영문이름'] = split_names.apply(combine_names)

        # 주민등록번호 분리
        selected_df['주민등록번호'] = selected_df['주민등록번호'].str.replace(' ', '').str.split('/')

        # 데이터 분할 하여 넣기
        selected_df = selected_df.explode(['한글이름', '영문이름', '주민등록번호'], ignore_index=True)
        selected_df['보험료'] = None

        table = self.list_table

        # 테이블 위젯의 행 및 열 수 설정 없을 경우 테이블에 데이터값 안들어감
        table.setRowCount(selected_df.shape[0])  # 행 수 설정
        table.setColumnCount(selected_df.shape[1])  # 열 수 설정

        for i, row in enumerate(selected_df.values):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter.AlignCenter)  # 중앙 정렬 설정
                table.setItem(i, j, item)
                if item is not None and item.text().strip() == '':
                    item.setBackground(QColor(255, 0, 0))  # 빨간색 배경으로 변경

            # 필요하지 않은 부분이라 삭제 i = i + 1
            # i = i * 2

    def load_tobe_data(self):
        # 파일 대화상자 열기
        file_name = QFileDialog.getOpenFileName(self, 'Select File', '', 'Excel Files (*.xlsx)')

        # 확장자를 제외한 파일명 가져오기
        self.excel_edit.setText(file_name[0])
        tobe_df = pd.read_excel(file_name[0], sheet_name=0, header=0, index_col=None)
        selected_columns = ['한글이름', '영문이름', '출발일', '도착일', '주민등록번호', '여행상품', '보험료']
        tobe_df = tobe_df[selected_columns].copy()
        print(tobe_df)

        table = self.list_table
        # 테이블 위젯의 행 및 열 수 설정 없을 경우 테이블에 데이터값 안들어감
        table.setRowCount(tobe_df.shape[0])  # 행 수 설정
        table.setColumnCount(tobe_df.shape[1])  # 열 수 설정

        for i, row in enumerate(tobe_df.itertuples(index=False), 0):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter.AlignCenter)  # 중앙 정렬 설정
                table.setItem(i, j, item)
                if item is not None and item.text().strip() == '':
                    item.setBackground(QColor(255, 0, 0))  # 빨간색 배경으로 변경

    def cal_price(self):
        table = self.list_table
        for row in range(0, table.rowCount()):  # 한 개의 행씩 반복
            traveler_name = table.item(row, 0).text()
            start_date = table.item(row, 2).text()
            end_date = table.item(row, 3).text()
            jumin_num = table.item(row, 4).text()

            if len(jumin_num) > 14:
                QMessageBox.information(self, '알림', f'{jumin_num} \n{traveler_name}님 주민번호에 문제가 있습니다.')
                return

            # 출발일이 도착일보다 큰 경우 알림
            if start_date >= end_date:
                QMessageBox.information(self, '알림',
                                        f'출발일 : {start_date} \n도착일 : {end_date} \n{traveler_name}님 도착일에 문제가 있습니다.')
                return

            # 두 개의 행 데이터를 리스트로 묶기
            amounts = [start_date, end_date, jumin_num]

            # 보험료 계산 결과를 테이블에 적용
            price = get_price(self, amounts)

            item = QTableWidgetItem(price)
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 오른쪽 정렬 설정
            table.setItem(row, 6, item)

        QMessageBox.information(self, '알림', '보험료 계산이 완료 되었습니다.')
        return

    def export_excel(self):
        data = []
        # print(self.list_table.rowCount())
        if self.list_table.rowCount() == 0:
            QMessageBox.information(self, 'Notice', '데이터가 없습니다.')
        else:
            for row in range(self.list_table.rowCount()):
                row_data = []
                for column in range(self.list_table.columnCount()):
                    item = self.list_table.item(row, column)
                    row_data.append(item.text())
                data.append(row_data)

            columns = ['한글이름', '영문이름', '출발일', '도착일', '주민등록번호', '여행상품', '보험료']
            # columns = ['한글이름', '영문이름', '출발일', '도착일', '주민등록번호']
            df = pd.DataFrame(data, columns=columns)

            # 인덱스를 1부터 시작 하도록 설정 # df.index = range(1, len(df) + 1)

            # DataFrame을 Excel 파일로 저장
            file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Excel Files (*.xlsx)')
            if file_name:
                df.to_excel(file_name)

    def toggle_action(self):
        current = self.pdf_btn.text()
        if current == "진행중":
            print("break")
        else:
            create_pdf(self)

    def create_pdf(self):
        table = self.list_table
        if table.rowCount() == 0:
            QMessageBox.information(self, 'Notice', '데이터가 없습니다.')
        else:
            self.progress_bar.setMinimum(0)
            self.pdf_btn.setText("진행중")
            self.pdf_btn.setDisabled(True)
            self.progress_bar.setMinimum(0)
            QApplication.processEvents()
            self.progress_bar.setVisible(True)
            self.progress_bar.setMaximum(table.rowCount())

            for row in range(0, table.rowCount(), 2):  # 두 개의 행씩 반복
                # 첫 번째 행의 데이터 가져오기
                kor_name1 = table.item(row, 0).text()
                en_name1 = table.item(row, 1).text()
                start_date1 = table.item(row, 2).text()
                end_date1 = table.item(row, 3).text()
                jumin_num1 = table.item(row, 4).text()
                price1 = table.item(row, 6).text()

                # 두 번째 행의 데이터 가져오기
                kor_name2 = table.item(row + 1, 0).text()
                en_name2 = table.item(row + 1, 1).text()
                start_date2 = table.item(row + 1, 2).text()
                end_date2 = table.item(row + 1, 3).text()
                jumin_num2 = table.item(row + 1, 4).text()
                price2 = table.item(row + 1, 6).text()

                # 두 개의 행 데이터를 리스트로 묶기
                amounts = [
                    [kor_name1, en_name1, start_date1, end_date1, jumin_num1, price1],
                    [kor_name2, en_name2, start_date2, end_date2, jumin_num2, price2]
                ]

                create_pdf(amounts)

                self.progress_bar.setValue(row + 1)
                QApplication.processEvents()  # UI 업데이트를 위해 이벤트 루프를 처리합니다.

            self.progress_bar.setMaximum(table.rowCount() - 1)
            QMessageBox.information(self, '알림', 'PDF 생성 완료')
            self.progress_bar.setVisible(False)
            self.pdf_btn.setText("PDF 생성")
            self.pdf_btn.setDisabled(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            selected_rows = set()
            for item in self.list_table.selectedItems():
                selected_rows.add(item.row())

            # 선택된 행을 역순으로 정렬하여 삭제 (이유 : 인덱스 영향)
            for row in sorted(selected_rows, reverse=True):
                self.list_table.removeRow(row)
        elif event.matches(QKeySequence.Copy):
            self.copy()
        elif event.matches(QKeySequence.Paste):
            self.paste()
        else:
            super().keyPressEvent(event)

    # email  에서 수정
    def copy(self):
        # 현재 선택한 셀의 값을 가져와서 클립보드에 복사합니다.
        selected_ranges = self.list_table.selectedRanges()
        if selected_ranges:
            selected = selected_ranges[0]  # 첫 번째 선택 범위를 사용합니다.
            text = ''
            for i in range(selected.topRow(), selected.bottomRow() + 1):
                for j in range(selected.leftColumn(), selected.rightColumn() + 1):
                    text += str(self.list_table.item(i, j).text()) + '\t'
                text = text[:-1] + '\n'
            QApplication.clipboard().setText(text)

    def paste(self):
        # 클립보드에서 텍스트를 가져옵니다.
        clipboard = QApplication.clipboard()
        text = clipboard.text().rstrip('\n')

        # 텍스트를 탭으로 분리합니다.
        rows = text.split('\n')

        # 현재 선택한 셀의 행과 열 위치를 가져옵니다.
        selected = self.list_table.selectedRanges()[0] if self.list_table.selectedRanges() else None
        start_row = selected.topRow() if selected else 0
        start_col = selected.leftColumn() if selected else 0

        for i, row in enumerate(rows):
            cols = row.split('\t')
            row_position = start_row + i  # 새로운 행 위치 계산

            # 행 추가
            self.list_table.insertRow(row_position)

            for j, col in enumerate(cols):
                col_position = start_col + j  # 새로운 열 위치 계산
                item = QTableWidgetItem(col)
                self.list_table.setItem(row_position, col_position, item)

    # return 여부 확인 필요

    def closeEvent(self, event):
        # X 버튼을 눌렀을 때의 동작.
        try:
            excel = win32com.client.GetActiveObject("Excel.Application")
            excel.Quit()
        except Exception:
            pass
        event.accept()  # 윈도우를 닫기.


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()