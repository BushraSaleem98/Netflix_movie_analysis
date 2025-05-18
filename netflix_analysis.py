# Netflix 1990s Analysis (DataCamp Project)
# Author: Bushra Saleem
# Dataset: DataCamp (netflix_data.csv)

# netflix_analysis.py
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")  # Note: "Download from DataCamp"

# Filter for only movies
movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Filter movies from the 1990s
movies_90s = movies_only[
    (movies_only["release_year"] >= 1990) & (movies_only["release_year"] <= 1999)
]

# Ensure the 'duration' column is string, then extract numeric part
movies_90s["duration"] = movies_90s["duration"].astype(str)
movies_90s["duration_mins"] = movies_90s["duration"].str.replace(" min", "")
movies_90s["duration_mins"] = movies_90s["duration_mins"].astype(int)

# Most frequent duration
duration = int(movies_90s["duration_mins"].mode()[0])
print("Most frequent duration in the 1990s is:", duration, "minutes.")

# Count short action movies
short_movies = movies_90s[movies_90s["duration_mins"] < 90]
short_action_movies = short_movies[short_movies["genre"].str.contains("Action", na=False)]
short_movie_count = len(short_action_movies)
print("Short action movies in the 1990s:", short_movie_count)