# 使用User-Agent伪装后请求网站
import urllib.request
import os

def get_page():
	url = 'https://www.zhihu.com/'
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
	}
	request = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(request)
	page_source = res.read().decode('utf-8')
	# fp = os.open('test.txt',os.O_CREAT)
	# os.write(fp,str.encode(page_source))
	# os.close(fp)
	print(page_source)


if __name__ == '__main__':
	get_page()
