import sys
def is_palindrome(str):
	s=len(str)
	for i in range(s):
		if str[i] == str[-i]:
			print "{} is palindrome".format(str)
			break
		else:
			print "not palindrome"
			break
is_palindrome(sys.argv[1])