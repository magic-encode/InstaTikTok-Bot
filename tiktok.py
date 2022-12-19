
def tk(link):
    import requests
    import json
    
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "ca467c7575mshaa509529780c0fcp10eb37jsn38301733cea7",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.text
    rest = json.loads(result)
    
    return {'video': rest['video'][0], 'music': rest['music'][0]}

