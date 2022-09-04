from flask import Flask, render_template, request
import os

app = Flask(__name__)

UploadDictList = [

{"FilePath": os.path.join("static", "genetics.pdf"), "ImagePath": os.path.join("static", "genetics.pdf"), "Filename": "Genetics", "name":"Anna", "tags":[], "ratings":[], "rating":3, "grade": 10},
{"FilePath": os.path.join("static", "homenotes.pdf"), "ImagePath": os.path.join("static", "homenotes.pdf"), "Filename": "Electricity", "name":"Ethan", "tags":[], "ratings":[], "rating":3, "grade": 5},
{"FilePath": os.path.join("static", "periodictable.pdf"), "ImagePath": os.path.join("static", "periodictable.pdf"), "Filename": "Periodic table", "name":"Dirk", "tags":[], "ratings":[], "rating":3, "grade": 4},
{"FilePath": os.path.join("static", "pollution.pdf"), "ImagePath": os.path.join("static", "pollution.pdf"), "Filename": "Pollution", "name":"Paul", "tags":[], "ratings":[], "rating":3, "grade": 9},
{"FilePath": os.path.join("static", "prokaryoticdiversity.pdf"), "ImagePath": os.path.join("static", "prokaryoticdiversity.pdf"), "Filename": "Prokaryotic Diversity", "name":"Billy", "tags":[], "ratings":[], "rating":3, "grade":10},
{"FilePath": os.path.join("static", "macro.pdf"), "ImagePath": os.path.join("static", "macro.pdf"), "Filename": "Macroeconomics", "name":"Tejinder", "tags":[], "ratings":[], "rating":1, "grade": 11},
{"FilePath": os.path.join("static", "biology.pdf"), "ImagePath": os.path.join("static", "biology.pdf"), "Filename": "Biology", "name":"Henry", "tags":[], "ratings":[], "rating":3, "grade":2},
{"FilePath": os.path.join("static", "periodictable.pdf"), "ImagePath": os.path.join("static", "periodictable.pdf"), "Filename": "War of 1812", "name":"Fred", "tags":[], "ratings":[], "rating":3, "grade":6},
{"FilePath": os.path.join("static", "pollution.pdf"), "ImagePath": os.path.join("static", "pollution.pdf"), "Filename": "Gender Studies", "name":"Bob", "tags":[], "ratings":[], "rating":3, "grade": 3},
]
Subjects = ["Math", "English", "Physics", "Chemistry", "Economics", "History", "Biology", "Psychology", "Geography", "Other", "Digital", "Physical", "Law", "Astronomy"]

@app.route("/")
def home1():
    return render_template("home.html")

@app.route("/home")
def home2():
    return render_template("home.html")

@app.route("/browse", methods=["GET", "POST"])
def browse():
    if request.method == "POST":
        notes = UploadDictList[:]
        for subject in Subjects:
            if request.form.get(subject):
                poplist = []
                for i in range(0, len(notes)-1):
                    if subject not in notes[i]["tags"]:
                        poplist.append(i)
   
        for index in sorted(poplist, reverse=True):
            del notes[index]
        poplist = []
        return notes
        for i in range(0, len(notes)-1):
            if abs(notes[i]["grade"] - request.form["gradeRange"]) > 1:
                poplist.append(i)
        
        for index in sorted(poplist, reverse=True):
            del notes[index]
       
        if len(notes) < 9:
            for i in range(0, 9-len(notes)):
                notes.append({"FilePath": None, "ImagePath": None, "Filename": None, "name": None, "tags":None, "ratings":None, "rating":0, "grade":0})

    else:
        notes = UploadDictList[:9]
    for note in notes:
        if note["rating"] == 1:
            note["rating"] = os.path.join("static", "1.png")
        elif note["rating"] == 2:
            note["rating"] = os.path.join("static", "2.png")
        elif note["rating"] == 3:
            note["rating"] = os.path.join("static", "3.png")
        elif note["rating"] == 4:
            note["rating"] = os.path.join("static", "4.png")
        else:
            note["rating"] = os.path.join("static", "5.png")
    return render_template(
    "browse.html",
    Filename1 = notes[0]["Filename"],
    Filename2 = notes[1]["Filename"],
    Filename3 = notes[2]["Filename"],
    Filename4 = notes[3]["Filename"],
    Filename5 = notes[4]["Filename"],
    Filename6 = notes[5]["Filename"],
    Filename7 = notes[6]["Filename"],
    Filename8 = notes[7]["Filename"],
    Filename9 = notes[8]["Filename"],
    ImagePath1 = notes[0]["ImagePath"],
    ImagePath2 = notes[1]["ImagePath"],
    ImagePath3 = notes[2]["ImagePath"],
    ImagePath4 = notes[3]["ImagePath"],
    ImagePath5 = notes[4]["ImagePath"],
    ImagePath6 = notes[5]["ImagePath"],
    ImagePath7 = notes[6]["ImagePath"],
    ImagePath8 = notes[7]["ImagePath"],
    ImagePath9 = notes[8]["ImagePath"],
    name1 = notes[0]["name"],
    name2 = notes[1]["name"],
    name3 = notes[2]["name"],
    name4 = notes[3]["name"],
    name5 = notes[4]["name"],
    name6 = notes[5]["name"],
    name7 = notes[6]["name"],
    name8 = notes[7]["name"],
    name9 = notes[8]["name"],
    rating1 = notes[0]["rating"],
    rating2 = notes[1]["rating"],
    rating3 = notes[2]["rating"],
    rating4 = notes[3]["rating"],
    rating5 = notes[4]["rating"],
    rating6 = notes[5]["rating"],
    rating7 = notes[6]["rating"],
    rating8 = notes[7]["rating"],
    rating9 = notes[8]["rating"],
    FilePath1 = notes[0]["FilePath"],
    FilePath2 = notes[1]["FilePath"],
    FilePath3 = notes[2]["FilePath"],
    FilePath4 = notes[3]["FilePath"],
    FilePath5 = notes[4]["FilePath"],
    FilePath6 = notes[5]["FilePath"],
    FilePath7 = notes[6]["FilePath"],
    FilePath8 = notes[7]["FilePath"],
    FilePath9 = notes[8]["FilePath"]
    )

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join("static", file.filename))
        name = request.form["name"]
        
        grade = request.form["gradeRange"]

        tags = []
        for subject in Subjects:
            if request.form.get(subject, False):
                tags.append(subject)

        imagename = os.path.splitext(file.filename)[0] + '.pdf'


        UploadDict = {"FilePath": os.path.join("static", file.filename), "ImagePath": os.path.join("static", imagename), "Filename": file.filename, "name":name, "tags":tags, "ratings":[], "rating":0, "grade":grade}
        UploadDictList.append(UploadDict)
    return render_template("upload.html")
