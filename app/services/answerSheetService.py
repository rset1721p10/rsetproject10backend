from ..db import answersheetCollection,questionPapersCollection,studentDetailsCollection,questionsCollection,classDetailsCollection
from fastapi.encoders import jsonable_encoder

def question_helper(question) -> dict:
    return {
        "qId": question["qId"],
        "question": question["question"],
        "type": question["type"],
        "answer": question["answer"],
        "markDistribution": question["markDistribution"],
        "QtotalMarks" : question["QtotalMarks"]
    }
def questionpaper_helper(question) -> dict:
    return {
        "qpId": question["qpId"],
        "serial": question["serial"],
        "date": question["date"],
        "time": question["time"],
        "duration": question["duration"],
        "questions": question["questions"],
        "marks" : question["marks"],
        "latest" : question["latest"]
    }
def answerSheet_helper(answerSheet) -> dict:
    return {
        "userid": answerSheet["userid"],
        "qpId":answerSheet["qpId"],
        "question": answerSheet["question"],
        "types": answerSheet["types"],
        "entries": answerSheet["entries"],
        "marks": answerSheet["marks"],
        "levelOfUnderstanding1": answerSheet["levelOfUnderstanding1"],
        "levelOfUnderstanding2": answerSheet["levelOfUnderstanding2"],
        "marks1": answerSheet["marks1"],
        "marks2": answerSheet["marks2"],
        "totalMarks" : answerSheet["totalMarks"]
    }
def studentDetails_helper(studentDetails) -> dict:
    return {
        "firstName": studentDetails["firstName"],
        "lastName": studentDetails["lastName"],
        "division": studentDetails["division"],
        "stream": studentDetails["stream"],
        "email": studentDetails["email"],
        "qPaperDetails": studentDetails["qPaperDetails"],
    }   
def classDetails_helper(classDetails) -> dict:
    return {
        "division": classDetails["division"],
        "stream": classDetails["stream"],
        "qPaperDetails": classDetails["qPaperDetails"],
    }

def updateAnswerSheet(AnswerSheet):
    newValues={"$set":AnswerSheet}
    filter = {"userid":AnswerSheet["userid"]}
    answersheetCollection.update_one(filter,newValues)

def updateStudents(studentlist):
    newValues={"$set":studentlist}
    filter = {"email":studentlist["email"]}
    studentDetailsCollection.update_one(filter,newValues)

def updateClass(classlist): 
    newValues={"$set":classlist}
    filter = {"division":classlist["division"]}
    classDetailsCollection.update_one(filter,newValues)

def abbr(l3):                  #function to replace abbreviations
    Abbrev={"Number":["no","No.","No","no.","Number","Num"],"Volume":["V","v","vol","Vol","Volume"],"Hydrogen":["H"],"Helium":["He"],"Lithium":["Li"],"Beryllium":["Be"],"Boron":["B"],"Carbon":["C"],"Nitrogen":["N"],"Oxygen":["O"],"Fluorine":["F"],"Neon":["Ne"],"Sodium":["Na"],"Magnesium":["Mg"],"Aluminium":["Al"],"Silicon":["Si"],"Phosphorus":["P"],"Sulfur":["S"],"Chlorine":["Cl"],"Argon":["Ar"],"Potassium":["K"],"Calcium":["Ca"],"Scandium":["Sc"],"Titanium":["Ti"],"Vanadium":["V"],"Chromium":["Cr"],"Manganese":["Mn"],"Iron":["Fe"],"Cobalt":["Co"],"Nickel":["Ni"],"Copper":["Cu"],"Zinc":["Zn"],"Gallium":["Ga"],"Germanium":["Ge"],"Arsenic":["As"],"Selenium":["Se"],"Bromine":["Br"],"Krypton":["Kr"],"Rubidium":["Rb"],"Strontium":["Sr"] ,"Yttrium":["Y"],"Zirconium":["Zr"],"Niobium":["Nb"],"Molybdenum":["Mo"],"Technetium":["Tc"],"Ruthenium":["Ru"],"Rhodium":["Rh"],"Palladium":["Pd"],"Silver":["Ag"] ,"Cadmium":["Cd"],"Indium":["In"],"Tin":["Sn"],"Antimony":["Sb"],"Tellurium":["Te"],"Iodine":["I"],"Xenon":["Xe"],"Cesium":["Cs"],"Barium":["Ba"],"Lanthanum":["La"],"Cerium":["Ce"],"Praseodymium":["Pr"],"Neodymium":["Nd"],"Promethium":["Pm"],"Samarium":["Sm"],"Europium":["Eu"],"Gadolinium":["Gd"],"Terbium":["Tb"],"Dysprosium":["Dy"],"Holmium":["Ho"],"Erbium":["Er"],"Thulium":["Tm"],"Ytterbium":["Yb"],"Lutetium":["Lu"],"Hafnium":["Hf"],"Tantalum":["Ta"],"Tungsten":["W"],"Rhenium":["Re"],"Osmium":["Os"],"Iridium":["Ir"],"Platinum":["Pt"],"Gold":["Au"],"Mercury":["Hg"],"Thallium":["Tl"],"Lead":["Pb"],"Bismuth":["Bi"],"Polonium":["Po"],"Astatine":["At"],"Radon":["Rn"],"Francium":["Fr"],"Radium":["Ra"],"Actinium":["Ac"],"Thorium":["Th"],"Protactinium":["Pa"],"Uranium":["U"],"Neptunium":["Np"],"Plutonium":["Pu"],"Americium":["Am"],"Curium":["Cm"],"Berkelium":["Bk"],"Californium":["Cf"],"Einsteinium":["Es"],"Fermium":["Fm"],"Mendelevium":["Md"],"Lawrencium":["Lr"],"Rutherfordium":["Rf"],"Dubnium":["Db"],"Seaborgium":["Sg"],"Bohrium":["Bh"],"Hassium":["Hs"],"Meitnerium":["Mt"],"Darmstadtium":["Ds"],"Roentgenium":["Rg"],"Copernicium":["Cn"],"Nihonium":["Nh"],"Flerovium":["Fl"],"Moscovium":["Mc"],"Livermorium":["Lv"],"Tennessine":["Ts"],"Oganesson":["Og"]}
    c=0
    for el in l3:
        for x in Abbrev:
            if el in Abbrev[x]:
                j=l3.index(el)
                l3[j]=x
                break
    return(l3)
def add_answerSheet(answerSheet):
    dbquestionlist = questionsCollection.find()
    dbQuestions=[]
    for i in dbquestionlist:
        dbQuestions.append(question_helper(i))
    #All Questions
    questionPaperSet = questionPapersCollection.find()
    questionPaperlist=[]
    for i in questionPaperSet:
        questionPaperlist.append(questionpaper_helper(i))
    finalQuestionpaper=len(questionPaperlist)-1
    latestQuestionPaper=[]
    latestQuestionPaper.append(questionpaper_helper(questionPaperlist[finalQuestionpaper]))
    dbQuestionPaper=latestQuestionPaper[0]
    #Latest Question Paper
    next_answerSheet = jsonable_encoder(answerSheet)
    #AnswerSheet = answerSheet_helper(answerSheet)
    AnswerSheet = next_answerSheet
    #AnswerSheet is set
    onestudent=studentDetailsCollection.find_one({'email': AnswerSheet['userid']})
    Sdetails=studentDetails_helper(onestudent)
    #Sdetails is set
    oneclass=classDetailsCollection.find_one({'division': Sdetails['division']})
    CDetails=classDetails_helper(oneclass)
    #CDetails is set
    print(dbQuestions)
    print('\n')
    print(dbQuestionPaper)
    print('\n')
    print(AnswerSheet)
    print('\n')
    print(Sdetails)
    print('\n')

    #print





    me=0                                                               #Variable to calculate the total alloted marks for the equation questions
    mn=0                                                               #Variable to calculate the total alloted marks for the numericals questions
    for el in AnswerSheet.get("entries"):

        for el1 in dbQuestions:
            if el1["qId"]==el:
                print(el1["type"])

                if el1["type"]=="Numericals":
                    mn=mn+el1["QtotalMarks"]
                    l1=AnswerSheet["entries"][el]
                    for i in range(len(l1)):
                        l2=l1[i][0].split("=")                               #split line in answer in submitted answer to LHS and RHS
                        l3=l2[0].split(" ")                                  #split LHS into words 
                        l4=el1["answer"][i].split("=")                       #split line in answer in db to LHS and RHS
                        l5=l4[0].split(" ")                                  #split LHS into keywords
                        c=0
                        abbr(l3)                                             #function to replace abbreviations   
                        for q in l5:                                         #Here we check the presence of keywords,if we find a keyword we increment c
                            if q in l3:
                                c=c+1
                        val=0                                                #val is the variable used to store value
                        val1=0                                               #val1 is the variable used to store value
                        if c==len(l5):
                            AnswerSheet["entries"][el][i][1]=AnswerSheet["entries"][el][i][1]+0.25*el1["markDistribution"][i] #if keywords are correct mark is incremented.example here check line 4, changes made during evaluation
                            for j in range(len(l2[1])):
                                if (l2[1][0].isdigit()==True):
                                    for x in range(1,len(l2[1])):
                                        if (l2[1][x].isalpha()==True):
                                            break
                                    val=l2[1][0:x]                        #value in submitted ans            
                                    u=l2[1][x:len(l2[1])+1]               #unit  in submitted ans
                                
                                elif(l2[1][0].isalpha()==True):
                                    kk1=""
                                    for z in range(0,len(l2[1])):
                                        if(l2[1][z])!=" ":
                                            kk1=kk1+l2[1][z]
                                    pp=kk1


                           #equation in submitted ans
                            for j1 in range(len(l4[1])):
                                if (l4[1][0].isdigit()==True):
                                    for x1 in range(1,len(l4[1])):
                                        if (l4[1][x1].isalpha()==True):
                                            break
                                    val1=l4[1][0:x]                         #value in db ans            
                                    u1=l4[1][x1:len(l2[1])+1]               #unit  in db ans
                                
                                elif(l4[1][0].isalpha()==True):
                                    kk=""
                                    for z in range(0,len(l4[1])):
                                        if(l4[1][z])!=" ":
                                            kk=kk+l4[1][z]
                                    pp1=kk
                                
 
                            if(val1!=0):
                                if("." in val1):
                                    if((((abs(float(val1)-float(val)))/float(val1))*100)<=1):   #in case of decimal points 1% error is permitted(optional)
                                        AnswerSheet["entries"][el][i][1]=AnswerSheet["entries"][el][i][1]+(0.5*el1["markDistribution"][i])  #mark changed again if value is correct
                                
                                else:
                                    if(val1==val):                         #
                                        AnswerSheet["entries"][el][i][1]=AnswerSheet["entries"][el][i][1]+(0.5*el1["markDistribution"][i]) #mark changed again if value is correct
                                if(u==u1):
                                    AnswerSheet["entries"][el][i][1]=AnswerSheet["entries"][el][i][1]+(0.25*el1["markDistribution"][i]) #mark changed again if unit is correct
                            elif(pp==pp1):
                                AnswerSheet["entries"][el][i][1]=AnswerSheet["entries"][el][i][1]+(0.75*el1["markDistribution"][i]) #in case of equations
                        AnswerSheet["marks"][el]=AnswerSheet["marks"][el]+AnswerSheet["entries"][el][i][1] #mark of each line added to the total mark of the question
                        print("Mark for line:", AnswerSheet["entries"][el][i][1]) 
                    AnswerSheet["marks2"]=AnswerSheet["marks2"]+AnswerSheet["marks"][el]
                elif(el1["type"]=='Balancing Equations'):
                    me=me+el1["QtotalMarks"]
                    l1=AnswerSheet["entries"][el]

                    for i in range(len(l1)):
                        st=""
                        for b in range(len(l1[i][0])):
                            if (l1[i][0][b]!=" "):
                                st=st+l1[i][0][b]
                        l2=st.split("→")                               #split line in answer in submitted answer to LHS and RHS
                        l2lhs=l2[0].split("+")                               #split LHS of submitted ans into constituent chemical compounds
                        l2rhs=l2[1].split("+") 
                        st1=""
                        for b1 in range(len(el1["answer"][i])):
                            if (el1["answer"][i][b1]!=" "):
                                st1=st1+el1["answer"][i][b1] 
                        print("DB",st1)                                               #split RHS of submitted ans into constituent chemical compounds
                        l3=st1.split("→")                       #split line in answer in db to LHS and RHS
                        l3lhs=l3[0].split("+")                               #split LHS of db answer into constituent chemical compounds
                        l3rhs=l3[1].split("+")                            #split RHS of db answer into constituent chemical compounds
                        c=0
                        if (len(l2lhs)==len(l3lhs)):
                            for k in l2lhs:
                                if k in l3lhs:
                                    c=c+1
                        if c==len(l3lhs):
                            AnswerSheet["entries"][el][i][1]=AnswerSheet["entries"][el][i][1]+(0.5*el1["markDistribution"][i]) #50% mark alloted for correct lhs
                        q=0
                        if (len(l2rhs)==len(l3rhs)):                                                                            
                            for h in l2rhs:
                                if h in l3rhs:
                                    q=q+1
                        if q==len(l3rhs):
                            AnswerSheet["entries"][el][i][1]=AnswerSheet["entries"][el][i][1]+(0.5*el1["markDistribution"][i]) #50% mark alloted for correct lhs
                        AnswerSheet["marks"][el]=AnswerSheet["marks"][el]+AnswerSheet["entries"][el][i][1] #mark of each line added to the total mark of the question
                        print("Mark for line:", AnswerSheet["entries"][el][i][1])                
                    AnswerSheet["marks1"]=AnswerSheet["marks1"]+AnswerSheet["marks"][el]       #Total marks for equations obtained incremented                
            AnswerSheet["totalMarks"]=AnswerSheet["marks1"]+AnswerSheet["marks2"]              #Total marks for the paper
    if me!=0:
        AnswerSheet["levelOfUnderstanding1"]=(AnswerSheet["marks1"]/me)*100
    else:
        print("No questions in question paper from Equations")                        #level of understanding for equations calculated
    if mn!=0:
        AnswerSheet["levelOfUnderstanding2"]=(AnswerSheet["marks2"]/mn)*100  
    else:
        print("No questions in question paper from Numericals")                       #level of understanding for numericals calculated

    if (AnswerSheet["userid"]==Sdetails["email"]):                                             #Compares user id in answersheet and email in student etails
        for i in range((len(Sdetails["qPaperDetails"]))):                                      #Access each dictionary containing details of each exam
                if Sdetails["qPaperDetails"][i]["qPaperId"]==AnswerSheet["qpId"]:
                    Sdetails["qPaperDetails"][i]["sdmarks1"]=AnswerSheet["marks1"]
                    print("AAAAAAAAA",Sdetails["qPaperDetails"][i]["sdmarks1"])
                    Sdetails["qPaperDetails"][i]["sdmarks2"]=AnswerSheet["marks2"]
                    print("BBBBBBBBBBBBBB",Sdetails["qPaperDetails"][i]["sdmarks2"])
                    Sdetails["qPaperDetails"][i]["levelOfUnderstanding1"]=AnswerSheet["levelOfUnderstanding1"]
                    print("CCCCCCCCCCCCCCC",Sdetails["qPaperDetails"][i]["levelOfUnderstanding1"])
                    Sdetails["qPaperDetails"][i]["levelOfUnderstanding2"]=AnswerSheet["levelOfUnderstanding2"]
                    print("DDDDDDDD",Sdetails["qPaperDetails"][i]["levelOfUnderstanding2"])
                    Sdetails["qPaperDetails"][i]["sdtotalMarks"]=AnswerSheet["totalMarks"]
                    print("EEEEEEEEEE",Sdetails["qPaperDetails"][i]["sdtotalMarks"])
                    if (CDetails["division"]==Sdetails["division"]) and (CDetails["stream"]==Sdetails["stream"]):
                        for Celement in CDetails["qPaperDetails"]:
                            if Celement["qPaperId"]==AnswerSheet["qpId"]:
                                tempcel = Celement["studentsAttended"]+1
                                Celement["cdmarks1"]=((Celement["cdmarks1"]+Sdetails["qPaperDetails"][i]["sdmarks1"])/(tempcel))
                                Celement["cdmarks2"]=((Celement["cdmarks2"]+Sdetails["qPaperDetails"][i]["sdmarks2"])/(tempcel))
                                Celement["studentsAttended"]=tempcel
                                print(Celement["studentsAttended"])
    updateClass(CDetails)
    updateStudents(Sdetails)
    #next_answerSheet = jsonable_encoder(AnswerSheet)
    answersheetCollection.insert_one(next_answerSheet)
    return {"data": answerSheet,
            "message": "Answer Sheet added successfully"}

def update_Answersheet(answerSheet):
    dbquestionlist = questionsCollection.find()
    dbQuestions=[]
    for i in dbquestionlist:
        dbQuestions.append(question_helper(i))
    #All Questions
    questionPaperSet = questionPapersCollection.find()
    questionPaperlist=[]
    for i in questionPaperSet:
        questionPaperlist.append(questionpaper_helper(i))
    finalQuestionpaper=len(questionPaperlist)-1
    latestQuestionPaper=[]
    latestQuestionPaper.append(questionpaper_helper(questionPaperlist[finalQuestionpaper]))
    dbQuestionPaper=latestQuestionPaper[0]
    #Latest Question Paper
    next_answerSheet = jsonable_encoder(answerSheet)
    #AnswerSheet = answerSheet_helper(answerSheet)
    Answersheet=next_answerSheet
    #AnswerSheet is set
    onestudent=studentDetailsCollection.find_one({'email': Answersheet['userid']})
    Sdetails=studentDetails_helper(onestudent)
    #Sdetails is set
    oneclass=classDetailsCollection.find_one({'division': Sdetails['division']})
    CDetails=classDetails_helper(oneclass)

    newtotalmarks=0
    marks=Answersheet["marks"]
    for i in Answersheet["marks"]:
        newtotalmarks=newtotalmarks+marks[i]
    Answersheet["totalMarks"]=newtotalmarks
    idealTotalMarks1=0
    achievedTotalMarks1=0
    idealTotalMarks2=0
    achievedTotalMarks2=0
    types=Answersheet["types"]
    for i in Answersheet["question"]:
        if(types[i]=="Balancing Equations"):
            achievedTotalMarks1=achievedTotalMarks1+marks[i]
            for j in dbQuestions:
                if(j["qId"]==i):
                    idealTotalMarks1=idealTotalMarks1+j["QtotalMarks"]
        if(types[i]=="Numericals"):
            achievedTotalMarks2=achievedTotalMarks2+marks[i]
            for j in dbQuestions:
                if(j["qId"]==i):
                    idealTotalMarks2=idealTotalMarks2+j["QtotalMarks"]
    newLOU1=(achievedTotalMarks1/idealTotalMarks1)*100
    newLOU2=(achievedTotalMarks2/idealTotalMarks2)*100
    Answersheet["marks1"]=achievedTotalMarks1
    Answersheet["marks2"]=achievedTotalMarks2
    Answersheet["levelOfUnderstanding1"]=newLOU1
    Answersheet["levelOfUnderstanding2"]=newLOU2
    for i in Sdetails["qPaperDetails"]:
        if(Answersheet["qpId"]==i["qPaperId"]):
            oldsdmarks1=i["sdmarks1"]
            oldsdmarks2=i["sdmarks2"]
            i["levelOfUnderstanding1"]=newLOU1
            i["levelOfUnderstanding2"]=newLOU2
            i["sdmarks1"]=achievedTotalMarks1
            i["sdmarks2"]=achievedTotalMarks2
            i["sdtotalMarks"]=achievedTotalMarks1+achievedTotalMarks2
    for i in CDetails["qPaperDetails"]:
        if(Answersheet["qpId"]==i["qPaperId"]):
            oldcdmarks1=i["cdmarks1"]
            oldcdmarks2=i["cdmarks2"]
            i["cdmarks1"]=((oldcdmarks1*i["studentsAttended"])-oldsdmarks1+achievedTotalMarks1)/i["studentsAttended"]
            i["cdmarks2"]=((oldcdmarks2*i["studentsAttended"])-oldsdmarks2+achievedTotalMarks2)/i["studentsAttended"]
    print(Answersheet)
    print(CDetails)
    print(Sdetails)
    updateAnswerSheet(Answersheet)
    updateClass(CDetails)
    updateStudents(Sdetails)
    return {"data": Answersheet,
            "message": "Answer Sheet updated successfully"}










def get_SingleAnswerSheet(email):
    result=answersheetCollection.find_one({'userid': email})
    return {"data": answerSheet_helper(result)}

def get_answerSheets():
    answerSheetSet = answersheetCollection.find()
    result=[]
    for i in answerSheetSet:
        result.append(answerSheet_helper(i))
    return {"data": result}





