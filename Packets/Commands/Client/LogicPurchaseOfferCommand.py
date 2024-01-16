from Packets.Commands.Server.LogicBoxDataCommand import LogicBoxDataCommand
from Packets.Commands.Server.LogicBuyItem import LogicBuyItem
from Packets.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage
from Database.DatabaseManager import DataBase
from Logic.Shop import Shop

import random
import time
from Utils.Reader import BSMessageReader

class LogicPurchaseOfferCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.offer_index = self.read_Vint()
        self.BrawlerID = self.read_Vint()


    def process(self):
        id1 = Shop.offers[self.offer_index]['ID'][0]
        id2 = Shop.offers[self.offer_index]['ID'][1]
        id3 = Shop.offers[self.offer_index]['ID'][2]
        multi1 = Shop.offers[self.offer_index]['Multiplier'][0]
        multi2 = Shop.offers[self.offer_index]['Multiplier'][1]
        multi3 = Shop.offers[self.offer_index]['Multiplier'][2]
        brawler1 = Shop.offers[self.offer_index]['BrawlerID'][0]
        brawler2 = Shop.offers[self.offer_index]['BrawlerID'][1]
        brawler3 = Shop.offers[self.offer_index]['BrawlerID'][2]
        skin1 = Shop.offers[self.offer_index]['SkinID'][0]
        skin2 = Shop.offers[self.offer_index]['SkinID'][1]
        skin3 = Shop.offers[self.offer_index]['SkinID'][2]

        ID1 = 0
        ID2 = 0
        ID3 = 0

        if Shop.offers[self.offer_index]['ShopType'] == 0:
            self.player.gems = self.player.gems - Shop.offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'gems', self.player.gems)
        elif Shop.offers[self.offer_index]['ShopType'] == 1:
            self.player.gold = self.player.gold - Shop.offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'gold', self.player.gold)   
        elif Shop.offers[self.offer_index]['ShopType'] == 3:
            self.player.star_points = self.player.star_points - Shop.offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'starpoints', self.player.star_points) 

        if id1 == 1:
            self.player.gold = self.player.gold + multi1
            DataBase.replaceValue(self, 'gold', self.player.gold)
            ID1 = 1
        if id2 == 1:
            self.player.gold = self.player.gold + multi2
            DataBase.replaceValue(self, 'gold', self.player.gold)
            ID2 = 1
        if id3 == 1:
            self.player.gold = self.player.gold + multi3
            DataBase.replaceValue(self, 'gold', self.player.gold)
            ID3 = 1

        if id1 == 16:
            self.player.gems = self.player.gems + multi1
            DataBase.replaceValue(self, 'gems', self.player.gems)
            ID1 = 2
        if id2 == 16:
            self.player.gems = self.player.gems + multi2
            DataBase.replaceValue(self, 'gems', self.player.gems)
            ID2 = 2
        if id3 == 16:
            self.player.gems = self.player.gems + multi3
            DataBase.replaceValue(self, 'gems', self.player.gems)
            ID3 = 2

        if id1 == 7:
            self.player.tickets = self.player.tickets + multi1
            DataBase.replaceValue(self, 'tickets', self.player.tickets)
            ID1 = 3
        if id2 == 7:
            self.player.tickets = self.player.tickets + multi2
            DataBase.replaceValue(self, 'tickets', self.player.tickets)
            ID2 = 3
        if id3 == 7:
            self.player.tickets = self.player.tickets + multi3
            DataBase.replaceValue(self, 'tickets', self.player.tickets)
            ID3 = 3

        if id1 == 9:
            self.player.tokensdoubler = self.player.tokensdoubler + multi1
            DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
            ID1 = 4
        if id2 == 9:
            self.player.tokensdoubler = self.player.tokensdoubler + multi2
            DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
            ID2 = 4
        if id3 == 9:
            self.player.tokensdoubler = self.player.tokensdoubler + multi3
            DataBase.replaceValue(self, 'tokensdoubler', self.player.tokensdoubler)
            ID3 = 4

        if id1 == 8:
            self.player.brawlers_upgradium[str(brawler1)] += multi1
            DataBase.replaceValue(self, 'brawlersUpgradePoints', self.player.brawlers_upgradium)
            ID1 = 5
        if id2 == 8:
            self.player.brawlers_upgradium[str(brawler2)] += multi2
            DataBase.replaceValue(self, 'brawlersUpgradePoints', self.player.brawlers_upgradium)
            ID2 = 5
        if id3 == 8:
            self.player.brawlers_upgradium[str(brawler3)] += multi3
            DataBase.replaceValue(self, 'brawlersUpgradePoints', self.player.brawlers_upgradium)
            ID3 = 5

        if id1 == 3:
            self.player.BrawlersUnlockedState[str(brawler1)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID1 = 6
        if id2 == 3:
            self.player.BrawlersUnlockedState[str(brawler2)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID2 = 6
        if id3 == 3:
            self.player.BrawlersUnlockedState[str(brawler3)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID3 = 6

        if id1 == 4:
            self.player.UnlockedSkins.append(skin1)
            DataBase.replaceValue(self, 'UnlockedSkins', self.player.UnlockedSkins)
            ID1 = 7
        if id2 == 4:
            self.player.UnlockedSkins.append(skin2)
            DataBase.replaceValue(self, 'UnlockedSkins', self.player.UnlockedSkins)
            ID2 = 7
        if id3 == 4:
            self.player.UnlockedSkins.append(skin3)
            DataBase.replaceValue(self, 'UnlockedSkins', self.player.UnlockedSkins)
            ID3 = 7

        if id1 == 2:
            brawlers = []
            if skin1 == 0: # Trophy Road
                brawlers = [1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
            if skin1 == 1: # Rare
                brawlers = [6, 10, 13, 24, 29, 36]
            if skin1 == 2: # Super Rare
                brawlers = [4, 18, 19, 25]
            if skin1 == 3: # Epic
                brawlers = [15, 16, 20, 26, 31]
            if skin1 == 4: # Mythic
                brawlers = [11, 17, 21, 31, 32, 34]
            if skin1 == 5: # Legendary
                brawlers = [5, 12, 23, 28]
            if skin1 == 6: # Chromatic
                brawlers = [35, 38, 39]
            brawler1 = brawlers[random.randint(0, len(brawlers) - 1)]
            print('Brawler: ', brawler1)
            while brawler1 not in self.player.brawlers_id or self.player.BrawlersUnlockedState[str(brawler1)] == 1:
                brawler1 = brawlers[random.randint(0, len(brawlers) - 1)]
                print('Brawler: ', brawler1)
            self.player.BrawlersUnlockedState[str(brawler1)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID1 = 6

        if id2 == 2:
            brawlers = []
            if skin2 == 0: # Trophy Road
                brawlers = [1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
            if skin2 == 1: # Rare
                brawlers = [6, 10, 13, 24, 29, 36]
            if skin2 == 2: # Super Rare
                brawlers = [4, 18, 19, 25]
            if skin2 == 3: # Epic
                brawlers = [15, 16, 20, 26, 31]
            if skin2 == 4: # Mythic
                brawlers = [11, 17, 21, 31, 32, 34]
            if skin2 == 5: # Legendary
                brawlers = [5, 12, 23, 28]
            if skin2 == 6: # Chromatic
                brawlers = [35, 38, 39]
            brawler2 = brawlers[random.randint(0, len(brawlers) - 1)]
            print('Brawler: ', brawler2)
            while brawler2 not in self.player.brawlers_id or self.player.BrawlersUnlockedState[str(brawler2)] == 1:
                brawler2 = brawlers[random.randint(0, len(brawlers) - 1)]
                print('Brawler: ', brawler2)
            self.player.BrawlersUnlockedState[str(brawler2)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID2 = 6

        if id3 == 2:
            brawlers = []
            if skin3 == 0: # Trophy Road
                brawlers = [1, 2, 3, 7, 8, 9, 14, 22, 27, 30]
            if skin3 == 1: # Rare
                brawlers = [6, 10, 13, 24, 29, 36]
            if skin3 == 2: # Super Rare
                brawlers = [4, 18, 19, 25]
            if skin3 == 3: # Epic
                brawlers = [15, 16, 20, 26, 31]
            if skin3 == 4: # Mythic
                brawlers = [11, 17, 21, 31, 32, 34]
            if skin3 == 5: # Legendary
                brawlers = [5, 12, 23, 28]
            if skin3 == 6: # Chromatic
                brawlers = [35, 38, 39]
            brawler3 = brawlers[random.randint(0, len(brawlers) - 1)]
            print('Brawler: ', brawler3)
            while brawler3 not in self.player.brawlers_id or self.player.BrawlersUnlockedState[str(brawler3)] == 1:
                brawler3 = brawlers[random.randint(0, len(brawlers) - 1)]
                print('Brawler: ', brawler3)
            self.player.BrawlersUnlockedState[str(brawler3)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.BrawlersUnlockedState)
            ID3 = 6





        if id1 in [6, 10, 14]:
            if id1 == 6:
                self.player.box_id = 5
                LogicBoxDataCommand(self.client, self.player).send()
            if id1 == 10:
                self.player.box_id = 3
                LogicBoxDataCommand(self.client, self.player).send()
            if id1 == 14:
                self.player.box_id = 4
                LogicBoxDataCommand(self.client, self.player).send()
        elif id2 in [6, 10, 14]:
            if id2 == 6:
                self.player.box_id = 5
                LogicBoxDataCommand(self.client, self.player).send()
            if id2 == 10:
                self.player.box_id = 3
                LogicBoxDataCommand(self.client, self.player).send()
            if id2 == 14:
                self.player.box_id = 4
                LogicBoxDataCommand(self.client, self.player).send()
        elif id3 in [6, 10, 14]:
            if id3 == 6:
                self.player.box_id = 5
                LogicBoxDataCommand(self.client, self.player).send()
            if id3 == 10:
                self.player.box_id = 3
                LogicBoxDataCommand(self.client, self.player).send()
            if id3 == 14:
                self.player.box_id = 4
                LogicBoxDataCommand(self.client, self.player).send()
        else:
            if id1 != 0 and id2 != 0 and id3 != 0:
                LogicBuyItem(self.client, self.player, ID1, ID2, ID3, multi1, multi2, multi3, brawler1, brawler2, brawler3, skin1, skin2, skin3).send()
            elif id1 != 0 and id2 != 0:
                LogicBuyItem(self.client, self.player, ID1, ID2, 0, multi1, multi2, 0, brawler1, brawler2, 0, skin1, skin2, 0).send()
            else:
                LogicBuyItem(self.client, self.player, ID1, 0, 0, multi1, 0, 0, brawler1, 0, 0, skin1, 0, 0).send()





        #if id == 0:
        #    self.player.box_id = 5
        #    for i in range(multi):
        #        self.player.box_id = 5
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()
        #if id == 6:
        #    self.player.box_id = 5
        #    for i in range(multi):
        #        self.player.box_id = 5
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()
        #if id == 14:
        #    self.player.box_id = 4
        #    for i in range(multi):
        #        self.player.box_id = 4
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()
        #if id == 10:
        #    self.player.box_id = 3
        #    for i in range(multi):
        #        self.player.box_id = 3
        #        time.sleep(1)
        #        LogicBoxDataCommand(self.client, self.player).send()


