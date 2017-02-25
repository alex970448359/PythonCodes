import sys
from curl import curl

DOMAIN =   [
			]

"""
	for domain in DOMAIN:
		result = eval(curl('GET', 'http://www.kuaizhan.com/site/ajax-check-domain?domain=' + domain + '&site_id=5810593358', 'gr_user_id=277ac672-e0e9-476c-82f0-03071848a98c; KUAIZHAN=9gp07m14uuj43cv0a193ac1q74; email=18811464633; device_id=7Q5ly0Oo; KUAIZHAN_V2=54421%7C1487323213%7C8733324462%7Cabcbb8c621c0d6ed48b020f6707941c6a208af11; uid=226258588.392592213.1485613781477.1487323214629.1487323217951.73; gr_session_id_994a7a3e1f7a9f57=a796256a-b03c-4121-97dd-3ec8c30483a8; sid=226258588.618140784.1487323199467.1487323245261', ('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',)))
		if result["msg"] == "":
			print domain
"""
	
if __name__ == '__main__':
	print curl('GET', 'http://weibo.com/1663418681/fans', '', ('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',));
