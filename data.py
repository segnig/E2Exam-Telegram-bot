import pandas as pd
from datetime import datetime 


class User:
    def __init__(self, user_id, username=None, first_name=None, last_name=None):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.last_day_logged_in = datetime.now()
        self.daily_challenge_coin = 0
        self.login_days = 1  


def register_users(user, filename="user_info.csv"):
    try:
        users = pd.read_csv(filename).set_index("user_id")

        registered_users = set(users.index.to_list())

        if user.user_id not in registered_users:
            users.loc[user.user_id] = [user.username, user.first_name, user.last_name, 
                    user.last_day_logged_in, user.daily_challenge_coin, user.login_days]
            users.to_csv(filename)
            return True
        return False
    except Exception as e:
        print(f"An error occurred while registering user: {e}")
        return False

def update_user(user, filename="user_info.csv", daily_challenge=False, login_day=True):
    """
    This function updates the user's information in the CSV file. If the user doesn't exist, it registers the user.
    """
    try:
    
        users = pd.read_csv(filename).set_index("user_id")
        
        if user.user_id in set(users.index.tolist()):
            if daily_challenge:
                users.loc[user.user_id, "daily_challenge_coin"] += 1
                
            if login_day:
                users.loc[user.user_id, "last_day_logged_in"] = datetime.now()
                users.loc[user.user_id, "login_days"] += 1
            
            users.to_csv(filename)

        else:
            register_users(users)
    except Exception as e:
        print(f"An error occurred while updating user: {e}")





def get_coin(user_id, filename="user_info.csv"):#+
    """#+
    This function retrieves and updates the daily challenge coin balance for a user based on their login history.#+
    It also handles the scenario where a user logs in after a certain period of time.#+

    Parameters:#+
    user_id (int): The unique identifier of the user.#+
    filename (str): The name of the CSV file containing user information. Default is "user_info.csv".#+

    Returns:#+
    str: A success message with the updated coin balance if the user exists.#+
         If the user doesn't exist, it registers the user and calls get_coin again.#+
    """
    try:
        users = pd.read_csv(filename)
        if user_id in users["user_id"].values:
            
            last_date_str = users.loc[users["user_id"] == user_id, "last_day_logged_in"].values[0]#+
            
            last_date = datetime.strptime(last_date_str, "%Y-%m-%d %H:%M:%S.%f")
            
            # Get the current date as a datetime object
            current_date = datetime.now()
        
            # Calculate the difference in days between now and the last login
            delta_days = (current_date - last_date).days

            if delta_days == 1:
                users.loc[users["user_id"] == user_id, "daily_challenge_coin"] += 5
                users.loc[users["user_id"] == user_id, "login_days"] += 1

            elif delta_days == 2:
                
                current_coins = users.loc[users["user_id"] == user_id, "daily_challenge_coin"].values[0]
                new_coin_balance = max(0, current_coins - 5)  
                users.loc[users["user_id"] == user_id, "daily_challenge_coin"] = new_coin_balance
                users.loc[users["user_id"] == user_id, "login_days"] += 1
            
            elif delta_days > 2:
                users.loc[users["user_id"] == user_id, "daily_challenge_coin"] = 5
                users.loc[users["user_id"] == user_id, "login_days"] += 1
            
            users.loc[users["user_id"] == user_id, "last_day_logged_in"] = current_date.strftime("%Y-%m-%d %H:%M:%S.%f")
        
            
            users.to_csv(filename, index=False)
        
            coins = users.loc[users["user_id"] == user_id, "daily_challenge_coin"].values[0]
            return f"Wow! You’ve accumulated {coins} 🪙 E2Exam Coins and made remarkable progress—what an achievement!"

        else:
            # If user doesn't exist, register the user and call get_coin again
            register_users(User(user_id))  # Assuming register_users is defined elsewhere
            return get_coin(user_id, filename)
    except Exception as e:
        print(f"An error occurred while retrieving coin balance: {e}")
        return "Error retrieving coin balance"
    

def my_coins(user_id, filename="user_info.csv"):
    """#+
    This function retrieves the daily challenge coin balance for a user from the CSV file.
    """
    try:
        users = pd.read_csv(filename)
        if user_id in users["user_id"].values:
            coins = users.loc[users["user_id"] == user_id, "daily_challenge_coin"].values[0]
            return f"You have {coins} ��� E2Exam Coins."
        else:
            return "User not found. Please register first."
    except Exception as e:
        print(f"An error occurred while retrieving coin balance: {e}")
        return "Error retrieving coin balance"
