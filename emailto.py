import sys
def email_to_username(email):
	username=email[:email.find('@')]
	return username

def email_to_domain(email):
	domain=email[email.find('@')+1:]
	return domain
print email_to_username(email=sys.argv[1])
print email_to_domain(email=sys.argv[1])


