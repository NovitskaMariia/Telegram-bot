import config
import telebot
import openai

bot = telebot.TeleBot(config.BOT_TOKEN)
openai.api_key = config.openai_key

welcome_text = False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global welcome_text
    if not welcome_text:
        bot.send_message(message.chat.id, "Виберіть опцію:", reply_markup=create_keyboard())
        welcome_text = True


def create_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Спілкуватись з чатом GPT")
    btn2 = telebot.types.KeyboardButton("Згенерувати картинку")
    btn3 = telebot.types.KeyboardButton("Втрати русні на сьогодні")
    markup.add(btn1, btn2, btn3)
    return markup

@bot.message_handler(func=lambda message: message.text == "Спілкуватись з чатом GPT")
def write_question(message):
    print("Напиши своє питання:")
    bot.send_message(message.chat.id, "Напиши своє питання:")

# @bot.message_handler(func=lambda message: True)
# def handle_text(message):
#     print("GPT")
#     if message.text == "Спілкуватись з чатом GPT":
#         bot.send_message(message.chat.id, "Напиши своє питання:")
#         ask_gpt_question(message)
#     elif message.text == "Згенерувати картинку":
#         bot.send_message(message.chat.id, "Що має бути на картинці?")
#     elif message.text == "Втрати русні на сьогодні":
#         # Реалізуйте функцію для отримання інформації зі сторінки та відправки її користувачу тут
#         pass
@bot.message_handler(func=lambda message: True)
def ask_gpt_question(message):
    print("go to GPT")
    response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message.text,
            max_tokens=100  # Кількість слів у відповіді
        )
    bot.send_message(message.chat.id, response.choices[0].text)
    
if __name__ == '__main__':
    print("loop works")
    bot.infinity_polling()