import requests
import tools.helper as Helper
import config as Config

Target_URL = Config.Target_URL
Subdomain_List = open(Config.Subdomain_List_Path, 'r', encoding='utf8')
Directories_Files_List = open(Config.Directories_Files_List_Path, 'r', encoding='utf8').readlines()


# # Subdomain Scanner: Search for Subdomain in the target URL [www/mail/admin ...]
def Search_Subdomains():
    Subdomain_Data = set()
    protokoll_type = Helper.is_http_or_https(Target_URL)
    target_url = Target_URL.split(str(protokoll_type))
    for single_subdomain in Subdomain_List:
        test_subdomain = single_subdomain.strip()
        test_url = f"{protokoll_type}{test_subdomain}.{target_url[1]}"
        print('Testing:' + test_url)
        response = None
        # try connection
        try:
            response = requests.get(test_url)
        except requests.exceptions.ConnectionError:
            pass
        if response is not None and response.status_code == 200:
            print(f" -> subdomain discovered: {test_url}")
            Subdomain_Data.add(test_url)
    if len(Subdomain_Data) == 0:
        print("No Subdomains Found")
    else:
        Helper.save_result_as_text_file(result=Subdomain_Data, method="subdomain_scan")


# Directories and Files Scanner: Search for directories and files in the target URL
def Search_Directories_and_Files():
    Directories_Files_Data = set()
    protokoll_type = Helper.is_http_or_https(Target_URL)
    target_url = Target_URL.split(str(protokoll_type))
    dir_file_sum = len(Directories_Files_List)
    dir_file_counter = 1
    for single_item in Directories_Files_List:
        test_url = f"{protokoll_type}{target_url[1]}{single_item.strip()}"
        print(f'Status {dir_file_counter}/{dir_file_sum} | Testing:' + test_url)
        response = requests.get(test_url)
        # check url and status code
        if response.url == test_url and response.status_code == 200:
            print(f" -> Status:{response.status_code} Directory or File discovered: {test_url}")
            Directories_Files_Data.add(test_url)
        dir_file_counter += 1
    # check Directories and Files Data
    if len(Directories_Files_Data) == 0:
        print("No Directories and Files Found")
    else:
        Helper.save_result_as_text_file(result=Directories_Files_Data, method="directories_files_scan")
