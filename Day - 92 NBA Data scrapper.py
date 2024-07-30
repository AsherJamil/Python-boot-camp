# This program will create a CSV file

from nba_api.stats.endpoints import leagueleaders
import pandas as pd
import time


def fetch_nba_stats():
    try:
        # Fetch data from the API
        leaders = leagueleaders.LeagueLeaders()
        df = leaders.get_data_frames()[0]

        # Select relevant columns
        columns = ['PLAYER', 'TEAM', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A',
                   'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV']
        df = df[columns]

        # Save to CSV
        df.to_csv('nba_player_stats.csv', index=False)
        print("Data has been fetched and saved to 'nba_player_stats.csv'")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    max_retries = 3
    for attempt in range(max_retries):
        try:
            fetch_nba_stats()
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in 5 seconds... (Attempt {
                      attempt + 2}/{max_retries})")
                time.sleep(5)
            else:
                print(
                    "Max retries reached. Please check your internet connection or the API status.")
