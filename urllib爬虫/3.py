# 基于urllib库的POST请求，并用cookie保持会话
import urllib.request
import urllib.parse

def get_page():
	url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LcN2z'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
	}
	data = {
		'username':'StrivePy',
		'password':'XXX'
	}
	postdata = urllib.parse.urlencode(data).encode('utf-8')
	req = urllib.request.Request(url=url,data=postdata,headers=headers)
	res = urllib.request.urlopen(req)
	page_source = res.read().decode('gbk')
	print(page_source)

	url1 = 'http://bbs.chinaunix.net/thread-4263876-1-1.html'
	res1 = urllib.request.urlopen(url=url1)
	page_source1 = res1.read().decode('gdk')
	print(page_source1)
if __name__ == '__main__':
	get_page()