import joblib
import pandas as pd
import numpy as np
import re
model=joblib.load(r"C:\Users\MOHANKUMAR\PROJECTS\Machine Learning\career-guidance-tool\website\careertool\model1.joblib")
def eprediction(circuit_design,control_systems,power_electronics,analog_communication,r_f,cpp,electrical_system,cad,pcb,labview):
    
        epred = pd.DataFrame({
            'CIRCUIT DESIGN': [circuit_design],
            'CONTROL SYSTEMS': [control_systems],
            'POWER ELECTRONICS':[power_electronics],    
            'ANALOG COMMUNICATION':[analog_communication],
            'RF':[r_f],
            'C++':[cpp],
            'ELECTRICAL SYSTEM':[electrical_system],
            'CAD':[cad],
            'PCB':[pcb],
            'LABVIEW':[labview]},index=[0])
        predict1 = model.predict(epred)
        ans = np.array(predict1)
        print("".join(map(str, ans)))
        return ans
model1=joblib.load(r"C:\Users\MOHANKUMAR\PROJECTS\Machine Learning\career-guidance-tool\website\careertool\model2.joblib")
def cprediction(data_base,c_architecture,cyber_security,networking,software_development,ai_ml, graphics_designer,data_science):
        cpred = pd.DataFrame({
            'DATABASE': [data_base],
            'Computer Architecture': [c_architecture],
            'Cyber Security':[cyber_security],    
            'Networking':[networking],
            'Software Development':[software_development],
            'AI ML':[ai_ml],
            'Data Science':[graphics_designer],
            'Graphics Design':[data_science],},index=[0])
        predict1 = model1.predict(cpred)
        ans = np.array(predict1)
        print("".join(map(str, ans)))
        return ans
def send(lst):
        a = eprediction(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9])
        return a
def sendcs(clst):
        a = cprediction(clst[0],clst[1],clst[2],clst[3],clst[4],clst[5],clst[6],clst[7])
        return a

def numberofwords(pattern, search_words,df):
    s1 = df['title'].str.count(pattern, flags=re.IGNORECASE).sum()
    s2 = df['url'].str.count(pattern, flags=re.IGNORECASE).sum()
    print(f"Number of matches for {', '.join(search_words)}: {s2}")
    return s1 + s2

def get(history_data):
    df = pd.DataFrame(history_data)
    cs = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "MachineLearning",
    "Ruby",
    "Kotlin",
    "Merge Sort",
    "Quick Sort",
    "Linked List",
    "Hash Table",
    "ArtificialIntelligence",
    "Big Data",
    "stackoverflow",
    "technology",
    "tech",
    "OperatingSystems",
    "Databases",
    "Computer Networks",
    "VisualStudio Code",
    "Git",
    "Github"
    "Django",
    "web",
    "React",
    "TensorFlow",
    "NumPy",
    "Pandas",
    "Coursera",
    "edX",
    "Udacity",
    "Khan Academy",
    "Debugging Techniques",
    "Problem Solving Strategies",
    "Segmentation Fault",
    "Resume Building for Computer Science",
    "Job Interview Tips for Programmers",
    "Internship Opportunities",
    ]

    electronics = [
    "Electronics",
    "Circuit",
    "Microcontroller",
    "Arduino",
    "Raspberry Pi",
    "Digital Signal Processing",
    "Analog Electronics",
    "Electronic Components",
    "Amplifier",
    "Transistor",
    "Voltage",
    "Current",
    "Semiconductor",
    "Oscilloscope",
    "Multimeter",
    "PCB Design",
    "Embedded Systems",
    "Power Electronics",
    "Sensor",
    "Robotics",
    "Communication Systems",
    "Signal Processing",
    "Electronic Projects",
    "Electronic Tutorials",
    ]
    a = '|'.join(electronics)
    f1 = numberofwords(a, electronics,df)
    pattern = '|'.join(re.escape(word) for word in cs)
    f2 = numberofwords(pattern, cs,df)
    if(f1>f2):
        print("electronics")
        return 0
    else:
        print("CS")
        
        
        return 1
def cse(history_data):
      df = pd.DataFrame(history_data)
      database = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(database)
      one = numberofwords(a,database,df)
      computerarchitecture = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(computerarchitecture)
      two = numberofwords(a,computerarchitecture,df)
      cybersecurity = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(cybersecurity)
      three = numberofwords(a,cybersecurity,df)
      networking = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(networking)
      four = numberofwords(a,networking,df)
      softwaredv = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(softwaredv)
      five = numberofwords(a,softwaredv,df)
      aiml = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(aiml)
      six = numberofwords(a,aiml,df)
      datascience = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(datascience)
      seven = numberofwords(a,datascience,df)
      graphicdesgin = ["SQL",   "NoSQL",        "MySQL",        "PostgreSQL",        "MongoDB",        "SQLite","Database design",        "Data modeling",      "Database management",
        "Relational databases",        "Non-relational databases",        "Database normalization",        "Indexing",        "ACID properties",       "Transactions",
        "Big data",        "Data warehousing","Database security",        "Data migration",        "Data backup and recovery"]
      

      a = '|'.join(graphicdesgin)
      eight = numberofwords(a,graphicdesgin,df)
      max = 0
      if one>max:
            max = one
      if two>max:
            max = two
      if three>max:
            max = three
      if four>max:
            max = four
      if five>max:
            max = five
      if six>max:
            max = six
      if seven>max:
            max = seven
      if eight>max:
            max = eight

      print(max)
      print("Foo")

      return one
def topfive(list):
     a = loop() 
          
def loop(a):
      
      int_list = [int(item.strip('[]')) for item in a]
      print(int_list)
      a = arrange_repeated_first(int_list)
      print(int_list)
      return a
def arrange_repeated_first(lst):
    seen = set()
    repeated = []
    result = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
        else:
            repeated.append(item)

    print(repeated + result)
    a = remove_duplicates(repeated+result)
    return a
def remove_duplicates(lst):
    unique_items = []
    result = []

    for item in lst:
        if item not in unique_items:
            unique_items.append(item)
            result.append(item)

    print(result)
    return result


      
    
      
    
     






