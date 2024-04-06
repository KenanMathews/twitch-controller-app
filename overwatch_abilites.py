# overwatch_abilities.py

from fps_controller import FPSController
from TwitchPlays_KeyCodes import *

class OverwatchAbilities(FPSController):
    def __init__(self, mode='HoldKey'):
        super().__init__(mode)
        self.set_overwatch_abilities()

    def set_overwatch_abilities(self):
        # Tracer's abilities
        self.set_action("blink", F)
        self.set_action("recall", E)
        self.set_action("pulse bomb", Q)
        
        # Reaper's abilities
        self.set_action("wraith form", E)
        self.set_action("shadow step", F)
        self.set_action("death blossom", Q)
        
        # Genji's abilities
        self.set_action("swift strike", LEFT_SHIFT)
        self.set_action("deflect", E)
        self.set_action("dragonblade", Q)
        
        # Mercy's abilities
        self.set_action("guardian angel", LEFT_SHIFT)
        self.set_action("resurrect", E)
        self.set_action("valkyrie", Q)
        
        # Winston's abilities
        self.set_action("jump pack", LEFT_SHIFT)
        self.set_action("barrier projector", E)
        self.set_action("primal rage", Q)
        
        # Pharah's abilities
        self.set_action("jump jet", LEFT_SHIFT)
        self.set_action("concussive blast", E)
        self.set_action("barrage", Q)
        
        # McCree's abilities
        self.set_action("combat roll", LEFT_SHIFT)
        self.set_action("flashbang", E)
        self.set_action("deadeye", Q)
        
        # Bastion's abilities
        self.set_action("reconfigure", E)
        self.set_action("self-repair", LEFT_SHIFT)
        self.set_action("tank configuration", Q)
        
        # Hanzo's abilities
        self.set_action("sonic arrow", E)
        self.set_action("scatter arrow", F)
        self.set_action("dragonstrike", Q)
