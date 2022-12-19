import json


def instadown(link):
    import requests

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "ca467c7575mshaa509529780c0fcp10eb37jsn38301733cea7",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    
    if 'error' in rest:
        return 'Tashlagan linkiyizda xatolik bor...'
    else:
        dict = {}
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Story-Video':
            dict['type'] = 'story-video'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Tashlagan linkplain xatolik bor...'
        
