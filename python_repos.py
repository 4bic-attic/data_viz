import requests

#make API call and store the responce
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

#store API responce in a variable
responce_dict = r.json()

#process results
print(responce_dict.keys())
