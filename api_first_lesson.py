import requests


def main() -> None:
    url_template = 'http://wttr.dvmn.org/{}'
    lst = [{'location': 'svo', 'params': ''}, {'location': 'london', 'params': ''}, {'location': 'Cherepovets', 'params': {"MnqT": "","lang": "ru"}}]

    for place in lst:
        response = requests.get(url_template.format(place['location']), params=place['params'])
        try: 
            response.raise_for_status()
            print(response.text)
        except:
            print(response.status_code)
    
if __name__ == '__main__':
    main()