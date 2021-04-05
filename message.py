"""
Copyright (c) 2018 Keitaro AB

Use of this source code is governed by an MIT license
that can be found in the LICENSE file or at
https://opensource.org/licenses/MIT.
"""

# encoding: utf-8

import yaml


class Message(object):
    
    def __init__(self):
        super(Message, self).__init__()
        self.channel = ''
        self.timestamp = ''
        self.text = ("Welcome to Toto-Boto", "\n Collect pinned messages")
        self.pin_attachment = {}
        self.share_attachments = {}
        self.attachments = [self.pin_attachment, self.share_attachments]

    def create_attachments(self):
    
        with open('welcome.json') as json_file:
            json_dict = yaml.safe_load(json_file)
            json_attachments = json_dict["attachments"]
            [self.attachments[i].update(json_attachments[i]) for i
             in range(len(json_attachments))]

