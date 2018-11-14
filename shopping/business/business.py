class Product:
    def __init__(self, id=0, name="", price=0.0, discountPercent=0):
            self.__id = id
            self.name = name
            self.price = price
            self.discountPercent = discountPercent

    def getDiscountAmount(self):
        discountAmount = self.price * self.discountPercent / 100
        return round(discountAmount, 2)

    def getDiscountPrice(self):
        discountPrice = self.price - self.getDiscountAmount()
        return round(discountPrice, 2)

class LineItem:
    def __init__(self, orderID=0, lineID=1, product=None, quantity=1):
            self.__orderID = oderID
            self.__lineID = lineID
            self.__product = product
            self.quantity = quantity

    @property
    def name(self):
        return self.__product.name

    def getTotal(self):
        total = self.__product.getDiscountPrice() * self.quantity
        return total

class Cart:
    def __init__(self, orderID=0, status=1, date_changed=None):
        self.__orderID=orderID
        self.__status=status
        self.__date_changed=date_changed
        self.__lineItems = []

    @property
    def orderID(self):
        return self.__orderID

    @orderID.setter
    def orderID(self, value):
        self.__orderID = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        n = 0
        try:
            n = int(value)
        except Exception as e:
            print >>sys.stderr, "Exception Occurred: %s" % e
            raise e
        if n < 0 and n > 3:
            raise ValueError("Order status must be between 1 and 2")
        self.__orderID = value

    @property
    def orderDate(self):
        return self.__date_changed

    def addItem(self, item):
        self.__lineItems.append(item)

    def removeItem(self, index):
        self.__lineItems.pop(index)

    def getTotal(self):
        total = 0.0
        for item in self.__lineItems:
            total += item.getTotal()
        return total

    def getItemCount(self):
        return len(self.__lineItems)

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lineItems)-1:
            raise StopIteration
        self.__index += 1
        lineItem = self.__lineItems[self.__index]
        return lineItem