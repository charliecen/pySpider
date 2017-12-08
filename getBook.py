# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import requests
from bs4 import BeautifulSoup


driver = webdriver.Chrome('./chromedriver')
driver.get('http://book.zongheng.com/')
# assert u'纵横中文网' in driver.title

# 输入下载的书名
bookName = raw_input("请输入你要下载的书名：")
bookName = bookName.decode('utf8')

# 输入框
elem = driver.find_element_by_name('keyword')

# 模拟键盘输入
elem.send_keys(bookName)

# 模拟键盘回车
elem.send_keys(Keys.RETURN)

# 切换新窗口
driver.switch_to.window(driver.window_handles[1])

# 获取网页元素
info = driver.page_source

# 正则匹配,获取url
p = r'<a href="(.*?)" target="(.*?)"><span class="fred"'

result = re.findall(p, info)

# 获取书名
soup = BeautifulSoup(info, 'lxml')

book_name = soup.find_all(class_='search_text')[0].find_all('h2')[0].text

# 判断书名是否匹配正确,并获取书籍URL
if result:
	if book_name == bookName:
		url = soup.find_all(class_='search_text')[0].find_all('a')[0].get('href')
	else:
		print '小说未找到'
		exit()

# 打开书籍URL
driver.get(url)

# 获取网页元素
info = driver.page_source

soup = BeautifulSoup(info, 'lxml')

# 获取目录url
dir_url = soup.find_all(class_="btn_dl")[0].get('href')

# 新页面查看目录
check_dir = driver.find_element_by_class_name('btn_dl')

# 打开目录页
check_dir.click()

# 根据url获取所有章节的url
all_urls = []
html = requests.get(dir_url)
soup = BeautifulSoup(html.text, 'lxml')
all_td = soup.find_all('td', class_="chapterBean")
for a in all_td:
	all_urls.append(a.find('a').get('href'))

# 获取html
def get_html(section_url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
	}
	html = requests.get(section_url, headers=headers)
	return html

# 获取所有内容
for each in all_urls:
	soup = BeautifulSoup(get_html(each).text, 'lxml')
	# 获取卷名
	juan_name = soup.select('#reader_width #uiViewPanel #uiContentPanel h3')[0].text

	# 获取章节标题
	title = soup.find('em', itemprop="headline").text.encode('utf8')

	# 获取章节内容
	all_info = soup.select('#readerFs')[0].encode('utf8')

	re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)
	
	# 删除无用字符串
	content = re_script.sub('', all_info)

	content = BeautifulSoup(content, 'lxml')

	content = content.find(id="readerFs").text.encode('utf8')

	# 下载
	try:
		with open(book_name + '.txt', 'a') as f:
			f.write(title + '\n')
			f.write(content + '\n')
			print "下载成功: %s" % title
	except:
		print "下载失败: %s" % title


