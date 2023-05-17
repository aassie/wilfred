import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
channel_id = 'CHANNEL_ID'
try:
    response = client.conversations_join(channel=channel_id)
    print("Bot has joined the channel: ", response['channel']['name'])
except SlackApiError as e:
    print("Error joining channel: {}".format(e))

try:
    response = client.chat_postMessage(
        channel=channel_id,
        text="Hello, World! I am Wilfred your personal assistant."
    )
    print("Message sent: ", response['message']['text'])
except SlackApiError as e:
    print("Error sending message: {}".format(e))
