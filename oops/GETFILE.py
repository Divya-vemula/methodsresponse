import requests

# API URL

url = "https://reqres.in/api/users?page=2"


# send get request

response=requests.get(url)

# display content
print(response.content)



