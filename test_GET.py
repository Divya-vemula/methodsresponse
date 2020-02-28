import requests

def test_get_employees_check_status_code_equals_200():
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    assert response.status_code == 200
    print(response)



