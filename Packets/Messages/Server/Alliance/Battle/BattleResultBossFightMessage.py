from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class BattleResultBossFightMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        # Stuff
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        brawler_trophies_for_rank = self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)]
        #if self.player.Brawler_starPower[str(self.player.brawler_id)] >= 1:
        #    brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 2
        #else:
        #    brawler_level = self.player.Brawler_level[str(self.player.brawler_id)] + 1
        # Rewards
        exp_reward = [0]
        token_list = [0]
        mvp_exp_reward = [10]    
        # Result Rewards
        if self.player.battle_tokens <= 0 and self.player.experience >= self.player.max_experience:
            result = 7
        elif self.player.battle_tokens <= 0:
            result = 5
        elif self.player.experience >= self.player.max_experience:
            result = 3
        else:
            result = 1
        if self.player.battle_result == 0:
            gainedtokens = token_list[0]
            gainedexperience = exp_reward[0]
                
        if self.player.battle_result == 1:
            gainedtokens = token_list[0]
            gainedexperience = exp_reward[0]
        if self.player.battle_result == 2:
            gainedtokens = token_list[0]
            gainedexperience = exp_reward[0]
                
        if 0 <= result <= 15:
            starplayer = 1
        else:
            starplayer = 5
        # Star Player Info
        if starplayer == 5:
            starplayerexperience = mvp_exp_reward[0]
        else:
            starplayerexperience = 0
        # Results Balance
        if result in [0, 1, 2, 3, 8, 9, 10, 11, 16, 17, 18, 19, 24, 25, 26, 27]:
            tokens = gainedtokens
        if result in [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]:
            tokens = 0
        if result in [0, 1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29]:
            mvpexperience = starplayerexperience
            experience = gainedexperience
        if result in [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]:
            mvpexperience = 0
            experience = 0
        if result in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]:
            startoken = 1
        if result in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]:
            startoken = 0
        if 0 <= result <= 31:
            trophies = 0
        # DataBase Stuff            
        self.player.experience += experience + mvpexperience
        if self.player.battle_tokens <= 0:
            token = 0
        if self.player.battle_tokens > tokens:
            token = tokens
        if tokens >= self.player.battle_tokens: 
            token = self.player.battle_tokens
        if self.player.tokenevent:
            tokenevent = token
        else:
            tokenevent = 0
        if self.player.tokensdoubler <= 0:
            doubledtokens = 0
        if self.player.tokensdoubler > token + tokenevent:
            doubledtokens = token + tokenevent
        if token + tokenevent >= self.player.tokensdoubler: 
            doubledtokens = self.player.tokensdoubler
        battle_tokens = self.player.battle_tokens - token
        remainingtokens = (self.player.tokensdoubler) - doubledtokens
        totaltokens = token + tokenevent + doubledtokens
        if self.player.coinevent:
            coinevent = totaltokens
        else:
            coinevent = 0
        new_gold = self.player.gold + coinevent
        new_trophies = self.player.trophies + trophies
        new_tokens = self.player.brawl_boxes + totaltokens
        new_startokens = self.player.big_boxes + startoken
        self.player.brawlers_trophies[str(self.player.brawler_id)] = brawler_trophies + trophies
        if self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] < self.player.brawlers_trophies[str(self.player.brawler_id)]:
            self.player.brawlers_trophies_in_rank[str(self.player.brawler_id)] = brawler_trophies_for_rank - brawler_trophies_for_rank + brawler_trophies + trophies
        DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
        DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
        DataBase.replaceValue(self, 'brawlersTrophiesForRank', self.player.brawlers_trophies_in_rank)
        DataBase.replaceValue(self, 'trophies', new_trophies)
        DataBase.replaceValue(self, 'brawlBoxes', new_tokens)
        DataBase.replaceValue(self, 'bigBoxes', new_startokens)
        DataBase.replaceValue(self, 'availableTokens', battle_tokens)
        DataBase.replaceValue(self, 'tokensdoubler', remainingtokens)
        DataBase.replaceValue(self, 'playerExp', self.player.experience)
        DataBase.replaceValue(self, 'cappedExp', self.player.experience)
        DataBase.replaceValue(self, 'gold', new_gold)
        self.player.tokensAnim = totaltokens
        self.player.trophiesAnim = trophies
        self.player.bigTokensAnim = 1
        
        self.writeVint(6) # Battle End Game Mode (2 = Showdown, 3 = Robo Rumble, 4 = Big Game, 5 = Duo Showdown, 6 = Boss Fight. Else is 3vs3)
        self.writeVint(self.player.battle_result) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVint(token) # Tokens Gained
        self.writeVint(0) # Trophies Result 
        self.writeVint(doubledtokens) # Doubled Tokens
        self.writeVint(tokenevent) # Double Token Weekend
        self.writeVint(remainingtokens) # Token Doubler Remaining
        self.writeVint(0) # Big Game/Robo Rumble Time and Boss Fight Level Cleared
        self.writeVint(result) # Battle Result Type (0-15 = Practice Battle End, 16-31 = Matchmaking Battle End, 32-47 = Friendly Game Battle End, 48-63  = Spectate and Replay Battle End)
            
        # Players Array
        self.writeVint(self.player.players) # Battle End Screen Players
        
        self.writeVint(starplayer) # Player Team and Star Player Type
        self.writeScId(16, self.player.brawler_id) # Player Brawler
        self.writeScId(29, self.player.skin_id) # Player Skin
        self.writeVint(brawler_trophies) # Brawler Trophies
        self.writeVint(10) # Brawler Power Level
        self.writeBoolean(True) # Player HighID and LowID Array
        self.writeInt(self.player.high_id) # HighID
        self.writeInt(self.player.low_id) # LowID
        self.writeString(self.player.name) # Player Name
        self.writeVint(self.player.experience -experience -mvpexperience) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color

        if self.player.team == 0:
            if self.player.bot1_team == 0:
                self.writeVint(0) # Team and Star Player Type
            else:
                self.writeVint(2) # Team and Star Player Type
        else:
            if self.player.bot1_team == 0:
                self.writeVint(2) # Team and Star Player Type
            else:
                self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.player.bot1) # Bot 1 Brawler
        self.writeVint(0) # Bot 1 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(10) # Brawler Power Level
        self.writeBoolean(False) # Player HighID and LowID Array
        #self.writeInt(self.player.high_id) # HighID
        #self.writeInt(self.player.low_id) # LowID
        self.writeString(self.player.bot1_n) # Bot 1 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color

        if self.player.team == 0:
            if self.player.bot2_team == 0:
                self.writeVint(0) # Team and Star Player Type
            else:
                self.writeVint(2) # Team and Star Player Type
        else:
            if self.player.bot2_team == 0:
                self.writeVint(2) # Team and Star Player Type
            else:
                self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.player.bot2) # Bot 1 Brawler
        self.writeVint(0) # Bot 1 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(10) # Brawler Power Level
        self.writeBoolean(False) # Player HighID and LowID Array
        #self.writeInt(self.player.high_id) # HighID
        #self.writeInt(self.player.low_id) # LowID
        self.writeString(self.player.bot2_n) # Bot 1 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        
        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(experience) # Normal Experience Gained
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(mvpexperience) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Trophies Bar Milestone ID
        self.writeVint(brawler_trophies) # Brawler Trophies
        self.writeVint(brawler_trophies_for_rank) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Bar Milestone ID
        self.writeVint(self.player.experience -experience -mvpexperience) # Player Experience
        self.writeVint(self.player.experience -experience -mvpexperience) # Player Experience for Level
        
        self.writeScId(28, self.player.profile_icon)  # Player Profile Icon
        self.writeBoolean(True)  # Play Again