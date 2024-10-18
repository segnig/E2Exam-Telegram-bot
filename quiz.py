from datetime import datetime
import pandas as pd


def daily_challenge():
    return get_quiz(daily_challenge=True)



def get_quiz(daily_challenge=False, file_name="daily_challenge.csv"):
    questions = pd.read_csv(file_name)

    choosen = []
    
    if daily_challenge:
        try:
            if datetime.now().strftime("%Y-%m-%d") in set(questions["tag"].to_list()):
                choosen = questions[questions["tag"] == datetime.now().strftime("%Y-%m-%d")]
            else:
                choosen = questions[questions["tag"] == "cooming"].head()

            for index, row in questions.iterrows():
                if index in choosen.index:
                    if row["tag"] == "cooming":
                        questions.at[index, "tag"] = datetime.now().strftime("%Y-%m-%d")
                    questions.at[index, "total_participants"] = int(row["total_participants"]) + 1
            questions.to_csv(file_name, index=False)  # Specify index=False here to exclude the index column
            return choosen
        except Exception as e:
            print(f"Error occurred while getting quiz: {e}")
            return None
    
    else:
        try:
            questions = questions.sample(frac=1).reset_index(drop=True)
            return questions.head()
        except Exception as e:
            print(f"Error occurred while getting quiz: {e}")
            return None