from googleapiclient.discovery import build
import pandas as pd


api_key = 'AIzaSyDBDPtzYfi0DKoh81MlmHAVc6zoQl4ish8'
youtube = build('youtube', 'v3', developerKey=api_key)

channel_ids = [
    'UCZSNzBgFub_WWil6TOTYwAg',  # Netflix India
    'UC8md0UEGj7UbjcZtMjBVrgQ',  # Behindwoods TV
    'UC38z3fT9RO4yugLJoCZLygw',
    'UC1_GAegUKlzJVskZKcwpZuA'
]


def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    response = request.execute()
    return {
        'Channel_name': response['items'][0]['snippet']['title'],
        'Subscribers': int(response['items'][0]['statistics']['subscriberCount']),
        'Views': int(response['items'][0]['statistics']['viewCount']),
        'Total_videos': int(response['items'][0]['statistics']['videoCount'])
    }

channel_data = [get_channel_stats(youtube, channel_id) for channel_id in channel_ids]
df = pd.DataFrame(channel_data)

# sns.barplot(x='Channel_name', y='Subscribers', data=df)
# sns.barplot(x='Channel_name', y='Views', data=df)
# sns.barplot(x='Channel_name', y='Total_videos', data=df)


df.to_excel("youtube_channel_stats.xlsx", index=False)

