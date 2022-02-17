import os
# Use the package we installed
from slack_bolt import App
import re
import requests
import json


# Initializes your app with your bot token and signing secret
app = App(
    token="xoxb-694445403205-1307989234645-ksLPh7LtPyWrC4J3Bs3WmPQX",
    signing_secret="c97587b07ab3591fcfb95520e33969bd"
)

# Add functionality here
# @app.event("app_home_opened") etc

@app.event("message")
def handle_message_events(body, logger,say):
    
    question = body["event"]["text"]
    
    url = "https://wikibot1.azurewebsites.net/qnamaker/knowledgebases/5be741d0-9680-4d54-b1cb-3c34e7272538/generateAnswer"
    payload = json.dumps({'question': str(question)})
    headers = {
    'Authorization': 'EndpointKey 0070275e-e5e4-44da-a5bb-4702df2ff482',
    'Content-type': 'application/json',
        }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    data = response.json()
    print(data)
    output = data["answers"][0]["answer"]
  
    
    say(str(output))

    
        
    
# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))