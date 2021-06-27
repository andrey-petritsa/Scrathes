# Подключаем библиотеки
import httplib2
import time
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Имя файла с закрытым ключом, вы должны подставить свое
CREDENTIALS_FILE = 'credentials.json'
SPREAD_SHEET_ID = '1GkjycKCb7gT0d7C3M79l40iMkPD2FAYulDYlqKhgSgk'

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [
                                                               'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
# Выбираем работу с таблицами и 4 версию API
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

print('https://docs.google.com/spreadsheets/d/' + SPREAD_SHEET_ID)


driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API

i = 0
while True:
    
    results = service.spreadsheets().values().batchUpdate(spreadsheetId = SPREAD_SHEET_ID, body = {
        "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
        "data": [
            {"range": "Лист номер один!A1:B2",
            "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
            "values": [
                        ["Число"], # Заполняем первую строку
                        [i]  # Заполняем вторую строку
                    ]}
        ]
    }).execute()
    print(i)
    i += 1
    time.sleep(5)
