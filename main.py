import telebot
from telebot import types

TOKEN = '6781150801:AAHauw6N7LAtxrvtdL7w-GaDPYijFqtEW6Y'

admin_user_id = 741705263

bot = telebot.TeleBot(TOKEN)

budget_inst = {
    "В какие дни можно подать?": "Вторник, среда, четверг 13.30 - 14.15 в Р-126",
    "Что нужно для подачи заявления?": "Форма заявления, ее можно распечатать и заполнить заранее или взять в Р-126, документы, подтверждающие причину подачи.",
    "Причины и документы": "Все причины и необходимые документы можно найти в памятке",
    "Сколько раз можно подать на материальную помощь?": "Можно один раз за семестр",
    "Когда придет материальная помощь?": "Если вы подаете до 27 числа текущего месяца, то мат. помощь прийдет через одну стипендию. Например, если вы подали заявление 25 октября, то она придет вместе с ноябрьской стипендией, а если вы подаете 28 октября, то вместе с декабрьской"
}

budget_univ = {
    "График работы": "По будням 12.00 - 16.00 в ГУК-309",
    "Какие документы нужны для подачи заявления?": "Форма заявления, ее можно распечатать и заполнить заранее или взять в ГУК-309, документы, подтверждающие причину подачи.",
    "Причины и документы": "Все причины и необходимые документы можно найти в памятке",
    "Сколько раз можно подать на материальную помощь?": "Один раз в семестр",
    "Когда придет мат. помощь?": "Если вы подаете до 10 числа текущего месяца, то мат. помощь придет в этом месяце вместе со стипендией. Например, если вы подали заявление 7 октября, то она придет вместе с октябрьской стипендией, а если вы подаете 11 октября, то вместе с ноябрьской"
}

contract = {
    "Когда можно подать?": "По будням 12.00 - 16.00 в ГУК - 309",
    "Необходимые документы для подачи заявления": "Форма заявления, ее можно распечатать и заполнить заранее или взять в ГУК-309, документы, подтверждающие причину подачи, реквизиты карты",
    "Причины и документы": "Все причины и необходимые документы можно найти в памятке",
    "Сколько раз можно подавать на материальную помощь?": "Один раз в течении учебного года",
    "Когда придет мат. помощь?": "Если вы подаете до 10 числа текущего месяца, то мат. помощь прийдет в этом месяце вместе со стипендией. Например, если вы подали заявление 7 октября, то она придет вместе с октябрьской стипендией, а если вы подаете 11 октября, то вместе с ноябрьской"
}

trade_union = {
    "График работы профсоюза": "Понедельник, пятница с 13.30 - 14.15 в Р-126",
    "Как вступить?": "Необходимо подойти в Р-126, заполнить заявление на вступление в профсоюз и внести взнос в размере:"
    "\nДля бакалавров: 55 рублей"
    "\nДля магистратуры: 82 рубля",
    "Как продлить?": "Для продления необходимо подойти в Р-126, сообщить свое ФИО и группу, чтобы вам отметили продление в таблице."
    "Для контрактников и бюджетников без стипендии также необходимо оплатить весь семестр обучения, это 330 рублей для бакалавров, 510 рублей для магистратуры",
    "Как выйти?": "Для выхода из профсоюза необходимо подойти в Р-126 и заполнить заявление на выход",
    "Узнать номер профсоюзного билета": "Необходимо написать ответственному(ссылка ниже) за профсоюз, сообщить свои ФИО, группу и дату рождения"
    "\nhttps://vk.com/elmsberry - Эмма"
    "\nhttps://vk.com/lads_mart - Лада",
    "Контрактникам для получения материальной помощи": "Для получения материальной помощи контрактникам необходимо продлить профсоюзный билет на два семестра. "
                                                       "Для этого нужно подойти в Р-126 и внести взнос. Если ранее продлений не было, то размер взноса за оба семестра будет составлять 660 рублей для бюджетников и 1020 для магистратуры"
}

contacts = {
"Профбюро": "Корякин Игорь"
            "\nПредседатель Союза Студентов ИРИТ-РТФ"
            "\nВк: roggi7"
            "\nTelegram: roggi7"
            "\nТелефон: +7(904)549-50-03"
            "\n\nПо вопросам продления и получения профсоюзных билетов:"
            "\nМиргалямова Эмма"
            "\nЗаместитель председателя по организационно-массовой работе"
            "\nВк: elmsberry"
            "\nTelegram: elmsberry"
            "\nТелефон: +7(917)779-63-02"
            "\n\nМартемьянова Лада"
            "\nВ составе комиссии по организационно-массовой работе"
            "\nВк: lads_mart"
            "\nTelegram: o0pSis"
            "\n\nПо вопросам получения материальной помощи:"
            "\nДергачева Полина"
            "\nЗаместитель председателя по социально-правовой работе"
            "\nВк: polyaa_dd"
            "\nTelegram: Polinaria_d"
            "\nТелефон: +7(965)508-22-43"
            "\n\nПопова Ксения"
            "\nВ составе комиссии по социально-правовой работе"
            "\nВк: ksushasolnyshko"
            "\nTelegram: ksushasolnyshko"
            "\n\nПо вопросам поселения:"
            "\nКовтонюк Полина"
            "\nЗаместитель председателя Союза студентов ИРИТ-РТФ по жилищно-бытовой работе"
            "\nВк: polinakovtonyuk"
            "\nTelegram: polinakovt"
            "\n\nПо вопросам размещения информации в социальных сетях института:"
            "\nФиляева Алена"
            "\nЗаместитель председателя Союза студентов ИРИТ-РТФ по информационной работе"
            "\nВк: aaaaalllooooo"
            "\nTelegram: alyona_filyaeva"
            "\nТелефон: +7(912)051-14-42",

    "Тьюторы": "\n\nБазаров Георий"
            "\nИнформатика и вычислительная техника, Программная инженерия"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-138а"
            "\nЭлектронная почта: gdbazarov@urfu.ru"
            "\n\nВалиева Эльмира"
            "\nРадиотехника, Инфокоммуникационные технологии и системы связи, Управление в технических системах, Технология полиграфического и упаковочного производства, Конструирование и технология электронных средств"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-138а"
            "\nЭлектронная почта: e.r.valieva@urfu.ru"
            "\n\nКолмогорцева Ирина"
            "\nПрограммная инженерия"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-138а"
            "\nЭлектронная почта: i.s.kolmogortseva@urfu.ru"
            "\n\nХрушков Артем"
            "\nПрикладная информатика"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-138а"
            "\nЭлектронная почта: ae.khrushkov@urfu.ru"
            "\n\nАндреевских Софья"
            "\nИнформационная безопасность"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-217а"
            "\nЭлектронная почта: andreevskikh.sofia@urfu.ru",

    "Деканат": "\n\nОрехова Ирина Сергеевна"
            "\nНачальник отдела"
            "\nБакалавриат (ИРИТ-РТФ и ИнФО), с понедельника по пятницу с 10:00 до 16:00"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-219"
            "\nТелефон: +7 (343) 375-41-65"
            "\nЭлектронная почта: i.s.orekhova@urfu.ru"
            "\n\nБутусова Галина Валентиновна"
            "\nНачальник отдела"
            "\nМагистратура, специалитет (ИРИТ-РТФ и ИнФО)"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-217а"
            "\nТелефон: +7 (343) 375-45-34"
            "\nЭлектронная почта: G.V.Butusova@urfu.ru"
            "\n\nДанилова Анна Андреевна"
            "\nСпециалист по вопросам перевода и восстановления"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-219"
            "\nЭлектронная почта: a.a.danilova@urfu.ru"
            "\n\nКийко Наталья Григорьевна"
            "\nСтарший диспетчер"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-219"
            "\nТелефон: +7 (343) 375-48-99"
            "\nЭлектронная почта: n.g.kiyko@urfu.ru"
            "\n\nКозырева Наталья Андреевна"
            "\nСпециалист по работе со студентами"
            "\nС понедельника по пятницу с 10:00 до 12:00 и 12:30 до 17:00"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-219"
            "\nТелефон: +7 (343) 375-48-99"
            "\nЭлектронная почта: n.a.kozyreva@urfu.ru"
            "\n\nКурочкина Марина Сергеевна"
            "\nДелопроизводитель"
            "\nС понедельника по пятницу с 9:00 до 12:00 и 12:30 до 16:30"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-219"
            "\nТелефон: +7 (343) 375-48-99"
            "\nЭлектронная почта: m.s.kurochkina@urfu.ru"
            "\n\nВолкова Анна Владимировна"
            "\nСпециалист по образовательной деятельности"
            "\nС понедельника по пятницу с 10:00 до 17:00"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-137"
            "\nТелефон: 375-48-99"
            "\n+7 (992) 002-88-37"
            "\nЭлектронная почта: a.v.volkova@urfu.ru"
            "\n\nЛомыскина Людмила Владимировна"
            "\nСпециалист по образовательной деятельности"
            "\nОтдел организации образовательной деятельности по программам бакалавриата"
            "\nАдрес: ул. Мира, 32"
            "\nАудитория: Р-219"
            "\nТелефон: 375-48-99"
            "\nЭлектронная почта: l.v.lomyskina@urfu.ru"
}

custom_questions = {
    "Когда стипа?": "Завтра"
}


def create_categories():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add('Материальная помощь', 'Профсоюз', 'Контакты', 'Другие вопросы')
    return keyboard


def create_trade_union():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*trade_union.keys())
    keyboard.add('Назад')
    return keyboard


def create_budget_inst():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*budget_inst.keys())
    keyboard.add('Назад')
    return keyboard


def create_budget_univ():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*budget_univ.keys())
    keyboard.add('Назад')
    return keyboard


def create_contract():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*contract.keys())
    keyboard.add('Назад')
    return keyboard


def create_contacts():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*contacts.keys())
    keyboard.add('Назад')
    return keyboard


def create_aid_types():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add('Бюджет Институт', 'Бюджет Университет', 'Контракт')
    keyboard.add('Назад')
    return keyboard


def create_custom_questions():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*custom_questions.keys())
    keyboard.add('Назад')
    return keyboard


@bot.message_handler(commands=['get_chat_id'])
def get_chat_id(message):
    bot.send_message(message.chat.id, f"Ваш Chat ID: {message.chat.id}")


@bot.message_handler(commands=['start'])
def handle_start(message):
        bot.send_message(message.chat.id, "Привет! Я бот с ответами на часто задаваемые вопросы, "
                                          "связанные с материальной помощью и профсоюзом.",
                         reply_markup=create_categories())


@bot.message_handler(commands=['promote'])
def promote_user(message):
    if message.chat.id == admin_user_id:
        if message.reply_to_message and message.reply_to_message.from_user:
            user_id = message.reply_to_message.from_user.id
            bot.send_message(message.chat.id, f"Пользователь {user_id} назначен администратором.")
        else:
            bot.send_message(message.chat.id, "Ответьте на сообщение пользователя, которого вы хотите назначить администратором.")
    else:
        bot.send_message(message.chat.id, "У вас нет прав для выполнения этой команды.")


@bot.message_handler(commands=['admin'])
def handle_add_question(message):
    if message.chat.id == admin_user_id:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('/add_question')
        keyboard.add('/delete_question')
        keyboard.add('Назад')
        bot.send_message(message.chat.id,
                         "Привет, администратор! \nИспользуйте /add_question для добавления нового вопроса."
                         "\nЧтобы удалить вопрос используйте /delete_question", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "У вас нет прав для выполнения этой команды.")


@bot.message_handler(commands=['add_question'])
def handle_add_question(message):
    if message.chat.id == admin_user_id:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Отмена')
        bot.send_message(message.chat.id, "Введите новый вопрос:", reply_markup=keyboard)
        bot.register_next_step_handler(message, process_new_question)
    else:
        bot.send_message(message.chat.id, "У вас нет прав для выполнения этой команды.")


@bot.message_handler(commands=['delete_question'], func=lambda message: message.text)
def delete_question(message):
    if message.from_user.id == admin_user_id:
        keyboard = create_delete_question_menu()
        bot.send_message(message.chat.id, "Выберите вопрос для удаления:", reply_markup=keyboard)
        bot.register_next_step_handler(message, delete_question_choice)
    else:
        bot.send_message(message.chat.id, "У вас нет прав для выполнения этой команды.")


def create_delete_question_menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(*custom_questions.keys())
    keyboard.add('Отмена')
    return keyboard


def delete_question_choice(message):
    if message.from_user.id == admin_user_id:
        if message.text == 'Отмена':
            bot.send_message(message.chat.id, "Удаление вопроса отменено.", reply_markup=create_categories())
        else:
            question_to_delete = message.text
            del custom_questions[question_to_delete]
            bot.send_message(message.chat.id, f"Вопрос '{question_to_delete}' успешно удален.", reply_markup=create_categories())
    else:
        bot.send_message(message.chat.id, "У вас нет прав для выполнения этой команды.")


def process_new_question(message):
    new_question = message.text
    if new_question == 'Отмена':
        bot.send_message(message.chat.id, "Добавление вопроса отменено.", reply_markup=create_categories())
    else:
        bot.send_message(message.chat.id, "Введите ответ на вопрос:")
        bot.register_next_step_handler(message, lambda m: process_new_answer(m, new_question))


def process_new_answer(message, new_question):
    new_answer = message.text
    custom_questions[new_question] = new_answer
    bot.send_message(message.chat.id, "Новый вопрос и ответ успешно добавлены.", reply_markup=create_categories())


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_input = message.text

    if user_input in budget_inst:
        bot.send_message(message.chat.id, budget_inst[user_input])
        if "Причины и документы" in user_input:
            send_handbook(message)

    elif user_input in budget_univ:
        bot.send_message(message.chat.id, budget_univ[user_input])

    elif user_input in contract:
        bot.send_message(message.chat.id, contract[user_input])

    elif user_input in trade_union:
        bot.send_message(message.chat.id, trade_union[user_input])

    elif user_input in contacts:
        bot.send_message(message.chat.id, contacts[user_input])

    elif user_input in custom_questions:
        bot.send_message(message.chat.id, custom_questions[user_input])

    elif "Материальная помощь" in user_input:
        bot.send_message(message.chat.id, "Выберите тип матпомощи:", reply_markup=create_aid_types())

    elif "Профсоюз" in user_input:
        bot.send_message(message.chat.id, "Информация о профсоюзе", reply_markup=create_trade_union())

    elif "Бюджет Институт" in user_input:
        bot.send_message(message.chat.id, "Информация о матпомощи в институте для бюджетников", reply_markup=create_budget_inst())

    elif "Бюджет Университет" in user_input:
        bot.send_message(message.chat.id, "Информация о матпомощи в университете для бюджетников", reply_markup=create_budget_univ())

    elif "Контракт" in user_input:
        bot.send_message(message.chat.id, "Информация о матпомощи для контрактников", reply_markup=create_contract())

    elif "Контакты" in user_input:
        bot.send_message(message.chat.id, "Контакты", reply_markup=create_contacts())

    elif "Другие вопросы" in user_input:
        bot.send_message(message.chat.id, "Другие вопросы", reply_markup=create_custom_questions())

    elif "Назад" in user_input:
        bot.send_message(message.chat.id, "Возврат на главную", reply_markup=create_categories())

    else:
        bot.send_message(message.chat.id, "Извините, не могу понять ваш вопрос. Попробуйте другой.")


def send_handbook(message):
    with open('Obnovlennaya_pamyatka_po_matpomoschi.pdf', 'rb') as handbook:
        bot.send_document(message.chat.id, handbook, caption="Вот ваша памятка!")


if __name__ == "__main__":
    bot.polling(none_stop=True)
