from datetime import datetime
import pandas as pd
import time 


NOTIFICATION_SEND_TIMES = set(
    [
        "07:30", "10:02", "12:30", "15:40","17:20","20:00","22:00",
    ]
)

MESSAGES = """
🌟 Attention, Future Scholars! 🌟

With a significant number of students 
facing challenges in the entrance exam, 
remember that every little effort counts.

Our daily quizzes and lessons are 
designed to help you strengthen your 
knowledge and boost your confidence. 
Why not take a few minutes 
today to explore the quiz? 
Your future self will appreciate it!

Stay focused, and let’s succeed together! 🚀
"""

def daily_notification_message(bot, message=MESSAGES):
    # Check if the current time matches any notification send times
    current_time = datetime.now().strftime("%H:%M")
    print(f"Current time: {current_time}")
    
    if current_time in NOTIFICATION_SEND_TIMES:
        # Read the CSV file and get the list of user IDs
        try:
            users = pd.read_csv("user_info.csv")["user_id"].tolist()
            print("Users in the database are:", users)
        except Exception as e:
            print("Error reading the user database:", e)
            return
        
        # Send the notification message to each user
        for user_id in users:
            try:
                bot.send_message(user_id, message)
            except Exception as e:
                print(f"Error sending message to user {user_id}: {e}")
        time.sleep(60)
            

