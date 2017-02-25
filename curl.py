import sys
import pycurl
import StringIO

"""
	method:	GET/POST
	url:
	cookie:
	header: an array like ()
"""
def curl(method, url, cookie, header):
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, url)
	curl.setopt(pycurl.COOKIE, cookie)
	curl.setopt(pycurl.HTTPHEADER, header)
	
	string_out = StringIO.StringIO()
	curl.setopt(pycurl.WRITEFUNCTION, string_out.write) #redefine output
	curl.perform()
	return string_out.getvalue()




#for i in range (1, len(sys.argv)):
#print "name file : ", sys.argv[0]
