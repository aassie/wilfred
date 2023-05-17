import os
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
channel_id = 'CHANNEL_ID'
message = " ".join(sys.argv[1:])
try:
    response = client.chat_postMessage(
        channel=channel_id,
        text=message
    )
    print("Message sent: ", response['message']['text'])
except SlackApiError as e:
    print("Error sending message: {}".format(e))
