import sqlite3 as sqlite
import random
import os
import uuid
import string

##    cursor.execute("INSERT INTO test VALUES ('Jon', 'Snow', 2000, 'Knows Nothing')")
##    cursor.execute("INSERT INTO test VALUES ('Ned', 'Stark', 2159, 'Honorable')")
##    cursor.execute("INSERT INTO test VALUES ('Bran', 'Stark', 2159, 'Raven')")
##    cursor.execute("INSERT INTO test VALUES ('Dany', 'Targaryen', 2126, 'Dragon')")

def Build(option):
    sqlite.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
    sqlite.register_adapter(uuid.UUID, lambda u: u.bytes_le)
    connection = sqlite.connect("Database.db", detect_types = sqlite.PARSE_DECLTYPES)
    cursor = connection.cursor()
    
    cursor.execute("drop table if exists Firm")
    cursor.execute("drop table if exists Lawyer")
    cursor.execute("drop table if exists Language")
    cursor.execute("drop table if exists Profession")
    cursor.execute("drop table if exists Suburb")
    cursor.execute("drop table if exists Cookies")
    cursor.execute("drop table if exists FirmLawyers")
    cursor.execute("drop table if exists LawyerLanguages")

    #Foreign key relationships are not enforced by default.
    cursor.execute("""create table Cookies (
                      Cookie GUID primary key,
                      State text,
                      Time timestamp not null)""")
    cursor.execute("""create table Firm (
                      ID GUID primary key,
                      SuburbID GUID references Suburb(ID),
                      FirmName text,
                      Phone text)""")
    cursor.execute("""create table Language (
                      ID GUID primary key,
                      LanguageName text)""")
    cursor.execute("""create table Lawyer (
                      ID GUID primary key,
                      FirstName text,
                      LastName text,
                      Specialty text)""")
    cursor.execute("""create table Profession (
                      ID GUID primary key,
                      ProfessionName text)""")
    cursor.execute("""create table Suburb (
                      ID GUID primary key,
                      SuburbName text,
                      PostCode text,
                      State text)""")

    cursor.execute("""create table FirmLawyers (
                      LawyerID GUID references Lawyer(ID),
                      FirmID GUID references Firm(ID))""")
    cursor.execute("""create table LawyerLanguages (
                      LawyerID GUID references Lawyer(ID),
                      LanguageID GUID references Language(ID))""")
                      

    if option:
        male_file = open(os.path.join(os.path.dirname(__file__), "male.txt"), 'r')
        female_file = open(os.path.join(os.path.dirname(__file__), "female.txt"), 'r')
        names = [name.strip() for name in male_file.readlines()]
        names.extend([name.strip() for name in female_file.readlines()])
        male_file.close()
        female_file.close()
        SuburbIDs = []
        LawyerIDs = []
        FirmIDs = []
        LanguageIDs = []
        
        for postcode in range(4000):
            ID = uuid.uuid4()
            state = random.choice(["NT", "NSW", "VIC", "QLD", "SA", "WA", "TAS"])
            postcode = ["NT", None, "NSW", "VIC", "QLD", "SA", "WA", "TAS"].index(state) * 1000
            postcode += random.randint(0, 999)
            cursor.execute("Insert into Suburb values (?, ?, ?, ?)", [ID, None, str(postcode), state])
            SuburbIDs.append(ID)
            print(len(SuburbIDs))
            
        professions = ["Accountant General", "Adjudicator", "Advocate", "Advocate General", "Advocatus", "Arbitrator", "Articled clerk", "Assessor", "Associate Justice", "Attorney at foreign law"]
        for i in range(33000):
            ID = uuid.uuid4()
            LawyerIDs.append(ID)
            cursor.execute("insert into Lawyer values (?, ?, ?, ?)", [ID, random.choice(names), random.choice(names), random.choice(professions)])
        for i in range(14000):
            ID = uuid.uuid4()
            FirmIDs.append(ID)
            Name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + " & " + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + " Partners"
            cursor.execute("insert into Firm values (?, ?, ?, ?)", [ID, random.choice(SuburbIDs), Name, str(random.randint(10000000, 99999999))])
        english = uuid.uuid4()
        cursor.execute("insert into Language values (?, ?)", [english, "English"])
        for language in ["Italian", "Greek", "French", "Arabic", "Hindi", "Manndarin", "German"]:
            ID = uuid.uuid4()
            LanguageIDs.append(ID)
            cursor.execute("insert into Language values (?, ?)", [ID, language])
        for lawyer in LawyerIDs:
            cursor.execute("insert into FirmLawyers values (?, ?)", [lawyer, random.choice(FirmIDs)])
            cursor.execute("insert into LawyerLanguages values (?, ?)", [lawyer, english])
            if random.randint(0, 99) < 20:
                for reps in range(random.randint(1, 3)):
                    cursor.execute("insert into LawyerLanguages values (?, ?)", [lawyer, random.choice(LanguageIDs)])
        cursor.execute("create index FirmIndex on Firm (FirmName)")
        cursor.execute("create index SuburbIndex on Suburb (PostCode)")
        
    else:
        cursor.execute("""INSERT INTO FALUSER_MEMBER (MEMBER_ID, FIRST_NAME, LAST_NAME, CERTIFICATE)
                       VALUES (1, 'Jon', 'Snow', 'Civil')""")
        cursor.execute("""INSERT INTO FALUSER_MEMBER (MEMBER_ID, FIRST_NAME, LAST_NAME, CERTIFICATE)
                       VALUES (2, 'Ned', 'Stark', 'Family')""")               


    
    connection.commit()
    connection.close()
