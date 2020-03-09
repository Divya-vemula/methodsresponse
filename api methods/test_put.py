import requests
import pytest
def test_put_data():
 url = "http://jsonplaceholder.typicode.com/posts/1"
 payload = "{\"id\": \"1\", \"title\": \"foo\", \"userId\": \"1\"}"

 headers={
 "Content-Type": "application/json"
 }

 response = requests.request("put", url, headers=headers, data = payload)

 print(response.text)

 print(response.status_code)