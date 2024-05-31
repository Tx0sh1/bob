import requests

def get_movie_info(title):
    base_url = "http://www.omdbapi.com/"
    params = {
        'apikey': 'YOUR API KEY HERE',
        't': title,
        'plot': 'short',
        'type': 'movie'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['Response'] == 'True':
        return data  # Movie information found
    else:
        return None  # Movie not found


def info():
    title = input("Enter movie name: ")  # Store user input in a variable
    movie_data = get_movie_info(title)

    if movie_data:
        print(f"Title: {movie_data['Title']}")  # Use f-strings for cleaner output
        print(f"Year: {movie_data['Year']}")
        print(f"Plot: {movie_data['Plot']}")
    else:
        print(f"Movie '{title}' not found.")  # Inform user if movie isn't found


