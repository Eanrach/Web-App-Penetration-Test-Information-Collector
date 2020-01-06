# 此项目为博主的毕设，博主已毕业，项目已废弃。
# Web-App-Penetration-Test-Information-Collector

Web应用渗透测试信息收集器

这是我的毕业设计项目, 因为本人目前在进行渗透测试实习, 收集信息阶段要占用我非常多的时间, 同时打开很多的扫描器也非常地累, 本工具意在节省时间, 希望路过大佬多多支持和提供修改意见, 此工具会持续更新.

## app结构

/app

../mod.py #功能和api

../\__init\__.py #启动器(名称暂定)

../test.py #测试用文件, 里面有未完善功能, 如果偶遇路过大佬看到这个项目, 希望可以帮助完善一下, 感激不尽!

## api标准

```python
/mod.py/

def api(argument):
	#内容
	#如果需要使用写入文件功能需要返回两个参数
	#文件名为字符串, 文件内容建议为json
	return(文件名,文件内容)
```

## 已有api
```python
import mod
	#传入主机域名或ip(字符串),并进行whois,并且输出whois文件名和whois结果(json)
	mod.whoisDomain(domain)
	#传入主机域名或ip(字符串),并进行nslookup,并且输出nslookup文件名和nslookup结果(json)
	mod.nslookup(domain)
	#传入主机域名或ip(字符串),并扫描端口,并且输出文件名和扫描结果(json)
	mod.scanner(host)
	#传入文件名和文件内容,生成一个json文件, 文件名:args[0][0], 文件内容:args[0][1]
	mod.writeFile(*args)
```