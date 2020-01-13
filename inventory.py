import shelve, random

class Inventory():

    def __init__(self, brand, productName, quantity, cost_price, selling_price):
        invDict = {}
        db = shelve.open("inventory.db", "r")
        invDict = db["inventory"]
        db.close()

        IDlist = []
        for keys in invDict:
            good = invDict.get(keys)
            id = good.get_stockID()
            IDlist.append(id)
        id = 0
        while id == 0 or id in IDlist:
            if brand.lower() == "pilot":
                id = random.randint(1000,1999)
            elif brand.lower() == "uni-ball":
                id = random.randint(2000,2999)

        self.__stockID = id
        self.set_name(brand, productName)
        self.__currentStock = quantity
        self.__soldStock = 0
        self.__costPrice = cost_price
        self.__sellingPrice = selling_price
        self.__profit = 0
        self.__image = ""

    def get_stockID(self):
        return self.__stockID

    def get_name(self):
        return self.__name

    def get_currentStock(self):
        return self.__currentStock

    def get_soldStock(self):
        return self.__soldStock

    def get_costPrice(self):
        return self.__costPrice

    def get_sellingPrice(self):
        return self.__sellingPrice

    def get_profit(self):
        return self.__profit

    def get_image(self):
        return self.__image

    def set_name(self, brand, productName):
        name = (brand + " " + productName).split()
        self.__name = " ".join(name).title()

    def set_currentStock(self, currentStock):
        self.__currentStock = currentStock

    def set_soldStock(self, soldStock):
        self.__soldStock = soldStock

    def set_costPrice(self, cost_price):
        self.__costPrice = cost_price

    def set_sellingPrice(self, selling_price):
        self.__sellingPrice = selling_price

    def transaction_to_update_inventory(self, stock):
        self.__currentStock -= stock
        self.__soldStock += stock
        self.__profit += (self.__sellingPrice * stock)

    def set_profit(self):
        self.__profit = (self.__soldStock * self.__sellingPrice) - (self.__currentStock + self.__soldStock) * self.__costPrice

    def set_image(self, image):
        self.__image = image
