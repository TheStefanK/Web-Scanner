import requests
import urllib.parse as urlparse
from bs4 import BeautifulSoup, Comment
import tools.helper as Helper
import config as Config

# Config Settings
Target_URL = Config.Target_URL
Target_Link_List = open(Config.Target_List_Path, 'r', encoding='utf8')

# Sets for Link categories
Internal_Links = set()
Broken_Links = set()
External_Links = set()


def Search_Links(url):
    Link_List = []
    response = requests.get(url=url)
    # check response
    if response is not None and response.status_code == 200:
        print(f"Collect links from: {url}")
        content = BeautifulSoup(response.content, 'html.parser')
        href_tags = content.find_all(href=True)
        Link_List = [tag.get('href') for tag in href_tags]
    else:
        Broken_Links.add(url)

    for single_link in Link_List:
        test_link = urlparse.urljoin(url, single_link)
        if "#" in test_link:
            test_link = test_link.split("#")[0]
        # check internal url
        if Target_URL in test_link and test_link not in Internal_Links:
            Internal_Links.add(test_link)
            Search_Links(test_link)
        # check external Url
        if Target_URL not in test_link and test_link not in External_Links:
            External_Links.add(test_link)
    result = {"Internal_Links": Internal_Links,
              "External_Links": External_Links,
              "Broken_Links": Broken_Links
              }
    return result

# Test Broken Link from list
def Test_Broken_Links_from_List():
    for single_link in Target_Link_List:
        single_link = single_link.strip()
        print(f"Testing: {single_link}")
        response = None
        session = requests.session()
        # try connection
        try:
            response = session.get(single_link)
        except requests.exceptions.RequestException:
            pass
        # check response
        if response == None or response.status_code != 200 and response.url == single_link :
            print(f"-> Broken Link: {single_link}")
            Broken_Links.add(single_link)
        else:
            print(f"Status: {response.status_code} - {single_link}")
    if Broken_Links:
        Helper.save_result_as_text_file(result=Broken_Links, method="Target_List__Broken_Links")


Comment_List = []

# Search Comment
def Search_Comments(url):
    Internal_Links_List = Search_Links(url)
    Link_List_Sum = len(Internal_Links)
    Counter = 1
    for single_link in Internal_Links_List["Internal_Links"]:
        response = requests.get(single_link)
        print(f"Status: {Counter} / {Link_List_Sum} currently url: {single_link}")
        # check status code
        if response.status_code == 200:
            content = BeautifulSoup(response.content, 'html.parser')
            omments_countent = content.find_all(text=is_comment)
            for element in omments_countent:
                text = f'{response.url} --> Comment Found:{element}'
                Comment_List.append(text)

        Counter +=1
    # check comments list
    if len(Comment_List) == 0:
        print("No Comments Found")
    else:
        Helper.save_result_as_text_file(result=sorted(Comment_List), method="Find_Comments")

# is comment
def is_comment(element):
    return isinstance(element, Comment)
