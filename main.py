from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTabWidget
from amocrm.v2 import tokens, Lead as _Lead, custom_field
import openpyxl
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive




import sys

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


CRM_LIVE_IDS = [511733, 511795, 511763, 512185, 511767, 511769, 511771, 511773, 511777, 511775, 511779, 511799,
                512127, 519487, 519657, 511785, 511787, 512189, 512187, 517861, 511781, 511853, 512005, 511999,
                512965, 512001, 511861, 511855, 517851, 517853, 517863, 517857, 517859, 517865]

class Lead(_Lead):
    event_type = custom_field.UrlCustomField("Тип мероприятия")
    broadcast_type = custom_field.UrlCustomField("Вид трансляции")
    address = custom_field.UrlCustomField("Адрес мероприятие")
    airing_time = custom_field.DateTimeCustomField("Дата и время выхода в эфир")
    montage_time = custom_field.DateTimeCustomField("Дата и время монтажа")
    duration = custom_field.UrlCustomField("Продолжительность эфира в часах")
    broadcast_days = custom_field.UrlCustomField("Кол-во дней трансляции")
    number_of_halls = custom_field.UrlCustomField("Кол-во залов")
    number_of_cameras = custom_field.UrlCustomField("Кол-во камер")
    number_of_speakers = custom_field.UrlCustomField("Общее кол-во спикеров")
    max_active_speakers = custom_field.UrlCustomField("Максимум активных спикеров, включая вопросы из зала")
    number_of_remote_speakers = custom_field.UrlCustomField("Кол-во удаленных спикеров")
    number_of_restream = custom_field.UrlCustomField("Кол-во площадок рестрима")
    has_presentation = custom_field.UrlCustomField("Будут презентации")
    has_microphone_on_the_site = custom_field.UrlCustomField("Микрофоны на площадке")
    has_audio_mixer_on_the_site = custom_field.UrlCustomField("Аудиомикшер на площадке")
    has_loudspeakers_on_the_site = custom_field.UrlCustomField("Колонки на площадке")
    has_tv_on_the_site = custom_field.UrlCustomField("Проектор/плазма на площадке")
    has_wired_internet_on_the_site = custom_field.UrlCustomField("Проводной интернет на площадке")
    who_makes_graphic = custom_field.UrlCustomField("Эфирную графику делает")
    broadcast_platforms = custom_field.UrlCustomField("Площадки эфира")
    reporting_video = custom_field.UrlCustomField("Отчетный ролик")
    photo = custom_field.UrlCustomField("Фотосъемка")
    duplicate_prompter_screens = custom_field.UrlCustomField("Дублирующие экраны-суфлеры")
    additional_options = custom_field.UrlCustomField("Дополнительные опции")
    additional_rent = custom_field.UrlCustomField("Доп. аренда")
    additional = custom_field.UrlCustomField("Дополнительно")
    has_memo_was_sent_to_customer = custom_field.CheckboxCustomField("Заказчику отправлена памятка")
    has_access_to_channels = custom_field.CheckboxCustomField("Получены доступы к каналу/соц-сетям")
    has_broadcast_scheduled = custom_field.CheckboxCustomField("Трансляция запланирована")
    has_speakers_list = custom_field.CheckboxCustomField("Получен список спикеров для подписей")
    has_speakers_regalia = custom_field.CheckboxCustomField("Получена таблица удаленных спикеров")
    has_graphics = custom_field.CheckboxCustomField("Создана/получена эфирная графика")
    has_and_agreed_GT_titles = custom_field.CheckboxCustomField("Созданы и согласованы титры GT Tittle")

def get_lead(lead_name: str) -> Lead:
    tokens.default_token_manager(
        client_id="5ebcd675-ea67-46ec-8a2b-b60980b973e1",
        client_secret="pzIj58pVFqICAdgeWxCpAQS2LBtyOhL8t8i6dGIEP2IdNusugFSmo28UfeaTtDou",
        subdomain="zolotovstudio",
        redirect_url="https://ya.ru",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )

    tokens.default_token_manager.init(
        code="def502003d0170413a847b9cb605552607deb30f28f6740a8ec361c4ef2f16a3e89956567e246b568cc6967ca2e477aab60e678329fcbd1beec23181b323febf049efffeb55d260d6022f21c042c56cb8b23336675c28dd18be936a89865c3c463832e1034c4f6f059ec3559e7fc572e1ea1a7ec2cb6c8acf590cca5e62aef725d400db764d329e89d02aeba46981f46f9477283e105c0e4325c66c607aa1c65679395382fa6b176edf7c2fcddd4fc308f48f97677ada7d5ae99247a30665d00681f7ebb0e0a21468ec5edc6b1f883eaabfe31a254933db40f403dd020601c58ec9fab3d7581ce86c7f573a2dc76aa9f7631dd28856b9a576f3da5f799a51cc84f24e7fa4d9bb4835b2d521e27f94f1a9858c47540a5d37b8ec4824baf3abf0fbfd530cbaaeec7e77fabee395858485bc427ca94460054b4161751de3a253ff829ac1a56a8608d935a0533ae3d45e93d08b80cc25aa43ae5d24e4c2e11854702e85e7527db5ff82e20f265e2d98d8138e17dfbb133f3b7be39c6d44f02eaaeedf79d1dee1dd6b4d0b61d2c1c9cc1a871b728d115391cd4f71a9f6ec5bd4c3409fbf3069a264a791145dec1b5f2169aafddc19748297fd627419ac394e70f6e91dc579a6a54085587f350785a8ff98010e66ed442e2adb17f176a8a68e5",
        skip_error=True)

    # leads = Lead.objects.all()

    # for lead in leads:
    #     print(lead.id, lead.name)
    # lead_name = self.tab1_input.text()
    lead = Lead.objects.get(query=lead_name)
    print('взята сделка из: [' + lead.name + ']')
    # lead.name = 'ТЕСТ ДЛЯ ДЖУ 2'
    # lead.save()
    # print(lead.event_type)
    # print(lead.broadcast_type)
    # print(lead.address)
    # print(lead.airing_time)
    # print(lead.montage_time)
    # print(lead.duration)
    # print(lead.broadcast_days)
    # print(lead.number_of_halls)
    # print(lead.number_of_cameras)
    # print(lead.number_of_speakers)
    # print(lead.max_active_speakers)
    # print(lead.number_of_remote_speakers)
    # print(lead.number_of_restream)
    # print(lead.has_presentation)
    # print(lead.has_microphone_on_the_site)
    # print(lead.has_audio_mixer_on_the_site)
    # print(lead.has_loudspeakers_on_the_site)
    # print(lead.has_tv_on_the_site)
    # print(lead.has_wired_internet_on_the_site)
    # print(lead.who_makes_graphic)
    # print(lead.broadcast_platforms)
    # print(lead.reporting_video)
    # print(lead.photo)
    # print(lead.duplicate_prompter_screens)
    # print(lead.additional_options)
    # print(get_field_values(lead, 512187))
    # print(lead.additional)
    # print(lead.has_memo_was_sent_to_customer)
    # print(lead.has_access_to_channels)
    # print(lead.has_broadcast_scheduled)
    # print(lead.has_speakers_list)
    # print(lead.has_speakers_regalia)
    # print(lead.has_graphics)
    # print(lead.has_and_agreed_GT_titles)

    # print(get_field_values(lead, 511795))
    return lead

def optimize_lead_to_data(lead:Lead):

    fields_data = {}
    data = vars(lead)
    # print(data)
    # Проход по списку custom_fields_values и запись полей field_name и value в словарь
    for field in data['_data']['custom_fields_values']:
        if field['field_id'] in CRM_LIVE_IDS:
            field_id = field['field_id']
            field_name = field['field_name']
            values = [str(value['value']) for value in field['values']]  # Преобразуем значения в строки
            value = ', '.join(values)  # Объединяем значения в строку, разделенную запятыми
            fields_data[field_id] = {'field_name': field_name, 'value': value}
    return fields_data
def lead_to_excel(*, lead_name, project_name):
    lead = get_lead(lead_name)
    fields_data = optimize_lead_to_data(lead)
    # print(fields_data)

    # Создание нового файла Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Fields Data'

    # Запись данных из словаря в файл Excel
    header = ['Field Name', 'Value']
    sheet.append(header)

    for data in fields_data.values():
        row = [data['field_name'], data['value']]
        sheet.append(row)

    # Сохранение файла
    workbook.save('fields_data.xlsx')

def create_and_upload_file(file_name='test.txt', file_content='Hey Dude!', project_name= '2024-00-00 - testing'):

    # Создание папки
    drive = GoogleDrive(gauth)
    parent_folder_id = "1Xgs_mvBwKp3g4p4MI4Qfe0AENFLe0E5w"  # идентификатор папки 1.КП
    folder_name = project_name
    sourceKP_folder_id = "1GxPO5Dtg_Sgtd3IMQ07lZY-B0vvxrMOm"

    # Проверка существования папки
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(parent_folder_id)}).GetList()
    for file in file_list:
        if file['title'] == folder_name and file['mimeType'] == 'application/vnd.google-apps.folder':
            return f"папка с названием {folder_name} существует. Удалите существующую папку или создайте проект с другим названием"


    # Создание метаданных папки
    folder_metadata = {
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [{'id': parent_folder_id}]
    }

    # Загрузка папки
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    destination_folder_id = folder['id']
    print(f"Папка {folder_name} успешно создана с идентификатором {destination_folder_id}")

    # Копирование всех файлов из source папки в папку проекта
    sourceKP_folder_files = drive.ListFile({'q': f"'{sourceKP_folder_id}' in parents"}).GetList()
    for file in sourceKP_folder_files:
        folder = destination_folder_id
        title = file['title']
        file = file['id']
        drive.auth.service.files().copy(fileId=file,
                                        body={"parents": [{"kind": "drive#fileLink",
                                                           "id": folder}], 'title': title}).execute()

    return "код выполнен"



def lead_to_googlesheets(*, lead_name, project_name):
    lead = get_lead(lead_name)
    fields_data = optimize_lead_to_data(lead)


    print(create_and_upload_file(file_name='hello.txt', file_content='Hello Friend', project_name=project_name))



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создание элементов первой вкладки
        self.tab1_label = QLabel('Введи название сделки')
        self.tab1_input = QLineEdit()
        self.tab1_button1 = QPushButton('Запустить')
        self.tab1_button2 = QPushButton('Если не работает')

        # Создание элементов второй вкладки
        self.tab2_label1 = QLabel('Текстовое поле 1')
        self.tab2_input1 = QLineEdit()
        self.tab2_label2 = QLabel('Текстовое поле 2')
        self.tab2_input2 = QLineEdit()
        self.tab2_label3 = QLabel('Текстовое поле 3')
        self.tab2_input3 = QLineEdit()
        self.tab2_label4 = QLabel('Текстовое поле 4')
        self.tab2_input4 = QLineEdit()
        self.tab2_button = QPushButton('Вернуться назад')

        # Создание макетов для элементов первой и второй вкладок
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(self.tab1_label)
        tab1_layout.addWidget(self.tab1_input)
        tab1_layout.addWidget(self.tab1_button1)
        tab1_layout.addWidget(self.tab1_button2)

        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(self.tab2_label1)
        tab2_layout.addWidget(self.tab2_input1)
        tab2_layout.addWidget(self.tab2_label2)
        tab2_layout.addWidget(self.tab2_input2)
        tab2_layout.addWidget(self.tab2_label3)
        tab2_layout.addWidget(self.tab2_input3)
        tab2_layout.addWidget(self.tab2_label4)
        tab2_layout.addWidget(self.tab2_input4)
        tab2_layout.addWidget(self.tab2_button)

        # Создание виджета вкладок и добавление в него макетов
        self.tabs = QTabWidget()
        self.tabs.addTab(QWidget(), 'Первая вкладка')
        self.tabs.addTab(QWidget(), 'Вторая вкладка')
        self.tabs.widget(0).setLayout(tab1_layout)
        self.tabs.widget(1).setLayout(tab2_layout)

        # Создание макета для главного окна и добавление в него виджета вкладок
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tabs)

        # Установка главного макета для главного окна
        self.setLayout(main_layout)

        # Подключение обработчиков событий для кнопок
        self.tab1_button1.clicked.connect(self.on_tab1_button1_clicked)
        self.tab1_button2.clicked.connect(self.on_tab1_button2_clicked)
        self.tab2_button.clicked.connect(self.on_tab2_button_clicked)

    def on_tab1_button1_clicked(self):
        # Обработчик события для кнопки "Запустить"
     lead_to_excel(lead_name=self.tab1_input.text(), project_name="1")

    def on_tab1_button2_clicked(self):
        # Обработчик события для кнопки "Если не работает"
        self.tabs.setCurrentIndex(1)


    def on_tab2_button_clicked(self):
        # Обработчик события для кнопки "Вернуться назад"
        self.tabs.setCurrentIndex(0)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

lead_to_googlesheets(lead_name="ТЕСТ ДЛЯ ДЖУ 2", project_name="zolotov_test")



