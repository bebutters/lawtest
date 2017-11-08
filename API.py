import bottle
import DBController
import RawTestData.DBBuilder as DBBuilder
import stopgap
import uuid

app = bottle.Bottle()
def Wildify(string):
    if not string:
        return("%")
    else:
        return string + "%"

@app.route('/')
def hello():
    GUID = str(uuid.uuid4())
    bottle.response.set_cookie("access", GUID, max_age = 28800) #Domain
    print(GUID)
    return(stopgap.a)
    

@app.post("/Lawyer")
def Lawyer():
    string = """<table style="width:25%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>PostCode</th>
    <th>Specialty</th>
  </tr>"""
    FirstName = Wildify(bottle.request.forms.get("FirstName"))
    LastName = Wildify(bottle.request.forms.get("LastName"))
    PostCode = Wildify(bottle.request.forms.get("PostCode"))
    print(bottle.request.forms.get("PostCode"))
    Accreditation = Wild_ify(bottle.request.forms.get("Accreditation"))
    for entry in DBController.QueryLawyer(FirstName, LastName, PostCode, Accreditation):
        string += "<tr>"
        for field in entry:
            string += "<td>" + str(field) + "</td>"
        string += "</tr>"
    string += "</table>"
    return(string)

@app.post("/Practise")
def Practise():
    pass   

@app.route('/Build/Test')
def BuildTest():
    DBController.Build(0)

@app.route('/Build/Performance')
def BuildPerformance():
    DBBuilder.Build(1)

@app.route('/AddCookie')
def AddCookie():
    cookie = bottle.request.query["cookie"]
    print(cookie)
    DBController.AddCookie()

bottle.run(app, host='localhost', port=8080)

