import pickle
from fps_controller import FPSController

class OverwatchAbilities(FPSController):
    def __init__(self, mode='HoldKey'):
        super().__init__(mode)
        self.hero_abilities = {}

    def load_all_hero_abilities(self):
        self.load_tracer_abilities()
        self.load_reaper_abilities()
        self.load_genji_abilities()
        # Add more hero abilities loading methods here as needed

    def load_tracer_abilities(self):
        self.hero_abilities["Tracer"] = {
            "blink": "F",
            "recall": "E",
            "pulse bomb": "Q"
        }

    def load_reaper_abilities(self):
        self.hero_abilities["Reaper"] = {
            "wraith form": "E",
            "shadow step": "F",
            "death blossom": "Q"
        }

    def load_genji_abilities(self):
        self.hero_abilities["Genji"] = {
            "swift strike": "LSHIFT",
            "deflect": "E",
            "dragonblade": "Q"
        }

    # Add more hero abilities loading methods here as needed

    def set_all_hero_abilities(self):
        for hero, abilities in self.hero_abilities.items():
            for ability, key in abilities.items():
                self.set_action(f"{hero} {ability}", key)

    def save_config(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.hero_abilities, file)

    def load_config(self, filename):
        with open(filename, "rb") as file:
            self.hero_abilities = pickle.load(file)

overwatch_controller = OverwatchAbilities(mode='HoldKey')
overwatch_controller.load_all_hero_abilities()
overwatch_controller.set_all_hero_abilities()
overwatch_controller.save_config("overwatch_config.pickle")
