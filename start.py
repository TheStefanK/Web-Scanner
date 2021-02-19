import os
import time

import config as Config
import tools.scanner as Scanner
import tools.finder as Finder
import tools.xss as XSS
import tools.helper as Helper
import tools.attack as Attack

# Create Output Folder if not exists
if not os.path.exists("./output"):
    os.makedirs("./output")
    print("directory: -- output -- created")


# ! Menu Options
def Menu():
    print("""
    1) Scan Subdomain [search for subdomains]
    2) Scan Directories & Files [search for Directories and Files]
    3) Find Links [Internal, External, Broken]
    4) Find Broken Links from Target_List
    5) Find Comments 
    6) Dictionary Attack [Login Form]
    7) XSS Testing [XSS Form|stored|reflected]
    
    """)
    return input("Please Enter Testing Mode: ")


# input result
result = Menu()

# Subdomain Scanner: search for subdomain from Target URL
if result == "1":
    Start_Time = time.time()
    Start_Date = time.ctime()
    Scanner.Search_Subdomains()
    End_Time = time.time()
    End_Date = time.ctime()
    print(Start_Date)
    print(End_Date)
    print("Time:", End_Time - Start_Time, "seconds")

# Directories and File Scanner: search for Directories and File from Target URL
if result == "2":
    Start_Time = time.time()
    Start_Date = time.ctime()
    Scanner.Search_Directories_and_Files()
    End_Time = time.time()
    End_Date = time.ctime()
    print(Start_Date)
    print(End_Date)
    print("Time:", End_Time - Start_Time, "seconds")

# Link Finder: search for Links from Target URL [Internal, External, Broken]
if result == "3":
    Start_Time = time.time()
    Start_Date = time.ctime()
    result = Finder.Search_Links(url=Config.Target_URL)
    if len(result["Internal_Links"]):
        Helper.save_result_as_text_file(result=result["Internal_Links"], method="Internal_Links")
    if len(result["External_Links"]):
        Helper.save_result_as_text_file(result=result["External_Links"], method="External_Links")
    if len(result["Broken_Links"]):
        Helper.save_result_as_text_file(result=result["Broken_Links"], method="Broken_Links")
    End_Time = time.time()
    End_Date = time.ctime()
    print(Start_Date)
    print(End_Date)
    print("Time:", End_Time - Start_Time, "seconds")

# Broken Link Finder From List
if result == "4":
    Start_Time = time.time()
    Start_Date = time.ctime()
    Finder.Test_Broken_Links_from_List()
    End_Time = time.time()
    End_Date = time.ctime()
    print(Start_Date)
    print(End_Date)
    print("Time:", End_Time - Start_Time, "seconds")

# Find Comments
if result == "5":
    Start_Time = time.time()
    Start_Date = time.ctime()
    Finder.Search_Comments(url=Config.Target_URL)
    End_Time = time.time()
    End_Date = time.ctime()
    print(Start_Date)
    print(End_Date)
    print("Time:", End_Time - Start_Time, "seconds")

# Dictionary Attack (Login Form)
if result == "6":
    Start_Time = time.time()
    Start_Date = time.ctime()
    result = Attack.Dictionary_Attack()
    End_Time = time.time()
    End_Date = time.ctime()
    print(Start_Date)
    print(End_Date)
    print("Time:", End_Time - Start_Time, "seconds")

# XSS Finder
if result == "7":
    Start_Time = time.time()
    Start_Date = time.ctime()
    XSS.XSS_Search()
    End_Time = time.time()
    End_Date = time.ctime()
    print(Start_Date)
    print(End_Date)
    print("Time:", End_Time - Start_Time, "seconds")
