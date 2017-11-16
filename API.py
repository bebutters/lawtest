import bottle
import DBController
import RawTestData.DBBuilder as DBBuilder
import stopgap
import uuid
import timeit
import datetime

app = bottle.Bottle()
def Wildify(string):
    if not string:
        return("%")
    else:
        return(string + "%")

@app.route('/')
def hello():
    try:
        GUID = uuid.uuid4()
        DBController.AddCookie(GUID, "NSW")
        bottle.response.set_cookie("access", str(GUID), max_age = 28800) #Domain
        return(stopgap.a)
    except Exception as e:
        return(e)

@app.post("/Lawyer")
def Lawyer():
    if bottle.request.get_cookie("access"):
        State = DBController.CheckCookie(uuid.UUID(hex = bottle.request.get_cookie("access")))
        if State:
            bottle.response.headers["Content-Type"] = "application/json"
            FirstName = Wildify(bottle.request.forms.get("FirstName"))
            LastName = Wildify(bottle.request.forms.get("LastName"))
            PostCode = Wildify(bottle.request.forms.get("PostCode"))
            Specialty = Wildify(bottle.request.forms.get("Specialty"))
            Language = bottle.request.forms.get("Language")
            return(DBController.QueryLawyer(FirstName, LastName, PostCode, Language, State))
    return({"error": "Sorry you are not authorised to access this data. Please try a page refresh"})

@app.post("/Firm")
def Firm():
    if bottle.request.get_cookie("access"):
        State = DBController.CheckCookie(uuid.UUID(hex = bottle.request.get_cookie("access")))
        if State:
            bottle.response.headers["Content-Type"] = "application/json"
            Name = Wildify(bottle.request.forms.get("Name"))
            PostCode = Wildify(bottle.request.forms.get("PostCode"))
            Language = bottle.request.forms.get("Language")
            return(DBController.QueryFirm(Name, PostCode, Language, State))
    return({"error": "Sorry you are not authorised to access this data. Please try a page refresh"})   

@app.route('/Build/Test')
def BuildTest():
    DBController.Build(0)

@app.route('/Build/Performance')
def BuildPerformance():
    DBBuilder.Build(1)

@app.route('/Performance/Test')
def Test():
    stime = datetime.datetime.now()
    res = DBController.QueryFirm('g%', '%', "hindi", 'NSW')
    ftime = datetime.datetime.now()
    print(ftime - stime)
    return(res)

@app.route('/AddCookie')
def AddCookie():
    cookie = bottle.request.query["cookie"]
    state = bottle.request.query["state"]
    print(cookie)
    DBController.AddCookie(cookie, state)

bottle.run(app)

