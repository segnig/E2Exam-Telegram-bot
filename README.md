# E2Exam Telegram Bot

Welcome to the E2Exam Telegram Bot! This bot is designed to assist users in preparing for exams by providing daily quizzes, lessons, and notifications. It also allows users to track their progress and manage their virtual wallets.

## Features

- **Daily Quiz**: Participate in daily quizzes to test your knowledge.
- **Daily Lesson**: Receive educational lessons every day.
- **Countdown to Exam**: Stay informed about the number of days left until the exam.
- **Wallet Management**: Check your E2Exam coins balance.
- **Join Channel**: Easily join the E2Exam Telegram channel for updates.

## Installation

To set up the E2Exam Telegram Bot, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/e2exam-telegram-bot.git
   cd e2exam-telegram-bot
   ```

2. **Install required packages**:
   Make sure you have Python 3.x installed. Then, install the required packages using pip:
   ```bash
   pip install pyTelegramBotAPI telebot
   ```

3. **Set up your bot token**:
   Replace the `BOT_TOKEN` variable in the code with your own Telegram bot token, which you can obtain by creating a new bot through [BotFather](https://t.me/botfather).

4. **Configure additional modules**:
   Ensure that the `notification`, `data`, `quiz`, `lesson`, and `text_format` modules are correctly implemented and imported. These modules should contain the necessary functions and data for the bot to operate.

## Usage

1. **Start the bot**:
   Run the bot by executing the main script:
   ```bash
   python main.py
   ```

2. **Interact with the bot**:
   - Send `/start` to initialize the bot and fetch user details.
   - Use `/help` to get assistance with bot commands.
   - Click the buttons in the main menu to access different features:
     - **Daily Quiz**: Start a daily quiz challenge.
     - **Daily Lesson**: Receive the daily lesson.
     - **Join Channel**: Join the E2Exam channel for updates.
     - **My Wallet**: Check your E2Exam coins balance.
     - **Countdown**: See how many days are left until the exam.

## Logging

The bot includes logging functionality to help troubleshoot issues. Logs are printed to the console, and you can adjust the logging level in the code if necessary.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.


## Contact

For any questions or support, don't hesitate to get in touch with segni.girma@astu.edu.et
