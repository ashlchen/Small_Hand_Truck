###############################################################################
#                         IMPORT REQUIRED LIBRARIES/MODULES
###############################################################################
from flask import Flask #The FLASK framework (the webserver)
from flask import render_template  # For opening and read the HTML file and showing them as the webpage
from flask import redirect
from cs50 import SQL
from objects import *
# from flask_table import table, col, linkcol

db = SQL("sqlite:///HandTrucks.db")


import sqlite3

#Needed for OPTION 4 (See below)
from flask import request  #Allows me to get stuff from the URL (the ?)

app=Flask(__name__) # Create a Flask instance



###############################################################################
#   SET FILE (CSV backend) or Databaser (SQLITE backend)
###############################################################################

type="Database"

# PAGE: INDEX
#------------------------------------------------------------------------------------
@app.route("/")         # Decorator - Place above any other app.route to set "homepage"
@app.route("/index")    # Decorator - Now
def index():
    return render_template('index.html')


# PAGE: DISPLAY CUSTOMERS
#------------------------------------------------------------------------------------
@app.route("/customers", methods=["GET", "POST"])
def customers():
    c_list = getDictList_DB()
    return render_template("customers.html", customer = c_list)

# PAGE: DISPLAY SUPPLIERS
#------------------------------------------------------------------------------------
@app.route("/suppliers", methods=["GET", "POST"])
def suppliers():
    s_list = getSuppDictList_DB()
    return render_template("suppliers.html", supplier = s_list)



# PAGE: DISPLAY PRODUCTS
#------------------------------------------------------------------------------------
@app.route("/products", methods=["GET", "POST"])
def products():
    p_list = getPDictList_DB()
    return render_template("products.html", product = p_list)


# PAGE: EDIT CUSTOMERS
#------------------------------------------------------------------------------------
@app.route("/edit", methods=["POST","GET"])
def edit():

    customerid = request.args.get('CustomerID')
    if request.method == "GET":
        e_customer=getCustomer_DB(customerid)
        print(customerid)
        return render_template("edit.html",customer = e_customer)

    else:
        CustomerID = getIntegerFormVariable("CustomerID")
        Fname = getFormVariable("fname")
        Lname =  getFormVariable("lname")
        ZipCode =  getFormVariable("ZipCode")
        Telephone =  getIntegerFormVariable("Telephone")
        email =  getFormVariable("email")
        Category =  getFormVariable("Category")

        updateCustomerDB(CustomerID,Fname, Lname, ZipCode, Telephone, email, Category)
         #delete and save
        #update(CustomerID,Fname, Lname, ZipCode, Telephone, email, Category)
        print(updateCustomerDB(CustomerID,Fname, Lname, ZipCode, Telephone, email, Category))
        c_list=getDictList_DB()
        return render_template("customers.html",customer=c_list)







# PAGE: ADD CUSTOMER
#------------------------------------------------------------------------------------
@app.route("/add", methods=["POST", "GET"]) # Decorator - Now
def add():
    if request.method == "GET":
        cList=getDictList_DB()
        return render_template("add.html", message=cList)
    else:
        CustomerID = getIntegerFormVariable("CustomerID")
        Fname = getFormVariable("fname")
        Lname =  getFormVariable("lname")
        ZipCode =  getFormVariable("ZipCode")
        Telephone =  getIntegerFormVariable("Telephone")
        email =  getFormVariable("email")
        Category =  getFormVariable("Category")

        saveCustomerDB(CustomerID, Fname, Lname, ZipCode, Telephone, email, Category )

        cList=getDictList_DB()
        return render_template("customers.html", customer=cList)

# PAGE: CREATE ORDER -1
#------------------------------------------------------------------------------------
@app.route("/createorder1", methods=["POST", "GET"]) # Decorator - Now
def createorder1():
    if request.method == "GET":
        dList=getDDictList_DB()
        # oList = getODictList_DB()
        return render_template("createorder1.html", message=dList)
    else:
        OrdDet_ID = getIntegerFormVariable("OrdDet_ID")
        Product_ID = getIntegerFormVariable("Product_ID")
        OrderID =  getIntegerFormVariable("OrderID")
        Quantity =  getIntegerFormVariable("Quantity")
        CustomerID= getIntegerFormVariable("CustomerID")
        OrderDate= getFormVariable("OrderDate")
        OrderType = getFormVariable("OrderType")
        SalesPerson = getIntegerFormVariable("SalesPerson")

        saveOrdDetDB(OrdDet_ID, Product_ID, OrderID,Quantity,OrderDate, CustomerID, OrderType, SalesPerson)
        dList=getDDictList_DB()
        oList = getODictList_DB()


        if getIntegerFormVariable("OrdDet_ID2") != 0:
            OrdDet_ID = getIntegerFormVariable("OrdDet_ID2")
            Product_ID = getIntegerFormVariable("Product_ID2")
            OrderID =  getIntegerFormVariable("OrderID")
            Quantity =  getIntegerFormVariable("Quantity2")

            saveOrdDetDB2(OrdDet_ID, Product_ID, OrderID, Quantity)
            dList=getDDictList_DB()

            # return render_template("createorder1.html", message=dList)
        if getIntegerFormVariable("OrdDet_ID3") != 0:
            OrdDet_ID = getIntegerFormVariable("OrdDet_ID3")
            Product_ID = getIntegerFormVariable("Product_ID3")
            OrderID =  getIntegerFormVariable("OrderID")
            Quantity =  getIntegerFormVariable("Quantity3")

            saveOrdDetDB2(OrdDet_ID, Product_ID, OrderID,Quantity)
            dList=getDDictList_DB()


        if getIntegerFormVariable("OrdDet_ID4") != 0:
            OrdDet_ID = getIntegerFormVariable("OrdDet_ID4")
            Product_ID = getIntegerFormVariable("Product_ID4")
            OrderID =  getIntegerFormVariable("OrderID")
            Quantity =  getIntegerFormVariable("Quantity4")

            saveOrdDetDB2(OrdDet_ID, Product_ID, OrderID,Quantity)
            dList=getDDictList_DB()


        if getIntegerFormVariable("OrdDet_ID5") != 0:
            OrdDet_ID = getIntegerFormVariable("OrdDet_ID5")
            Product_ID = getIntegerFormVariable("Product_ID5")
            OrderID =  getIntegerFormVariable("OrderID")
            Quantity =  getIntegerFormVariable("Quantity5")
            CustomerID= getIntegerFormVariable("CustomerID")

            saveOrdDetDB2(OrdDet_ID, Product_ID, OrderID,Quantity)
            dList=getDDictList_DB()

        return render_template("createorder1.html", message=dList)







###################################################################################
#                                  "NORMAL" PYTHON
###################################################################################

# 1. GET VARIABLES FROM FORMS
#---------------------------
def getFormVariable(variableName):
    return request.form.get(variableName, 0)

def getIntegerFormVariable(variableName):
    return int(request.form.get(variableName, 0))




########################################################################################
########################################################################################
#                   IF DATABASE BASED ....
########################################################################################
########################################################################################


# Customer Dictionary
#-------------------------------------
def getDictList_DB():
    con = sqlite3.connect('HandTrucks.db')
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM Customer;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        c = Customer(row[0], row[1],row[2],row[3],row[4],row[5],row[6])
        rowSTRING2 += "{" + c.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2



#Supplier DB
def getSuppDictList_DB():
    con = sqlite3.connect('HandTrucks.db')
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM Supplier;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        s = Supplier(row[0], row[1],row[2],row[3],row[4])
        rowSTRING2 += "{" + s.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2

#Product Dictionaries
def getPDictList_DB():
    con = sqlite3.connect('HandTrucks.db')
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM Product;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        p = Product(row[0], row[1],row[2],row[3])
        rowSTRING2 += "{" + p.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2

#Order Dictionaries
def getODictList_DB():
    con = sqlite3.connect('HandTrucks.db')
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM Orders;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        o = Order(row[0], row[1],row[2],row[3], row[4])
        rowSTRING2 += "{" + o.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2

#OrdDet Dictionary
def getDDictList_DB():
    con = sqlite3.connect('HandTrucks.db')
    cursorObj = con.cursor()

    rowSTRING2 = "["

    cursorObj.execute('SELECT * FROM OrderDet;')
    rows = cursorObj.fetchall()
    for row in rows:
        newRow = []
        d = OrderDet(row[0], row[1],row[2],row[3])
        rowSTRING2 += "{" + d.getDict() + "},"
    rowSTRING2 = rowSTRING2[0:-1]
    rowSTRING2 = rowSTRING2 + "]"
    rowSTRING2 = eval(rowSTRING2)
    return rowSTRING2



# # 5. DELETE Customer and Update to a New One
# #-------------------------------------
def update(CustomerID,Fname, Lname, ZipCode, Telephone, email, Category):
    def delCustomer_DB(CustomerID):
        database = "HandTrucks.db"
        # create a database connection
        conn = None
        conn = sqlite3.connect(database)
        sql='DELETE FROM customer WHERE CustomerID=?'
        cur = conn.cursor()
        cur.execute(sql, (CustomerID,))
        conn.commit()

    delCustomer_DB(CustomerID)

    def saveCustomerDB(CustomerID, Fname, Lname, ZipCode, Telephone, email, Category ):
        database = "HandTrucks.db"
        # create a database connection
        conn = None
        conn = sqlite3.connect(database)
        sql='INSERT INTO Customer(CustomerID, Fname,Lname, ZipCode, Telephone,email,Category) VALUES(?,?,?,?,?,?,?)'
        cur = conn.cursor()
        cur.execute(sql, (CustomerID, Fname, Lname, ZipCode, Telephone, email, Category, ))
        conn.commit()

    saveCustomerDB(CustomerID, Fname, Lname, ZipCode, Telephone, email, Category )


# GET ONE CUSTOMER
def getCustomer_DB(CustomerID):
    database = "HandTrucks.db"
    conn = None
    conn = sqlite3.connect(database)
    sql='SELECT * FROM Customer WHERE CustomerID = ?'
    cur= conn.cursor()
    cur.execute(sql, [CustomerID])
    row = cur.fetchone()
    return row

    # print(row)
    # for row in rows:
    #     print (row)
    # todo = cur.fetchone()



# # 5. ADD CUSTOMER FROM DB
# #-------------------------------------
def saveCustomerDB(CustomerID, Fname, Lname, ZipCode, Telephone, email, Category ):
    database = "HandTrucks.db"
    # create a database connection
    conn = None
    conn = sqlite3.connect(database)
    sql='INSERT INTO Customer(CustomerID, Fname,Lname, ZipCode, Telephone,email,Category) VALUES(?,?,?,?,?,?,?)'
    cur = conn.cursor()
    cur.execute(sql, (CustomerID, Fname, Lname, ZipCode, Telephone, email, Category, ))
    conn.commit()



# # 6. UPDATE CUSTOMER
# # -------------------------------
def updateCustomerDB(CustomerID,Fname, Lname, ZipCode, Telephone, email, Category):
  database = "HandTrucks.db"
  conn = None
  conn = sqlite3.connect(database)
  sql="UPDATE Customer SET Fname= ?, Lname = ?, ZipCode=?, Telephone= ?, email= ?, Category= ?  WHERE CustomerID = ?"
  cur = conn.cursor()
  cur.execute(sql, (Fname, Lname, ZipCode, Telephone, email, Category,CustomerID, ))
  conn.commit()


# These functions insert data into the OrderDet table and the Orders Table after the order is created.
def saveOrdDetDB(OrdDet_ID, Product_ID, OrderID, Quantity, OrderDate, CustomerID, OrderType, SalesPerson):
    database = "HandTrucks.db"
    # create a database connection
    conn = None
    conn = sqlite3.connect(database)
    sql="INSERT INTO OrderDet(OrdDet_ID, Product_ID, OrderID, Quantity) VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, (OrdDet_ID, Product_ID, OrderID, Quantity, ))
    conn.commit()
    conn = None
    conn = sqlite3.connect(database)
    sql="INSERT INTO Orders(OrderID, OrderDate, CustomerID, OrderType, SalesPerson) VALUES(?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, (OrderID, OrderDate, CustomerID, OrderType, SalesPerson,  ))
    conn.commit()

def saveOrdDetDB2(OrdDet_ID, Product_ID, OrderID, Quantity):
    database = "HandTrucks.db"
    # create a database connection
    conn = None
    conn = sqlite3.connect(database)
    sql="INSERT INTO OrderDet(OrdDet_ID, Product_ID, OrderID, Quantity) VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, (OrdDet_ID, Product_ID, OrderID, Quantity, ))
    conn.commit()
    conn = None


