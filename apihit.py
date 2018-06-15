from sys import argv
import requests
api_key="luN3c4FF1bBKqx7qk7fF2nVGGz8klDzy"
def get_person_data(api_key, email):
    url = "https://api.fullcontact.com/v3/person.enrich"
    headers = {
        "Authorization":"Bearer {}".format(api_key)
    }
    data = {
        "email": email
    }
    r = requests.post(url=url, headers=headers, json=data)
    return r.json()

if __name__ == "__main__":
    email = argv[1]
    print get_person_data(api_key, email)
