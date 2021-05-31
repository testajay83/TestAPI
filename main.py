# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json

base_url = 'https://reqres.in/api/'
#CaseA:
#a) Test the Register API by registering the user successfully using https://reqres.in/api/register and by logging in using the data used for the registration on API https://reqres.in/api/login.
# Pass it only if the user is created and able to login
def test_register():
    api_body = ''
    print(f'Testing register api {base_url}register')
    api_header = {'Content-type':'application/json', 'Accept':'application/json'}
    response = requests.get(url=f'{base_url}register', headers=api_header)
    print(f'Response: {str(response)}')
    print(f'Response json: {str(response.content)}')

def test_userlogin(username):
    print(f'Testing register api {base_url}login')
    api_header = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.get(url=f'{base_url}login', headers=api_header)
    print(f'Response: {str(response)}')
    json_response = response.json()
    users = json_response['data']
    flag = False
    user_detail = {}
    for user in users:
        if user['name'] == username:
            user_detail = user
            flag = True
            break
    if flag:
        print(f'{username} logged in successfully, detail {user_detail}')
    else:
        print(f'{username} is not authorize.')

#Caseb:Using details of the user created in step a,  Delete the user registered above and assert an unsuccessful login attempt on login API https://reqres.in/api/login.
# Pass it only if the user created in Step a is deleted and unable to login
#Answer:We need delete API to execute this case.

#Casec:
# Assert a resource on https://reqres.in/api/unknown where page=1 and ID=2, year=2001
def test_unknown(page, id, year):
    print(f'page: {page}, id {id}, year: {year}')
    print(f'Testing register api {base_url}unknown')
    api_header = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.get(url=f'{base_url}unknown', headers=api_header)
    print(f'Response: {str(response)}')
    json_response = response.json()
    resp_page = json_response['page']
    resp_users = json_response['data']
    flag = False
    user_detail ={}
    for user in resp_users:
        if user['id'] == id and user['year'] == year:
            user_detail = user
            flag = True
            break
    if flag and resp_page == page:
        print(f'Input found in response {user_detail}')
    else:
        print('Input not found in response')
#Cased:
#d) Assert a user on https://reqres.in/api/users?page=2 where the assertion is passed if the payload contains user with ID=7, Lastname =Lawson
def test_user(id,last_name):
    resp = requests.get("https://reqres.in/api/users?page=2")
    assert (resp.status_code == 200)
    #print("str(resp.status_code")
    for record in resp.json()['data']:
        if record['id'] == 7:
            record['last_name'] == 'Lawson'
            print(f'Input found in response {id},{last_name}')
            break
        else:
            print(f'Input not found in response')
#Casee
#e) Assert the payload in API https://reqres.in/api/users/2 where it will check for first_name as "John" and fails the test if it's not "John"
def test_name(first_name):
    resp = requests.get("https://reqres.in/api/users/2")
    assert (resp.status_code == 200)
    if (resp.json()['data']['first_name'])!= first_name:
          print("fail")
    else:
        print("Input Record found")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 test_register()
test_userlogin('ajay')
test_userlogin('cerulean')
test_unknown(1, 2, 2001)
test_user(7, 'Lawson')
test_name('Janet')

