"""
sample.py : A sample program for LINE BOT API (for Python)

Copyright (c) 2016 Gaku Nakagawa
This software is released under the MIT License.
Please see LICENSE or visit http://opensource.org/licenses/mit-license.php
"""

import linebot

# api config
id     = "Your Channel ID"
mid    = "Your Channel MID"
secret = "Your Channel Secret"

# Test target user
target = "Target user MID"

# initialize API
api = linebot.LINEbot(channel_id=id, channel_secret=secret, channel_mid=mid)

# send message
api.send_text_msg(target, "IMAGINE THE FUTURE.")

# get user info
info = api.get_user_info(target)
print("User Name: {0}".format(info['displayName']))
print("MID: {0}".format(info['mid']))
print("Profile Picture: {0}".format(info['pictureUrl']))
print("Status: {0}".format(info['statusMessage']))
