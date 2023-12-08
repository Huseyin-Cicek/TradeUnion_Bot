import telebot

TOKEN = '6781150801:AAHauw6N7LAtxrvtdL7w-GaDPYijFqtEW6Y'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот с ответами на частозадаваемые вопросы"
                                      ", связанные с материальной помощью и работой профсоюза.")
    bot.send_message(message.chat.id, "Чтобы узнать список доступных вопросов, введи /help")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if "что ты умеешь" in message.text.lower():
        bot.send_message(message.chat.id, "Я умею отвечать на частозадаваемые вопросы!")

    elif "/help" in message.text.lower():
        bot.send_message(message.chat.id, "⋅ какие сроки для подачи заявления на матпомощь\n\n"
                                          "⋅ общие правила матпомощи\n\n"
                                          "⋅ скачать памятку")

    elif "какие сроки для подачи заявления на матпомощь" in message.text.lower():
        bot.send_message(message.chat.id, "Подавать заявление на матпомощь можно до 10 числа каждого месяца. "
                                          "В будние дни с 10:00 до 17:00")

    elif "общие правила матпомощи" in message.text.lower():
        bot.send_message(message.chat.id,
                         "⋅ Подавать на материальную помощь в институте могут только студенты-бюджетники;\n"
                         "⋅ Нельзя подавать заявление на материальную помощь в комиссию института и университета одновременно по одному основанию, а то в гуке могут и отказать;\n"
                         "⋅ Со студентов-контрактников при подаче в университет налог НДФЛ не взимается!\n"
                         "⋅ Иностранным студентам при подаче на матпомощь требуется предоставить копии ВСЕХ страниц каждого из прикладываемых документов;\n"
                         "⋅ По достижении возраста 20 лет и смене паспорта, для того, чтобы в будущем получать материальную помощь, необходимо обновить свои паспортные данные в деканате, обратившись к Курочкиной Марине Сергеевне или отправив их ей на почту m.s.kurochkina@urfu.ru;\n"
                         "⋅ В заявлении на матпомощь можно указывать одновременно несколько причин, но в любом случае, в институте вернётся до 5000 рублей, а в университете до 10 000 рублей;\n"
                         "⋅ Если ты планируешь получить материальную помощь со следующей стипендией, заявление необходимо подать до 27 числа текущего месяца включительно (иногда дата может меняться, внимательно следи за новостями в группе Союза студентов ИРИТ-РТФ);\n"
                         "⋅ Иногда сумма возмещения может приходить в неполном размере. Это может быть связано с распределением средств из бюджетного фонда, которых бывает недостаточно в связи с большим количеством заявлений, поданных за месяц. Либо какой-то из приложенных тобой чеков не подошел под причину подачи и в итоге не был учтен в общей сумме;"
                         "⋅ На чеках за лекарства и одежду обязательно должны присутствовать дата покупки, названия того, что куплено, или qr-код;\n"
                         "⋅ При покупке в интернет-магазине необходимо прикладывать документ-чек, который обычно приходит вам на почту после совершения покупки. На нем должны быть указаны: наименование товара, дата покупки, сумма и qr-код. Скриншоты с сайта, на которых обычно содержится не полная информация не подходят;\n"
                         "⋅ Деньги возвращаются только за верхнюю одежду и обувь. За спортивную одежду, платья, футболки, джемперы, юбки, а также перчатки и шапки они не возвращаются;\n"
                         "⋅ Чеки с покупки одежды/лекарств/билетов являются действительными, если покупка совершена в течение текущего учебного года;\n"
                         "⋅ Чеки на мужскую одежду могут подаваться только студентами мужского пола, чеки на женскую одежду — студентками женского пола;\n"
                         "⋅ За услуги офтальмолога и стоматолога деньги НЕ возвращаются даже при наличии медицинского направления;\n"
                         "⋅ Для того, чтобы возместить деньги за проживание в общежитии, необходимо приложить в качестве документов договор найма, ордер и квитанцию об оплате;\n"
                         "⋅ При возмещении средств за съем квартиры справка о непоселении должна иметь подпись и печать, которые нужно проставить в деканате;\n"
                         "⋅ Деньги за съем жилья возможно вернуть, если договор аренды был заключён перед текущим учебным годом/во время текущего учебного года и в том случае, если студент проживает в квартире на момент подачи заявления;\n"
                         "⋅ В первом семестре подавать на МП по причине аренды жилья можно только в ГУК-309 (и возместить до 12 т.р.), во втором семестре — только в институт, Р-126 (и возместить до 5 т.р.);\n"
                         "⋅ Студенты с инвалидностью один раз в семестр могут обращаться в университетскую комиссию на основании справки об инвалидности;\n"
                         "⋅ При возмещении денег за пребывание в санатории, поездка должна быть совершена в течении учебного года;\n"
                         "⋅ При подаче заявления по причине проезда до места жительства, время пересадки может составлять не более суток;\n"
                         "⋅ При возмещении затрат за проезд на олимпиады, форумы, конференции, а также за сопутствующие затраты необходимо иметь визу завкафедры;\n"
                         "⋅ При подаче в университет заявления по причине создания семьи, а также рождения ребенка, соответствующие документы (свидетельство о заключении брака/рождении) должны быть получены не более чем за 12 месяцев на момент подачи на матпомощь;")

    elif "скачать памятку" in message.text.lower():
        send_handbook(message)

    else:
        bot.send_message(message.chat.id, "Извините, не могу понять ваш вопрос. Попробуйте другой.")


def send_handbook(message):
    with open('Obnovlennaya_pamyatka_po_matpomoschi.pdf', 'rb') as handbook:
        bot.send_document(message.chat.id, handbook, caption="Вот ваша памятка!")


if __name__ == "__main__":
    bot.polling(none_stop=True)
