# encoding: utf-8

import os
import message

from slackclient import SlackClient

authed_teams = {}


class TotoBoto(object):
    def __init__(self):
        super(TotoBoto, self).__init__()
        self.name = "pythonboardingbot"
        self.emoji = ":robot_face:"

        self.oauth = {"client_id": os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")

        self.client = SlackClient("")

        self.messages = {}

    def auth(self, code):
        auth_response = self.client.api_call(
                                "oauth.access",
                                client_id=self.oauth["client_id"],
                                client_secret=self.oauth["client_secret"],
                                code=code
                                )

        team_id = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token":
                                 auth_response["bot"]["bot_access_token"]}

        self.client = SlackClient(authed_teams[team_id]["bot_token"])

    def update_pin(self, slack_event):
        print slack_event
