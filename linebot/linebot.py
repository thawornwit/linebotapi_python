"""
linebot.py : A Python module for LINE BOT API (https://developers.line.me/bot-api/overview)

Copyright (c) 2016 Gaku Nakagawa
This software is released under the MIT License.
Please see LICENSE or visit http://opensource.org/licenses/mit-license.php
"""

import urllib.error
import urllib.request
import json

class LINEbot:
    def __init__(self, channel_id, channel_secret, channel_mid):
        self.channel_id     = channel_id
        self.channel_secret = channel_secret
        self.channel_mid    = channel_mid

    def __generate_request_header(self):
        header = {
            "X-Line-ChannelID":self.channel_id,
            "X-Line-ChannelSecret":self.channel_secret,
            "X-Line-Trusted-User-With-ACL":self.channel_mid
        }
        return header
        
    def send_text_msg(self, target_mid, text):
        data = {
            "to":[target_mid],
            "toChannel":1383378250,
            "eventType":"138311608800106203",
            "content":{"contentType":1,"toType":1,"text":text}
        }

        header = self.__generate_request_header()
        header["Content-Type"] = "application/json;charset=UTF-8"
        
        send_data = json.dumps(data).encode("utf-8")
        req = urllib.request.Request("https://trialbot-api.line.me/v1/events",send_data, header)
        try:
            response = urllib.request.urlopen(req)
        except urllib.error.HTTPError as err:
            print("Ooops! Got a error (send_text_msg)")
            print("----Error log----")
            print(err)
            print(err.headers)
            print("----Error log----")
            
    def get_user_info(self, target_mid):
        header = self.__generate_request_header()
        data = {"mids":target_mid}
        url = "https://trialbot-api.line.me/v1/profiles?" + urllib.parse.urlencode(data)
        req = urllib.request.Request(url, None, header)
        try:
            response = urllib.request.urlopen(req)
        except urllib.error.HTTPError as err:
            print("Ooops! Got a error (get_user_info)")
            print("----Error log----")
            print(err)
            print(err.headers)
            print("----Error log----")
    

        return (json.loads(response.read().decode('utf-8')))['contacts'][0]
        
