import pickle
from fps_controller import FPSController
from TwitchPlays_KeyCodes import *

class OverwatchAbilities(FPSController):
    def __init__(self, mode='HoldKey'):
        super().__init__(mode)
        self.hero_abilities = {}

    def load_all_hero_abilities(self):
        self.load_tracer_abilities()
        self.load_reaper_abilities()
        self.load_genji_abilities()
        self.load_d_va_abilities()
        self.load_lucio_abilities()
        self.load_lucio_abilities()
        self.load_reinhardt_abilities()
        self.load_widowmaker_abilities()
        self.load_winston_abilities()
        # Add more hero abilities loading methods here as needed

    def load_tracer_abilities(self):
        self.hero_abilities["Tracer"] = {
            "blink": LEFT_SHIFT,
            "recall": E,
            "pulse bomb": Q
        }

    def load_reaper_abilities(self):
        self.hero_abilities["Reaper"] = {
            "wraith form": E,
            "shadow step": F,
            "death blossom": Q
        }

    def load_genji_abilities(self):
        self.hero_abilities["Genji"] = {
            "swift strike": LEFT_SHIFT,
            "deflect": E,
            "dragonblade": Q
        }
    def load_reinhardt_abilities(self):
        self.hero_abilities["Reinhardt"] = {
            "fire strike": LEFT_SHIFT,
            "charge": E,
            "earthshatter": Q
        }

    def load_mercy_abilities(self):
        self.hero_abilities["Mercy"] = {
            "guardian angel": LEFT_SHIFT,
            "resurrect": E,
            "valkyrie": Q
        }

    def load_widowmaker_abilities(self):
        self.hero_abilities["Widowmaker"] = {
            "grappling hook": LEFT_SHIFT,
            "venom mine": E,
            "infra-sight": Q
        }

    def load_d_va_abilities(self):
        self.hero_abilities["D.Va"] = {
            "boosters": LEFT_SHIFT,
            "defense matrix": RIGHT_MOUSE,
            "self-destruct": Q
        }

    def load_winston_abilities(self):
        self.hero_abilities["Winston"] = {
            "jump pack": LEFT_SHIFT,
            "barrier projector": E,
            "primal rage": Q
        }

    def load_lucio_abilities(self):
        self.hero_abilities["Lúcio"] = {
            "crossfade": LEFT_SHIFT,
            "amp it up": E,
            "sound barrier": Q
        }

    def load_zarya_abilities(self):
        self.hero_abilities["Zarya"] = {
            "particle barrier": LEFT_SHIFT,
            "projected barrier": E,
            "graviton surge": Q
        }

    # Add more hero abilities loading methods here as needed

    def set_all_hero_abilities(self):
        for hero, abilities in self.hero_abilities.items():
            for ability, key in abilities.items():
                self.set_action(f"{ability}", key)

    def save_config(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.hero_abilities, file)

    def load_config(self, filename="overwatch_config.pickle"):
        with open(filename, "rb") as file:
            self.hero_abilities = pickle.load(file)

overwatch_controller = OverwatchAbilities(mode='HoldAndReleaseKey')
overwatch_controller.load_all_hero_abilities()
overwatch_controller.set_all_hero_abilities()
overwatch_controller.save_config("overwatch_config.pickle")
