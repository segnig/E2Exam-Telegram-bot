import logging
import nest_asyncio
import telebot
import time
from telebot import types
import threading

from notification import daily_notification_message
from data import * 
from quiz import * 
from lesson import *
from text_format import *


# Apply nest_asyncio
nest_asyncio.apply()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


BOT_TOKEN = "7634182668:AAFdXvpABJfi7ju2y1QzIjg_Sxoi3b1sU-Y"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['get'])
def start(message):
    bot.send_message(message.chat.id, f"{datetime.now().strftime("%H:%M")}")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'Contact us',)


from datetime import datetime
daily_notification_message(bot=bot)
def main_menu(message):
    EXAM_DAY = datetime.strptime("2025-07-12", "%Y-%m-%d")

    CURRENT_DAY = datetime.now()
    DAY_LEFT = EXAM_DAY - CURRENT_DAY
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    countdown_button = types.KeyboardButton(f"{DAY_LEFT.days} Days left!")
    daily_quiz_button = types.KeyboardButton("Daily Quiz")
    daily_lesson_button = types.KeyboardButton("Daily Lesson")
    join_channel_button = types.KeyboardButton("Join Channel")
    random_quiz_button = types.KeyboardButton("Random Quiz")
    my_wallet = types.KeyboardButton("My Wallet")

    
    markup.add(countdown_button)
    markup.add( daily_quiz_button, daily_lesson_button, random_quiz_button)
    markup.add(join_channel_button, my_wallet)

    try:
        check_list = bot.send_video(message.chat.id, r"https://cdn-icons-mp4.flaticon.com/512/6416/6416398.mp4", 
                   caption="Welcome! To E2Exam \n Choose an option:")
    except Exception as e:
        logger.error(f"Failed to send video: {str(e)}")
        bot.send_message(message.chat.id, "Failed to send message, please try again later.")
        return

    bot.send_message(message.chat.id, "Menu:", reply_markup=markup)
    time.sleep(60)
    bot.delete_message(chat_id=message.chat.id, message_id=check_list.message_id)



def fetch_user(message):
    user = User(message.from_user.id)
    user.first_name = message.from_user.first_name
    user.last_name = message.from_user.last_name
    user.username = message.from_user.username
    register_users(user=user)




# Command handler for /start
@bot.message_handler(commands=['start'])
def start(message):
    fetch_user(message)
    main_menu(message)


from datetime import datetime


def start_days_left_countdown(message):
    EXAM_DAY = datetime.strptime("2025-07-12", "%Y-%m-%d")
    CURRENT_DAY = datetime.now()
    days_left = (EXAM_DAY - CURRENT_DAY).days

    emoji_days_left = format_days_left_in_emoji_clock(days_left)
    try:
        countdown_message = bot.send_message(message.chat.id, f"𝓓𝓪𝔂𝓼 𝓛𝓮𝓯𝓽\n{emoji_days_left}")
    except Exception as e:
        logger.error(f"Failed to send countdown message: {str(e)}")
        return

    time.sleep(10)
    bot.delete_message(message.chat.id, countdown_message.message_id)


# Command handler for countdown
@bot.message_handler(func=lambda message: message.text[-10:] == "Days left!")
def countdown(message):
    # Start the countdown for days left
    try:
        threading.Thread(target=start_days_left_countdown, args=(message,)).start()
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        logger.error(f"Failed to start countdown: {str(e)}")




# Handler for the daily quiz button (poll format)
@bot.message_handler(func=lambda message: message.text == "Daily Quiz")
def daily_quiz(message):
    daily_questions = daily_challenge()
    try:
        quiz_bot = bot.send_photo(message.chat.id, "https://cdn-icons-png.flaticon.com/256/8764/8764648.png")
        bot.delete_message(message.chat.id, message_id=message.message_id)
        for i in range(len(daily_questions)):
            question = daily_questions.iloc[i]["question"]
            options = [daily_questions.iloc[i]["choice_a"], daily_questions.iloc[i]["choice_b"], daily_questions.iloc[i]["choice_c"], daily_questions.iloc[i]["choice_d"]]
            correct_option = ord(daily_questions.iloc[i]["answer"].lower()) - ord("a")

            
            
            bot.send_message(message.chat.id, "30 seconds")
            bot.send_poll(
                message.chat.id,
                question,
                options,
                is_anonymous=False,
                type="quiz",
                correct_option_id=correct_option,
                explanation=daily_questions.iloc[i]["solution"]
            )
            time.sleep(30)
    except Exception as e:
        logger.error(f"Failed to send daily quiz: {str(e)}")

        # Daily challenge coins
    try:
        bot.send_message(
            message.chat.id,
            get_coin(user_id=message.from_user.id)
        )
    except Exception as e:
        logger.error(f"Failed to send daily challenge coins: {str(e)}")





@bot.message_handler(func=lambda message: message.text == "Random Quiz")
def daily_quiz(message):
    daily_questions = get_quiz()
    try:

        bot.delete_message(message.chat.id, message_id=message.message_id)
        for i in range(len(daily_questions)):
            question = daily_questions.iloc[i]["question"]
            options = [daily_questions.iloc[i]["choice_a"], daily_questions.iloc[i]["choice_b"], daily_questions.iloc[i]["choice_c"], daily_questions.iloc[i]["choice_d"]]
            correct_option = ord(daily_questions.iloc[i]["answer"].lower()) - ord("a")
            
            bot.send_message(message.chat.id, "30 seconds")
            bot.send_poll(
                message.chat.id,
                question,
                options,
                is_anonymous=False,
                type="quiz",
                correct_option_id=correct_option,
                explanation=daily_questions.iloc[i]["solution"]
            )
            time.sleep(30)
    except Exception as e:
        logger.error(f"Failed to send daily quiz: {str(e)}")   

# Handler for the daily lesson button
@bot.message_handler(func=lambda message: message.text == "Daily Lesson")
def daily_lesson(message):
    try:
        daily_tittle_head = bot.send_message(message.chat.id, f"Daily Lesson {datetime.now().strftime("%Y-%m-%d")}")
        lesson = bot.send_message(message.chat.id, today_lesson())
        bot.delete_message(message.chat.id, message_id=message.message_id)
        time.sleep(300)
        bot.delete_message(message.chat.id, message_id=daily_tittle_head.message_id)
        bot.delete_message(message.chat.id, message_id=lesson.message_id)
    except Exception as e:
        logger.error(f"Failed to send daily lesson: {str(e)}")
        return




# Handler for the join channel button
@bot.message_handler(func=lambda message: message.text == "Join Channel")
def join_channel(message):
    try:
        bot.send_message(
            message.chat.id, 
            "Join our channel here: [Click Here](https://t.me/E2Exam)", 
            parse_mode='Markdown'
        )
        bot.delete_message(message.chat.id, message_id=message.message_id)
    except Exception as e:
        logger.error(f"Failed to send join channel message: {str(e)}")
        return


@bot.message_handler(func= lambda message: message.text == "My Wallet")
def send_wallet(message):
    try:
        wallet_image = bot.send_photo(
            message.chat.id,
            "https://cdn-icons-png.flaticon.com/128/6826/6826311.png",
            caption=f"Your wallet has: {get_coin(user_id=message.from_user.id)} E2Exam coins."
        )

        bot.delete_message(message.chat.id, message_id=message.message_id)
        time.sleep(10)
        bot.delete_message(message.chat.id, message_id=wallet_image.message_id)
    except Exception as e:
        logger.error(f"Failed to send wallet message: {str(e)}")
        return


def main():
    try:
        notification_thread = threading.Thread(target=daily_notification_message, args=(bot,))
        notification_thread.start()
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(f"Failed to start bot polling: {str(e)}")

if __name__ == '__main__':
    main()

