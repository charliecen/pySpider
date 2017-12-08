# pySpider


### 安装

##### 安装selenium

```sh
$ pip install selenium
```

基本用法，详见[官网](http://selenium-python.readthedocs.io/getting-started.html#simple-usage)

##### 浏览器驱动

```sh
$ pip install chromedriver
```

[官网地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)

##### PhantomJS

[下载地址](http://phantomjs.org/download.html)

PhantomJS 是没有界面的浏览器，可以帮助我们像浏览器一样渲染 JS 处理的页面，需要将文件位置配置到环境变量；

##### lxml

```sh
$ pip install lxml
```

用于辅助 BeautifulSoup 解析 html 页面

### 下载思路

* 使用 `selenium` 和 `PhantomJs` 模拟浏览器访问小说网站页面
* 用户输入下载的书名， 找到首页搜索框，键入书名并回车
* 浏览器切换至搜索页， 通过 `BeautifulSoup` 解析html, 找到目录`url`
* 打开目录`url`， 获取所有章节`url`
* 循环访问每个章节，找到章节名和章节正文
* 保存至对应的文件中

### 实现

```sh
$ python getBook.py
请输入你要下载的书名：修真世界
下载成功: 第一节 《小云雨诀》
下载成功: 第二节 玉简
下载成功: 第三节 小院
下载成功: 第四节 无妄
下载成功: 第五节 冷雾谷
下载成功: 第六节 高危
下载成功: 第七节 爷等你 【第二更】
下载成功: 第八节 变化 【第三更】
下载成功: 第九节 炼器
下载成功: 第十节 杂草  【第二更】
下载成功: 第十一节 财迷僵尸  【第三更】
```
 