import telebot
from telebot import types
import sqlite3

TOKEN = '6781150801:AAHauw6N7LAtxrvtdL7w-GaDPYijFqtEW6Y'

admin_user_id = [741705263]

# Для входа в панель администратора нужно написать в боте /admin
# Чтобы назначить пользователя администратором, нужно добавить chat id пользователя в переменную admin_user_id
# Чтобы получить chat id пользователя, нужно в боте написать команду "/get_id"

bot = telebot.TeleBot(TOKEN)

db_path = 'faq_database.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('SELECT question, answer FROM budget_institute')
budget_inst = {question: answer for question, answer in cursor.fetchall()}

cursor.execute('SELECT question, answer FROM budget_university')
budget_univ = {question: answer for question, answer in cursor.fetchall()}

cursor.execute('SELECT question, answer FROM contract')
contract = {question: answer for question, answer in cursor.fetchall()}

cursor.execute('SELECT question, answer FROM trade_union')
trade_union = {question: answer for question, answer in cursor.fetchall()}

cursor.execute('SELECT question, answer FROM contacts')
contacts = {question: answer for question, answer in cursor.fetchall()}

cursor.execute('SELECT question, answer FROM other_questions')
custom_questions = {question: answer for question, answer in cursor.fetchall()}

conn.close()


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


@bot.message_handler(commands=['get_id'])
def get_chat_id(message):
    bot.send_message(message.chat.id, f"Ваш Chat ID: {message.chat.id}")


@bot.message_handler(commands=['start'])
def handle_start(message):
        bot.send_message(message.chat.id, "Привет! Я бот с ответами на часто задаваемые вопросы, "
                                          "связанные с материальной помощью и профсоюзом.",
                         reply_markup=create_categories())


@bot.message_handler(commands=['admin'])
def handle_add_question(message):
    if message.chat.id in admin_user_id:
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
    if message.chat.id in admin_user_id:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Отмена')
        bot.send_message(message.chat.id, "Введите новый вопрос:", reply_markup=keyboard)
        bot.register_next_step_handler(message, process_new_question)
    else:
        bot.send_message(message.chat.id, "У вас нет прав для выполнения этой команды.")


@bot.message_handler(commands=['delete_question'], func=lambda message: message.text)
def delete_question(message):
    if message.from_user.id in admin_user_id:
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
    if message.from_user.id in admin_user_id:
        if message.text == 'Отмена':
            bot.send_message(message.chat.id, "Удаление вопроса отменено.", reply_markup=create_categories())
        else:
            question_to_delete = message.text
            del custom_questions[question_to_delete]

            db_path = 'faq_database.db'
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM other_questions WHERE question = ?', (question_to_delete,))
            conn.commit()
            conn.close()

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

    db_path = 'faq_database.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO other_questions (question, answer) VALUES (?, ?)', (new_question, new_answer))
    conn.commit()
    conn.close()

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
