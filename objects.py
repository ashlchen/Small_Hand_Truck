class Customer:
    def __init__(self, CustomerID = 123, fname = "", lname = "", ZipCode = "", Telephone = 1231234123, email = "", Category = ""):
        self.__customerID = CustomerID
        self.__fname = fname
        self.__lname = lname
        self.__ZipCode = ZipCode
        self.__Telephone = Telephone
        self.__email = email
        self.__Category = Category

    def getStr(self):
        # RETURNS "Customer string"
        return str(self.__customerID) + "|"  + self.__fname + "|" + self.__lname +  "|" + str(self.__ZipCode) + "|" + str(self.__Telephone) + "|" + self.__email + "|" + self.__Category

    def getDict(self):
        # RETURNS 'Name': 'Monty Python and the Holy Grail', 'Year': '1975'
        return "'CustomerID':'" + str(self.__customerID) + "', 'fname':'" + str(self.__fname) + "', 'lname':'" + str(self.__lname) + "', 'ZipCode':'" + str(self.__ZipCode) + "', 'Telephone':'" + str(self.__Telephone) + "', 'email':'" + str(self.__email) + "', 'Category':'" + str(self.__Category) + "'"


class Supplier:
    def __init__(self, SupplierID=123, SupplierName="", ZipCode="",Telephone=1231231234, email=""):
        self.__SupplierID = SupplierID
        self.__SupplierName = SupplierName
        self.__ZipCode = ZipCode
        self.__Telephone = Telephone
        self.__email = email

    def getStr(self):
        # RETURNS "Supplier info as string"
        return str(self.__SupplierID) + " "  + self.__SupplierName + " " + self.__ZipCode + " " + str(self.__Telephone) + " " + self.__email

    def getDict(self):
        # RETURNS 'Name': 'Monty Python and the Holy Grail', 'Year': '1975'
        return "'SupplierID':'" + str(self.__SupplierID) + "', 'SupplierName':'" + str(self.__SupplierName) + "', 'ZipCode':'" + str(self.__ZipCode) + "', 'Telephone':'" + str(self.__Telephone) + "', 'email':'" + str(self.__email) + "'"


class Product:
    def __init__(self, Product_ID=1, Product_Name="", Color="", Price=0):
        self.__Product_ID = Product_ID
        self.__Product_Name = Product_Name
        self.__Color = Color
        self.__Price = Price

    def getStr(self):
        # RETURNS "product info as string)"
        return str(self.__Product_ID) + " " + self.__Product_Name + " " + self.__Color + " " + str(self.__Price)

    def getDict(self):
        # RETURNS 'product info as dictionary'
        return "'Product_ID':'" + str(self.__Product_ID) + "', 'Product_Name':'" + str(self.__Product_Name) + "', 'Color':'" + str(self.__Color) + "', 'Price':'" + str(self.__Price) + "'"

class OrderDet:
    def __init__(self, OrdDet_ID= 1, Product_ID=1, OrderID=1, Quantity=1 ):
        self.__OrdDet_ID = OrdDet_ID
        self.__Product_ID= Product_ID
        self.__OrderID = OrderID
        self.__Quantity = Quantity

    #  def getStr(self):
    #     # RETURNS "product info as string)"
    #     return str(self.__OrdDet_ID) + " " + str(self.__Product_ID) + " " + str(self.__OrderID) +" " + str(self.__Quantity)

    def getDict(self):
        # RETURNS 'product info as dictionary'
        return "'OrdDet_ID':'" + str(self.__OrdDet_ID) + "', 'Product_ID':'" + str(self.__Product_ID) + "', 'OrderID':'" + str(self.__OrderID) + "', 'Quantity':'" + str(self.__Quantity) + "'"


class Order:
    def __init__(self, OrderID=1, OrderDate="", CustomerID=1, OrderType="", SalesPerson=1):
        self.__OrderID = OrderID
        self.__OrderDate = OrderDate
        self.__CustomerID = CustomerID
        self.__OrderType = OrderType
        self.__SalesPerson = SalesPerson

    def getStr(self):
        # RETURNS "product info as string)"
        return str(self.__OrderID) + " " + self.__OrderDate + " " + str(self.__CustomerID) +" " + self.__OrderType + " " + str(self.__SalesPerson)

    def getDict(self):
        # RETURNS 'product info as dictionary'
        return "'OrderID':'" + str(self.__OrderID) + "', 'OrderDate':'" + self.__OrderDate + "', 'CustomerID':'" + str(self.__CustomerID) + "', 'OrderType':'" + str(self.__OrderType) + "', 'SalesPerson':'" + str(self.__SalesPerson) + "'"


# class EditSupplier(table):
#     SupplierID = col('id', show=false)
#     SupplierName = col('artist')
#     ZipCode = col('title')
#     Telephone = col('release date')
#     email = col('publisher')
#     edit = linkcol('edit', 'edit', url_kwargs=dict(id='id'))