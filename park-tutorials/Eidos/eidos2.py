import requests

text = """The pandemic of obesity, type 2 diabetes mellitus (T2DM) and nonalcoholic fatty liver disease (NAFLD) has frequently been associated with dietary intake of saturated fats (1) and specifically with dietary palm oil (PO) (2)."""

webservice = 'http://localhost:9000/process_text'
res = requests.post(webservice, 
    headers={'Content-type': 'application/json'}, 
    json={'text': text})


json_dict = res.json()
print(json_dict)