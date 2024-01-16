class Notifications:
    """
    << Notification IDs List >>
    
    81 = Custom Message
    82 = Club Message
    74 = Ticket Compensation Message
    77 = ???
    79 = Season End
    
    """



    messages = [

        {
            'NotificationID': 81,
            'NotificationIndex': 3,
            'NotificationRead': False,
            'NotificationTime': 43200,
            'NotificationText': f'Welcome to Classic Brawl v20 Remake!',
            'NotificationType': 0
        },

        {
            'NotificationID': 82,
            'NotificationIndex': 3,
            'NotificationRead': False,
            'NotificationTime': 43200,
            'SenderName': 'Player',
            'SenderThumbnail': 0,
            'SenderNameColor': 6,
            'NotificationText': f'Hi!'
        },

        {
            'NotificationID': 79,
            'NotificationIndex': 3,
            'NotificationRead': True,
            'NotificationTime': 43200,
            'NotificationText': None,
            'Brawlers': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            'TrophiesPlus': [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
            'TrophiesMinus': [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
            'Starpoints': [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
        }

    ]
    
    
    
    def EncodeNotificationsMessages(self):
        count = len(Notifications.messages)
        self.writeVint(count) # Count
        for i in range(count):
            item = Notifications.messages[i]
            
            self.writeVint(item['NotificationID'])
            self.writeInt(item['NotificationIndex'])
            self.writeBoolean(item['NotificationRead'])
            self.writeInt(item['NotificationTime'])
            self.writeString(item['NotificationText'])
            
            if item['NotificationID'] == 81:
                self.writeVint(item['NotificationType']) # 0 - Support Service, 1 - System

            elif item['NotificationID'] == 82:
                self.writeString(item['SenderName'])
                self.writeVint(100)
                self.writeVint(28000000 + item['SenderThumbnail'])
                self.writeVint(43000000 + item['SenderNameColor'])
                #self.writeVint(-1)
            
            elif item['NotificationID'] == 74:
                self.writeVint(item['Tickets'])
                self.writeVint(item['Gems'])
            
            elif item['NotificationID'] == 77:
                self.writeVint(1)
                for i in range(1):
                    self.writeVint(1)
                    self.writeVint(14)  # ItemType
                    self.writeVint(1)
                    self.writeVint(0)  # CsvID
                    self.writeVint(0)
                self.writeVint(7)
                self.writeVint(3)
                self.writeString('SUMMER SPORTS CHALLENGE!')

            elif item['NotificationID'] == 79:
                self.writeVint(len(item['Brawlers'])) # Brawlers Count
                for brawler in range(len(item['Brawlers'])):
                    self.writeVint(16000000 + brawler) # Brawler ID
                    self.writeVint(item['TrophiesPlus'][brawler]) # Brawler Trophies
                    self.writeVint(item['TrophiesMinus'][brawler]) # Brawler Trophy Loss
                    self.writeVint(item['Starpoints'][brawler]) # Star Points Gained
