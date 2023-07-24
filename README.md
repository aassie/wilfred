# wilfred

This project was the idea of coding a personal assistant on Slack. The bot's current main function is to keep me updated when a remote job end on a computing cluster by sending a message on a dedicated channel on my personal Slack.

## Installation

1. Install the Slack Developer Kit for Python:
a. Open a terminal window and run the command:
`pip install slack-sdk.`

2. Get the bot token:
a. In the Slack API dashboard, go to the “Install App” section.
b. Click “Install App to Workspace” and follow the prompts.
c. Allow Bot token. I used the following ones:`channels:join`, `channels:read` and `channels:write`

d. Copy the “Bot User OAuth Access Token” - this will be used to authenticate your bot.

## Usage

1. Bot configuration:
  Authentification: Set the bot token as environment variable
`export SLACK_BOT_TOKEN="THE_TOKEN"`
2. Bot join your channel
On Slack, right-click on the channel you want your bot to join, then click `View channel details`. You will find the channel ID information at the bottom of the new pop-up window. Use that token and replace the `CHANNEL_ID` placeholder in both Python codes.

3. Bot message
This code, when used as `python wilfred_message.py "My message"` will post "My message' in the channel joined above.
