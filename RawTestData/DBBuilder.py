import sqlite3
import random
import os

##    cursor.execute("INSERT INTO test VALUES ('Jon', 'Snow', 2000, 'Knows Nothing')")
##    cursor.execute("INSERT INTO test VALUES ('Ned', 'Stark', 2159, 'Honorable')")
##    cursor.execute("INSERT INTO test VALUES ('Bran', 'Stark', 2159, 'Raven')")
##    cursor.execute("INSERT INTO test VALUES ('Dany', 'Targaryen', 2126, 'Dragon')")

def Build(option):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    
    cursor.execute("drop table if exists faluser_firm")
    cursor.execute("drop table if exists faluser_member")
    cursor.execute("drop table if exists faluser_suburb")
    cursor.execute("drop table if exists Cookies")

    cursor.execute("""create table Cookies
                      

    cursor.execute("""
        CREATE TABLE "FALUSER_SUBURB" 
   (	"ID" int NOT NULL, 
	"NAME" text, 
	"POSTCODE" text,
	"STATE" text)
  """ )
    cursor.execute("""
        CREATE TABLE "FALUSER_MEMBER" 
   (	"MEMBER_ID" int NOT NULL, 
	"MEMBER_REG_ID" int,
	"YEAR_APPOINTED" int,
	"FIRST_NAME" text, 
	"MIDDLE_NAME" text, 
	"LAST_NAME" text, 
	"ADMISSION_DATE" DATE, 
	"MEM_EMAIL" text, 
	"MEM_NON_DISCLOSURE" int, 
	"INCLUDE_ON_WEBSITE" int, 
	"EXCLUDE_FIRM_DETAILS" int, 
	"MEM_PHONE_AREA_CD" text, 
	"MEM_PHONE" text, 
	"MEM_FAX_AREA_CD" text, 
	"MEM_FAX" text, 
	"MEM_DX_NO" int, 
	"MEM_DX_EXCHANGE_ID" int, 
	"LAST_UPDATE" DATE, 
	"ACTIVE_CD" int, 
	"PREFERRED_NAME" text, 
	"IS_MEMBER" int, 
	"CERTIFICATE" text) 
  """ )
    cursor.execute("""
        CREATE TABLE "FALUSER_FIRM" 
   (	"FIRM_ID" int NOT NULL, 
	"FIRM_REG_ID" int,
	"ID" int NOT NULL,
	"FIRM_NAME" text, 
	"TRADING_NAME" text, 
	"FIRM_WEB_NAME" text, 
	"FIRM_STREET_ADDR_1" text, 
	"FIRM_STREET_ADDR_2" text, 
	"FIRM_POSTAL_ADDR_1" text, 
	"FIRM_POSTAL_ADDR_2" text, 
	"FIRM_DX_NO" int, 
	"FIRM_DX_EXCHANGE_ID" int, 
	"FIRM_PHONE_AREA_CD" text, 
	"FIRM_PHONE" text, 
	"FIRM_MOBILE" text, 
	"FIRM_FAX_AREA_CD" text, 
	"FIRM_FAX" text, 
	"FIRM_EMAIL" text, 
	"FIRM_BRANCH_NO" int, 
	"FIRM_URL" text, 
	"FIRM_NON_DISCLOSURE" int, 
	"FIRM_NON_DISCLOSURE_ADDR" int, 
	"ACTIVE_CD" int, 
	"LAST_UPDATE" DATE, 
	"FIRM_INCLUDE_ON_WEBSITE" int, 
	"IS_SPECACC" int, 
	"DISP_CODE" int, 
	"DISP_DATE" DATE, 
	"DISP_NOTES" text) 
  """ )

    if option:
        postcodes = open(os.path.join(os.path.dirname(__file__), "addresses.txt"), 'r')
        lines = [line.strip() for line in postcodes.readlines()]
        postcodes.close()
        codes = set(lines[1::2])
        count = 0
        for postcode in codes:
            name, others = postcode.split(',')
            state, postcode = others.split()
            cursor.execute("Insert into FALUSER_SUBURB values (?, ?, ?, ?)", [count, name, postcode, state])
            count += 1
        
        count -= 1
        male_file = open(os.path.join(os.path.dirname(__file__), "male.txt"), 'r')
        female_file = open(os.path.join(os.path.dirname(__file__), "female.txt"), 'r')
        names = [name.strip() for name in male_file.readlines()]
        names.extend([name.strip() for name in female_file.readlines()])
        male_file.close()
        female_file.close()
        random.shuffle(names)
        fnames = names[:]
        random.shuffle(names)
        lnames = names[:]
        professions = ["Accountant General", "Adjudicator", "Advocate", "Advocate General", "Advocatus", "Arbitrator", "Articled clerk", "Assessor", "Associate Justice", "Attorney at foreign law"]
        ID = 0
        #insert practises
        for i in range(len(fnames)):
            values = [ID, fnames[i], lnames[i], random.choice(professions)]
            cursor.execute("insert into FALUSER_MEMBER (MEMBER_ID, FIRST_NAME, LAST_NAME, CERTIFICATE) values (?, ?, ?, ?)", values)
            ID += 1
    else:
        cursor.execute("""INSERT INTO FALUSER_MEMBER (MEMBER_ID, FIRST_NAME, LAST_NAME, CERTIFICATE)
                       VALUES (1, 'Jon', 'Snow', 'Civil')""")
        cursor.execute("""INSERT INTO FALUSER_MEMBER (MEMBER_ID, FIRST_NAME, LAST_NAME, CERTIFICATE)
                       VALUES (2, 'Ned', 'Stark', 'Family')""")               


    
    connection.commit()
    connection.close()
