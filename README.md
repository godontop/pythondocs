# Python文档
Python相关文档不完全翻译。  

* [Python 3标准库](#python-3标准库)
	* [2. 内置函数](#2-内置函数)
	* [4.](#4)
		* [4.6](#46)
			* [4.6.4. 列表](#464-列表)
		* [4.7. 文本序列类型 — str](#47-文本序列类型--str)
		* [4.10. 映射类型 — 字典](#410-映射类型--字典)
			* [4.10.1. 字典视图对象](#4101-字典视图对象)
			* [6.2.2. 模块内容](#622-模块内容)
		* [21.6. urllib.request — 打开URLs的可扩展库](#216-urllibrequest--打开urls的可扩展库)
* [Python HOWTOs](#python-howtos)
    * [如何使用urllib包获取互联网资源](#如何使用urllib包获取互联网资源)
        * [头信息](#头信息)
* [Python打包用户指南](#python打包用户指南)
    * [教程](#教程)
        * [安装包](#安装包)
            * [Source Distributions vs Wheels](#source-distributions-vs-wheels)
            * [Requirements files](#requirements-files)
* [PEPs](#peps)
    * [PEP 453 -- Explicit bootstrapping of pip in Python installations](#pep-453----explicit-bootstrapping-of-pip-in-python-installations)
        * [在Windows下执行脚本](#在windows下执行脚本)
* [术语表](#术语表)
* [pip](#pip)
    * [安装](#安装)
        * [我需要安装pip吗？](#我需要安装pip吗)
        * [升级pip](#升级pip)
    * [参考指南](#参考指南)
        * [pip install](#pip-install)
            * [选项](#选项)
* [IPython](#ipython)
    * [Installation](#installation)
        * [安装IPython内核](#安装ipython内核)
            * [Kernels for Python 2 and 3](#kernels-for-python-2-and-3)

[Python 2标准库](https://github.com/godontop/pythondocs/blob/master/python2/README.md)

# Python 3标准库
Python版本：3.6.4
## 2. 内置函数
Python解释器内置了许多总是可用的函数和类型。在这里以字母顺序列出它们。

|          |          |Built-in Functions|          |          |
|----------|----------|------------------|----------|----------|
|          |          |                  |          |          |
|all()     |          |hex()             |          |          |
|          |          |                  |          |          |
|          |          |                  |          |          |
|          |          |int()             |open()    |          |
|          |          |                  |ord()     |          |
|          |          |                  |          |          |
|          |          |                  |print()   |          |

**all**(*iterable*)  
如果 *iterable* 的所有元素都为真则返回`True` (或者如果iterable为空)。相当于：

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

用法举例
```python
>>> a = []
>>> b = [1, 2, 3]
>>> c = [1, 2, None]
>>> print(all(a))
True
>>> print(all(b))
True
>>> print(all(c))
False
```

**hex**(*x*)  
将一个整型数转换成一个以 "0x" 为前缀的小写字母十六进制字符串。

```python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
```
          
*class* **int**(*x=0*)  
*class* **int**(*x, base=10*)  
返回一个从数字或者字符串 *x* 构建的整数对象，如果没有给定参数则返回0。

如果 *x* 不是一个数字或者指定了 *base*，则 *x* 必须是一个表示一个以 *base* 为基数的[整型文字](https://docs.python.org/3.6/reference/lexical_analysis.html#integers)的字符串，[字节](https://docs.python.org/3.6/library/stdtypes.html#bytes)或[字节数组](https://docs.python.org/3.6/library/stdtypes.html#bytearray)实例。*base* 的默认值是10。允许的值是 0 和 2-36. 

将十六进制转换为十进制：

```python
>>> int('0xff', 16)
255
>>> int('0xFF', 16)
255
>>> int('0x9FFF', 16)
40959
```

**open**(*file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None*)  
打开 *file* 并返回一个对应的[文件对象](https://docs.python.org/3.6/glossary.html#term-file-object)。如果文件不能被打开，则抛出一个[OSError](https://docs.python.org/3.6/library/exceptions.html#OSError)异常。

*file* is a [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object) giving the pathname (绝对的或者相对于当前工作目录的) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed, unless *closefd* is set to `False`.)

*mode* 是一个可选字符串，用于指定打开文件的模式。默认值为`'r'`，意味着在文本模式下以只读方式打开。其它常用值是`'w’`意味着写(如果文件已经存在则截断文件), `'x'`意味着专门创建（exclusive creation），而`'a'`意味着附加 (在一些Unix系统，意味着所有写操作被附加到文件末尾而不考虑当前搜索位置). 在文本模式下，如果 *encoding* 没有指定，使用的编码将依赖于平台：`locale.getpreferredencoding(False)` 将被调用以得到当前区域编码（locale encoding）。(读写裸字节 (raw bytes)使用binary模式且不要指定 *encoding*.) 可用的模式是：

|Character |Meaning                                        |
|----------|-----------------------------------------------|
|`'r'`     |只读模式打开（默认）                              |
|`'w'`     |open for writing, 首先截断文件                   |
|`'x'`     |open for exclusive creation, 如果文件已存在则失败 |
|`'a'`     |open for writing, 如果文件存在则附加到文件末尾     |
|`'b'`     |二进制模式                                      |
|`'t'`     |文本模式（默认）                                 |
|`'+'`     |open a disk file for updating (读和写)          |
|`'U'`     |[通用新行](https://docs.python.org/3.6/glossary.html#term-universal-newlines) 模式（已弃用）        |

默认模式是 `'r'` (打开只读文本, 同义词 `'rt'`). 对于二进制读写访问，模式 `'w+b'` 打开并将文件截断为0字节。`'r+b'` 打开文件时不截断。

就像在[概述](https://docs.python.org/3.6/library/io.html#io-overview)中提到的，Python区分二进制和文本I/O。以二进制模式（*mode*参数包含`'b'`）打开的文件返回内容作为[bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes)对象无需任何解码。在文本模式(默认, 或者当 *mode* 参数中包含 `'t'` ), 文件内容作为[str](https://docs.python.org/3.6/library/stdtypes.html#str)被返回，字节首先被一个平台相关的编码或者指定的*编码*（如果指定了*encoding*参数）解码。

`**注意：**Python不依赖于底层操作系统的文本文件的概念；所有的处理都是由Python自己完成，因此是跨平台的。`

**ord**(*c*)  
给定一个表示一个Unicode字符的字符串，返回一个代表该字符的Unicode代码点的整型数。例如， `ord('a')` 返回整型数 `97`，`ord('€')` (欧元符号) 返回 `8364`。这是 [chr()](https://docs.python.org/3.6/library/functions.html#chr) 的逆向操作。

函数 ord(c) 返回的是一个十进制整型数。

```python
>>> ord('a')
97
>>> ord('€')
8364
>>> ord('中')
20013
>>> hex(20013)
'0x4e2d'
>>> u'\u4e2d'
'中'
```

__print__(_*objects, sep=' ', end='\n', file=sys.stdout, flush=False_)  
打印 *objects* 到文本流 *file*, separated by *sep* and followed by *end*. 如果出现*sep*, *end*, *file* 和 *flush*, 则必须被作为关键字参数给出。  

所有非关键字参数被转换成字符串就像 [str()](https://docs.python.org/3.6/library/stdtypes.html#str) 做的那样并写入到流，separated by *sep* and followed by *end*。*sep* 和 *end* 都必须是字符串；它们也可以是 `None`，意味着使用默认值（*sep* 的默认值为一个空格，*end* 的默认值为一个换行符）。如果没有给定 *objects*， [print()](https://docs.python.org/3.6/library/functions.html#print) 将仅写入 *end*。  

_在版本3.3中发生变化：_ 增加了 *flush* 关键字参数。

## 4.
### 4.6
#### 4.6.4. 列表
列表是可变序列，通常用于存储同类元素的集合(元素精确的相似度因应用程序而变化).

class **list**([*iterable*])

列表实现了所有的通用序列操作和可变序列操作。列表还提供如下额外的方法：  
**sort**(_*, key=None, reverse=False_)  
这个方法就地对列表进行排序，仅使用 `<` 比较元素。

[sort()](https://docs.python.org/3.6/library/stdtypes.html#list.sort) 仅接受传递两个关键字参数([仅关键字参数](https://docs.python.org/3.6/glossary.html#keyword-only-parameter)):

*reverse* 是一个布尔值。如果设置为 True，则列表元素将按逆序排列（即从大到小）。

To remind users that it operates by side effect, 它不返回排序后的序列(使用 sorted() 明确地请求一个新的排序后的列表实例).  

```python
letters = ['d', 'a', 'e', 'c', 'b']
print(letters.sort())
```

**Result:**  
None

list.sort()方法的返回值是None，要打印排序后的列表，应使用下面的代码：

```python
letters = ['d', 'a', 'e', 'c', 'b']
letters.sort()
print(letters)
```

**Result:**  
['a', 'b', 'c', 'd', 'e']

### 4.7. 文本序列类型 — str
在Python中，文本数据是通过 [str](https://docs.python.org/3.6/library/stdtypes.html#str) 对象或 *strings* 来处理的。字符串是不可变的Unicode代码点[序列](https://docs.python.org/3.6/library/stdtypes.html#typesseq)。字符串的写法有多种方式：

* 单引号: `'allows embedded "double" quotes'`
* 双引号: `"allows embedded 'single' quotes"`.
* 三引号: `'''Three single quotes'''`, `"""Three double quotes"""`

三引号字符串可能跨越多行 - 所有关联的空白都将被包含在字符串中。

如果一个单一表达式的各个字符串之间仅有空格，那么它们将被含蓄地转换成一个单字符串。即，`("spam " "eggs") == "spam eggs"`。单一字符串等于单一表达式中各个字符串拼接的结果。

```python
>>> ("spam" "eggs") == "spameggs"
True
>>> ("spam " "eggs") == "spam eggs"
True
>>> ("spam "  "eggs") == "spam eggs"
True
```

### 4.10. 映射类型 — 字典
一个[映射](https://docs.python.org/3.6/glossary.html#term-mapping) 对象映射 [可哈希的](https://docs.python.org/3.6/glossary.html#term-hashable) 值到任意对象。映射是可变对象。目前仅有一个标准映射类型，*字典*。 (其它容器请参考内置[列表](https://docs.python.org/3.6/library/stdtypes.html#list)，[集合](https://docs.python.org/3.6/library/stdtypes.html#set)和[元组](https://docs.python.org/3.6/library/stdtypes.html#tuple)类，以及 [collections](https://docs.python.org/3.6/library/collections.html#module-collections) 模块.)

字典的键 *几乎* 可以是任意值。不[可哈希的](https://docs.python.org/3.6/glossary.html#term-hashable)值，即值包含列表，字典或其它可变类型 (通过比较值而不是对象身份) 不能被用作键。 

*class* __dict__(_\**kwarg_)  
*class* __dict__(_mapping, \**kwarg_)  
*class* __dict__(_iterable, **kwarg_)

这些是字典支持的操作 (因此，自定义映射类型也应该支持)：

**get**(*key*[, *default*])  
如果 *key* 在字典中，则返回 *key* 的值，否则返回 *default*。If default is not given, it defaults to `None`, 所以这个方法永远不会抛出 [KeyError](https://docs.python.org/3.6/library/exceptions.html#KeyError)。

**items()**  
返回一个新的字典的元素的视图 (`(key, value)` pairs)。请看[视图对象的文档](https://docs.python.org/3.6/library/stdtypes.html#dict-views)。

**keys()**  
返回一个字典的键的新的视图。请看[视图对象的文档](https://docs.python.org/3.6/library/stdtypes.html#dict-views)。

**values()**  
返回一个字典的值的新的视图。请看[视图对象的文档](https://docs.python.org/3.6/library/stdtypes.html#dict-views)。

#### 4.10.1. 字典视图对象
[dict.keys()](https://docs.python.org/3.6/library/stdtypes.html#dict.keys), [dict.values()](https://docs.python.org/3.6/library/stdtypes.html#dict.values) 和 [dict.items()](https://docs.python.org/3.6/library/stdtypes.html#dict.items) 返回的对象是 *视图对象*。它们提供了一个关于字典条目的动态视图，这意味着当字典变化的时候，视图将反映这些变化。

字典视图用法的一个例子：

```python
>>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
>>> keys = dishes.keys()
>>> values = dishes.values()

>>> keys
dict_keys(['eggs', 'sausage', 'bacon', 'spam'])
>>> values
dict_values([2, 1, 1, 500])

>>> type(keys)
<class 'dict_keys'>
>>> type(values)
<class 'dict_values'>

>>> # iteration
...
>>> n = 0
>>> for val in values:
...     n += val
...
>>> print(n)
504

>>> # keys and values are iterated over in the same order
...
>>> list(keys)
['eggs', 'sausage', 'bacon', 'spam']
>>> list(values)
[2, 1, 1, 500]

>>> # view objects are dynamic and reflect dict changes
...
>>> del dishes['eggs']
>>> del dishes['sausage']
>>> list(keys)
['bacon', 'spam']
>>> list(values)
[1, 500]

>>> # set operations
...
>>> keys & {'eggs', 'bacon', 'salad'}
{'bacon'}
>>> keys ^ {'sausage', 'juice'}
{'juice', 'sausage', 'spam', 'bacon'}
```

#### 6.2.2. 模块内容
这个模块定义了数个函数，常量和一个异常。Some of the functions are simplified versions of the full featured methods for compiled regular expressions. 大多数面对较重大的应用总是使用编译后的形式。

re.**match**(*pattern, string, flags=0*)  
如果 *string* 的开始位置有0个或多个字符匹配正则表达式 *pattern*，则返回一个对应的[匹配对象](https://docs.python.org/3.6/library/re.html#match-objects)。如果字符串不匹配模式，则返回 `None`；注意，这不同于 zero-length match。

注意，即使在[多行](https://docs.python.org/3.6/library/re.html#re.MULTILINE)模式下，[re.match()](https://docs.python.org/3.6/library/re.html#re.match) 将仅匹配字符串的开始位置而不是每一行的开始位置。

如果你想在 *string* 的任意位置定位一个匹配，使用 [search()](https://docs.python.org/3.6/library/re.html#re.search) 替代。

```python
>>> import re
>>> re.match('c', 'abcdef')   # No match
>>> re.search('c', 'abcdef')  # Match
<_sre.SRE_Match object; span=(2, 3), match='c'>
```

**匹配中文**    
[\u4e00-\u9fd5]虽然不是所有中文的Unicode代码点范围，但它几乎已经包含了所有常用的汉字的Unicode代码点。在Unicode标准版本10.0.0中包含汉字代码点的块共有9个，具体可以查询Unicode官网。Python 3.6.4支持的Unicode标准版本为9.0.0，[\u4e00-\u9fd5]是Unicode标准版本8.0的CJK Unified Ideographs块的代码点范围。

匹配一个或多个中文

```python
>>> import re
>>> s = 'Python is a programming language.'
>>> re.search(u'[\u4e00-\u9fd5]+', s)
>>> s = 'Python不是大蟒蛇。'
>>> re.search(u'[\u4e00-\u9fd5]+', s)
<_sre.SRE_Match object; span=(6, 11), match='不是大蟒蛇'>
```

### 21.6. urllib.request — 打开URLs的可扩展库
**Source code:** [Lib/urllib/request.py](https://github.com/python/cpython/tree/3.6/Lib/urllib/request.py)

The [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — 基本的和摘要认证，重定向，cookies等等。

__另请参阅：__ 更高层次的HTTP客户端接口推荐 [Requests package](http://docs.python-requests.org/)。

[urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) 模块定义了下面的函数：

urllib.request.**urlopen**(_url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None_)  
打开URL _url_，_url_ 可以是一个字符串或者一个 [Request](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) 对象。

*data* must be an object specifying additional data to be sent to the server, or `None` if no such data is needed. 详见 [Request](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) 。

This function always returns an object which can work as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) and has methods such as

* geturl() — return the URL of the resource retrieved, commonly used to determine if a redirect was followed  
* info() — 返回页面的元信息，例如头信息， in the form of an [email.message_from_string()](https://docs.python.org/3/library/email.parser.html#email.message_from_string) instance (see [Quick Reference to HTTP Headers](https://www.cs.tut.fi/~jkorpela/http.html))  
* getcode() – 返回响应的HTTP状态代码。

提供下面的类：

class urllib.request.**Request**(*url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None*)  
This class is an abstraction of a URL request.

*url* 应该是一个包含一个有效的URL的字符串。

*headers* 应该是一个字典， and will be treated as if [add_header()](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header) was called with each key and value as arguments. This is often used to “spoof” the `User-Agent` header value, which is used by a browser to identify itself – 一些HTTP服务器仅允许来自普通浏览器的请求而阻止来自脚本的请求。例如，Mozilla Firefox 可能标识自己为 `"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0"`, 而 [urllib](https://docs.python.org/3/library/urllib.html#module-urllib) 的默认用户代理字符串是 `"Python-urllib/3.6"` (on Python 3.6)。

# Python HOWTOs
## 如何使用urllib包获取互联网资源
### 头信息
我们将在这讨论一个具体的HTTP头信息，详细解释如何为你的HTTP请求增加头信息。

一些网站不喜欢被程序浏览，或者给不同的浏览器发送不同的版本。默认情况下urllib以Python-urllib/x.y (x和y分别为Python发行版的主版本号和次版本号，如 Python-urllib/3.6)标识自己，这可能使网站迷惑，或者无法正常工作。一个浏览器标识自己的方式是通过User-Agent(用户代理)头信息。当你创建一个Request对象时，你可以传递一个头信息字典进去。

```python
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.whatismybrowser.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) \
Gecko/20100101 Firefox/58.0'
}

req = Request(url, headers=headers)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'lxml')
myuseragent = soup.find_all('div', class_="user-agent")[0].a.get_text()
print(myuseragent)
```

上面代码的执行结果是：  
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0

当Request对象没有传递headers参数时，执行结果是：  
Python-urllib/3.6

# Python打包用户指南 
## 教程
### 安装包
#### Source Distributions vs Wheels
[pip](https://packaging.python.org/key_projects/#pip) 可以从 [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-source-distribution-or-sdist) 或者 [Wheels](https://packaging.python.org/glossary/#term-wheel) 安装，但如果两者都存在于 PyPI，则pip将优先安装一个兼容的 [wheel](https://packaging.python.org/glossary/#term-wheel)。

[Wheels](https://packaging.python.org/glossary/#term-wheel) are a pre-built [distribution](https://packaging.python.org/glossary/#term-distribution-package) format that provides faster installation compared to [Source Distributions (sdist)](https://packaging.python.org/glossary/#term-source-distribution-or-sdist), 特别是当一个项目包含编译的扩展时。

If [pip](https://packaging.python.org/key_projects/#pip) does not find a wheel to install, it will locally build a wheel and cache it for future installs, instead of rebuilding the source distribution in the future.

#### Requirements files
Install a list of requirements specified in a [Requirements File](https://pip.pypa.io/en/latest/user_guide/#requirements-files).

`pip install -r requirements.txt`

# PEPs
## PEP 453 -- Explicit bootstrapping of pip in Python installations
### 在Windows下执行脚本
Python 3.3 默认为Windows提供了Python Launcher (和相关的 **py** 命令)。

```
C:\Users\YWH>py -2 -m pip list --format=columns
Package    Version
---------- -------
pip        9.0.1
setuptools 28.8.0

C:\Users\YWH>py -3 -m pip list --format=columns
Package     Version
----------- -------
pip         9.0.1
pycodestyle 2.3.1
setuptools  28.8.0

C:\Users\YWH>py -2 --version
Python 2.7.14

C:\Users\YWH>py -3 --version
Python 3.6.4
```

# 术语表
**`>>>`**    
Python交互式shell的默认提示符。常见于可以在解释器中交互式执行的示例代码中。

**`...`**  
The default Python prompt of the interactive shell when entering code for an indented code block or within a pair of matching left and right delimiters (parentheses, square brackets or curly braces).

**file object**  
An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource. Depending on the way it was created, a file object can mediate access to a real on-disk file or to another type of storage or communication device (例如标准输入/输出，in-memory buffers, sockets, pipes, etc.). 文件对象也被称为 *file-like objects* 或 *streams*.

事实上有三种文件对象：raw [binary files](https://docs.python.org/3/glossary.html#term-binary-file), buffered [binary files](https://docs.python.org/3/glossary.html#term-binary-file) 和 [文本文件](https://docs.python.org/3/glossary.html#term-text-file). 它们的接口被定义在 [io](https://docs.python.org/3/library/io.html#module-io) 模块中. 创建一个文件对象的标准方式是通过使用 [open()](https://docs.python.org/3/library/functions.html#open) 函数。

**file-like object**  
[文件对象](https://docs.python.org/3/glossary.html#term-file-object) 的同义词。

# pip
## 安装
### 我需要安装pip吗？
pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from [python.org](https://www.python.org/) or if you are working in a [Virtual Environment](https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments) created by [virtualenv](https://packaging.python.org/key_projects/#virtualenv) or [pyvenv](https://packaging.python.org/key_projects/#venv). Just make sure to [upgrade pip](https://pip.pypa.io/en/latest/installing/#upgrading-pip).

### 升级pip
On Linux or macOS:  
`pip install -U pip`

On Windows:  
`python -m pip install -U pip`

## 参考指南
### pip install
#### 选项
-U, --upgrade  
升级所有指定的包到最新的可用版本。依赖的处理依赖于使用的 upgrade-strategy。

--user  
Install to the Python user install directory for your platform. Typically ~/.local/, or %APPDATA%Python on Windows. (See the Python documentation for site.USER_BASE for full details.)

# IPython
## Installation
### 安装IPython内核
#### Kernels for Python 2 and 3
If you’re running Jupyter on Python 3, you can set up a Python 2 kernel like this:

```
python2 -m pip install ipykernel
python2 -m ipykernel install --user
```

**On Windows:**  

```
py -2 -m pip install ipykernel
py -2 -m ipykernel install --user
```

If you’re running Jupyter on Python 2 and want to set up a Python 3 kernel, follow the same steps, replacing `2` with `3`.

The last command installs a [kernel spec](https://jupyter-client.readthedocs.io/en/latest/kernels.html#kernelspecs) file for the current python installation. Kernel spec 文件是JSON文件，可以被普通文本编辑器浏览和修改。