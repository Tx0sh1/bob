import requests

def get_movie_info(title):
    base_url = "http://www.omdbapi.com/"
    params = {
        'apikey': 'YOUR API HERE', 
        't': title,
        'plot': 'short',  
        'type': 'movie' 
    }

    response = requests.get(base_url, params=params)

    # Check for valid response
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return data  
        else:
            return None 
    else:
        print("Error fetching data from OMDb API.")
        return None  

def info():
    while True:
        title = input("Enter movie name (or 'exit' to quit): ")
        if title.lower() == 'exit':
            break

        movie_data = get_movie_info(title)

        if movie_data:
            print(f"Title: {movie_data['Title']}")  
            print(f"Year: {movie_data['Year']}")
            print(f"Plot: {movie_data['Plot']}")
        else:
            print(f"Movie '{title}' not found.") 
