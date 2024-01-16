import time
from Utils.Helpers import Helpers

class EventSlots:

    '''
    << Modifiers List >>
    1 = Energy Drink
    2 = Angry Robo
    3 = Meteor Shower
    4 = Graveyard Shift
    5 = Healing Mushrooms
    8 = Boss Lasers
    9 = Boss Chain Lighting
    10 = Boss Rockets
    11 = Ship Tilting
    
    Status | 3 = Nothing, 2 = Star Token, 1 = New Event
    '''

    Timer = 86400

    maps = [
        {
            'ID': 58, # Gemgrab
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },
        {
            'ID': 33, # Showdown
            'Status': 3,
            'Ended': False,
            'Modifier': 2,
            'CollectReward': 10
        },
        {
            'ID': 164, # Brawlball
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },
        {
            'ID': 142, # Siege
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },
        {
            'ID': 44, # Duo Showdown
            'Status': 3,
            'Ended': False,
            'Modifier': 2,
            'CollectReward': 10
        },
        {
            'ID': 53, # Heist
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },
        {
            'ID': 84, # Bounty
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        },
        {
            'ID': 21, # Big Game
            'Status': 3,
            'Ended': False,
            'Modifier': 0,
            'CollectReward': 10
        }
    ]