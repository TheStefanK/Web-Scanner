from datetime import datetime
import os
import config as Config

Save_Path = Config.Output_Path
Project_Name = Config.Project_Name


# Get Protokoll Type [http:// or https://]
def is_http_or_https(target_url):
    if "https://" in target_url:
        return "https://"
    if "http://" in target_url:
        return "http://"


#  Save result as text file
def save_result_as_text_file(result, method):
    output_path = Save_Path + Project_Name
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"directory: -- {Project_Name} -- created")
    created_time = str(datetime.now())
    file_path = output_path + '/' + Project_Name + '_' + method + '_' + created_time.replace(":", "_") + '.txt'
    file = open(file_path, 'a+', encoding='utf-8')
    for x in result:
        file.write(str(x) + "\n")
    print("Done! File save -->", file_path)


# save Account data
def save_account_data_as_text_file(account_name, password):
    created_time = str(datetime.now())
    file_path = Save_Path + Project_Name + '_Account_' + created_time.replace(":", "_") + '.txt'
    file = open(file_path, 'a+')
    print("Account Found")
    print('Account Data \n Username:', account_name, 'Password:', password)
    file.write('account-name:' + str(account_name))
    file.write('account-password:' + str(password) + "\n")
    print("Done! File save -->", file_path)


# Dict append Value
def dict_append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value




