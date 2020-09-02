import requests

text = """Drought increases regional insecurity."""

webservice = 'http://localhost:9000/process_text'
res = requests.post(webservice, 
    headers={'Content-type': 'application/json'}, 
    json={'text': text})


json_dict = res.json()
print(json_dict)