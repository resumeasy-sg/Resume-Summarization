import requests
import json
import wikipedia as wp
import pandas as pd
from pandas import json_normalize
import re

def skills_list_extraction():
    auth_endpoint = "https://auth.emsicloud.com/connect/token"  # auth endpoint

    client_id = "r6tueqfc2eglnvbh"
    client_secret = "41QN7WBO"
    scope = "emsi_open"

    payload = "client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials&scope=" + scope  # set credentials and scope
    headers = {'content-type': 'application/x-www-form-urlencoded'}  # headers for the response
    access_token = json.loads((requests.request("POST", auth_endpoint, data=payload, headers=headers)).text)[
        'access_token']  # grabs request's text and loads as JSON, then pulls the access token from that

    def extract_skills_list():
        all_skills_endpoint = "https://emsiservices.com/skills/versions/latest/skills"  # List of all skills endpoint
        auth = "Authorization: Bearer " + access_token  # Auth string including access token from above
        headers = {'authorization': auth}  # headers
        response = requests.request("GET", all_skills_endpoint, headers=headers)  # response
        response = response.json()['data']  # the data

        all_skills_df = pd.DataFrame(
            json_normalize(response));  # Where response is a JSON object drilled down to the level of 'data' key
        return all_skills_df

    skills_dataset = extract_skills_list()
    skills_dataset['name'] = skills_dataset['name'].str.lower()
    skills_dataset['name'] = skills_dataset['name'].apply(lambda x: re.sub("\(.*\)", "", x))
    skills_dataset['name'] = skills_dataset['name'].apply(lambda x: re.sub(' +', ' ', x))
    skills_dataset['name'] = skills_dataset['name'].apply(lambda x: x.strip())
    skills_list = list(skills_dataset['name'])
    return skills_list