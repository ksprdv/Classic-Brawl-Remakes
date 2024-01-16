from Database.DatabaseManager import DataBase
from Utils.Writer import Writer
from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand

class LogicBuyItem(Writer):

    def __init__(self, client, player, id11, id22, id33, mult11, mult22, mult33, brawler11, brawler22, brawler33, skin11, skin22, skin33):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.client = client
        self.id1 = id11
        self.id2 = id22
        self.id3 = id33
        self.mult1 = mult11
        self.mult2 = mult22
        self.mult3 = mult33
        self.brawler1 = brawler11
        self.brawler2 = brawler22
        self.brawler3 = brawler33
        self.skin1 = skin11
        self.skin2 = skin22
        self.skin3 = skin33

    def encode(self):
        #box header start
        self.writeVint(203)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(100)
        #box header end
        
        #reward info start

        if self.id1 != 0 and self.id2 != 0 and self.id3 != 0:
            self.writeVint(3) # Reward count
        elif self.id1 != 0 and self.id2 != 0:
            self.writeVint(2) # Reward count
        else:
            self.writeVint(1) # Reward count
        
        #reward 1

        if self.id1 == 1: # Gold
            self.writeVint(self.mult1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id1 == 2: # Gems
            self.writeVint(self.mult1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(8) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id1 == 3: # Tickets
            self.writeVint(self.mult1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(3) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id1 == 4: # Token Doubler
            self.writeVint(self.mult1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(2) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id1 == 5: # Power points
            self.writeVint(self.mult1) # Reward amount
            self.writeScId(16, self.brawler1) # BrawlerID
            self.writeVint(6) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id1 == 6: # Brawler
            self.writeVint(self.mult1) # Reward amount
            self.writeScId(16, self.brawler1) # BrawlerID
            self.writeVint(1) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id1 == 7: # Skin
            self.writeVint(self.mult1)
            self.writeVint(0)
            self.writeVint(9)
            self.writeScId(29, self.skin1)
            self.writeHexa('''00 00 00''')

        #reward 2
        if self.id2 == 1: # Gold
            self.writeVint(self.mult2) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id2 == 2: # Gems
            self.writeVint(self.mult2) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(8) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id2 == 3: # Tickets
            self.writeVint(self.mult2) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(3) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id2 == 4: # Token Doubler
            self.writeVint(self.mult2) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(2) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id2 == 5: # Power points
            self.writeVint(self.mult2) # Reward amount
            self.writeScId(16, self.brawler2) # BrawlerID
            self.writeVint(6) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id2 == 6: # Brawler
            self.writeVint(self.mult2) # Reward amount
            self.writeScId(16, self.brawler2) # BrawlerID
            self.writeVint(1) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id2 == 7: # Skin
            self.writeVint(self.mult2)
            self.writeVint(0)
            self.writeVint(9)
            self.writeScId(29, self.skin2)
            self.writeHexa('''00 00 00''')

        #reward 3
        if self.id3 == 1: # Gold
            self.writeVint(self.mult3) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id3 == 2: # Gems
            self.writeVint(self.mult3) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(8) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id3 == 3: # Tickets
            self.writeVint(self.mult3) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(3) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id3 == 4: # Token Doubler
            self.writeVint(self.mult3) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(2) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id3 == 5: # Power points
            self.writeVint(self.mult3) # Reward amount
            self.writeScId(16, self.brawler3) # BrawlerID
            self.writeVint(6) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id3 == 6: # Brawler
            self.writeVint(self.mult3) # Reward amount
            self.writeScId(16, self.brawler3) # BrawlerID
            self.writeVint(1) # Reward ID
            self.writeHexa('''00 00 00''')
        elif self.id3 == 7: # Skin
            self.writeVint(self.mult3)
            self.writeVint(0)
            self.writeVint(9)
            self.writeScId(29, self.skin3)
            self.writeHexa('''00 00 00''')


        #reward info end
        for i in range(13):
            self.writeVint(0)