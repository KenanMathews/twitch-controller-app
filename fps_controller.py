from TwitchPlays_KeyCodes import *
class FPSController:
    def __init__(self, mode='HoldKey'):
        self.actions = {}

    def set_action(self, action_name, key):
        self.actions[action_name] = key

    def handle_message(self, message):
        try:
            msg = message['message'].lower()
            username = message['username'].lower()

            print("Got this message from " + username + ": " + msg)

            if msg in self.actions:
                    HoldAndReleaseKey(self.actions[msg], 1)  

        except Exception as e:
            print("Encountered exception: " + str(e))
