BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "e_cost" (
	"Reason"	TEXT,
	"Birr"	INTEGEr,
	"Comment"	TEXT,
	"User"	TEXT,
	"Date"	TEXT
);
CREATE TABLE IF NOT EXISTS "empty_box" (
	"Type"	TEXT,
	"Box"	TEXT,
	"Amount"	INTEGER,
	"Date"	TEXT
);
CREATE TABLE IF NOT EXISTS "credit_box" (
	"Name"	TEXT,
	"Amount"	INTEGER,
	"Date"	TEXT
);
CREATE TABLE IF NOT EXISTS "t_cost" (
	"Birr"	INTEGE,
	"Date"	TEXT
);
CREATE TABLE IF NOT EXISTS "t_income" (
	"Credit"	TEXT,
	"Total_c"	INTEGER,
	"Total"	INTEGER,
	"Date"	TEXT
);
CREATE TABLE IF NOT EXISTS "user_auth" (
	"Auth_Type"	TEXT,
	"Username"	TEXT,
	"Password"	TEXT
);
CREATE TABLE IF NOT EXISTS "Item_conf" (
	"Name"	TEXT,
	"Price"	INTEGER
);
CREATE TABLE IF NOT EXISTS "e_income" (
	"Type"	TEXT,
	"Box"	TEXT,
	"Amount"	INTEGER,
	"Date"	TEXT
);
CREATE TABLE IF NOT EXISTS "stock" (
	"ID"	INTEGER,
	"Coca Pet"	INTEGER,
	"Ambo"	INTEGER,
	"Novida"	INTEGER,
	"Predator"	INTEGER,
	"Ambo_Flavor"	INTEGER,
	"Coca"	INTEGER,
	PRIMARY KEY("ID")
);
INSERT INTO "empty_box" VALUES ('Coca Pet','Case',20,'2023-07-01 ');
INSERT INTO "empty_box" VALUES ('Predator','Case',5,'2023-07-01 ');
INSERT INTO "t_income" VALUES ('0',8970,8970,'2023-07-01 ');
INSERT INTO "user_auth" VALUES ('Casher','Hana','Hana@20');
INSERT INTO "user_auth" VALUES ('Admin','Kirubel','Kiru@21');
INSERT INTO "user_auth" VALUES ('Store_keeper','Adiss','adiss12');
INSERT INTO "Item_conf" VALUES ('Coca Pet',420);
INSERT INTO "Item_conf" VALUES ('Ambo',370);
INSERT INTO "Item_conf" VALUES ('Novida',416);
INSERT INTO "Item_conf" VALUES ('Predator',432);
INSERT INTO "Item_conf" VALUES ('Ambo_Flavor',310);
INSERT INTO "Item_conf" VALUES ('Coca',410);
INSERT INTO "e_income" VALUES ('Coca','Case',23,'2023-07-01 ');
INSERT INTO "e_income" VALUES ('Coca Pet','Case',55,'2023-07-01 ');
INSERT INTO "e_income" VALUES ('Predator','Case',100,'2023-07-01 ');
INSERT INTO "stock" VALUES (1,50,100,110,110,110,NULL);
COMMIT;
