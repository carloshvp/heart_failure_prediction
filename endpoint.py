import requests
import json

# URL for the web service, should be similar to:
# 'http://17fb482f-c5d8-4df7-b011-9b33e860c111.southcentralus.azurecontainer.io/score'
scoring_uri = 'http://078ed0c5-0bd9-4dd3-9462-ad425f0827ba.southcentralus.azurecontainer.io/score'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "age": 50,
            "anaemia": 0,
            "creatinine_phosphokinase": 318,
            "diabetes": 0,
            "ejection_fraction": 40,
            "high_blood_pressure": 1,
            "platelets": 216000,
            "serum_creatinine": 2.3,
            "serum_sodium": 131,
            "sex": 0,
            "smoking": 0,
            "time": 60
          },
          {
            "age": 55,
            "anaemia": 0,
            "creatinine_phosphokinase": 109,
            "diabetes": 0,
            "ejection_fraction": 35,
            "high_blood_pressure": 0,
            "platelets": 254000,
            "serum_creatinine": 1.1,
            "serum_sodium": 139,
            "sex": 1,
            "smoking": 1,
            "time": 60
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


