import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Set your API credentials file path
CLIENT_SECRETS_FILE = 'path/to/client_secrets.json' # insert this folder

# Set the YouTube playlist ID
PLAYLIST_ID = 'your_playlist_id'
PLAYLIST_ID = 'PLeCGyxHfyxFfJm9t4XVQEEn9W6CJG6Fsv'

def authenticate():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, ['https://www.googleapis.com/auth/youtube.force-ssl']
    )
    credentials = flow.run_local_server(port=0)
    return googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

def add_to_playlist(youtube, video_id):
    request = youtube.playlistItems().insert(
        part='snippet',
        body={
            'snippet': {
                'playlistId': PLAYLIST_ID,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id,
                },
            },
        },
    )
    try:
        response = request.execute()
        print(f'Successfully added video to playlist. ID: {response["id"]}')
    except googleapiclient.errors.HttpError as e:
        print(f'Error adding video to playlist: {e}')

def main():
    youtube = authenticate()

    # Replace 'VIDEO_ID' with the actual video ID you want to add
    video_id = 'e_E9W2vsRbQ'
    add_to_playlist(youtube, video_id)

if __name__ == '__main__':
    main()



#Replace `'your_playlist_id'` and `'VIDEO_ID'` with your actual playlist ID and the ID of the video you want to add, respectively. Also, make sure to replace `'path/to/client_secrets.json'` with the path to your API credentials file.