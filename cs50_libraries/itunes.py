import requests
import sys
import json
#If the user does not provide with the name of the file they want to
#run and the name of a band
if len(sys.argv) != 2:
    sys.exit()

#Making a http request using python to the server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
#Grabbing the servers reponse json's object
o = response.json()
for result in o["results"]:
    print(result["trackName"])