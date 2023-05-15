import requests
import pprint
import pandas as pd
api_key = "f54e9e41716e8d9622bb4b4f3a8b4175"
api_keyv4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNTRlOWU0MTcxNmU4ZDk2MjJiYjRiNGYzYThiNDE3NSIsInN1YiI6IjY0NjBjY2U2OGM0NGI5MDE1M2RiNTRjMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B8dTLhVzRm242UtaskDVB6EEVcqy1GYQ1cqJ4Umb5sk"
# HTTP requests

# Endpoint - URL

# What is the HTTP method that we need?

# https://api.themoviedb.org/3/movie/550?api_key=f54e9e41716e8d9622bb4b4f3a8b4175 
'''movie_id = 550
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
r=requests.get(endpoint) #data={"api_key" : api_key})
print(r.status_code)
print(r.text)'''

#search
movie_id = 550
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix" 
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
#print(endpoint)
r=requests.get(endpoint) 
#pprint.pprint(r.json())
if r.status_code in range(200,299):
    data=r.json()
    results=data['results']
    if len(results)>0: 
        #print(results[0].keys())
        movie_ids=set()
        for result in results:
            _id = result['id']
            #print(result['title'],_id)
            movie_ids.add(_id)
        #print(list(movie_ids))

output = 'movies.csv'
movie_data=[]
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r=requests.get(endpoint)
    if r.status_code in range(200,229):
        data = r.json()
        movie_data.append(data)

df=pd.DataFrame(movie_data)
print(df.head()) 
df.to_csv(output,index=False)
