import openpyxl

workbook = openpyxl.load_workbook('/Users/baiwenkai/PycharmProjects/mihuiTestProject/mihuiapi_test_unittest'
                                  '/test_data/mihuiui_test_data.xlsx')
sheet = workbook['login']


def read_login():
    allList = []
    for row in range(3, 8):
        tempList = []
        for colnum in range(2, 10):
            tempList.append(sheet.cell(row, colnum).value)
        allList.append(tempList)
    return allList