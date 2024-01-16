class Shop:
    offers = [
        {
            'ID': [3, 0, 0],
            'OfferTitle': 'SPECIAL OFFER',
            'Cost': 15,
            'OldCost': 30,
            'OfferView': 0,
            'Multiplier': [1, 1, 0],
            'SkinID': [2, 0, 0],
            'BrawlerID': [0, 0, 0],
            'ShopType': 0,
            'ShopDisplay': 0,
            'Timer': 99999,
            'Purchased': False
        }
    ]

    gold = [
        {
            'Cost': 20,
            'Amount': 150
        },

        {
            'Cost': 50,
            'Amount': 400
        },

        {
            'Cost': 140,
            'Amount': 1200
        },

        {
            'Cost': 280,
            'Amount': 2600
        }

    ]
    
    tickets = [
        {
            'Cost': 10,
            'Amount': 6
        },

        {
            'Cost': 30,
            'Amount': 20
        },

        {
            'Cost': 80,
            'Amount': 60
        }

    ]

    boxes = [
        {
            'Name': 'Big Box',
            'Cost': 30,
            'Multiplier': 1
        },

        {
            'Name': 'Mega Box',
            'Cost': 80,
            'Multiplier': 1
        }

    ]


    token_doubler = {

        'Cost': 50,
        'Amount': 1000
    }

    def EncodeShopOffers(self):
        count = len(Shop.offers)
        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]
            if item['ID'][0] != 0 and item['ID'][1] != 0 and item['ID'][2] != 0:
                self.writeVint(3)
                self.writeVint(item['ID'][0]) # ItemID
                self.writeVint(item['Multiplier'][0]) # Ammount
                self.writeScId(16, item['BrawlerID'][0])
                self.writeVint(item['SkinID'][0]) # ItemID
                
                self.writeVint(item['ID'][1]) # ItemID
                self.writeVint(item['Multiplier'][1]) # Ammount
                self.writeScId(16, item['BrawlerID'][1])
                self.writeVint(item['SkinID'][1]) # ItemID
                
                self.writeVint(item['ID'][2]) # ItemID
                self.writeVint(item['Multiplier'][2]) # Ammount
                self.writeScId(16, item['BrawlerID'][2])
                self.writeVint(item['SkinID'][2]) # ItemID
            elif item['ID'][0] != 0 and item['ID'][1] != 0:
                self.writeVint(2)
                self.writeVint(item['ID'][0]) # ItemID
                self.writeVint(item['Multiplier'][0]) # Ammount
                self.writeScId(16, item['BrawlerID'][0])
                self.writeVint(item['SkinID'][0]) # ItemID
                
                self.writeVint(item['ID'][1]) # ItemID
                self.writeVint(item['Multiplier'][1]) # Ammount
                self.writeScId(16, item['BrawlerID'][1])
                self.writeVint(item['SkinID'][1]) # ItemID
            else:
                self.writeVint(1)
                self.writeVint(item['ID'][0]) # ItemID
                self.writeVint(item['Multiplier'][0]) # Ammount
                self.writeScId(16, item['BrawlerID'][0])
                self.writeVint(item['SkinID'][0]) # ItemID

            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer']) # Timer

            self.writeVint(item['OfferView']) # Offer View | 0 = Absolutely "NEW", 1 = "NEW", 2 = Viewed
            self.writeVint(100)
            self.writeBoolean(item['Purchased'])  # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            #self.writeBoolean(False)
            self.writeVint(item['OldCost'])  # Cost
            self.writeVint(0)

            self.writeInt(0)
            self.write_string_reference(item['OfferTitle']) # Offers name

            self.writeBoolean(False)
