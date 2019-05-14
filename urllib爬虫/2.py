# 使用User-Agent伪装后请求网站
import urllib.request


def get_page():
	url = 'http://www.baidu.com'
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
	}
	request = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(request)
	page_source = res.read().decode('utf-8')
	print(page_source)


if __name__ == '__main__':
	get_page()
