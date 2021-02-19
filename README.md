# Web-Scanner
Web Scanner, collects information from a website and searches for vulnerabilities





## install

1| install Python Download: https://www.python.org/

2| Create virtual environment (*optional)

3| install requirements with the command:


    pip install -r requirements.txt
    
4| Open config.py and change the setting for your project   

    Project_Name = "MyWebsite" #Your Project Name
    Output_Path = "./output/"  #Your Output Path for save files

    Target_URL = "http://mywebsite.local/"  #Your Project URL
    Target_Login_URL = "http://dvwa.local/login.php"  #Your Project Login URL
5| Start the script

    python start.py
    or
    python3 start.py  


    
## Menu
The scanner has the following functions
  1) Scan Subdomain [search for subdomains]
  2) Scan Directories & Files [search for Directories and Files]
  3) Find Links [Internal, External, Broken]
  4) Find Broken Links from Target_List
  5) Find Comments
  6) Dictionary Attack [Login Form]
  7) XSS Testing [XSS Form|stored|reflected]

 
