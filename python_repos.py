import requests

# make a api calls

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

print("Status code:", r.status_code)

# store the api request into a variable

response_dict = r.json()

# Show the results

print(response_dict.keys())