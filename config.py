# ! Basic Settings
Project_Name = "Project-Name"  # Name of the project to be saved
Output_Path = "./output/"  # Output Path for save files

# ! Target Website Settings / Target_List_Setting
Target_URL = "http://example.local/"  # Target Website Url example http://mywebsite.dev/
Target_Login_URL = "http://example.local/login.php"  # Target Website Login Url example http://mywebsite.dev/login/
Target_List_Path = "./lists/Link_List.txt" # Target list path is used for External Broken Links and XSS Testing



# ! Lists Settings for Scanner
Subdomain_List_Path = "./lists/subdomain_list.txt"  # Subdomain List Path
Directories_Files_List_Path = "./lists/directories_files_list.txt"  # Directories and Files List Path

# Dictionary Attack Settings
Input_Name = "username" # Change the name of the input field for Username example <input type="text" name="username">
Input_Password = "password" # Change the name of the input field for Password example <input type="password" name="password">
Username_List_Path = "./lists/user_list.txt" # Username List
Password_List_Path = "./lists/password_list.txt"  # Password List


# !XSS Settings
Testing_Script_Path = "./lists/xss_payload_list.txt" # Testing Scripts Path
