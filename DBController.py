import sqlite3
import random


def QueryLawyer(FirstName, LastName, PostCode, Accreditation):
    args = [FirstName, LastName, PostCode, Accreditation]
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    return [record for record in cursor.execute("""select FIRST_NAME, LAST_NAME, PostCode, CERTIFICATE from FALUSER_MEMBER inner join FALUSER_SUBURB on FALUSER_MEMBER.ID = FALUSER_SUBURB.ID 
where FIRST_NAME LIKE ? and LAST_NAME LIKE ? and POSTCODE LIKE ? and CERTIFICATE like ?""", args)]

def AddCookie():
    pass
