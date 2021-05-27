from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


def get_thumbs(items):

    thumb_urls = []
    video_urls = []

    DEVELOPER_KEY = ""
    YOUTUBE_API_SERVICE_NAME="youtube"
    YOUTUBE_API_VERSION="v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    for item in items:
        temp1 = []
        temp2 = []
        for query in item:
            search_response = youtube.search().list(
            q = query,
            order = "relevance",
            part = "snippet",
            maxResults = 1
            ).execute()
            temp1.append(search_response['items'][0]['snippet']['thumbnails']['default']['url'])
            temp2.append("https://www.youtube.com/watch?v=" + search_response['items'][0]['id']['videoId'])
        thumb_urls.append(temp1)
        video_urls.append(temp2)

    return thumb_urls, video_urls   


if __name__ == '__main__':
     test = ['mac ayres- Easy']#, 'mac ayres-Walking Home', 'Green Day - Welcome to Paradise', 'Imagine Dragons - Believer']
     get_thumbs(test)
