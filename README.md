# Python文档
Python相关文档不完全翻译。  

* [Python 3标准库](#python-3标准库)
	* [2. 内置函数](#2-内置函数)
	* [4.](#4)
        * [4.2. 布尔运算 — and, or, not](#42-布尔运算--and-or-not)
		* [4.6](#46)
			* [4.6.4. 列表](#464-列表)
		* [4.7. 文本序列类型 — str](#47-文本序列类型--str)
            * [4.7.1. 字符串方法](#471-字符串方法)
            * [4.8.3. 字节和字节数组操作](#483-字节和字节数组操作)
		* [4.10. 映射类型 — 字典](#410-映射类型--字典)
			* [4.10.1. 字典视图对象](#4101-字典视图对象)
        * [4.13. 特殊属性](#413-特殊属性)
    * [5. 内置异常](#5-内置异常)
        * [5.2. 具体异常](#52-具体异常)
            * [5.2.1. OS异常](#521-os异常)
            * [6.1.3. 格式化字符串语法](#613-格式化字符串语法)
        * [6.2. re — 正则表达式运算](#62-re--正则表达式运算)
            * [6.2.1. 正则表达式语法](#621-正则表达式语法)
            * [6.2.2. 模块内容](#622-模块内容)
            * [8.1.3. date对象](#813-date对象)
        * [9.6. random — 生成伪随机数](#96-random--生成伪随机数)
            * [9.6.2. 用于整型数的函数](#962-用于整型数的函数)
            * [9.6.3. 用于序列的函数](#963-用于序列的函数)
            * [10.1.1. Itertool函数](#1011-itertool函数)
        * [10.2. functools — 高阶函数和操作可调用对象](#102-functools--高阶函数和操作可调用对象)
        * [11.2. os.path — 通用路径名操作](#112-ospath--通用路径名操作)
            * [16.1.8. 各种各样的系统信息](#1618-各种各样的系统信息)
            * [16.2.3. 类层次结构](#1623-类层次结构)
                * [16.2.3.1. I/O 基类](#16231-io-基类)
                * [16.2.3.2. 原始文件 I/O](#16232-原始文件-io)
                * [16.2.3.3. 缓冲流](#16233-缓冲流)
                * [16.2.3.4. 文本 I/O](#16234-文本-io)
            * [16.3.1. 函数](#1631-函数)
        * [16.5. getopt — C-风格的命令行选项解析器](#165-getopt--c-风格的命令行选项解析器)
            * [16.6.2. 日志级别](#1662-日志级别)
            * [16.6.7. LogRecord属性](#1667-logrecord属性)
            * [16.6.10. 模块级别的函数](#16610-模块级别的函数)
            * [16.16.2. ctypes reference](#16162-ctypes-reference)
                * [16.16.2.1. 查找共享库](#161621-查找共享库)
                * [16.16.2.5. 实用函数](#161625-实用函数)
		* [21.6. urllib.request — 打开URLs的可扩展库](#216-urllibrequest--打开urls的可扩展库)
        * [21.8. urllib.parse — 将URLs解析为组件](#218-urllibparse--将urls解析为组件)
            * [21.8.1. URL解析](#2181-url解析)
        * [21.9. urllib.error — urllib.request抛出的异常类](#219-urlliberror--urllibrequest抛出的异常类)
        * [21.10. urllib.robotparser — 解析robots.txt](#2110-urllib-robotparser--解析robotstxt)
        * [21.12. http.client — HTTP协议客户端](#2112-httpclient--http协议客户端)
            * [21.12.2. HTTPResponse对象](#21122-httpresponse对象)
        * [21.21. socketserver — 一个网络服务器框架](#2121-socketserver--一个网络服务器框架)
            * [21.21.2. 服务器对象](#21212-服务器对象)
        * [21.22. http.server — HTTP 服务器](#2122-httpserver--http-服务器)
        * [29.1. sys — 系统专用参量和函数](#291-sys--系统专用参量和函数)
* [Python教程](#python教程)
    * [2. 使用Python解释器](#2-使用python解释器)
        * [2.1. 调用解释器](#21-调用解释器)
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
|abs()     |          |                  |          |          |
|all()     |          |hex()             |          |          |
|          |          |                  |          |          |
|          |          |                  |          |          |
|          |          |int()             |open()    |          |
|          |          |isinstance()      |ord()     |          |
|          |          |                  |pow()     |          |
|          |          |                  |print()   |          |
|          |          |                  |          |type()    |
|          |          |                  |          |          |
|          |          |                  |          |          |
|          |          |                  |          |          |
|          |hasattr() |                  |          |          |

**abs**(*x*)  
返回一个数的绝对值。参数可以是一个整型数或者一个浮点数。如果参数是一个复数，its magnitude is returned.

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

**hasattr**(*object, name*)  
参数是一个对象和一个字符串。如果字符串是对象的某个属性的名称则结果为 `True` ，否则返回 `False` 。(这是通过调用 `getattr(object, name)` 并看它是否抛出一个 [AttributeError](https://docs.python.org/3.6/library/exceptions.html#AttributeError) 来实现的。)

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

**isinstance**(*object, classinfo*)  
Return true if the *object* argument is an instance of the *classinfo* argument, or of a (direct, indirect or [virtual](https://docs.python.org/3.6/glossary.html#term-abstract-base-class)) subclass thereof. 如果 *object* 不是一个指定类型的对象，则函数总是返回 false. If *classinfo* is a tuple of type objects (or recursively, other such tuples), return true if *object* is an instance of any of the types. If *classinfo* is not a type or tuple of types and such tuples, a [TypeError](https://docs.python.org/3.6/library/exceptions.html#TypeError) exception is raised.

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

**注意：** Python不依赖于底层操作系统的文本文件的概念；所有的处理都是由Python自己完成，因此是跨平台的。

*buffering*是一个可选整型数用于设置缓冲区策略。传递0关闭缓冲区(仅在二进制模式下允许), 1 选择行缓冲区 (仅在文本模式下可用), 
大于1的整型数表示一个固定大小的块缓冲区的大小，以字节为单位。当没有给出*buffering*参数时, 默认的缓冲区策略工作如下：  
* 二进制文件被缓冲在固定大小的块中；the size of the buffer is chosen using a heuristic trying to determine the underlying device's "block size" and falling back on [io.DEFAULT_BUFFER_SIZE](https://docs.python.org/3.6/library/io.html#io.DEFAULT_BUFFER_SIZE). 在许多系统中，缓冲区通常是4096或者8192字节长。  
* "Interactive" 文本文件([isatty()](https://docs.python.org/3.6/library/io.html#io.IOBase.isatty) 返回`True`的文件) 使用行缓冲区。其它文本文件使用上面描述的二进制文件的缓冲策略。

*encoding* 是用来解码或者编码文件的编码的名字。这个应该仅用于文本模式。默认编码依赖于平台(不管 [locale.getpreferredencoding()](https://docs.python.org/3.6/library/locale.html#locale.getpreferredencoding) 返回什么), 但任何Python支持的[文本编码](https://docs.python.org/3.6/glossary.html#term-text-encoding)都可以被使用。支持的编码列表请看[codecs](https://docs.python.org/3.6/library/codecs.html#module-codecs)模块。

*errors* 是一个可选字符串，用于指定如何处理编码及解码错误——这不能被用于二进制模式。许多标准错误处理程序是可用的 (listed under [Error Handlers](https://docs.python.org/3.6/library/codecs.html#error-handlers)), 但任何已经通过[codecs.register_error()](https://docs.python.org/3.6/library/codecs.html#codecs.register_error)注册的错误处理名字也是有效的。标准名字包括：  
* `'strict'` 如果有编码错误则抛出一个[ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)异常。默认值 `None` 有相同的效果。
* `'ignore'` 忽略错误。注意，忽略编码错误可能导致数据丢失。
* `'replace'` 导致一个替换标记(例如`'?'`)被插入到有畸形数据的地方。
* `'surrogateescape'` 将任何不正确的字节表示为Unicode私有使用区域范围（从 U+DC80 到 U+DCFF）内的代码点。当写数据且`surrogateescape`错误处理程序被使用时这些私有代码点将被转回为相同的字节。这在处理未知编码文件时很有用。
* `'xmlcharrefreplace'` 仅当向文件中写数据时支持。字符不被编码支持的时候被替换为适当的XML字符引用 `&#nnn;`.
* `'backslashreplace'` 通过Python的反斜杠转义序列替换畸形数据。
* `'namereplace'` (也是仅当写数据的时候支持) 用`\N{...}`转义序列替换不支持的字符。

*newline* 控制[通用新行](https://docs.python.org/3.6/glossary.html#term-universal-newlines)模式如何工作(它仅用于文本模式). 它可以是 `None`, `''`, `'\n'`, `'\r'`, 和 `'\r\n'`. 它的工作方式如下：  
* 当从流读取输入时，如果 *newline* 是 `None`，通用换行模式开启。输入中的行可以以 `'\n'`, `'\r'`, 或者 `'\r\n'` 结尾，且在返回给调用方以前这些被翻译成 `'\n'` 。如果 *newline* 是 `''`，通用换行模式开启，行尾结束符号返回给调用方的时候没有被翻译。如果 *newline* 是其它合法的值，输入行仅被给定的字符串终结，且返回给调用方的行尾结束符号没有被翻译。
* 当向流写入输出的时候，如果 *newline* 是 `None`，所有写入的 `'\n'` 字符都被翻译成系统默认的行分隔符，[os.linesep](#https://docs.python.org/3.6/library/os.html#os.linesep). 如果 *newline* 是 `''` 或者 `'\n'`, 则不翻译。如果 *newline* 是任何其它的合法值，所有写入的 `'\n'` 字符都被翻译为指定的字符串。

如果 *closefd* 是 `False` 且给定的是一个文件描述符而不是一个文件名，则当文件被关闭的时候底层的文件描述符将保持打开状态。如果给定的是一个文件名则 *closefd* 必须是 `True` (默认值) ，否则将抛出一个错误。

A custom opener can be used by passing a callable as *opener*. The underlying file descriptor for the file object is then obtained by calling *opener* with (*file, flags*). *opener* must return an open file descriptor (passing [os.open](https://docs.python.org/3.6/library/os.html#os.open) as *opener* results in functionality similar to passing `None`).

新创建的文件是[不可继承的](https://docs.python.org/3.6/library/os.html#fd-inheritance)。

下面的例子使用[os.open()](https://docs.python.org/3.6/library/os.html#os.open)函数的 [dir_fd](https://docs.python.org/3.6/library/os.html#dir-fd) 参数打开一个相对于给定目录的文件：

```python
>>> import os
>>> dir_fd = os.open('somedir', os.O_RDONLY)
>>> def opener(path, flags):
...     return os.open(path, flags, dir_fd=dir_fd)
...
>>> with open('spamspam.txt', 'w', opener=opener) as f:
...     print('This will be written to somedir/spamspam.txt', file=f)
...
>>> os.close(dir_fd)  # don't leak a file descriptor
```

[open()](https://docs.python.org/3.6/library/functions.html#open)函数返回的[文件对象](https://docs.python.org/3.6/glossary.html#term-file-object)的类型依赖于模式。当[open()](https://docs.python.org/3.6/library/functions.html#open)以文本模式打开一个文件时(`'w'`, `'r'`, `'wt'`, `'rt'`, etc.), 它返回一个 [io.TextIOBase](https://docs.python.org/3.6/library/io.html#io.TextIOBase) 的子类(具体地是 [io.TextIOWrapper](https://docs.python.org/3.6/library/io.html#io.TextIOWrapper)). When used to open a file in a binary mode with buffering, 返回类是[io.BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase)的一个子类. The exact class varies: in read binary mode, 它返回一个[io.BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader)类; in write binary and append binary modes, 它返回一个[io.BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter)类, and in read/write mode, 它返回一个[io.BufferedRandom](https://docs.python.org/3.6/library/io.html#io.BufferedRandom)类. 当buffering关闭时，the raw stream, 返回一个[io.RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase)的子类[io.FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO)。

### 文本模式
```python
>>> with open('test.txt', 'r') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'w') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'rt') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'wt') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'a') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'at') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'r+') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'r+t') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'w+') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> with open('test.txt', 'w+t') as f:
...     print(type(f))
...
<class '_io.TextIOWrapper'>
>>> import io
>>> issubclass(io.TextIOWrapper, io.TextIOBase)
True
```

### 开启buffering的二进制模式
```python
>>> with open('test.txt', 'rb') as f:
...     print(type(f))
...
<class '_io.BufferedReader'>
>>> with open('test.txt', 'wb') as f:
...     print(type(f))
...
<class '_io.BufferedWriter'>
>>> with open('test.txt', 'ab') as f:
...     print(type(f))
...
<class '_io.BufferedWriter'>
>>> with open('test.txt', 'r+b') as f:
...     print(type(f))
...
<class '_io.BufferedRandom'>
>>> with open('test.txt', 'w+b') as f:
...     print(type(f))
...
<class '_io.BufferedRandom'>
>>> import io
>>> issubclass(io.BufferedReader, io.BufferedIOBase)
True
>>> issubclass(io.BufferedWriter, io.BufferedIOBase)
True
>>> issubclass(io.BufferedRandom, io.BufferedIOBase)
True
```

### 关闭buffering的二进制模式
```python
>>> with open('test.txt', 'rb', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'wb', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'ab', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'r+b', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> with open('test.txt', 'w+b', buffering=0) as f:
...     print(type(f))
...
<class '_io.FileIO'>
>>> import io
>>> issubclass(io.FileIO, io.RawIOBase)
True
```

也看下文件处理模块，例如，[fileinput](https://docs.python.org/3.6/library/fileinput.html#module-fileinput), [io](https://docs.python.org/3.6/library/io.html#module-io) (where [open()](https://docs.python.org/3.6/library/functions.html#open) is declared), [os](https://docs.python.org/3.6/library/os.html#module-os), [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path), [tempfile](https://docs.python.org/3.6/library/tempfile.html#module-tempfile), and [shutil](https://docs.python.org/3.6/library/shutil.html#module-shutil).

*在版本3.3中发生变化：*  
* 增加了*opener*参量（parameter）.
* 增加了 `'x'` 模式。
* [IOError](https://docs.python.org/3.6/library/exceptions.html#IOError) used to be raised, it is now an alias of [OSError]().
* 如果以exclusive creation mode (`'x’`) 打开的文件已经存在，则抛出 [FileExistsError](https://docs.python.org/3.6/library/exceptions.html#FileExistsError).

*在版本3.4中发生变化：*  
* The file is now non-inheritable.

`'U'` 模式 *从版本3.4开始弃用，将在版本4.0中被移除*。

*在版本3.5中发生变化：*  
* 如果系统调用被终止且信号处理程序没有抛出异常，现在函数将重试系统调用而不是抛出一个[InterruptedError](https://docs.python.org/3.6/library/exceptions.html#InterruptedError)异常 (原理请看 [PEP 475](https://www.python.org/dev/peps/pep-0475)).
* 新增 `'namereplace'` 错误处理程序。

*在版本3.6中发生变化：*  
* 增加支持：接受实现了 [os.PathLike](https://docs.python.org/3.6/library/os.html#os.PathLike) 的对象。
* 在 Windows平台, opening a console buffer may return a subclass of [io.RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) other than [io.FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO).

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

**pow**(*x*, *y*[, *z*])  
返回 *x* 的 *y* 次方；如果 *z* 出现，则返回 *x* 的 *y* 次方再以 *z* 取模(比`pow(x, y) % z`的计算效率更高).两个参数的形式 `pow(x, y)` 等同于使用幂运算: `x**y`。

The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. 对于 [整型数](https://docs.python.org/3.6/library/functions.html#int) 操作数，结果与操作数的类型相同 (强制之后) 除非第二个参数是负的；在那种情况下，所有参数被转换成浮点数并返回一个浮点数结果。例如，`10**2` 返回 `100`，但 `10**-2` 返回 `0.01`。如果第二个参数是负的，第三个参数必须被省略。如果 *z* 出现，*x* 和 *y* 必须是整数类型，且 *y* 必须是非负的。

**print**(_*objects, sep=' ', end='\n', file=sys.stdout, flush=False_)  
打印 *objects* 到文本流 *file*, separated by *sep* and followed by *end*. 如果出现*sep*, *end*, *file* 和 *flush*, 则必须被作为关键字参数给出。  

所有非关键字参数被转换成字符串就像 [str()](https://docs.python.org/3.6/library/stdtypes.html#str) 做的那样并写入到流，separated by *sep* and followed by *end*。*sep* 和 *end* 都必须是字符串；它们也可以是 `None`，意味着使用默认值（*sep* 的默认值为一个空格，*end* 的默认值为一个换行符）。如果没有给定 *objects*， [print()](https://docs.python.org/3.6/library/functions.html#print) 将仅写入 *end*。  

The *file* argument must be an object with a `write(string)` method; if it is not present or `None`, [sys.stdout](https://docs.python.org/3.6/library/sys.html#sys.stdout) will be used. Since printed arguments are converted to text strings, [print()](https://docs.python.org/3.6/library/functions.html#print) cannot be used with binary mode file objects. For these, use `file.write(...)` instead.

输出是否缓冲通常由 *file* 决定，但如果 *flush* 关键字参数是 true, 则流被强制 flushed.

_在版本3.3中发生变化：_ 增加了 *flush* 关键字参数。

*class* **type**(*object*)  
*class* **type**(*name, bases, dict*)  
带一个参数时，返回 *object* 的类型。返回值是一种类型对象并且通常和 [object.\_\_class\_\_](https://docs.python.org/3.6/library/stdtypes.html#instance.__class__) 返回相同的对象。

推荐使用内置函数 [isinstance()](https://docs.python.org/3.6/library/functions.html#isinstance) 测试一个对象的类型, because it takes subclasses into account.

```python
>>> obj = "It's a string."
>>> type(obj)
<class 'str'>
>>> obj.__class__
<class 'str'>
>>> isinstance(obj, str)
True
```

## 4.
### 4.2. 布尔运算 — and, or, not
这些是布尔运算，按优先级升序排列：

|Operation   |Result                            |Notes |
|------------|----------------------------------|------|
|`x or y`    |如果x是false，则y，否则x            |(1)   |
|`x and y`   |如果x是false，则x，否则y            |(2)   |
|`not x`     |如果x是false，则`True`，否则`False` |(3)   |

备注：  
1. 这是一个缩短操作，因此仅当第一个参数为false时，它才会计算第二个参数。
2. 这是一个缩短操作，因此仅当第一个参数为true时，它才会计算第二个参数。
3. `not` 的优先级低于非布尔运算，因此 `not a == b` 被解释为 `not (a == b)`, 而 `a == not b` 是一个语法错误。

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

#### 4.7.1. 字符串方法
字符串实现了所有[常见的](https://docs.python.org/3.6/library/stdtypes.html#typesseq-common)序列操作，连同下面描述的额外的方法。

str.**encode**(*encoding="utf-8", errors="strict"*)  
返回一个编码的字符串版本作为一个字节对象。默认编码是 `'utf-8'`。*errors* 可以设置为一个不同的错误处理方案。*errors* 的默认值是 `'strict'`，意为编码错误将抛出一个 [UnicodeError](https://docs.python.org/3.6/library/exceptions.html#UnicodeError)。其它可能的值是 `'ignore'`, `'replace'`, `'xmlcharrefreplace'`, `'backslashreplace'` 和任何其它通过 [codecs.register_error()](https://docs.python.org/3.6/library/codecs.html#codecs.register_error) 注册的名字，参考 [Error Handlers](https://docs.python.org/3.6/library/codecs.html#error-handlers) 章节。可能的编码列表，请参考 [Standard Encodings](https://docs.python.org/3.6/library/codecs.html#standard-encodings) 章节。

*在版本3.1中发生变化：* 增加了对关键字参数的支持。

str.**endswith**(*suffix*[, *start*[, *end*]])  
如果字符串以指定的 *suffix* 结尾返回 `True`，否则返回 `False`。*suffix* can also be a tuple of suffixes to look for. With optional *start*, test beginning at that position. With optional *end*, stop comparing at that position.

str.**join**(*iterable*)  
返回一个由 *iterable* 中的字符串串联而成的字符串。如果 *iterable* 中有任何非字符串值则抛出一个 [TypeError](https://docs.python.org/3.6/library/exceptions.html#TypeError)，包括 [bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes) 对象。元素之间的分隔符是提供这个方法的字符串。

```python
>>> a = ['apple', 'banana', 'cisco', 'decode']
>>> '*'.join(a)
'apple*banana*cisco*decode'
>>> ' '.join(a)
'apple banana cisco decode'
>>> ''.join(a)
'applebananaciscodecode'
>>>
```

str.**lower()**  
Return a copy of the string with all the cased characters [[4]](https://docs.python.org/3.6/library/stdtypes.html#id15) converted to lowercase.

The lowercasing algorithm used is described in section 3.13 of the Unicode Standard.

str.**replace**(*old*, *new*[, *count*])  
返回一个字符串的副本并将所有子串 *old* 替换为 *new*。如果指定了可选参数 *count*，则仅将前 *count* 个 *old* 替换为 *new*。

```python
>>> s = "tools for windows"
>>> s.replace('o', 'p')
'tppls fpr windpws'
>>> s.replace('o', 'p', 2)
'tppls for windows'
```

str.**split**(*sep=None, maxsplit=-1*)  
返回字符串中的一个单词列表，使用 *sep* 作为分隔字符串。If *maxsplit* is given, at most *maxsplit* splits are done (thus, the list will have at most `maxsplit+1` elements). If *maxsplit* is not specified or `-1`, then there is no limit on the number of splits (all possible splits are made).

如果指定 *sep*，连续的分隔符不会被聚集到一起而是被视为界定空串 (例如， `'1,,2'.split(',')` 返回 `['1', '', '2']`)。*sep* 参数可以包括多个字符 (例如，`'1<>2<>3'.split('<>')` 返回 `['1', '2', '3']`)。用一个指定的分隔符分隔一个空串返回 `['']`。

例如：

```python
>>> '1,2,3'.split(',')
['1', '2', '3']
>>> '1,2,3'.split(',', maxsplit=1)
['1', '2,3']
>>> '1,2,,3,'.split(',')
['1', '2', '', '3', '']
```

如果 *sep* 没有指定或者为 `None`，则应用一个不同的分隔算法：连续的空白被作为一个分隔符，而且如果字符串有前导和尾随空白，输出结果的起始或结束位置将不包含空串。因此，当分隔符为 `None` 时，分隔一个空串或者仅由空白组成的字符串返回 `[]`。

例如：

```python
>>> '1 2 3'.split()
['1', '2', '3']
>>> '1 2 3'.split(maxsplit=1)
['1', '2 3']
>>> '   1   2   3   '.split()
['1', '2', '3']
```

str.**startswith**(*prefix*[, *start*[, *end*]])  
如果字符串以指定的 *prefix* 开始则返回 `True`，否则返回 `False`。*prefix* can also be a tuple of prefixes to look for. With optional *start*, test string beginning at that position. With optional *end*, stop comparing string at that position.

#### 4.8.3. 字节和字节数组操作
字节和字节数组对象都支持[通用](https://docs.python.org/3.6/library/stdtypes.html#typesseq-common)序列操作。它们不仅可以与同类型的运算对象互操作，还可以与任何 [bytes-like 对象](https://docs.python.org/3.6/glossary.html#term-bytes-like-object)互操作。因为这种灵活性，它们可以自由地混合操作而不引起错误。然而，返回结果的类型可能依赖于操作数的顺序。

bytes.**decode**(*encoding="utf-8", errors="strict"*)  
bytearray.**decode**(*encoding="utf-8", errors="strict”*)  
从给定的字节返回一个解码的字符串。默认编码是 `'utf-8'`. `errors` 可以设置为一个不同的错误处理方案。`errors` 的默认值是 `'strict'`, 意为编码错误则抛出一个 [UnicodeError](https://docs.python.org/3.6/library/exceptions.html#UnicodeError). 其它可能的值是`'ignore'`, `'replace'` 和任何其它通过 [codecs.register_error()](https://docs.python.org/3.6/library/codecs.html#codecs.register_error) 注册的名字，参考[错误处理程序](https://docs.python.org/3.6/library/codecs.html#error-handlers)章节。对于可能的编码列表，请参考[标准编码](https://docs.python.org/3.6/library/codecs.html#standard-encodings)章节。

**Note:** Passing the *encoding* argument to [str](https://docs.python.org/3.6/library/stdtypes.html#str) allows decoding any [bytes-like object](https://docs.python.org/3.6/glossary.html#term-bytes-like-object) directly, without needing to make a temporary bytes or bytearray object.

*在版本3.1中发生变化：* 新增对关键字参数的支持。

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

### 4.13. 特殊属性
The implementation adds a few special read-only attributes to several object types, where they are relevant. 其中有些不被内置函数[dir()](https://docs.python.org/3.6/library/functions.html#dir) 报道。

object.**\_\_dict\_\_**  
一个字典或其它映射对象，用于存储对象的(可写的)属性。

instance.**\_\_class\_\_**  
一个类实例属于哪个类。

class.**\_\_bases\_\_**  
一个类对象的基类元组。

class.**\_\_subclasses\_\_()**  
每个类都保持了一份它的直接子类的弱引用列表。这个方法返回一个所有仍然活跃的引用的列表。例如：

```python
>>> import io
>>> io.IOBase.__subclasses__()
[<class 'io.RawIOBase'>, <class 'io.BufferedIOBase'>, <class 'io.TextIOBase'>]
```

## 5. 内置异常
### 5.2. 具体异常
下面的异常是经常被抛出的异常。

下面的异常是为了与之前的版本保持兼容；从Python 3.3开始，它们都是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的别名。

*exception* **EnvironmentError**

*exception* **IOError**

*exception* **WindowsError**  
仅Windows下可用。

#### 5.2.1. OS异常
下面的异常是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的子类，they get raised depending on the system error code.

*exception* **ConnectionError**  
连接相关的问题的一个基类。

子类是 [BrokenPipeError](https://docs.python.org/3.6/library/exceptions.html#BrokenPipeError), [ConnectionAbortedError](https://docs.python.org/3.6/library/exceptions.html#ConnectionAbortedError), [ConnectionRefusedError](https://docs.python.org/3.6/library/exceptions.html#ConnectionRefusedError) 和 [ConnectionResetError](https://docs.python.org/3.6/library/exceptions.html#ConnectionResetError)。

*exception* **ConnectionResetError**  
[ConnectionError](https://docs.python.org/3.6/library/exceptions.html#ConnectionError) 的一个子类，当一个连接被对方重置时抛出。相当于 errno `ECONNRESET`。

#### 6.1.3. 格式化字符串语法
The [str.format()](https://docs.python.org/3.6/library/stdtypes.html#str.format) method and the [Formatter](https://docs.python.org/3.6/library/string.html#string.Formatter) class share the same syntax for format strings (although in the case of [Formatter](https://docs.python.org/3.6/library/string.html#string.Formatter), 子类可以定义它们自己的格式化字符串语法). The syntax is related to that of [formatted string literals](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings), but there are differences.

*在版本3.1中发生变化：* 位置参数说明符可以被省略，所以 `'{} {}'` 相当于 `'{0} {1}'`。

一些简单的格式化字符串例子：
```python
"First, thou shalt count to {0}"  # 引用第一个位置参数
"Bring me a {}"                   # 不讲明地引用第一个位置参数
"From {} to {}"                   # 等同于 "From {0} to {1}"
```

### 6.2. re — 正则表达式运算
**Source code:** [Lib/re.py](https://github.com/python/cpython/tree/3.6/Lib/re.py)

这个模块提供与Perl中相似的正则表达式匹配运算。

#### 6.2.1. 正则表达式语法
特殊字符是：

`.`  
(点.) 默认模式下，这匹配除了一个换行符以外的任何字符。如果指定了 [DOTALL](https://docs.python.org/3.6/library/re.html#re.DOTALL) 标准，这将匹配任何字符，包括一个换行符。

`?`  
Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. `ab?` 将匹配 `‘a’` 或者 `‘ab’`。

`*?`, `+?`, `??`  
限定符 `'*'`, `'+'`, 和 `'?'` 都是*贪婪的*；它们匹配尽可能多的文本。有时这种行为不是被期望的；如果正则表达式 `<.*>` 与 `'<a> b <c>'` 进行匹配，它将匹配整个字符串，而不仅仅是 `'<a>'`。在限定符的后面添加 `?` 使它执行非贪婪匹配或最小匹配的方式；匹配尽可能少的字符。使用正则表达式 `<.*?>` 将仅匹配 `'<a>'`。

```python
>>> import re
>>> re.findall(r'a(.*)a', 'abcbaabcaabca')
['bcbaabcaabc']
>>> re.findall(r'a(.*?)a', 'abcbaabcaabca')
['bcb', 'bc', 'bc']
>>>
```

`\`  
转义特殊字符 (允许你匹配字符像 `'*'`，`'?'`，等等)，或者表示一个特殊序列；特殊序列在下面讨论。

如果你没有使用原始字符串来表达模式，记住在字符串中Python也使用反斜杠作为一个转义序列；如果转义序列没有被Python解析器识别，则反斜杠和后面的将被包含在结果字符串中。然而，如果Python将识别结果序列，则反斜杠应该被重复两次。这是复杂且难懂的，所以强烈推荐你使用原始字符串，除了最简单的表达式。

`[]`  
用来表明一个字符集合。在集合中：

* 字符可以被单独列出，如 `[amk]` 将匹配 `'a'`, `'m'`, 或者 `'k'`。  
* 可以通过给定两个字符并用一个 `-` 分隔它们来表示字符范围，例如 `[a-z]` 将匹配任意的小写ASCII字母，`[0-5][0-9]` 将匹配从 `00` 到 `59` 的所有两位数，`[0-9A-Fa-f]` 将匹配任意十六进制数字。如果 `-` 被转义了(如 `[a\-z]`) 或者 如果它被放在第一个或最后一个字符(如 `[-a]` 或者 `[a-]`)，它将匹配一个文字 `'-'`。  
* 在集合中特殊字符将失去他们的特殊含义。如，`[(+*)]` 将匹配任意文字字符 `'('`, `'+'`, `'*'`, 或者 `')'`。  
* 在一个集合中字符类如 `\w` 或者 `\S` (在下面定义) 也被接受，虽然它们匹配的字符依赖于 [ASCII](https://docs.python.org/3.6/library/re.html#re.ASCII) 或者 [LOCALE](https://docs.python.org/3.6/library/re.html#re.LOCALE) 模式是否生效。  
* 不在一个范围内的字符可以通过补全集合来匹配。如果集合的第一个字符是 `'^'`，则所有不在集合中的字符将被匹配。例如，`[^5]` 将匹配除了 `5` 以外的所有字符，而 `[^^]` 将匹配除了 `^` 以外的所有字符。如果 `^` 不是集合中的第一个字符则它没有特殊含义。  
* 要在集合中匹配文字 `']'` ，可以在它前面放一个反斜杠，或者将它放在集合的开始位置。例如，`[()[\]{}]` 和 `[]()[{}]` 都将匹配一个括号。

`\w`  
For Unicode (str) patterns:  
Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore. 如果 [ASCII](https://docs.python.org/3/library/re.html#re.ASCII) 标志被使用，则仅匹配 `[a-zA-Z0-9_]` (但标志影响整个正则表达式，所以在这种情况下使用一个明确的 `[a-zA-Z0-9_]` 可能是一个更好的选择)。

For 8-bit (bytes) patterns:  
匹配ASCII字符集中被认为是字母数字的字符；这相当于 `[a-zA-Z0-9_]`。如果 [LOCALE](https://docs.python.org/3/library/re.html#re.LOCALE) 标志被使用，则匹配当前区域设置中被认为是字母数字的字符及下划线。

#### 6.2.2. 模块内容
这个模块定义了数个函数，常量和一个异常。一些函数是编译的正则表达式的全功能方法的简化版。大多数重大的应用总是使用编译后的形式。

*在版本3.6中发生变化：* 标志常量现在是 RegexFlag 的实例，RegexFlag 是 [enum.IntFlag](https://docs.python.org/3.6/library/enum.html#enum.IntFlag) 的一个子类。

re.**compile**(*pattern, flags=0*)  
将一个正则表达式模式编译进一个[正则表达式对象](https://docs.python.org/3.6/library/re.html#re-objects)，正则表达式对象可以使用它的 [match()](https://docs.python.org/3.6/library/re.html#re.regex.match)，[search()](https://docs.python.org/3.6/library/re.html#re.regex.search) 和其它方法来进行匹配，详情如下。

表达式的行为可以通过指定一个 *flags* 值来进行修改。标志值可以是下面任何有一个变量，组合使用按位或(即 `|` 操作符)。

The sequence  

```python
prog = re.compile(pattern)
result = prog.match(string)
```

等同于

```python
result = re.match(pattern, string)
```

但当表达式在一个单一程序中将要被使用几次时，使用 [re.compile()](https://docs.python.org/3.6/library/re.html#re.compile) 及保存的结果正则表达式对象以重用是更高效的。

**注意：** 传递给 [re.compile()](https://docs.python.org/3.6/library/re.html#re.compile) 及模块级别的匹配函数最新的模式的编译版本被缓存，所以每次仅使用几个（a few）正则表达式的程序不必担心编译正则表达式。

re.**I**  
re.**IGNORECASE**  
执行不区分大小写的匹配；表达式像 `[A-Z]` 将也匹配小写字母。Full Unicode matching (例如 `Ü` 匹配 `ü`) also works unless the [re.ASCII](https://docs.python.org/3.6/library/re.html#re.ASCII) flag is used to disable non-ASCII matches. 当前区域设置不会改变这个标志的效果除非 [re.LOCALE](https://docs.python.org/3.6/library/re.html#re.LOCALE) 标志也被使用。相当于行内标志 `(?i)`。

注意当 Unicode 模式 `[a-z]` 或者 `[A-Z]` 与 [IGNORECASE](https://docs.python.org/3.6/library/re.html#re.IGNORECASE) 标志组合使用时，它们将匹配52个 ASCII 字母及 4 个额外的非ASCII字母：`‘İ’` (U+0130, 大写拉丁字母I上面带一个点), `‘ı’` (U+0131, 小写拉丁字母i不带点), `‘ſ’` (U+017F, Latin small letter long s) 和 `‘K’` (U+212A, 开尔文符号)。如果 [ASCII](https://docs.python.org/3.6/library/re.html#re.ASCII) 标志被使用，则仅字母 `‘a’` 到 `‘z’` 和 `‘A’` 到 `‘Z’` 被匹配 (但标志影响整个正则表达式，所以在这种情况下使用一个明确的 `(?-i:[a-zA-Z])` 可能是一个更好的选择)。

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

re.**findall**(*pattern, string, flags=0*)  
返回 *string* 中所有非重叠的 *模式* 匹配，作为一个字符串列表。*string* 被从左到右搜索，匹配按被找到的顺序返回。If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. 空匹配被包含在结果中。

**注意：** 因为当前实现的限制一个空匹配后面的字符没有被包含在下一个匹配中，所以 `findall(r'^|\w+', 'two words')` 返回 `['', 'wo', 'words']` (注意丢失的 “t”)。这在Python 3.7中将发送变化。

```python
>>> import re
>>> re.findall(r'^|\w+', 'two words')
['', 'wo', 'words']
>>> re.findall(r'^|\w+', 'three apples')
['', 'hree', 'apples']
>>> re.findall(r'^|\w+', 'flyhigh')
['', 'lyhigh']
>>> re.findall(r'^|.', 'abcdcba')
['', 'b', 'c', 'd', 'c', 'b', 'a']
>>> re.findall(r'a|b', 'abcba')
['a', 'b', 'b', 'a']
>>> re.findall(r'^a|b', 'abcba')
['a', 'b', 'b']
>>>
```

匹配sitemap文件中的所有链接

```python
import re
import urllib.request


sitemap = urllib.request.urlopen('https://example.com/sitemap.xml').read()
links = re.findall('<loc>(.*?)</loc>', sitemap.decode())

```

#### 8.1.3. date对象

日期可以被用作字典的键。在布尔上下文中，所有 [date](https://docs.python.org/3.6/library/datetime.html#datetime.date) 对象都被认为是真。

实例方法：

date.**weekday()**  
用一个整数返回星期几，星期一是0，星期天是6。例如，`date(2002, 12, 4).weekday() == 2`，星期三。另请参阅 [isoweekday()](https://docs.python.org/3.6/library/datetime.html#datetime.date.isoweekday)。

date.**isoweekday()**  
用一个整数返回星期几，星期一是1，星期天是7. 例如，`date(2002, 12, 4).isoweekday() == 3`，星期三。另请参阅 [weekday()](https://docs.python.org/3.6/library/datetime.html#datetime.date.weekday)，[isocalendar()](https://docs.python.org/3.6/library/datetime.html#datetime.date.isocalendar)。

### 9.6. random — 生成伪随机数
**Source code:** [Lib/random.py](https://github.com/python/cpython/tree/3.6/Lib/random.py)

这个模块为各个发行版实现伪随机数生成器。

**警告：** 这个模块的伪随机数生成器不应该被用于安全目的。为了安全或加密用途，请看 [secrets](https://docs.python.org/3.6/library/secrets.html#module-secrets) 模块。

#### 9.6.2. 用于整型数的函数
random.**randint**(*a, b*)  
返回一个随机整型数 *N*，且 `a <= N <= b`。`random.randint(a, b)` 为 `random.randrange(a, b+1)` 的别名。

#### 9.6.3. 用于序列的函数
random.**choice**(*seq*)  
从一个非空的序列 *seq* 返回一个随机元素。如果 *seq* 为空，则抛出 [IndexError](https://docs.python.org/3.6/library/exceptions.html#IndexError)。

#### 10.1.1. Itertool函数
下面的模块函数都构造并返回迭代器。一些提供无限长的流，所以它们应该仅被截断流的函数或循环访问。

itertools.**count**(*start=0, step=1*)  
创建一个以数字 *start* 开始返回等间隔值的迭代器。经常用来作为 [map()](https://docs.python.org/3.6/library/functions.html#map) 的一个参数来生产连续的数据点。也和 [zip()](https://docs.python.org/3.6/library/functions.html#zip) 一起用来增加序列数。大致等同于：

```python
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

```

当计算浮点数时，有时更高的精准度可以通过代入乘法代码来实现，例如：`(start + step * i for i in count())`。

*在版本3.1中发生变化：* 增加 *step* 参数并允许非整型数参数。

### 10.2. functools — 高阶函数和操作可调用对象
**Source code:** [Lib/functools.py](https://github.com/python/cpython/tree/3.6/Lib/functools.py)

[functools](https://docs.python.org/3.6/library/functools.html#module-functools) 模块是为了高阶函数：作用于或者返回其它函数的函数。通常，为了这个模块的目的，任何可调用对象都可以被作为一个函数。

[functools](https://docs.python.org/3.6/library/functools.html#module-functools) 模块定义了下列函数：

functools.**reduce**(*function*, *iterable*[, *initializer*])  
应用两个参数的 *function* 从左到右累积 *sequence* 中的项，以便减少序列到一个单值。例如，`reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])` 计算 `((((1+2)+3)+4)+5)`。左边的参数 *x*，是累积的值而右边的参数 *y*，是从 *sequence* 更新的值。如果可选的 *initializer* 存在，it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty. 如果没有指定 *initializer* 且 *sequence* 仅包含一个元素，则返回第一个元素。

大致上等价于：

```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```

### 11.2. os.path — 通用路径名操作
**Source code:** [Lib/posixpath.py](https://github.com/python/cpython/tree/3.6/Lib/posixpath.py) (for POSIX), [Lib/ntpath.py](https://github.com/python/cpython/tree/3.6/Lib/ntpath.py) (for Windows NT), and [Lib/macpath.py](https://github.com/python/cpython/tree/3.6/Lib/macpath.py) (for Macintosh)

这个模块实现了一些关于路径名的有用的函数。读或写文件请看 [open()](https://docs.python.org/3.6/library/functions.html#open)，访问文件系统请看 [os](https://docs.python.org/3.6/library/os.html#module-os) 模块。

os.path.**dirname**(*path*)  
返回路径名 *path* 的目录名。

*在版本3.6中发生变化：* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。

os.path.**exists**(*path*)  
如果 *path* 指向一个存在的路径或者一个打开的文件描述符则返回 `True`。如果指向损坏的符号链接，则返回 `False`。在一些平台，如果被请求的文件没有被授予执行 [os.stat()](https://docs.python.org/3.6/library/os.html#os.stat) 的权限，则这个函数可能返回 `False`，即使这个 *path* 物理存在。

*在版本3.3中发生变化：* *path* 现在可以是一个整型数：如果它是一个打开的文件描述符则返回 `True`，否则返回 `False`。

*在版本3.6中发生变化：* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。

os.path.**join**(_path, *paths_)  
智能地连接一个或多个路径组件。返回值是 *path* 和所有 _*paths_ 成员的串联，且除了最后一个部分，每一个非空的部分后面都跟着一个正确的目录分隔符 (`os.sep`)，这意味着如果最后一个部分为空则结果将必定以一个分隔符结尾。如果一个组件是一个绝对路径，则所有前面的组件都被丢弃且连接从绝对路径组件继续。

在 Windows 平台，当遇到一个绝对路径组件 (如，`r'\foo'`) 时驱动器号不重置。如果一个组件包含一个驱动器号，则所有前面的组件被丢弃且驱动器号被重置。注意，因为每个驱动器都有一个当前目录，`os.path.join("c:", "foo")` represents a path relative to the current directory on drive `C:` (`c:foo`), not `c:\foo`。

*在版本3.6中发生变化：* *path* 和 *paths* 接受 [path-like object](https://docs.python.org/3.6/glossary.html#term-path-like-object)。

#### 16.1.8. 各种各样的系统信息
**下面的数据值被用于支持路径操作运算。这些是为所有平台定义。**

高层次的路径名操作被定义在 [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path) 模块中。

os.**sep**  
操作系统用来分隔路径名组件的字符。POSIX 为 `'/'` 而 Windows 为 `'\\'`。Note that knowing this is not sufficient to be able to parse or concatenate pathnames — 使用 [os.path.split()](https://docs.python.org/3.6/library/os.path.html#os.path.split) 和 [os.path.join()](https://docs.python.org/3.6/library/os.path.html#os.path.join) — 但它偶尔是有用的。Also available via [os.path](https://docs.python.org/3.6/library/os.path.html#module-os.path)。

#### 16.2.3. 类层次结构
![class hierarchy](/image/tpsl_16_2_3_class_hierarchy.png)

##### 16.2.3.1. I/O 基类

*class* io.**IOBase**  
所有 I/O 类的抽象基类，作用于字节流。没有公共构造函数（constructor）。

从一个文件读取或写入二进制数据的基本类型是 [bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes)。其它 [bytes-like object](https://docs.python.org/3.6/glossary.html#term-bytes-like-object) 也可以作为方法参数被接受。在某些情况下，例如 [readinto()](https://docs.python.org/3.6/library/io.html#io.RawIOBase.readinto)，要求一个可写的对象如 [bytearray](https://docs.python.org/3.6/library/stdtypes.html#bytearray)。文本 I/O 类对 [str](https://docs.python.org/3.6/library/stdtypes.html#str) 数据有效。

[IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 也是一个上下文管理器，因此支持 [with](https://docs.python.org/3.6/reference/compound_stmts.html#with) 声明。在这个例子中，*file* is closed after the [with](https://docs.python.org/3.6/reference/compound_stmts.html#with) statement’s suite is finished——即使出现异常：

```python
>>> with open('spam.txt', 'w') as file:
...     file.write('Spam and eggs!')
...
14
>>> file.closed
True
```

[IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 提供这些数据属性和方法：

**closed**  
如果流是关闭的，则返回 `True`。

*class* io.**RawIOBase**  
原始二进制 I/O 的基类。它继承 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase)。没有公共构造函数。

除了从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的属性和方法，[RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 还提供下面的方法：

**read**(*size=-1*)  
Read up to *size* bytes from the object and return them. 为了方便起见，如果 *size* 没有指定或者为 -1, all bytes until EOF are returned. Otherwise, only one system call is ever made. Fewer than *size* bytes may be returned if the operating system call returns fewer than *size* bytes.

如果返回 0 字节，且 *size* 不是 0，this indicates end of file. If the object is in non-blocking mode and no bytes are available, `None` is returned.

默认实现遵守 [readall()](https://docs.python.org/3.6/library/io.html#io.RawIOBase.readall) 和 [readinto()](https://docs.python.org/3.6/library/io.html#io.RawIOBase.readinto)。

*class* io.**BufferedIOBase**  
支持某种缓冲的二进制流的基类。它继承 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase)。没有公共构造函数。

除了那些从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的方法和属性，[BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 还提供或重写了这些方法和属性：

**read**(*size=-1*)  
Read and return up to *size* bytes. If the argument is omitted, `None`, or negative, data is read and returned until EOF is reached. An empty [bytes](https://docs.python.org/3.6/library/stdtypes.html#bytes) object is returned if the stream is already at EOF.

##### 16.2.3.2. 原始文件 I/O
*class* io.**FileIO**(*name, mode='r', closefd=True, opener=None*)  
[FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO) 代表一个包含字节数据的操作系统级别的文件。它实现了 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 接口 (因此也实现了 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 接口)。

除了从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 和 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 继承的属性和方法，[FileIO](https://docs.python.org/3.6/library/io.html#io.FileIO) 还提供下面的数据属性：

**mode**  
构造函数中指定的模式。

##### 16.2.3.3. 缓冲流
缓冲 I/O 流比原始 I/O 流为 I/O 设备提供了一个更高层次的接口。

*class* io.**BufferedReader**(*raw, buffer_size=DEFAULT_BUFFER_SIZE*)  
除了那些从 [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 和 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的方法，[BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader) 还提供或重写了这些方法：

**read**([*size*])  
读取并返回 *size* 字节，或者如果 *size* 没有给出或者是负数，until EOF or if the read call would block in non-blocking mode.

*class* io.**BufferedWriter**(*raw, buffer_size=DEFAULT_BUFFER_SIZE*)  
一个为可写的，连续的 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 对象提供更高层次访问的缓冲区。它继承 [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase)。当向这个对象写数据时，数据通常被放进一个内部缓冲区。缓冲区在多种条件下将被写到底层的 [RawIOBase](https://docs.python.org/3.6/library/io.html#io.RawIOBase) 对象，包括：

* 对所有挂起的数据来说，当缓冲区太小时；
* 当 [flush()](https://docs.python.org/3.6/library/io.html#io.BufferedWriter.flush) 被调用时；
* 当 seek() 被请求时(对于 [BufferedRandom](https://docs.python.org/3.6/library/io.html#io.BufferedRandom) 对象);
* 当 [BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter) 对象被关闭或者销毁时。 

除了那些从 [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 和 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的方法，[BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter) 还提供或重写了这些方法：

**write**(*b*)  
写入 [bytes-like 对象](https://docs.python.org/3.6/glossary.html#term-bytes-like-object) *b*，并返回写入的字节数。When in non-blocking mode, a [BlockingIOError](https://docs.python.org/3.6/library/exceptions.html#BlockingIOError) is raised if the buffer needs to be written out but the raw stream blocks.

*class* io.**BufferedRandom**(*raw, buffer_size=DEFAULT_BUFFER_SIZE*)  
一个随机访问流的缓冲区接口。它继承 [BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader) 和 [BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter), and further supports seek() and tell() functionality.

The constructor creates a reader and writer for a seekable raw stream, given in the first argument. 如果 *buffer_size* 被省略，则它默认为 [DEFAULT_BUFFER_SIZE](https://docs.python.org/3.6/library/io.html#io.DEFAULT_BUFFER_SIZE)。

[BufferedRandom](https://docs.python.org/3.6/library/io.html#io.BufferedRandom) 可以做任何 [BufferedReader](https://docs.python.org/3.6/library/io.html#io.BufferedReader) 或者 [BufferedWriter](https://docs.python.org/3.6/library/io.html#io.BufferedWriter) 能做的事。

```python
>>> import io
>>> issubclass(io.BufferedRandom, io.BufferedReader)
False
>>> issubclass(io.BufferedRandom, io.BufferedWriter)
False
```

Python官方文档里说 `io.BufferedRandom` 继承 `io.BufferedReader` 和 `io.BufferedWriter`，但不知为何 `issubclass(io.BufferedRandom, io.BufferedReader)` 和 `issubclass(io.BufferedRandom, io.BufferedWriter)` 的返回结果都是 `False`。

##### 16.2.3.4. 文本 I/O
*class* io.**TextIOBase**  
文本流的基类。This class provides a character and line based interface to stream I/O. There is no readinto() method because Python’s character strings are immutable. 它继承 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase)。没有公共构造函数。

除了那些从 [IOBase](https://docs.python.org/3.6/library/io.html#io.IOBase) 继承的属性和方法，[TextIOBase](https://docs.python.org/3.6/library/io.html#io.TextIOBase) 提供或重写了这些数据属性和方法：

**read**(*size*)  
从流中读取并返回至多 *size* 个字符作为一个单一 [str](https://docs.python.org/3.6/library/stdtypes.html#str)。如果 *size* 是负数或者 `None`, reads until EOF.

*class* io.**TextIOWrapper**(*buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False*)  
A buffered text stream over a [BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) binary stream. 它继承 [TextIOBase](https://docs.python.org/3.6/library/io.html#io.TextIOBase)。

#### 16.3.1. 函数
time.**sleep**(*secs*)  
将当前线程按指定的秒数推迟执行。参数可以是一个浮点数以指定一个更精确的睡眠时间。The actual suspension time may be less than that requested because any caught signal will terminate the [sleep()](https://docs.python.org/3.6/library/time.html#time.sleep) following execution of that signal’s catching routine. Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.

*在版本3.5中发生变化：* The function now sleeps at least *secs* even if the sleep is interrupted by a signal, except if the signal handler raises an exception (原理请看 [PEP 475](https://www.python.org/dev/peps/pep-0475))。

### 16.5. getopt — C-风格的命令行选项解析器
**Source code:** [Lib/getopt.py](https://github.com/python/cpython/tree/3.6/Lib/getopt.py)

这个模块提供2个函数和1个异常：

getopt.**getopt**(*args, shortopts, longopts=[]*)  
分析命令行选项和参数列表。*args* 是被分析的参数列表，不包含首部的正在运行的程序引用。通常，这意为 `sys.argv[1:]`。*shortopts* 是脚本想要识别的选项字母字符串，要求一个参数的选项后面跟随一个冒号(`':'`；也就是，Unix getopt() 使用的相同的格式)。

**注意：** 和 GUN `getopt()` 不同，在一个非选项参数之后，所有更远的参数也都被认为是非选项。这和非GUN Unix系统的工作方式相似。

*longopts*，如果指定，必须是一个应该被支持的长选项名称的字符串列表。前导字符 `'--'` 不应该包含在选项名中。要求一个参数的长选项后面应该跟随一个等号(`'='`)。不支持可选参数。如果仅接受长选项，则 *shortopts* 应该是一个空串。命令行中的长选项只要它们提供的选项名前缀可以精确地匹配一个可以接受的选项就能够被识别。例如，如果 *longopts* 是 `['foo', 'frob']`，则选项 `--fo` 将匹配为 `--foo`，但 `--f` 就不能唯一匹配了，所以将抛出 [GetoptError](https://docs.python.org/3.6/library/getopt.html#getopt.GetoptError)异常。

返回值由2个元素组成：the first is a list of `(option, value)` pairs; 第二个是选项列表被截取后余下的程序参数列表(这是 *args* 的尾部切片)。对于每一个返回的 option-and-value pair，选项作为它的第一个元素，用一个连字符作为短选项的前缀(例如, `'-x'`)或者两个连字符作为长选项的前缀(例如, `'--long-option'`)，选项参数作为它的第二个元素，如果选项没有参数，则用一个空串。选项出现在列表中的顺序与它们被发现的顺序相同，因此允许多次出现。长选项和短选项可以混合。

#### 16.6.2. 日志级别
日志级别的数值已在下表给出。如果你想自定义级别这将是你最感兴趣的，它们必须有相对于预定义级别的特定的值。如果你使用相同的数值定义一个级别，它将覆盖预定义的值，且预定义的名称也将丢失。

|Level       |Numeric value  |
|------------|---------------|
|`CRITICAL`  |50             |
|`ERROR`     |40             |
|`WARNING`   |30             |
|`INFO`      |20             |
|`DEBUG`     |10             |
|`NOTSET`    |0              |

#### 16.6.7. LogRecord属性
LogRecord有许多属性，大多数来源于构造函数的参数。(注意，LogRecord构造函数的参数名称与LogRecord属性名称之间并非总是正确对应。)这些属性可以用来合并由记录转换成格式化字符串的数据。下表列出了（按字母顺序）属性名称，它们的意义以及对应的 %-style 格式化字符串占位符。

如果你使用 {}-formatting ([str.format()](https://docs.python.org/3.6/library/stdtypes.html#str.format)), 那么在格式化字符串中你可以使用 `{attrname}` 作为占位符。如果你使用 \$-formatting ([string.Template](https://docs.python.org/3.6/library/string.html#string.Template)), 那么使用 `${attrname}` 形式。在这两种情况下，当然，用你实际要用的属性名称替换 `attrname`。

在使用 {}-formatting 的情况下，你可以通过在属性名称之后指定格式化标志，用冒号(:)分隔。例如：`{msecs:03d}` 占位符将格式化毫秒值 `4` 为 `004`。关于可用选项的全部细节请参考 [str.format()](https://docs.python.org/3.6/library/stdtypes.html#str.format) 文档。

|Attribute name  |Format                     |Description                     |
|----------------|---------------------------|--------------------------------|
|args            |你不必自己格式化这个          |参数元组结合 `msg` 以产生 `message`，或者一个字典的值用来结合<br> `msg`（当仅有一个参数，且它是一个字典）。
|levelname       |`%(levelname)s`            |消息的文本日志级别(`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`)                                |
|message         |`%(message)s`              |记录的消息，计算 `msg % args`。当 [Formatter.format()](https://docs.python.org/3.6/library/logging.html#logging.Formatter.format) 被<br>调用时，这个属性被设置。
|msg             |你不必自己格式化这个          |传递给原始日志调用的格式化字符串。与 `args` 合并以产生 <br>`message`，或者一个任意对象（参考[使用任意对象作为消息](https://docs.python.org/3.6/howto/logging.html#arbitrary-object-messages)）。    

#### 16.6.10. 模块级别的函数
除了上面描述的类，还有一些模块级别的函数。

logging.**basicConfig**(_**kwargs_)  
通过创建一个带一个默认 [Formatter](https://docs.python.org/3.6/library/logging.html#logging.Formatter) 的 [StreamHandler](https://docs.python.org/3.6/library/logging.handlers.html#logging.StreamHandler) 来为日志系统做基本配置，并将其添加到根记录器。如果没有为根记录器定义处理器，则函数 [debug()](https://docs.python.org/3.6/library/logging.html#logging.debug), [info()](https://docs.python.org/3.6/library/logging.html#logging.info), [warning()](https://docs.python.org/3.6/library/logging.html#logging.warning), [error()](https://docs.python.org/3.6/library/logging.html#logging.error) 和 [critical()](https://docs.python.org/3.6/library/logging.html#logging.critical) 将自动调用
[basicConfig()](https://docs.python.org/3.6/library/logging.html#logging.basicConfig)。

如果已经为根记录器配置了处理器，则这个函数什么也不做。

**注意：** 这个函数应该在其它线程启动以前由main线程调用。在Python版本2.7.1和3.2以前，如果这个函数被多线程调用，可能（尽管这种情况很少出现）会使处理器（handler）被多次添加到根记录器，这将导致意外结果，如日志中的消息重复。

支持下列关键字参数（keyword arguments）。  

|Format     |Description    |
|-----------|---------------|
`format`    |为处理器使用指定的格式化字符串
`level`     |设置根记录器级别为指定的级别

#### 16.16.2. ctypes reference
##### 16.16.2.1. 查找共享库
当用编译语言编程时，当编译或者链接一个程序及当程序运行时，共享库被访问。

The purpose of the find_library() function is to locate a library in a way similar to what the compiler or runtime loader does (在一个共享库有几个版本的平台上应该加载最新版本), while the ctypes library loaders act like when a program is run, and call the runtime loader directly.

ctypes.util 模块提供了一个函数可以帮助检测要加载的库。

ctypes.util.**find_library**(*name*)  
尝试查找一个库并返回一个路径名。*name* 是不带任何前缀像 `lib`，后缀像 `.so`，`.dylib` 或版本号的库名 (this is the form used for the posix linker option -l). 如果不能找到库则返回 `None`。

准确的功能依赖于系统。

在Linux中，find_library() 尝试运行外部程序 (`/sbin/ldconfig`, `gcc`, `objdump` 和 `ld`) 查找库文件。它返回库文件的文件名。

*在版本3.6中发生变化：* 在Linux中，当搜索库时环境变量 `LD_LIBRARY_PATH` 的值被使用，如果一个库不能通过任何其它方法找到。

这里有一些例子：  
在Linux上：

```python
>>> from ctypes.util import find_library
>>> find_library("m")
'libm.so.6'
>>> find_library("c")
'libc.so.6'
>>> find_library("bz2")
'libbz2.so.1.0'
```

在macOS上，find_library() 尝试几个预定义的名称方案和路径以定位库，并返回一个完整的路径名如果成功的话：

```python
>>> from ctypes.util import find_library
>>> find_library("c")
'/usr/lib/libc.dylib'
>>> find_library("m")
'/usr/lib/libm.dylib'
>>> find_library("bz2")
'/usr/lib/libbz2.dylib'
>>> find_library("AGL")
'/System/Library/Frameworks/AGL.framework/AGL'
>>>
```

在Windows上, find_library() 沿着系统搜索路径搜索，并返回完整的路径名，但因为没有预定义的名称方案一个像 `find_library("c")` 的调用将失败并返回 `None`。

```python
>>> from ctypes.util import find_library
>>> find_library("c")
>>> find_library("m")
>>> find_library("bz2")
>>> find_library("apphelp")
'C:\\WINDOWS\\system32\\apphelp.dll'
>>> find_library("aphostclient")
'C:\\WINDOWS\\system32\\aphostclient.dll'
>>> find_library("APHostClient")
'C:\\WINDOWS\\system32\\APHostClient.dll'
>>> find_library("xinstaller")
'C:\\WINDOWS\\xinstaller.dll'
>>>
```

If wrapping a shared library with [ctypes](https://docs.python.org/3/library/ctypes.html#module-ctypes), it *may* be better to determine the shared library name at development time, and hardcode that into the wrapper module instead of using find_library() to locate the library at runtime.

##### 16.16.2.5. 实用函数
ctypes.util.**find_library**(*name*)  
尝试查找一个库并返回一个路径名。*name* 是不带任何前缀像 `lib`，后缀像 `.so`，`.dylib` 或版本号的库名 (this is the form used for the posix linker option -l). 如果不能找到库则返回 `None`。

准确的功能依赖于系统。

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

*class* urllib.request.**ProxyHandler**(*proxies=None*)  
使请求通过一个代理。如果给定 *proxies*，它必须是一个映射协议名称到代理URLs的字典。默认是从环境变量 `<protocol>_proxy` 中读取代理列表。如果没有设置代理环境变量，则在 Windows 环境下代理设置从注册表的Internet设置部分获取，而在 macOS 环境下代理信息从macOS系统配置框架中获取。

禁用自动检测代理可以通过传递一个空字典实现。

`no_proxy` 环境变量可以用于指定不应通过代理到达的主机；如果设置，它应该是一个逗号分隔的主机名后缀列表，可以选择附加 `:port`，例如 `cern.ch,ncsa.uiuc.edu,some.host:8080`。

**注意：** 如果设置了 `REQUEST_METHOD` 变量 `HTTP_PROXY` 将被忽略；请看关于 [getproxies()](https://docs.python.org/3.6/library/urllib.request.html#urllib.request.getproxies) 的文档。

### 21.8. urllib.parse — 将URLs解析为组件
**源代码:** [Lib/urllib/parse.py](https://github.com/python/cpython/tree/3.6/Lib/urllib/parse.py)

This module defines a standard interface to break Uniform Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.), to combine the components back into a URL string, and to convert a “relative URL” to an absolute URL given a “base URL.”

#### 21.8.1. URL解析
URL解析函数聚焦于将一个URL字符串分成多个组件，或组合URL组件为一个URL字符串。

urllib.parse.**urlparse**(*urlstring, scheme='', allow_fragments=True*)  
将一个URL解析为六个组件，返回一个6元组。这对应一个URL的常规结构：`scheme://netloc/path;parameters?query#fragment`。每一个元组元素都是一个字符串，也有可能是空的。The components are not broken up in smaller parts (例如，网络位置是一个单字符串), and % escapes are not expanded. 上面显示的分隔符不是结果的一部分，除了*路径*组件中的首部斜线，如果出现则保留。例如：

```python
>>> from urllib.parse import urlparse
>>> o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
>>> o
ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')
>>> o.scheme
'http'
>>> o.port
80
>>> o.geturl()
'http://www.cwi.nl:80/%7Eguido/Python.html'
>>>
```

根据 [RFC 1808](https://tools.ietf.org/html/rfc1808.html) 中的语法规范，只有当netloc由 '//' 正确引出时，urlparse 才能识别一个netloc。否则输入被假定是一个相对链接从而导致以一个路径组件开始。

```python
>>> from urllib.parse import urlparse
>>> urlparse('//www.cwi.nl:80/%7Eguido/Python.html')
ParseResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')
>>> urlparse('www.cwi.nl/%7Eguido/Python.html')
ParseResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html', params='', query='', fragment='')
>>> urlparse('help/Python.html')
ParseResult(scheme='', netloc='', path='help/Python.html', params='', query='', fragment='')
>>>
```

*scheme* 参数给定默认的寻址方案，仅用于当URL没有指定寻址方案时。它应该与 *urlstring* 是同种类型 (文本或字节), except that the default value `''` is always allowed, and is automatically converted to `b''` if appropriate.

如果 *allow_fragments* 参数是 false, 则分片标识符不被识别。相反，它们将被解析为 path, parameters 或 query 组件的一部分, 且在返回值中 `fragment` 被设置为空串。

返回值实际上是 [tuple](https://docs.python.org/3.6/library/stdtypes.html#tuple) 的一个子类的一个实例。This class has the following additional read-only convenience attributes:

Attribute   |Index  |Value                  |Value if not present
------------|-------|-----------------------|--------------------
scheme      |0      |URL scheme specifier   |*scheme* parameter
netloc      |1      |网络定位部分             |空串
path        |2      |Hierarchical path      |空串
params      |3      |最后一个路径元素的参数    |空串
query       |4      |Query 组件              |空串
fragment    |5      |分片标识符               |空串
username    |       |用户名                  |[None](https://docs.python.org/3.6/library/constants.html#None)
password    |       |密码                    |[None](https://docs.python.org/3.6/library/constants.html#None)
hostname    |       |主机名（小写字母）        |[None](https://docs.python.org/3.6/library/constants.html#None)
port        |       |数字端口号，如果存在      |[None](https://docs.python.org/3.6/library/constants.html#None)

如果在URL中指定了一个无效的端口，则读取端口属性时将抛出一个 [ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)。关于结果对象的详细信息请看 [Structured Parse Results](https://docs.python.org/3.6/library/urllib.parse.html#urlparse-result-object) 章节。

`netloc` 属性中不匹配的方括号将抛出一个 [ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)。

*在版本3.2中发生变化：* 增加解析IPv6 URL的功能。

*在版本3.3中发生变化：* The fragment is now parsed for all URL schemes (除非 *allow_fragment* 是 false), in accordance with [RFC 3986](https://tools.ietf.org/html/rfc3986.html). 之前，存在一个支持分片的方案的白名单。

*在版本3.6中发生变化：* 现在，超出范围的端口号抛出 [ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)，而不是返回 [None](https://docs.python.org/3.6/library/constants.html#None)。

urllib.parse.**urljoin**(*base, url, allow_fragments=True*)  
通过组合一个 "base URL" (*base*) 和另一个 URL (*url*) 来构造一个完整的 ("绝对的") URL。Informally, this uses components of the base URL, in particular the addressing scheme, the network location and (part of) the path, to provide missing components in the relative URL. 例如：

```python
>>> from urllib.parse import urljoin
>>> urljoin('https://docs.python.org/3.6/library/urllib.parse.html', 'urllib.error.html')
'https://docs.python.org/3.6/library/urllib.error.html'
>>>
```

The *allow_fragments* argument has the same meaning and default as for [urlparse()](https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.urlparse).

**注意：** 如果 *url* 是一个绝对 URL (即，以 `//` 或 `scheme://` 开头), 则 *url*’s 主机名和/或方案将出现在结果中。例如：

```python
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', '//www.python.org/%7Eguido')
'http://www.python.org/%7Eguido'
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'https://www.python.org/%7Eguido')
'https://www.python.org/%7Eguido'
>>>
```

If you do not want that behavior, preprocess the *url* with [urlsplit()](https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.urlsplit) and [urlunsplit()](https://docs.python.org/3.6/library/urllib.parse.html#urllib.parse.urlunsplit), removing possible *scheme* and *netloc* parts.

*在版本3.5中发生变化：* Behaviour updated to match the semantics defined in [RFC 3986](https://tools.ietf.org/html/rfc3986.html).

### 21.9. urllib.error — urllib.request抛出的异常类
**Source code:** [Lib/urllib/error.py](https://github.com/python/cpython/tree/3.6/Lib/urllib/error.py)

[urllib.error](https://docs.python.org/3.6/library/urllib.error.html#module-urllib.error) 模块为[urllib.request](https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request) 抛出的异常定义了异常类。异常基类是 [URLError](https://docs.python.org/3.6/library/urllib.error.html#urllib.error.URLError).

下列异常通过 [urllib.error](https://docs.python.org/3.6/library/urllib.error.html#module-urllib.error) 适当地抛出：

*exception* urllib.error.**URLError**  
当处理程序遇到一个问题时，抛出这个异常 (或者衍生的异常)。它是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的一个子类。

**reason**  
这个错误的原因。它可以是一个消息字符串或者另一个异常实例。

*在版本3.3中发生变化：* [URLError](https://docs.python.org/3.6/library/urllib.error.html#urllib.error.URLError) has been made a subclass of [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) instead of [IOError](https://docs.python.org/3.6/library/exceptions.html#IOError).

```python
>>> import urllib.error
>>> issubclass(urllib.error.ContentTooShortError, urllib.error.URLError)
True
>>> issubclass(urllib.error.HTTPError, urllib.error.URLError)
True
>>> issubclass(urllib.error.URLError, OSError)
True
```

从Python 3.3开始，[IOError](https://docs.python.org/3.6/library/exceptions.html#IOError) 是 [OSError](https://docs.python.org/3.6/library/exceptions.html#OSError) 的别名。

### 21.10. urllib.robotparser — 解析robots.txt
**源代码：** [Lib/urllib/robotparser.py](https://github.com/python/cpython/tree/3.6/Lib/urllib/robotparser.py)

这个模块提供一个单一的类，[RobotFileParser](https://docs.python.org/3.6/library/urllib.robotparser.html#urllib.robotparser.RobotFileParser), 这个类回答关于一个具体的用户代理是否能在一个发布了 `robots.txt` 的网站上提取一个URL的问题。关于 `robots.txt` 文件结构的详细信息，请参考 [http://www.robotstxt.org/orig.html](http://www.robotstxt.org/orig.html).

*class* urllib.robotparser.**RobotFileParser**(*url=''*)  
This class provides methods to read, parse and answer questions about the `robots.txt` file at *url*.

**set_url**(*url*)  
设置 `robots.txt` 文件的URL

**read()**  
读取 `robots.txt` URL 并将其提供给解析器。

**can_fetch**(*useragent, url*)  
根据解析的 `robots.txt` 文件中的规则，如果 *useragent* 允许获取 *url* ，则返回 `True`，否则返回 `False`。

### 21.12. http.client — HTTP协议客户端
**Source code:** [Lib/http/client.py](https://github.com/python/cpython/tree/3.6/Lib/http/client.py)

这个模块定义实现HTTP和HTTPS协议客户端的类。它通常不被直接使用 — 模块 [urllib.request](https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request) 使用它处理HTTP和HTTPS URLs。

**另请参阅：** 更高层次的HTTP客户端接口推荐 [Requests package](http://docs.python-requests.org/)。

**注意：** 如果Python编译了SSL支持 (通过 [ssl](https://docs.python.org/3.6/library/ssl.html#module-ssl) 模块)，HTTPS支持才可用。

这个模块提供了下面的类：

*class* http.client.**HTTPResponse**(*sock, debuglevel=0, method=None, url=None*)  
Class whose instances are returned upon successful connection. Not instantiated directly by user.

*在版本3.4中发生变化：* *strict* 参量被移除了。HTTP 0.9 风格 “Simple Responses” 不再支持。

#### 21.12.2. HTTPResponse对象
An [HTTPResponse](https://docs.python.org/3.6/library/http.client.html#http.client.HTTPResponse) instance wraps the HTTP response from the server. It provides access to the request headers and the entity body. The response is an iterable object and can be used in a with statement.

*在版本3.5中发生变化：* 现在实现了 [io.BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 接口，它的所有的读操作都支持。

HTTPResponse.**read**([*amt*])  
读取并返回响应正文，或者直到下一个 *amt* 字节。

HTTPResponse.**version**  
服务器使用的HTTP协议版本。HTTP/1.0 为 10，HTTP/1.1 为 11。

HTTPResponse.**status**  
服务器返回的状态代码。

### 21.21. socketserver — 一个网络服务器框架
**Source code:** [Lib/socketserver.py](https://github.com/python/cpython/tree/3.6/Lib/socketserver.py)

[socketserver](https://docs.python.org/3.6/library/socketserver.html#module-socketserver) 模块简化了写网络服务器的任务。

有四个基本的具体的服务器类：

*class* socketserver.**TCPServer**(*server_address, RequestHandlerClass, bind_and_activate=True*)  
这个类使用在客户端与服务器之间提供连续的数据流的互联网TCP协议，如果 *bind_and_activate* 是 true, 则构造函数自动地尝试调用 [server_bind()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.server_bind) 和 [server_activate()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.server_activate)。其它参数（parameters）被传递给基类 [BaseServer](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer)。

#### 21.21.2. 服务器对象
*class* socketserver.**BaseServer**(*server_address, RequestHandlerClass*)  
这是模块（socketserver）中所有服务器对象的超类。它定义了接口，如下，但大多数方法都没有实现，方法在子类中实现。两个参数（parameters）被分别存储在 [server_address](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.server_address) 和 [RequestHandlerClass](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.RequestHandlerClass) 属性中。

**serve_forever**(*poll_interval=0.5*)  
处理请求直到一个明确的 [shutdown()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.shutdown) 请求。每 *poll_interval* 秒投票关闭。忽略 [timeout](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.timeout) 属性。它也调用 [service_actions()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.service_actions)，`service_actions()` 可能被子类或混入类用来给一个给定的服务提供具体的动作。例如，[ForkingMixIn](https://docs.python.org/3.6/library/socketserver.html#socketserver.ForkingMixIn) 类使用 [service_actions()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.service_actions) 清理僵尸子进程。

*在3.3版本中发生变化：* 为 `serve_forever` 方法增加 `service_actions` 调用。

**service_actions()**  
这在 [serve_forever()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.serve_forever) 循环中被调用。这个方法可以被子类或混入类重写以便给一个给定的服务执行特定的动作，例如清理动作。

*版本3.3中新增。*

**shutdown()**  
Tell the [serve_forever()](https://docs.python.org/3.6/library/socketserver.html#socketserver.BaseServer.serve_forever) loop to stop and wait until it does.

**RequestHandlerClass**  
用户提供的请求处理程序类；每次请求都会创建一个该类的实例。

**server_address**  
服务器监听的地址。地址格式的变化依赖于协议族；详细信息请看 [socket](https://docs.python.org/3.6/library/socket.html#module-socket) 模块的文档。对于 Internet protocols (IP), 这是一个包含一个给定地址的字符串和一个整型数端口号的元组：`('127.0.0.1', 80)`, 例如。

### 21.22. http.server — HTTP 服务器
**源代码:** [Lib/http/server.py](https://github.com/python/cpython/tree/3.6/Lib/http/server.py)

这个模块定义实现HTTP服务器（Web服务器）的类。

*class* http.server.**SimpleHTTPRequestHandler**(*request, client_address, server*)  
这个类为当前目录及其子目录下的文件服务，直接映射目录结构到HTTP请求。

很多工作，例如解析请求，由基类 [BaseHTTPRequestHandler](https://docs.python.org/3.6/library/http.server.html#http.server.BaseHTTPRequestHandler) 完成。这个类实现了 [do_GET()](https://docs.python.org/3.6/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET) 和 [do_HEAD()](https://docs.python.org/3.6/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_HEAD) 方法。

下面是定义为 [SimpleHTTPRequestHandler](https://docs.python.org/3.6/library/http.server.html#http.server.SimpleHTTPRequestHandler) 类级别的属性：

**extensions_map**  
一个映射后缀到MIME类型的字典。默认值由空串表明，且被认为是 `application/octet-stream`。映射不区分大小写，所以应该仅包含小写键。

```python
from http.server import SimpleHTTPRequestHandler


SimpleHTTPRequestHandler.extensions_map = {
    '.html': 'text/html',
    '.sh': 'test/x-sh',
    '.js': 'application/javascript',
    '.pac': 'application/x-ns-proxy-autoconfig',
    '': 'application/octet/stream',
}

```

### 29.1. sys — 系统专用参量和函数
这个模块提供访问一些由解释器使用或维护的变量及与解释器有极大关系的函数。这个模块总是可用的。

sys.**argv**  
传递给Python脚本的命令行参数列表。`argv[0]` 是脚本的名字 (是否是full pathname依赖于操作系统)。If the command was executed using the [-c](https://docs.python.org/3.6/using/cmdline.html#cmdoption-c) command line option to the interpreter, `argv[0]` 将被设置为字符串 `'-c'`。如果没有脚本名称传递给Python解释器，则 `argv[0]` 是空串。

循环处理（loop over）标准输入，或者命令行中给出的文件列表，参考 [fileinput](https://docs.python.org/3.6/library/fileinput.html#module-fileinput) 模块。

sys.**exit**([*arg*])  
退出Python。

可选参数 *arg* 可以是给出退出状态的整型数 (默认为0)，或者另一种类型的对象。如果它是一个整型数，shells和与shells类似的认为0是"成功终止"，而任何非0的值被认为是"不正常的终止"。大多数系统要求它在0-127的范围内，否则将产生未定义的结果。一些系统对特定的退出代码分配特定的含义有一个约定，但这些通常是非充分开发的；Unix程序通常使用 2 表示命令行语法错误，而 1 表示所有其它类型的错误。如果传递的是另一种类型的对象，`None` 等价于传递 0，而任何其它对象则打印到 [stderr](https://docs.python.org/3.6/library/sys.html#sys.stderr) 并导致一个退出代码 1。特别是，当一个错误发生的时候，`sys.exit("some error message")` 是退出一个程序的一种快速的方式。

sys.**path**  
一个指定模块搜索路径的字符串列表。Initialized from the environment variable [PYTHONPATH](https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONPATH), plus an installation-dependent default.

As initialized upon program startup, the first item of this list, `path[0]`, is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), `path[0]` is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted *before* the entries inserted as a result of [PYTHONPATH](https://docs.python.org/3.6/using/cmdline.html#envvar-PYTHONPATH).

程序为了自己的目的可以自由修改这个列表。只有 strings 和 bytes 可以被添加到 [sys.path](https://docs.python.org/3.6/library/sys.html#sys.path)；所有其它数据类型在导入期间被忽略。

sys.**version_info**  
一个包含版本号的5个组成部分的元组：*major*, *minor*, *micro*, *releaselevel*, and *serial*. 除了 *releaselevel* 所有值都是整型数；发行版级别是 `'alpha'`, `'beta'`, `'candidate'`, 或者 `'final'`. Python版本2.0对应的 `version_info` 值是 `(2, 0, 0, 'final', 0)`. 组件也可以通过名称来访问，如 `sys.version_info[0]` 等价于 `sys.version_info.major`。

*在版本3.1中发生了变化：* 增加了名称组件属性。

# Python教程
## 2. 使用Python解释器
### 2.1. 调用解释器
Typing an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. 如果无效，你可以通过输入下面的命令：`quit()` 退出解释器。

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