import numpy as pn 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# API-> Application Programing Interface
# api-> 2 ta software ake oporer sathe jogajog kore
# or api -> data pipelines- ticket kata 

# website theke api link collect korte hobe
#TMDB
# themoviedb.org 
#pip install requests

import requests
r=requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1')
# p=pd.DataFrame(r.json()['results'])
# print(p)

#ata page 1 ar jonno 
# data = r.json() 

# results = data['results']
# # p=pd.DataFrame(results)[['id','title','overview','release_date','popularity','vote_average','vote_count']]
# # print(p)

# #page 1 to 429

# df=pd.DataFrame() # empty dataframe
# for i in range(1,429):
#     r=requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))# string formating 
#     p=pd.DataFrame(results)[['id','title','overview','release_date','popularity','vote_average','vote_count']]
#     df=df.append(p,ignore_index=True) # append kaj kore na 

import requests
import pandas as pd

# Create an empty list to store data
movies_list = []

# Loop through pages 1 to 428
for i in range(1, 429):
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={i}"
    
    # Fetch API response
    r = requests.get(url)
    
    # Check if response is valid
    if r.status_code == 200:
        data = r.json()  # Convert response to JSON
        if 'results' in data:
            results = data['results']  # Extract movie list
            movies_list.extend(results)  # Add to list (instead of appending DataFrame)
        else:
            print(f"Skipping page {i}, no 'results' found.")
    else:
        print(f"Error fetching page {i}: {r.status_code}")

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(movies_list)[['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average', 'vote_count']]

# Save to CSV
df.to_csv("top_rated_movies.csv", index=False)

# Print first few rows
# print(df.head())

# run hote 2-3 min lage 


### kaggle a acount khule dataset/ csv file upload kore job offer pawya jaite pare
