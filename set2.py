from sys import argv
import requests
email=argv[1]
api_key='aE3m3DpSVjr6szt8uODJMvqvyIZxEa4c'
url="https://api.fullcontact.com/v3/person.enrich"
headers={
		"Authorization":"Bearer{}".format(api_key)
}
data = {
	"email":email

}
r=requests.post(url=url,headers=headers,json=data)
print r.json()