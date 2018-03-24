# encoding: utf-8

import os
import message

from slackclient import SlackClient 

authed_items = {}

class Bot(object):

    def __init__(self):
        super(Bot, self).__init__()
        self.name = "toto-boto"
        self.emoji = ":fobot-face:"

        self()
