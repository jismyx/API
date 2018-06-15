import requests
email_list = [
"anubhav.yadav@fullcontact.com",
"aswani@fullcontact.com",
"sruthi.soman@fullcontact.com",
"aiswarya@fullcontact.com",
"sruthy@fullcontact.com",
"sivapriya@fullcontact.com",
"ramseena.pa@fullcontact.com",
"amitha.chalappuram@fullcontact.com",
"jismy@fullcontact.com",
"jidhu@fullcontact.com",
"anu@fullcontact.com",
"bimsha@fullcontact.com",
"haritha@fullcontact.com"
]
api_key = "luN3c4FF1bBKqx7qk7fF2nVGGz8klDzy"

def get_person_data_list(api_key,email_list):
               person_data=[]
               for email in email_list:
                  d = get_person_data(api_key,email)
                  person_data.append(d)
               print person_data

def get_person_data(api_key, email):
   url = "https://api.fullcontact.com/v3/person.enrich"
   headers = { "Authorization" : "Bearer {}".format(api_key) }
   data = {"email": email}
   r = requests.post(url=url, headers=headers, json=data)
   if r.status_code != 200:
       return None
   return r.json()

s=get_person_data_list(api_key,email_list)
print s