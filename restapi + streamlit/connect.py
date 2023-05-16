import requests
import pprint
import pandas as pd
api_key = "f54e9e41716e8d9622bb4b4f3a8b4175"
#api_keyv4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNTRlOWU0MTcxNmU4ZDk2MjJiYjRiNGYzYThiNDE3NSIsInN1YiI6IjY0NjBjY2U2OGM0NGI5MDE1M2RiNTRjMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B8dTLhVzRm242UtaskDVB6EEVcqy1GYQ1cqJ4Umb5sk"
import streamlit as st
# HTTP requests
# Endpoint - URL
# What is the HTTP method that we need?
# https://api.themoviedb.org/3/movie/550?api_key=f54e9e41716e8d9622bb4b4f3a8b4175 
#movie_id = 550
#api_version = 3
#api_base_url = f"https://api.themoviedb.org/{api_version}"
#endpoint_path = f"/movie/{movie_id}"
#endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
#print(endpoint)
#r=requests.get(endpoint) #data={"api_key" : api_key})
#print(r.status_code)
#print(r.text)'''




#search
movie_id = 550
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
st.write('# Search your movie!')
search_query = st.text_input(" Enter here! ")
st.write('### The current movie title is', search_query)
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
#print(endpoint)
r=requests.get(endpoint) 
#pprint.pprint(r.json())
if r.status_code in range(200,299):
    
    data=r.json()
    results=data['results']
    if len(results)>0: 
        st.success("The movie is available!")
        st.write("## Keys")
        st.write(results[0].keys())
        movie_ids=list()
        movie_title=set()
        movie_RD=set()
        st.write("## Titile and Movie ID")
        st.write("##### Result    ID")
        for result in results:
            _id = result['id']
            _RD = result['release_date']
            _title = result['title']
            st.write(result['title'],_id, _RD)
            
            if _id == "":
                _id = 0
            if _RD == "":
                _RD = 0
            if _title == "" :
                _title = "NULL"
                         
                
            movie_ids.append(_id)
            movie_title.add(_title)
            movie_RD.add(_RD)
            
    else :
        if len(results)<=0:
            st.error("The movie is not available!!")        
        #st.write("## List of IDs")    
        #st.write(list(movie_ids))
        

df=pd.DataFrame(movie_title , columns= "title")
st.table(data=df)
db=pd.DataFrame(movie_ids,movie_RD,movie_id , columns=(movie_ids,movie_RD,movie_id) )
st.table(data=db)
st.dataframe(db)

