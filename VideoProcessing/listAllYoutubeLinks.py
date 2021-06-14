from googleapiclient.discovery import build

api_key = 'AIzaSyAnKf80Rmc4ovHwtkO343Q9vNEtyRS64n4'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='schafer5'
    )

response = request.execute()

print(response)