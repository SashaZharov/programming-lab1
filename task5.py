import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import random
import matplotlib.pyplot as plt

n = int(5**0.5)*10
min = 1
max = 150
print(n)
xList = list()
yList = list()
while len(xList) < n:
    xList.append(int(max - random.random() * (max - min)))
    yList.append(int(max - random.random() * (max - min)))
print(xList, yList)

xy_awg = 0
x_sqr = 0

for i in range(n):
    xy_awg += xList[i] * yList[i]
    x_sqr += xList[i] ** 2

a = (sum(xList) * sum(yList) - n * xy_awg) / (sum(xList) ** 2 - n * x_sqr)
b = (sum(xList) * xy_awg - x_sqr * sum(yList)) / (sum(xList) ** 2 - n * x_sqr)


plt.plot([min, max], [min * a + b, max * a + b], linewidth = 2)
plt.scatter(xList, yList)
plt.scatter(xList, yList)
plt.show()

CREDENTIALS_FILE = 'lab1-info.json'
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
'''
# создаем таблицу
spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'lab1', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист номер один',
                               'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
}).execute()
spreadsheetId = spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
'''

spreadsheetId = '1459Ex4pOW__lXkVy1fpDVXP3-B1Q8bTisyIJ8hpnhtQ'
print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)

# открываем себе доступ
driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
access = driveService.permissions().create(
    fileId = spreadsheetId,
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'zhara190@gmail.com'},
    fields = 'id'
).execute()

results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "Лист номер один!A1:С21",
         "majorDimension": "COLUMNS",
         "values": [
                    xList, yList
                   ]}
    ]
}).execute()


