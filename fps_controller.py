from TwitchPlays_KeyCodes import *
class FPSController:
    def __init__(self, mode='HoldKey'):
        self.actions = {}
        self.mode = mode

    def set_action(self, action_name, key):
        self.actions[action_name] = key

    def handle_message(self, message):
        try:
            msg = message['message'].lower()
            username = message['username'].lower()

            print("Got this message from " + username + ": " + msg)

            if msg in self.actions:
                if msg == "stop" and self.mode == 'HoldAndReleaseKey':
                    # Release all movement keys
                    for action in ['forward', 'backward', 'left', 'right']:
                        if action in self.actions:
                            ReleaseKey(self.actions[action])
                else:
                    if self.mode == 'HoldKey':
                        HoldKey(self.actions[msg])
                    elif self.mode == 'HoldAndReleaseKey':
                        HoldAndReleaseKey(self.actions[msg], 0.5)  # Adjust the duration as needed

        except Exception as e:
            print("Encountered exception: " + str(e))
