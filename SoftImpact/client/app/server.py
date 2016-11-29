import sqlite3
import json
import io
import numpy
from bottle import request,run
from bottle import post, get, put, delete

from bottle import hook, route, response

#These libraries here will help us to have legal access to the urls
#otherwise we are not authorized to get access to the following URLS
_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

@hook('after_request')
def enable_cors():
    '''Add headers to enable CORS'''

    response.headers['Access-Control-Allow-Origin'] = _allow_origin
    response.headers['Access-Control-Allow-Methods'] = _allow_methods
    response.headers['Access-Control-Allow-Headers'] = _allow_headers

#define the Database which is creaded by the sq.py program
DB = "./todo.db"

#create new student record into the system
@post('/students', method='POST')
def add():
    #if the requst is POST then the system will try to identify the personal data of the student
    #then open a channel into the database
    #and the insert the new record into the database
    #the the system will inform the user that the entry is saved into the database and provide a link to show the new record
    if request.POST.save:
        studentid = request.POST.studentid.strip()
        name = request.POST.name.strip()
        birth = request.POST.birth.strip()
        stclass = request.POST.stclass.strip()
        Year = request.POST.Year.strip()
        Quarter = request.POST.Quarter.strip()
        math = request.POST.math.strip()
        computer = request.POST.computer.strip()
        literature = request.POST.literature.strip()

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO todo (studentid,name,birth,stclass,Year,Quarter,math,computer,literature)  VALUES (?,?,?,?,?,?,?,?,?)", (studentid,name,birth,stclass,Year,Quarter,math,computer,literature))
        conn.commit()
        c.close()
    return '<p> The new user is saved in the database. Return back to see the entry.</p><a href="/manage">Home</a>'

#Get the whole users in the database
@get('/students', method='GET')
def list_students():
    response.headers['Access-Control-Allow-Origin'] = '*' #security
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row 
    db = conn.cursor()
    result=db.execute("SELECT * FROM todo").fetchall()
    conn.commit()
    conn.close()
    return json.dumps( [dict(x) for x in result]) #CREATE JSON

#get the statistics of the three subjects for a specific student
#the user has to write the id of the student to show the suitable information
@get('/statistics/<student:re:[0-9]{1,2}>', method="GET")
def graph_data(student):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT name FROM todo WHERE studentid=(?)", (student) )
    name = c.fetchall()

    data1=[]
    for temp1 in name:
        for tempx in temp1:
            data1.append(tempx)
    unistrings=[str(x) for x in data1]
    name=unistrings[0]

    c.execute("SELECT math, Computer, Literature FROM todo WHERE studentid=(?) AND Quarter='Q1'", (student))
    result = c.fetchall()
    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
        n=numpy.mean(data)

    c.execute("SELECT math, Computer, Literature FROM todo WHERE studentid=(?) AND Quarter='Q2'", (student))
    result = c.fetchall()
    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
        n1=numpy.mean(data)

    c.execute("SELECT math, Computer, Literature FROM todo WHERE studentid=(?) AND Quarter='Q3'", (student))
    result = c.fetchall()
    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
        n2=numpy.mean(data)

    c.execute("SELECT math, Computer, Literature FROM todo WHERE studentid=(?) AND Quarter='Q4'", (student))
    result = c.fetchall()
    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
        n3=numpy.mean(data)

    
    re=[{"id":student,"studentid":student,"name":name,"q1":n,"q2":n1,"q3":n2,"q4":n3}]
    return json.dumps({'statistics':[dict(x) for x in re]}) #CREATE JSON

#Get the suitable information to get the graph which is refered to Computer subject
@get('/modules/computer', method="GET")
def graph_data():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT stclass FROM todo WHERE stclass='IT'")
    stclass = c.fetchall()

    data1=[]
    for temp1 in stclass:
        for tempx in temp1:
            data1.append(tempx)
    unistrings=[str(x) for x in data1]
    stclass=unistrings[4]

    c.execute("SELECT computer FROM todo WHERE Quarter='Q1'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n=numpy.mean(data)
    
    print(n)

    c.execute("SELECT computer FROM todo WHERE  Quarter='Q2'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n1=numpy.mean(data)
    
    print(n1)

    c.execute("SELECT computer FROM todo WHERE Quarter='Q3'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n2=numpy.mean(data)
    
    print(n2)

    c.execute("SELECT computer FROM todo WHERE Quarter='Q4'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n3=numpy.mean(data)
    
    print(n3)

    re1=[{"stclass":stclass,"q1":n,"q2":n1,"q3":n2,"q4":n3}]
    print('Computer',re1)
    return json.dumps({'computer':[dict(x) for x in re1]}) #CREATE JSON

#Get the suitable information to get the graph which is refered to Math subject
@get('/modules/math', method="GET")
def graph_data():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT stclass FROM todo WHERE stclass='MATH'")
    stclass = c.fetchall()

    data1=[]
    for temp1 in stclass:
        for tempx in temp1:
            data1.append(tempx)
    unistrings=[str(x) for x in data1]
    stclass=unistrings[4]

    c.execute("SELECT math FROM todo WHERE Quarter='Q1'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n=numpy.mean(data)
    
    print(n)

    c.execute("SELECT math FROM todo WHERE  Quarter='Q2'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n1=numpy.mean(data)
    
    print(n1)

    c.execute("SELECT math FROM todo WHERE Quarter='Q3'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n2=numpy.mean(data)
    
    print(n2)

    c.execute("SELECT math FROM todo WHERE Quarter='Q4'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n3=numpy.mean(data)
    
    print(n3)

    re1=[{"stclass":stclass,"q1":n,"q2":n1,"q3":n2,"q4":n3}]
    return json.dumps({'math':[dict(x) for x in re1]}) #CREATE JSON

#Get the suitable information to get the graph which is refered to Literacture subject
@get('/modules/literature', method="GET")
def graph_data():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT stclass FROM todo WHERE stclass='Literature'")
    stclass = c.fetchall()

    data1=[]
    for temp1 in stclass:
        for tempx in temp1:
            data1.append(tempx)
    unistrings=[str(x) for x in data1]
    stclass=unistrings[4]

    c.execute("SELECT literature FROM todo WHERE Quarter='Q1'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n=numpy.mean(data)
    
    print(n)

    c.execute("SELECT literature FROM todo WHERE  Quarter='Q2'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n1=numpy.mean(data)
    
    print(n1)

    c.execute("SELECT literature FROM todo WHERE Quarter='Q3'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n2=numpy.mean(data)
    
    print(n2)

    c.execute("SELECT literature FROM todo WHERE Quarter='Q4'")
    result = c.fetchall()

    #w=[x for t in result for x in t]
    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n3=numpy.mean(data)
    
    print(n3)

    re1=[{"stclass":stclass,"q1":n,"q2":n1,"q3":n2,"q4":n3}]
    return json.dumps({'literature':[dict(x) for x in re1]}) #CREATE JSON

#Get the suitable information to get the graph which is refered to a specific Quarter and Year
@get('/quarter', method="GET")
def graph_data():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT Year,Quarter FROM todo", () )
    name = c.fetchall()


    c.execute("SELECT math FROM todo WHERE Quarter='Q1' AND Year=2001", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n=numpy.mean(data)
    print(n)

    c.execute("SELECT computer FROM todo WHERE Quarter='Q1' AND Year=2001", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n1=numpy.mean(data)
    print(n1)

    c.execute("SELECT literature FROM todo WHERE Quarter='Q1' AND Year=2001", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n2=numpy.mean(data)
    print(n2)

    re2=[{"Year":2001,"Quarter":"Q1","Maths":n,"IT":n1,"Literature":n2}]
    return json.dumps({'quartone':[dict(x) for x in re2]}) #CREATE JSON

#Get the suitable information to get the graph which is refered to a specific Quarter and Year
@get('/quartertwo', method="GET")
def graph_data():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT Year,Quarter FROM todo", () )
    name = c.fetchall()


    c.execute("SELECT math FROM todo WHERE Quarter='Q1' AND Year=2002", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n=numpy.mean(data)
    print(n)

    c.execute("SELECT computer FROM todo WHERE Quarter='Q1' AND Year=2002", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n1=numpy.mean(data)
    print(n1)

    c.execute("SELECT literature FROM todo WHERE Quarter='Q1' AND Year=2002", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n2=numpy.mean(data)
    print(n2)

    re2=[{"Year":2002,"Quarter":"Q1","Maths":n,"IT":n1,"Literature":n2}]
    return json.dumps({'quarttwo':[dict(x) for x in re2]}) #CREATE JSON

#Get the suitable information to get the graph which is refered to a specific Quarter and Year
@get('/quarterthree', method="GET")
def graph_data():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("SELECT Year,Quarter FROM todo", () )
    name = c.fetchall()


    c.execute("SELECT math FROM todo WHERE Quarter='Q1' AND Year=2003", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n=numpy.mean(data)
    print(n)

    c.execute("SELECT computer FROM todo WHERE Quarter='Q1' AND Year=2003", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n1=numpy.mean(data)
    print(n1)

    c.execute("SELECT literature FROM todo WHERE Quarter='Q1' AND Year=2003", ())
    result = c.fetchall()
    print (result)

    data=[]
    for temp1 in result:
        for tempx in temp1:
            data.append(tempx)
    print(data)
    n2=numpy.mean(data)
    print(n2)

    re2=[{"Year":2003,"Quarter":"Q1","Maths":n,"IT":n1,"Literature":n2}]
    return json.dumps({'quartthree':[dict(x) for x in re2]}) #CREATE JSON


#the server 
run(host='localhost', port=8080)

