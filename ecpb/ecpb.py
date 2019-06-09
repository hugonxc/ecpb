import sys
import requests 
import json
import clipboard

def copy2clip(txt):
    cmd='echo '+ txt.strip() + '|clip'
    return subprocess.check_call(cmd, shell=True)

if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    option = ''
    iFile = ''
    baseURL = 'http://dontpad.com'

    option = sys.argv[1]

    if option == "send":
        iFile = sys.argv[2] 
        url = sys.argv[3]
        url = baseURL + url

        content = open(iFile, "r")
        data = {"text": content.read()}

        r = requests.post(url, data)

    elif option == "get":
        url = sys.argv[2]
        url = baseURL + url + ".body.json?lastUpdate=0"
        r = requests.get(url)

        content = r.content
        content = json.loads(content.decode())

        if content['body']:
            clipboard.copy(content['body'])
        else:
            print("URL is empty")

    else: 
        print("Don't fool me")
