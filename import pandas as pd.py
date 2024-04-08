import pandas as pd

# Read the spreadsheet into a DataFrame 1
data = pd.read_excel('C:/Users/evand/Downloads/baseball (1).xlsx')

# Extract the required columns
runs_scored = data.iloc[16, 3]
runs_allowed = data.iloc[16, 4]
wins = data.iloc[16, 5]
obp = data.iloc[16, 6]
slg = data.iloc[16, 7]
batting_avg = data.iloc[16, 8]

# Define the prediction model
def predict_playoffs(runs_scored, runs_allowed, wins, obp, slg, batting_avg):
    # Explanation for using each piece of information:
    # - Runs scored: A team that scores more runs is generally more likely to win games and make the playoffs.
    # - Runs allowed: A team that allows fewer runs is generally more likely to win games and make the playoffs.
    # - Wins: The number of wins directly reflects the team's performance and can be a good indicator of playoff chances.
    # - OBP (On-Base Percentage): A higher OBP indicates that the team's batters are getting on base more frequently, which can lead to more runs and wins.
    # - SLG (Slugging Percentage): A higher SLG indicates that the team's batters are hitting for more power, which can also lead to more runs and wins.
    # - Batting average: A higher batting average indicates that the team's batters are hitting the ball well, which can contribute to more runs and wins.

    # Make the prediction based on the given criteria
    if runs_scored > runs_allowed and wins > 90 and obp > 0.350 and slg > 0.450 and batting_avg > 0.250:
        return "The team is predicted to make the playoffs."
    else:
        return "The team is predicted to not make the playoffs."

# Call the prediction function and print the result
prediction = predict_playoffs(runs_scored, runs_allowed, wins, obp, slg, batting_avg)
print(prediction)