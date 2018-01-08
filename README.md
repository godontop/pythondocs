* [Python标准库](#python标准库)  
	* [2. 内置函数](#2-内置函数)  
		* [urllib2打开URLs的可扩展库](#urllib2打开URLs的可扩展库) 

# Python文档
Python官方文档不完全翻译。  
# Python标准库
Python版本：2.7.4
## 2. 内置函数
**input**([*prompt*])  
等同于 eval(raw_input(prompt))。  

常规用户输入请考虑使用 [raw_input()](https://docs.python.org/2.7/library/functions.html#raw_input) 函数。

**raw_input**([*prompt*])  
如果 *prompt* 参数存在，它将被写到标准输出且不带尾部换行符。接着函数从输入读取一行，将其转化为一个字符串(stripping a trailing newline), 并返回该字符串。当读到 EOF 时，抛出[EOFError](https://docs.python.org/2.7/library/exceptions.html#exceptions.EOFError) 。

### urllib2打开URLs的可扩展库
**注意：**[urllib2](https://docs.python.org/2.7/library/urllib2.html#module-urllib2) 模块在Python3中被分割为几个模块，名为`urllib.request` 和 `urllib.error`。当转换Python 2的源码为Python 3时，[2to3](https://docs.python.org/2.7/glossary.html#term-2to3) 工具将自动使导入适应Python 3。

The [urllib2](https://docs.python.org/2.7/library/urllib2.html#module-urllib2) module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — 基本的和摘要认证，重定向，cookies等等。

[urllib2](https://docs.python.org/2.7/library/urllib2.html#module-urllib2) 模块定义了下列函数：

urllib2.**urlopen**(*url[, data[, timeout[, cafile[, capath[, cadefault[, context]]]]]*)  
打开URL *url*，*url* 可以是一个字符串或者一个 [Request](https://docs.python.org/2.7/library/urllib2.html#urllib2.Request) 对象。