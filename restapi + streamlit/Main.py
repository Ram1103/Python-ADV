import requests
import streamlit as st
import pandas as pd
api_key = "f54e9e41716e8d9622bb4b4f3a8b4175"
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
        #st.write("## Keys")
        #st.write(results[0].keys())
        movie_ids=list()
        movie_title=set()
        movie_RD=set()
        st.write('### Here are the movies related to', search_query)
        col1, col2 ,col3 ,col4 = st.columns(4) 
        with col1:
            st.write("#### Poster")  
        with col2:
            st.write("#### Name")  
        with col3:
            st.write("#### Movie ID")  
        with col4:
            st.write("#### Release Date")  
        

        for result in results:
            _id = result['id']
            _RD = result['release_date']
            _title = result['title']
            
            poster = (result['poster_path'])
            full_path = f"https://image.tmdb.org/t/p/w500/{poster}"
            col1, col2 ,col3 ,col4 = st.columns(4) 
            with col1:
                st.image(full_path)  
            with col2:
                st.write(result['title'])
            with col3:
                st.write(_id)
            with col4:
                st.write(_RD)

                     
            #st.image(full_path, 50)
            movie_ids.append(_id)
            movie_title.add(_title)
            movie_RD.add(_RD)
            
        






            
    else :
        if len(results)<=0:
            st.error("The movie is not available!!")        
        #st.write("## List of IDs")    
        #st.write(list(movie_ids))


#output = 'movies.csv'
#movie_data=[]
#for movie_id in movie_ids:
#    api_version = 3
#    api_base_url = f"https://api.themoviedb.org/{api_version}"
#    endpoint_path = f"/movie/{movie_id}"
#    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
#    r=requests.get(endpoint)
#    if r.status_code in range(200,229):
#        data = r.json()
#        movie_data.append(data)

#st.write("## Table")
#df=pd.DataFrame(movie_data)
#st.write(df.head()) 
#df.to_csv(output,index=False)





#df=pd.DataFrame(movie_title)
#st.table(data=df)
#db=pd.DataFrame(movie_ids,movie_RD,movie_id , columns=(movie_ids,movie_RD,movie_id) )
#st.table(data=db)
#st.dataframe(db)






#def fetch_poster(movie_id):
#    url = "https://api.themoviedb.org/3/movie/{}?api_key='YOUR API KEY'&language=en-US".format(movie_id)
#    data = requests.get(url)
#    data = data.json()
#    poster_path = data['poster_path']
#    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#    return full_path



#a=len(results)
#while a>=0:
    
#    col1, col2, col3, col4, col5 = st.columns(5) 
#                with col1:
#                    st.image(full_path)
#                with col2:
#                    st.image(full_path)
#                with col3:
#                    st.image(full_path)
#                with col4:
#                    st.image(full_path)
#                with col5:
#                    st.image(full_path)