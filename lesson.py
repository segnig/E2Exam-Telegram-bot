import pandas as pd
from datetime import datetime

def today_lesson(file_name = "daily_lesson.csv"):
    """
    Read the CSV file containing daily lesson information and return the details of today's lesson.
    """
    # Read the CSV file
    try:
        df = pd.read_csv(file_name)
        
        # Get today's date

        if datetime.now().strftime("%Y-%m-%d") in set(df["tag"].to_list()):
            # Filter the DataFrame for today's lesson
            today_lesson = df[df["tag"] == datetime.now().strftime("%Y-%m-%d")]

        else:
            # If no lesson is scheduled for today, return a message
            today_lesson = df[df["tag"] == "cooming"].head(1)

        for index, row in df.iterrows():
            if index in today_lesson.index:
                df.at[index, "tag"] = datetime.now().strftime("%Y-%m-%d")
                
            df.to_csv(file_name, index=False)
        return today_lesson["lesson"]
    
    except Exception as e:
        return str(e)
