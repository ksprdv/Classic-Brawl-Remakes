from Database.DatabaseManager import DataBase
from Logic.Shop import Shop
from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader

class LogicPurchaseTicketsCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.ticket = self.read_Vint()


    def process(self):
        cost = Shop.tickets[self.ticket]['Cost']
        value = Shop.tickets[self.ticket]['Amount']

        newGems = self.player.gems - cost
        self.player.gems = newGems
        DataBase.replaceValue(self, 'gems', newGems)

        newTokens = self.player.tokens + value
        self.player.tokens = newTokens
        DataBase.replaceValue(self, 'tickets', newTokens)

