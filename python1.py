import sys
try:
	email=sys.argv[1]
except IndexError:
	print "please provide an input"
	exit()
email='jismy@fullcontact.com'
print email[email.find('@')+1:email.find('.com')]
print email[:email.find('@')]
domain=email[email.find('@')+1:email.find('.com')]
username=email[:email.find('@')]
print 'username:',username
print 'domain:',domain
print"{} is the user name".format(username)