import requests
import pytest
# 
API URL
def test_delect_employees_check_status_code_equals_204():
 url = "https://reqres.in/api/users/2"

 response = requests.delete(url)

 #fetch response code

 print(response.status_code)

 assert response.status_code==204