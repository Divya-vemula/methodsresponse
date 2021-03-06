import requests
import pytest
def test_post_data():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = "{\"name\":\"test\",\"salary\":\"123\",\"age\":\"23\"}"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)