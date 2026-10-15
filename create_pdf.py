import win32com.client
import re
import os


# 엑셀 강제 종료
def terminate_excel_instances():
    try:
        excel = win32com.client.GetActiveObject("Excel.Application")
        excel.DisplayAlerts = False
        excel.Application.Quit()
        excel.Quit()
    except:
        pass


def create_pdf(amounts):
    # 엑셀을 실행할 객체 생성
    # 기존에 열려 있는 Excel 인스턴스 닫기
    terminate_excel_instances()
    excel = win32com.client.Dispatch("Excel.Application")

    # pdf로 변환할 파일명 선택
    ws_sht = None
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 파일 경로를 절대 경로로 변환
    file_path = os.path.join(script_dir, "가입확인서.xlsx")
    excel.Visible = False

    # 엑셀 인스턴스를 숨김
    # excel.WindowState = 2
    wb = excel.Workbooks.Open(file_path)
    ws_sht = wb.Worksheets("Table 1")
    ws_sht.Select()

    # 셀 선택 (세로, 가로)
    # 피보험자 1
    cell_1 = ws_sht.Cells(9, 2)  # 피보험자 (한글 + 엉문)
    cell_2 = ws_sht.Cells(8, 2)  # 보험기간
    cell_3 = ws_sht.Cells(9, 5)  # 생년월일
    cell_type1 = ws_sht.Cells(11, 2)  # 플랜명
    cell_price1 = ws_sht.Cells(10, 5)  # 보험료
    cell_date = ws_sht.Cells(39, 7)  # 날짜

    # 피보험자 2
    cell_4 = ws_sht.Cells(49, 2)  # 피보험자 (한글 + 엉문)
    cell_5 = ws_sht.Cells(48, 2)  # 보험기간
    cell_6 = ws_sht.Cells(49, 5)  # 생년월일
    cell_type2 = ws_sht.Cells(51, 2)  # 플랜명
    cell_price2 = ws_sht.Cells(50, 5)  # 보험료

    # 셀에 값 할당
    # 피보험자 1
    cell_1.Value = amounts[0][0] + '(' + amounts[0][1] + ')'
    cell_2.Value = str(amounts[0][2]) + ' ~ ' + amounts[0][3]
    cell_3.Value = amounts[0][4][:6]
    cell_type1.Value = '성인 M0-2'
    cell_price1.Value = 'KRW ' + re.sub(r'(\d)(?=(\d{3})+(?!\d))', r'\1,', str(amounts[0][5]))

    # 셀에 값 할당
    # 피보험자 2
    cell_4.Value = amounts[1][0] + '(' + amounts[1][1] + ')'
    cell_5.Value = amounts[1][2] + ' ~ ' + amounts[1][3]
    cell_6.Value = amounts[1][4][:6]
    cell_type2.Value = '성인 M0-2'
    cell_price2.Value = 'KRW ' + re.sub(r'(\d)(?=(\d{3})+(?!\d))', r'\1,', str(amounts[1][5]))

    # PDF파일을 저장할 경로 및 파일명 지정
    file_name = re.sub('[\"/!@#:|?<>*]', '', amounts[0][0]) + '_' + re.sub('[\"/!@#:|?<>*]', '', amounts[1][0]) + '.pdf'

    # pdf 폴더 경로
    pdf_folder = os.path.join(os.getcwd(), 'pdf')

    # pdf 폴더가 없으면 생성
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    # 활성화된 시트를 pdf 저장
    wb.ActiveSheet.ExportAsFixedFormat(0, pdf_folder + '/' + file_name)

    # 엑셀 워크북 및 프로그램 종료
    # 종료를 제대로 해주어야 다음 실행시 에러 안생김
    wb.Close(False)
    excel.Quit()
    return
