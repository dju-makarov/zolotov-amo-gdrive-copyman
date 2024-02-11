from amocrm.v2 import tokens, Lead as _Lead, custom_field

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
    has_access_to_channels= custom_field.CheckboxCustomField("Получены доступы к каналу/соц-сетям")
    has_broadcast_scheduled= custom_field.CheckboxCustomField("Трансляция запланирована")
    has_speakers_list = custom_field.CheckboxCustomField("Получен список спикеров для подписей")
    has_speakers_regalia= custom_field.CheckboxCustomField("Получена таблица удаленных спикеров")
    has_graphics = custom_field.CheckboxCustomField("Создана/получена эфирная графика")
    has_and_agreed_GT_titles = custom_field.CheckboxCustomField("Созданы и согласованы титры GT Tittle")

    def print_fields():
        fields = ['event_type', 'broadcast_type', 'address', 'airing_time', 'montage_time', 'duration']
        for field in fields:
            print(field)





if __name__ == '__main__':
    tokens.default_token_manager(
        client_id="d3e149f4-19d1-4de3-92f4-d50e0113fac1",
        client_secret="6P098dcLVPF9lrVm8tDVJsQbrEgQUqcD29QK33s63pn3EZiywt1cj06vYc4txjuZ",
        subdomain="zolotovstudio",
        redirect_url="https://ya.ru",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )

    # tokens.default_token_manager.init(code="def5020039c1596b9a95a2f5cac6ce176835b3ceb70e0fdd0199dd9cd711953001338d477829aebbddba13db1b27265b0bcebe4b77e5d6791035debcec8e03f8dc3867780b1e958d1041bdb731ef0587784e38824aa2a1c6a7e9a11c6bb09e4c4136c7a7b99500c588afbc202cdd0e4467aeffba8141636011d3af9c8c416876ade4506dc42fcf3291f6fd7fe4950db9050e053dd8d0edfa7164523eba197b10e663b28a3c84c61a3db7bdbd9e09bb412ed5fa6b8c17a6523fe76d73ddeca71f6002dbe3eb1b65db75f6ca0356104570477e11f3049ffa4e07510317663f8225801823a1cffcc080183b6c8ccb2c30aba8b9a4dc701447c861c981150545e6db097437f8d70e0afa77e7da5dba720044656e93937375c37df22d49321f04715282412d59bc75af162526ece2046ceef062319a1b763d40949a2b4e5478d3d4ce152429c41ff8c69e580d6820eadd8058aefe9c1fb1c064a94bbc3c3228c7036b7a06b4d9b1cb488c835fd5332729c2eca7bfab79a80b3d98d422994a5b2a720c2c6a28e0144cbd982ee1360bfd30654fff4c1cee614521958b7669206c4b7942f7049e06ce42105c18a78573ab5faaba22febcff2e05289ece44e96963ae1987572154bc22bb1951ab1fac08c8637d1229b2dfc5c7390800b12c2c5330",
    #                                   skip_error=True)

    leads = Lead.objects.all()

    # for lead in leads:
    #     print(lead.id, lead.name)


    lead = Lead.objects.get(query='ТЕСТ ДЛЯ ДЖУ 2')
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
    # print(lead.additional_rent)
    # print(lead.additional)
    # print(lead.has_memo_was_sent_to_customer)
    # print(lead.has_access_to_channels)
    # print(lead.has_broadcast_scheduled)
    # print(lead.has_speakers_list)
    # print(lead.has_speakers_regalia)
    # print(lead.has_graphics)
    # print(lead.has_and_agreed_GT_titles)

    lead.print_fields()



    #ending
