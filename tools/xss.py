from bs4 import BeautifulSoup
import mechanize
import config as Config
import tools.helper as Helper

Link_List = open(Config.Target_List_Path, 'r', encoding='utf8').readlines()
Testing_Scripts = open(Config.Testing_Script_Path, 'r', encoding='utf8').readlines()

br = mechanize.Browser()
br.set_handle_robots(False)

# Cross Site Scripting Search
def XSS_Search():
    xss_possibility = []
    link_counter = 1
    link_list_sum = len(Link_List)
    for single_link in Link_List:
        #try connection
        try:
            response = br.open(single_link.strip())
        except:
            pass
        form_data = extract_form(response.read())
        # check form data
        if form_data['form_name'] == None or len(form_data['input_names']) == 0:
            print(f"Status: {link_counter}/{link_list_sum} No Form Name or Input Found in {single_link.strip()} - skip testing")
        else:
            for single_xss_script in Testing_Scripts:
                xss_result = test_form_of_xss(target_url=single_link, form_data=form_data, script=single_xss_script,
                                              link_counter=link_counter, links_sum=link_list_sum)
                xss_possibility.append(xss_result.strip())
        link_counter += 1
    # check xss possibility array
    if len(xss_possibility) == 0:
        print("No XSS possibilities found")
    else:
        Helper.save_result_as_text_file(result=xss_possibility, method="XSS_Testing")

# ectract form form web content
def extract_form(content):
    content_html = BeautifulSoup(content, 'html.parser')
    html_form = content_html.find('form')
    #check html form
    if html_form == None:
        return {"form_name": None, "input_names": None}
    else:
        form_name = html_form['name'] if html_form.has_attr('name') else None
        field_names = []
        input_list = html_form.select('form input')
        textarea_list = html_form.select('form textarea')
        for single_input in input_list:
            if single_input.has_attr('name') and single_input.get("type") == "text":
                field_names.append(single_input.get("name"))
        for single_textarea in textarea_list:
            if single_textarea.has_attr('name'):
                field_names.append(single_textarea.get("name"))
        return {"form_name": form_name, "input_names": field_names}

# test form of Cross Site Scripting
def test_form_of_xss(target_url, form_data, script, link_counter, links_sum):
    print(f"Status: {link_counter}/{links_sum} -> Testing: {target_url}".strip())
    br.open(target_url)
    if form_data['form_name'] != None:
        br.select_form(form_data['form_name'])
    else:
        br.select_form(nr=0)
    input_names = form_data['input_names']
    br.form[input_names[0]] = script
    for i in range(1, len(input_names)):
        br.form[input_names[i]] = "Testing XSS"
    br.submit()
    finalResult = br.response().read()
    Data = None
    # Checks the content for the test script
    if finalResult.find(script.encode()):
        print(f"xss possibility found: {br.geturl()} | Tested Script: {script}".strip())
        Data = br.geturl() + f" found xss possibility Tested Script: {script}".strip()
    else:
        print(f"No xss possibility Found: {br.geturl()}")
    return Data
