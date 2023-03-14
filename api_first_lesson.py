import requests


url_template = 'http://wttr.dvmn.org/{}'
params = {"MnqT": "","lang": "ru"}

response_svo = requests.get(url_template.format('svo'))
response_london = requests.get(url_template.format('london'))
response_cherep = requests.get(url_template.format('Cherepovets'), params = params)

print(response_svo.text)
print(response_london.text)
print(response_cherep.text)