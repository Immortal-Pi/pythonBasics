import requests
import sys
import json
def packagesExperiment(arg1):

    if len(sys.argv)!=2:
        sys.exit()
    else:
        # print(arg1[1])
        response=requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+arg1[1])
        # print(response.json())
        # print(json.dumps(response.json(), indent=2)) # format json object so its readable
        iterateJson=response.json()

        for song in iterateJson["results"]:
            print(song['trackName'])
    return

