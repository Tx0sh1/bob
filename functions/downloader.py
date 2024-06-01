import requests

def downloader():
    url = "https://youtube-mp3-downloader5.p.rapidapi.com/"
    try:
        video_url = input("input link: ")
    except:
        print("invalid link")
    
    querystring = {"url":video_url}

    headers = {
        "X-RapidAPI-Key": "YOUR API HERE",
        "X-RapidAPI-Host": "youtube-mp3-downloader5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    song = response.json()['status','title','link']
    print(song)