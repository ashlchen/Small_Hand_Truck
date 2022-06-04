
CREATE TABLE Employee (
	Employee_ID	INTEGER,
	FirstName	TEXT,
	LastName	TEXT,
	Posisiton	TEXT,
	HourlyRate	INTEGER,
	HireDate	TEXT,
	PRIMARY KEY(Employee_ID AUTOINCREMENT)
);

CREATE TABLE Product (
	Product_ID	INTEGER,
	Product_Name	TEXT,
	Color	TEXT,
	Price	INTEGER,
	PRIMARY KEY(Product_ID)
);

CREATE TABLE Material (
	SW_Part_No	TEXT,
	Supplier_Part_No	INTEGER,
	Supplier_ID	INTEGER,
	MaterialName	TEXT,
	Cost	INTEGER,
	QuantityAvailable	INTEGER,
	FOREIGN KEY(Supplier_ID) REFERENCES Supplier(SupplierID),
	PRIMARY KEY(SW_Part_No)
);

CREATE TABLE Supplier (
	SupplierID	INTEGER,
	SupplierName	TEXT,
	ZipCode	TEXT,
	Telephone	INTEGER,
	Email	TEXT,
	PRIMARY KEY(SupplierID)
);

CREATE TABLE BOM (
	BOM_ID	INTEGER,
	Product_ID	INTEGER,
	SW_Part_No	TEXT,
	Quantity	INTEGER,
	FOREIGN KEY(SW_Part_No) REFERENCES Material(SW_Part_No),
	PRIMARY KEY(BOM_ID)
);

CREATE TABLE OrderDet (
	OrdDet_ID	INTEGER,
	Product_ID	INTEGER,
	OrderID	INTEGER,
	Quantity	INTEGER,
	FOREIGN KEY(OrderID) REFERENCES Orders(OrderID),
	FOREIGN KEY(Product_ID) REFERENCES Product(Product_ID),
	PRIMARY KEY(OrdDet_ID)
);

CREATE TABLE Customer (
	CustomerID	INTEGER,
	Fname	TEXT,
	Lname	TEXT,
	ZipCode	TEXT,
	Telephone	INTEGER,
	email	TEXT,
	Category	TEXT,
	PRIMARY KEY(CustomerID)
);

CREATE TABLE Orders (
	OrderID	INTEGER,
	OrderDate	TEXT,
	CustomerID	INTEGER,
	OrderType	TEXT,
	SalesPerson	INTEGER,
	FOREIGN KEY(SalesPerson) REFERENCES Employee(Employee_ID),
	FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID),
	PRIMARY KEY(OrderID)
	
);
INSERT INTO Employee (Employee_ID,FirstName,LastName,Posisiton,HourlyRate,HireDate) VALUES (1,'Lisa','Simpson','Staff',20,'07-20-2020'),
 (3,'Bart','Simpson','Staff',15,'08-20-2020'),
 (6,'Larry','Larry','CEO',50,'01-15-2019'),
 (7,'Vijay','Larry','Technical Production Manager',30,'01-20-2019'),
 (8,'Aaron','Larry','Orders',25,'01-25-2019'),
 (9,'Chen','Larry','Bookkeeping and Payroll',25,'02-25-2019'),
 (10,'Hillol','Larry','1st Production Line Operative: Making Frames',25,'03-25-2019'),
 (11,'Bruce','Larry','2nd Production Line Operative: Welding',25,'04-25-2019'),
 (12,'Bipin','Larry','3rd Production Line Operative: Painting',25,'05-25-2019'),
 (13,'Beth','Larry','4th Production Line Operative: Packing',25,'06-25-2019'),
 (14,'Mike','Larry','Store Room Manager',23,'07-25-2019');
 
INSERT INTO Product (Product_ID,Product_Name,Color,Price) 
VALUES (1,'Standard Hand Truck','Red',120),
 (2,'Standard Hand Truck','Green',120),
 (3,'Standard Hand Truck','Black',120),
 (4,'Standard Hand Truck','White',120),
 (5,'Standard Hand Truck','Silver',125),
 (6,'Standard Hand Truck','Gold',125),
 (7,'Small Hand Truck','Red',70),
 (8,'Small Hand Truck','Green',70),
 (9,'Small Hand Truck','Black',70),
 (10,'Small Hand Truck','White',70),
 (11,'Small Hand Truck','Silver',75),
 (12,'Small Hand Truck','Gold',75);
 
INSERT INTO Material (SW_Part_No,Supplier_Part_No,Supplier_ID,MaterialName,Cost,QuantityAvailable) 
VALUES ('OS01','ES39',2,'Hinges',0.5,100),
 ('OS02','ES24',2,'Wheel',0.5,100),
 ('OS03','ES67',2,'Handle',0.5,100),
 ('OS04','ES09',2,'Fastener',0.25,1000),
 ('OS05','AB01',1,'Container',0.25,1000),
 ('OS06','TM01',3,'Aluminum Tube',0.5,100),
 ('OS07-1','QP04',4,'Red Paint',0.25,100),
 ('OS07-2','QP11',4,'Green Paint',0.25,100),
 ('OS07-3','QP18',4,'Black Paint',0.25,100),
 ('OS07-4','QP19',4,'White Paint',0.25,100),
 ('OS07-5','LP25',5,'Gold Paint',0.5,100),
 ('OS07-6','LP26',5,'Silver Paint',0.5,100),
 ('OS08','ES23',2,'Small Wheel',0.25,100),
 ('OS09','ES68',2,'Small Handle',0.25,100),
 ('OS10','ES08',2,'Small Fastener',0.25,100),
 ('OS11','LP02',1,'Small Container',0.25,100),
 ('OS12','ES69',2,'U-Clips',0.25,100),
 ('SW01','',NULL,'RHS Frame',0,100),
 ('SW02','',NULL,'LHS Frame',0,100),
 ('SW03','',NULL,'RHS Frame',0,100),
 ('SW04','',NULL,'LHS Frame',0,100);
 
INSERT INTO Supplier (SupplierID,SupplierName,ZipCode,Telephone,Email) 
VALUES (1,'Aluminum Boxes','IN 47401',9876543211,'aboxes@gmail.com'),
 (2,'Engineering Supplies','IN 47402',1112223333,'esupplies@gmail.com'),
 (3,'Top Materials','IN 47403',2223334444,'tmaterials@gmail.com'),
 (4,'Quality Paints','IN 47404',3332221111,'qualitypaints@gmail.com'),
 (5,'Luxury Paints','IN 47405',4443332222,'luxarypaints@gmail.com');
 
INSERT INTO BOM (BOM_ID,Product_ID,SW_Part_No,Quantity) 
VALUES (1,1,'OS02',1),
 (2,1,'OS01',4),
 (3,1,'OS03',2),
 (4,1,'OS04',4),
 (5,1,'OS05',1),
 (6,1,'OS07-1',0.5),
 (7,1,'OS12',4),
 (8,1,'SW01',1),
 (9,1,'SW02',1),
 (10,7,'SW03',1),
 (11,7,'SW04',1),
 (12,7,'OS08',1),
 (13,7,'OS09',2),
 (14,7,'OS10',4),
 (15,7,'OS07-1',0.25),
 (16,7,'OS11',1);
 
INSERT INTO OrderDet (OrdDet_ID,Product_ID,OrderID,Quantity) 
VALUES (1,3,1,10),
 (2,4,1,5),
 (3,8,2,1),
 (4,12,3,1),
 (5,5,3,3);
 
INSERT INTO Customer (CustomerID,Fname,Lname,ZipCode,Telephone,email,Category) VALUES (1,'Bill','Bob','IN 12345',8001231234,'billbob@gmail.com','Consumer'),
 (2,'Bob','Bill','IN 23456',1234567890,'bobbill@gmail.com','Consumer'),
 (3,'Mark','Bill','IN 12341',1234567891,'markbill@gmail.com','Consumer'),
 (4,'Bill','Mark','IN 12342',1234567892,'billmark@gmail.com','Consumer'),
 (5,'Marvin','Lark','IL 12343',1234567893,'marvinlark@gmail.com','Consumer'),
 (6,'Bright','Florist','NY 11375',1234567895,'brightflorist@gmail.com','Business'),
 (7,'Hilary','Smith','MA 02108',1234567896,'hilarysmith@gmail.com','Business'),
 (8,'Bliss Garden Center','','RI 02886',1234567899,'blissgarden@gmail.com','Consumer');
 
INSERT INTO Orders (OrderID,OrderDate,CustomerID,OrderType,SalesPerson)
 VALUES (1,'07-15-2021',8,'Purchase',1),
 (2,'07-15-2021',7,'Purchase',3),
 (3,'07-15-2021',6,'Purchase',6) ;

