# Python文档
Python相关文档。  

* [Python 3 标准库](#python-3-标准库)
	* [2. 内置函数](#2-内置函数)
    * [3. 内置常量](#3-内置常量)
	* [4. 内置类型](#4-内置类型)
        * [4.2. 布尔运算 — and, or, not](#42-布尔运算--and-or-not)
		* [4.6. 序列类型 — 列表, 元组, range](#46-序列类型--列表-元组-range)
            * [4.6.1. 通用序列操作](#461-通用序列操作)
            * [4.6.3. 可变序列类型](#463-可变序列类型)
			* [4.6.4. 列表](#464-列表)
            * [4.6.6. Ranges](#466-ranges)
		* [4.7. 文本序列类型 — str](#47-文本序列类型--str)
            * [4.7.1. 字符串方法](#471-字符串方法)
            * [4.7.2. printf-style 字符串格式化](#472-printf-style-字符串格式化)
            * [4.8.3. 字节和字节数组操作](#483-字节和字节数组操作)
		* [4.10. 映射类型 — 字典](#410-映射类型--字典)
			* [4.10.1. 字典视图对象](#4101-字典视图对象)
        * [4.13. 特殊属性](#413-特殊属性)
    * [5. 内置异常](#5-内置异常)
        * [5.2. 具体异常](#52-具体异常)
            * [5.2.1. OS异常](#521-os异常)
        * [8.1. datetime — 基本的日期和时间类型](#81-datetime--基本的日期和时间类型)
            * [8.1.1. 可用类型](#811-可用类型)
            * [8.1.2. timedelta对象](#812-timedelta对象)
            * [8.1.3. date对象](#813-date对象)
            * [8.1.4. datetime对象](#814-datetime对象)
        * [9.6. random — 生成伪随机数](#96-random--生成伪随机数)
            * [9.6.2. 用于整型数的函数](#962-用于整型数的函数)
            * [9.6.3. 用于序列的函数](#963-用于序列的函数)
        * [10.2. functools — 高阶函数和操作可调用对象](#102-functools--高阶函数和操作可调用对象)
    * [12. 数据持久性](#12-数据持久性)
        * [12.1. pickle — Python对象序列化](#121-pickle--python对象序列化)
            * [12.1.3. 模块接口](#1213-模块接口)
    * [13. 数据压缩和归档](#13-数据压缩和归档)
        * [13.1. zlib — 与gzip兼容的压缩](#131-zlib--与gzip兼容的压缩)
        * [13.5. zipfile — 与ZIP归档一起工作](#135-zipfile--与zip归档一起工作)
            * [13.5.1. ZipFile对象](#1351-zipfile对象)
    * [14. 文件格式](#14-文件格式)
        * [14.1. csv — CSV文件读写](#141-csv--csv文件读写)
            * [14.1.1. 模块内容](#1411-模块内容)
            * [14.1.4. Writer对象](#1414-writer对象)
                * [16.2.2.1. 内存流](#16221-内存流)
            * [16.2.3. 类层次结构](#1623-类层次结构)
                * [16.2.3.1. I/O 基类](#16231-io-基类)
                * [16.2.3.2. 原始文件 I/O](#16232-原始文件-io)
                * [16.2.3.3. 缓冲流](#16233-缓冲流)
                * [16.2.3.4. 文本 I/O](#16234-文本-io)
        * [16.5. getopt — C-风格的命令行选项解析器](#165-getopt--c-风格的命令行选项解析器)
            * [16.6.2. 日志级别](#1662-日志级别)
            * [16.6.7. LogRecord属性](#1667-logrecord属性)
            * [16.6.10. 模块级别的函数](#16610-模块级别的函数)
            * [16.16.2. ctypes reference](#16162-ctypes-reference)
                * [16.16.2.1. 查找共享库](#161621-查找共享库)
                * [16.16.2.5. 实用函数](#161625-实用函数)
        * [21.21. socketserver — 一个网络服务器框架](#2121-socketserver--一个网络服务器框架)
            * [21.21.2. 服务器对象](#21212-服务器对象)
        * [21.22. http.server — HTTP 服务器](#2122-httpserver--http-服务器)
    * [22. 互联网协议和支持](#22-互联网协议和支持)
        * [22.12. http.client — HTTP协议客户端](#2212-httpclient--http协议客户端)
            * [22.12.2. HTTPResponse对象](#22122-httpresponse对象)
        * [29.1. sys — 系统专用参量和函数](#291-sys--系统专用参量和函数)
* [Python语言参考](#python语言参考)
    * [3. 数据模型](#3-数据模型)
        * [3.2. 标准类型层次结构](#32-标准类型层次结构)
        * [3.3. 特殊方法名](#33-特殊方法名)
            * [3.3.6. 仿真可调用对象](#336-仿真可调用对象)
    * [7. 简单语句](#7-简单语句)
        * [7.3. assert语句](#73-assert语句)
        * [7.12. global语句](#712-global语句)
    * [8. 复合语句](#8-复合语句)
        * [8.5. with语句](#85-with语句)
* [Python教程](#python教程)
    * [2. 使用Python解释器](#2-使用python解释器)
        * [2.1. 调用解释器](#21-调用解释器)
    * [4. 更多控制流工具](#4-更多控制流工具)
        * [4.3. range() 函数](#43-range-函数)
        * [4.4. break 和 continue 语句, 和循环中的 else 子句](#44-break-和-continue-语句-和循环中的-else-子句)
    * [7. 输入和输出](#7-输入和输出)
        * [7.2. 读和写文件](#72-读和写文件)
            * [7.2.1. 文件对象的方法](#721-文件对象的方法)
* [PEPs](#peps)
    * [PEP 453 -- Explicit bootstrapping of pip in Python installations](#pep-453----explicit-bootstrapping-of-pip-in-python-installations)
        * [在Windows下执行脚本](#在windows下执行脚本)
* [术语表](#术语表)
* [cssselect](#cssselect)
* [Beautiful Soup](#beautiful-soup)
    * [输出](#输出)
        * [Pretty-printing](#pretty-printing)
* [lxml](#lxml)
    * [lxml.html](#lxmlhtml)
        * [解析HTML](#解析html)
            * [解析HTML片段](#解析html片段)
        * [HTML元素方法](#html元素方法)
* [Python Codes](#python-codes)
    * [download.py](#downloadpy)
    * [ssh.py](#sshpy)

[Python 2标准库](https://github.com/godontop/pythondocs/blob/master/python2/README.md)

# Python 3 标准库
## 2. 内置函数
Python解释器内置了许多总是可用的函数和类型。在这里以字母顺序列出它们。

|          |          |Built-in Functions|          |          |
|----------|----------|------------------|----------|----------|
|abs()     |          |                  |          |          |
|          |          |hex()             |          |          |
|          |          |id()              |          |          |
|          |          |int()             |          |          |
|          |          |isinstance()      |ord()     |          |
|          |          |                  |          |type()    |
|          |hasattr() |                  |          |          |

**abs**(*x*)  
返回一个数的绝对值。参数可以是一个整型数或者一个浮点数。如果参数是一个复数，its magnitude is returned.

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

**id**(*object*)  
返回一个对象的 “身份”。在这个对象的生命周期内这是一个保证唯一和不变的整型数。两个生命周期不重叠的对象可能有相同的 [id()](https://docs.python.org/3/library/functions.html#id) 值。

**CPython 实现细节：** 这是对象在内存中的地址。  

```python
>>> class >>> class A:
...     def __init__(self):
...         pass
...
>>> a = A()
>>> print(a)
<__main__.A object at 0x000001E4E5391518>
>>> id(a)
2082609894680
>>> hex(id(a))
'0x1e4e5391518'
>>> hex(id(a)).upper()
'0X1E4E5391518'
>>> hex(id(a))[0:2] + hex(id(a))[2:].upper()
'0x1E4E5391518'
>>>
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
<br />  

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

## 3. 内置常量
有一小部分常量在命名空间中。它们是：

**False**  
[bool](https://docs.python.org/3/library/functions.html#bool) 类型的false值。给 `False` 赋值是不合法的且会抛出一个 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)。

**True**  
[bool](https://docs.python.org/3/library/functions.html#bool) 类型的true值。给 `True` 赋值是不合法的且会抛出一个 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)。

**None**  
`NoneType` 类型唯一的值。`None` 经常用于表示一个不存在的值，如当默认参数没有传递给函数时。给 `None` 赋值是不合法的且会抛出一个 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)。

**\_\_debug\_\_**  
如果Python启动时没带 [-O](https://docs.python.org/3/using/cmdline.html#cmdoption-o) 选项则这个常量为真。另请参见 [assert](https://docs.python.org/3/reference/simple_stmts.html#assert) 语句。

**注意：** 名称 [None](https://docs.python.org/3/library/constants.html#None), [False](https://docs.python.org/3/library/constants.html#False), [True](https://docs.python.org/3/library/constants.html#True) 和 [__debug__](https://docs.python.org/3/library/constants.html#__debug__) 不能被再分配 (给它们赋值，哪怕是一个属性名称，也会抛出 [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError)), 所以它们可以被认为是 “true” 常量。

## 4. 内置类型
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

### 4.6. 序列类型 — 列表, 元组, range
有三种基本的序列类型：列表，元组, 和 range 对象。专门处理[二进制数据](https://docs.python.org/3/library/stdtypes.html#binaryseq)和[文本字符串](https://docs.python.org/3/library/stdtypes.html#textseq)的额外的序列类型在专门的章节中描述。

#### 4.6.1. 通用序列操作
大多数序列类型（不可变的和可变的）都支持下表中的操作。Python 提供的抽象基类 [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence) 使自定义序列类型正确地实现这些操作变得容易。

下表列出的序列操作按优先级升序排列。下表中，*s* 和 *t* 是相同类型的序列，*n*, *i*, *j* 和 *k* 是整型数，*x* 是符合由 *s* 所限制的类型及值的一个任意对象。

Operation  |Result                      |Notes
-----------|----------------------------|------
`s[i:j]`   |从 *i* 到 *j* 的 *s* 的分片  |(3)(4)

**注意：**

1. 

2. 

3. 

4. 从 *i* 到 *j* 的 *s* 的分片的定义就像序列的元素的索引为 *k* 且 `i <= k < j`。如果 *i* 或 *j* 大于 `len(s)`，使用 `len(s)`。如果 *i* 被忽略或者为 `None`，则使用 `0`。如果 *j* 被忽略或者为 `None`，使用 `len(s)`。如果 `i` 大于或等于 `j`，则分片为空。

```python
>>> s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> len(s)
7
>>> s[8:16]
[]
>>> s[len(s):len(s)]
[]
>>> s[3:16]
['d', 'e', 'f', 'g']
>>> s[3:len(s)]
['d', 'e', 'f', 'g']
>>>
```

#### 4.6.3. 可变序列类型
可变序列定义了下表中的操作。Python 提供的抽象基类 [collections.abc.MutableSequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence) 使自定义序列类型正确地实现这些操作变得更容易。

表中的 *s* 表示可变序列类型的一个实例，*t* 是任何可迭代对象，*x* 是符合由 *s* 所限制的类型及值的一个任意对象 (例如，[bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray) 仅接受符合 `0 <= x <= 255` 值限制的整型数)。

Operation                  |Result                |Notes
---------------------------|----------------------|-----
`s.extend(t)` 或 `s += t`  |用 `t` 的内容扩展 `s`  |

```python
>>> s = [1, 2]
>>> t = ('a', 'b')
>>> s.extend(t)
>>> print(s)
[1, 2, 'a', 'b']
>>>
```

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

#### 4.6.6. Ranges
[range](https://docs.python.org/3/library/stdtypes.html#range) 类型代表一种不可变的数字序列且通常用于在 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 循环中循环一个特定的次数。

*class* **range**(*stop*)  
*class* **range**(*start, stop*[*, step*])  
range 构造函数的参数必须是整型数(要么是内置 [int](https://docs.python.org/3/library/functions.html#int) 要么是任何实现了 `__index__` 特殊方法的对象)。如果省略了 *step* 参数，则它默认为 `1`。如果省略了 *start* 参数，则它默认为 `0`。如果 *step* 是 zero, 则抛出 [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)。

对于正数 *step*, 一个 range `r` 的内容由公式 `r[i] = start + step*i` 决定，其中 `i >= 0` 且 `r[i] < stop`。

对于负数 *step*, range的内容仍然由公式 `r[i] = start + step*i` 决定，但约束条件是 `i >= 0` 和 `r[i] > stop`。

如果 `r[0]` 不满足值的约束条件则range对象将为空。Ranges do support negative indices, but these are interpreted as indexing from the end of the sequence determined by the positive indices.

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

str.**upper**()  
返回一个字符串的副本且将所有的 cased characters（Cased characters are those with general category property being one of “Lu” (Letter, uppercase), “Ll” (Letter, lowercase), or “Lt” (Letter, titlecase).）转换为大写字母。 

#### 4.7.2. printf-style 字符串格式化
**注意：** 这里描述的格式化操作展示了一些导致若干常见错误的怪现象 (例如无法正确地显示元组和字典)。使用更新的[格式化字符串文字](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)，[str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) 接口，或者[模板字符串](https://docs.python.org/3/library/string.html#template-strings)可以帮助避免这些错误。这些替代选择每一个都提供了它们自己的权衡及简单，灵活，和/或可扩展性的好处。

字符串对象有一个唯一的内置运算： % 运算符 (模运算)。这也称为字符串*格式化*或*插值*运算符。给定 `format % values` (其中 *format* 是一个字符串)，`%` conversion specifications in *format* are replaced with zero or more elements of *values*. 效果与在C语言中使用 `sprintf()` 相似。

如果 *format* 要求一个单一参数，*values* 可以是一个单一的非元组对象。[\[5\]](https://docs.python.org/3/library/stdtypes.html#id16) 否则，*values* 必须是一个恰好带有由格式化字符串指定的项数的元组，或者一个单一的映射对象 (例如，一个字典)。

一个转换说明符包含2个或多个字符并拥有下面的组件，这些组件必须按下面的顺序出现：

1. `'%'` 字符，标识说明符的开始。
2. 映射键 (可选)，由一个圆括号括起来的字符序列组成 (例如， `(somename)` )。
3. 转换标志 (可选)，影响一些转换类型的结果。
4. 最小字段宽度 (可选)。If specified as an `'*'` (星号), the actual width is read from the next element of the tuple in *values*, and the object to convert comes after the minimum field width and optional precision.
5. 精度 (可选)，表示为一个 `'.'` (点) 后跟精度。If specified as `'*'` (一个星号)， the actual precision is read from the next element of the tuple in *values*, and the value to convert comes after the precision.
6. Length modifier (可选).
7. 转换类型。

当右边的参数是一个字典 (或者其它映射类型)时，则字符串中的 *formats* 必须包含一个圆括号括起来的映射键到那个字典且立即插入到 `'%'` 字符后面。映射键从映射中选择将被格式化的值。例如：

```python
>>> print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.
>>> print('%(language)s has %(number)03d quote types.' %
...       {"language": "Python", "number": 22})
Python has 022 quote types.
>>> print('%(language)s has %(number)03d quote types.' %
...       {"language": "Python", "number": 222})
Python has 222 quote types.
>>> print('%(language)s has %(number)03d quote types.' %
...       {"language": "Python", "number": 2222})
Python has 2222 quote types.
>>>
```

转换标志字符是：

Flag   |Meaning
-------|------------------
`'0'`  |转换将为数值填充0。

转换类型是：

Conversion    |Meaning            |Notes
--------------|-------------------|------
`'d'`         |象征十进制整型数。   |
`'f'`         |浮点小数格式。       |(3)
`'s'`         |字符串（使用 [str()](https://docs.python.org/3/library/stdtypes.html#str) 转换任何Python对象）。  |(5)

注释：

3. 替代形式导致结果总是包含一个小数点，即使它后面没有数字。

   精度决定小数点后面的位数，默认为6位。

4. 

5. 如果精度是 `N`，则输出被截断为 `N` 个字符。

```python
>>> print('%(language).2s has %(number)03d quote types.' %
...       {"language": "Python", "number": 222})
Py has 222 quote types.
>>>
```

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

## 8.1. datetime — 基本的日期和时间类型
**源代码：** [Lib/datetime.py](https://github.com/python/cpython/tree/3.6/Lib/datetime.py)

[datetime](https://docs.python.org/3.6/library/datetime.html#module-datetime) 模块提供以简单和复杂两种方式操作日期和时间的类。当支持日期和时间运算时，实现的焦点在于格式化和处理提取的属性输出的效率。相关的功能，参见 [time](https://docs.python.org/3.6/library/time.html#module-time) 和 [calendar](https://docs.python.org/3.6/library/calendar.html#module-calendar) 模块。

#### 8.1.1. 可用类型
*class* datetime.**date**  
An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. 属性：[year](https://docs.python.org/3.6/library/datetime.html#datetime.date.year), [month](https://docs.python.org/3.6/library/datetime.html#datetime.date.month), 和 [day](https://docs.python.org/3.6/library/datetime.html#datetime.date.day).

*class* datetime.**datetime**  
一个日期和一个时间的组合。属性：[year](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.year), [month](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.month), [day](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.day), [hour](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.hour), [minute](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.minute), [second](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.second), [microsecond](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.microsecond), 和 [tzinfo](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.tzinfo).

#### 8.1.2. timedelta对象
一个 [timedelta](https://docs.python.org/3.6/library/datetime.html#datetime.timedelta) 对象代表一段时长，是两个日期或时间之间的差异。

*class* datetime.**timedelta**(*days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0*)  
　　所有参数都是可选的且默认为 `0`。参数可以是整型数或浮点数，也可以是正的或负的。

　　内部仅存储 *天*，*秒* 和 *微秒*。参数都被转换成那些单元：

* 一毫秒被转换成1000微秒。
* 一分钟被转换成60秒。
* 一小时被转换成3600秒。
* 一星期被转换成7天。

　　而天，秒和微秒是标准化的，所以表现是唯一的，用

* `0 <= microseconds < 1000000`
* `0 <= seconds < 3600*24` (一天所含的秒数)
* `-999999999 <= days <= 999999999`

如果有任何一个参数是浮点数就会有小数微秒，the fractional microseconds left over from all arguments are combined and their sum is rounded to the nearest microsecond using round-half-to-even tiebreaker. 如果没有参数是浮点数，则转换及标准化处理就是精确的 (没有信息丢失)。

如果天数的标准化值位于指示的范围之外，就会抛出 [OverflowError](https://docs.python.org/3.6/library/exceptions.html#OverflowError)。

首先，请注意标准化负值可能令人感到意外。例如，

```python
>>> from datetime import timedelta
>>> d = timedelta(microseconds=-1)
>>> (d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)
>>>
```

实例属性 (只读)：

Attribute       |Value
----------------|------------------------------------
`days`          |-999999999 到 999999999 之间，包含两端
`seconds`       |0 到 86399 之间，包含两端
`microseconds`  |0 到 999999 之间，包含两端

#### 8.1.3. date对象

日期可以被用作字典的键。在布尔上下文中，所有 [date](https://docs.python.org/3.6/library/datetime.html#datetime.date) 对象都被认为是真。

实例方法：

date.**weekday()**  
用一个整数返回星期几，星期一是0，星期天是6。例如，`date(2002, 12, 4).weekday() == 2`，星期三。另请参阅 [isoweekday()](https://docs.python.org/3.6/library/datetime.html#datetime.date.isoweekday)。

date.**isoweekday()**  
用一个整数返回星期几，星期一是1，星期天是7. 例如，`date(2002, 12, 4).isoweekday() == 3`，星期三。另请参阅 [weekday()](https://docs.python.org/3.6/library/datetime.html#datetime.date.weekday)，[isocalendar()](https://docs.python.org/3.6/library/datetime.html#datetime.date.isocalendar)。

#### 8.1.4. datetime对象
一个 [datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) 对象是包含一个 [date](https://docs.python.org/3.6/library/datetime.html#datetime.date) 对象和一个 [time](https://docs.python.org/3.6/library/datetime.html#datetime.time) 对象的所有信息的一个单一对象。与一个 [date](https://docs.python.org/3.6/library/datetime.html#datetime.date) 对象相似，[datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) assumes the current Gregorian calendar extended in both directions; 与一个 time 对象相似，[datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) 假定每一天都精确地含有 3600*24 秒。

构造函数：

*class* datetime.**datetime**(_year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0_)  
　　year, month 和 day 参数是必须的。*tzinfo* 可以是 `None`，或者是一个 [tzinfo](https://docs.python.org/3.6/library/datetime.html#datetime.tzinfo) 子类的一个实例。其余的参数可以是整型数，范围如下：

* `MINYEAR <= year <= MAXYEAR`,
* `1 <= month <= 12`,
* `1 <= day <= number of days in the given month and year`,
* `0 <= hour < 24`,
* `0 <= minute < 60`,
* `0 <= second < 60`,
* `0 <= microsecond < 1000000`,
* `fold in [0, 1]`.

　　如果一个参数的值超出上面指定的范围，将抛出 [ValueError](https://docs.python.org/3.6/library/exceptions.html#ValueError)。

　　*在版本3.6中发生变化：* 新增了 `fold` 参数。

其它构造函数，所有类方法：

*classmethod* datetime.**now**(tz=None)  
　　返回当前本地的日期和时间。如果可选参数 *tz* 是 `None` 或者没有指定，这将类似于 [today()](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.today)，但是，if possible, supplies more precision than can be gotten from going through a [time.time()](https://docs.python.org/3.6/library/time.html#time.time) timestamp (例如，在提供 C gettimeofday() 函数的平台上这是可能的).

　　如果 *tz* 不是 `None`，它必须是 [tzinfo](https://docs.python.org/3.6/library/datetime.html#datetime.tzinfo) 子类的一个实例，且当前的日期和时间被转换成 *tz* 的时区。在这种情况下结果等同于 `tz.fromutc(datetime.utcnow().replace(tzinfo=tz))`。参见 [today()](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.today), [utcnow()](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.utcnow)。

*classmethod* datetime.**utcnow()**  
返回当前的UTC日期和时间，其中 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 为 `None`。这像 [now()](https://docs.python.org/3/library/datetime.html#datetime.datetime.now)，但返回当前的UTC日期和时间，作为一个 naive [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) 对象。可以通过调用 `datetime.now(timezone.utc)` 获取一个 aware 当前的 UTC datetime。参见 [now()](https://docs.python.org/3/library/datetime.html#datetime.datetime.now)。


支持的运算：

Operation                            |Result
-------------------------------------|--------------------------------
`datetime2 = datetime1 + timedelta`  |(1)
`datetime2 = datetime1 - timedelta`  |(2)
`timedelta = datetime1 - datetime2`  |(3)
`datetime1 < datetime2`              |比较 `datetime1` 和 `datetime2`. <br>(4)

* 1.如果 `timedelta.days > 0` ，则 datetime2 是在时间轴上以 datetime1 为基准点向前移动一个 timedelta 时长，如果 `timedelta.days < 0` ，则向后移动。结果与输入的 datetime 拥有相同的 [tzinfo](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.tzinfo) 属性，且 datetime2 - datetime1 == timedelta。如果 datetime2.year 比 [MINYEAR](https://docs.python.org/3.6/library/datetime.html#datetime.MINYEAR) 小或者比 [MAXYEAR](https://docs.python.org/3.6/library/datetime.html#datetime.MAXYEAR) 大，则抛出 [OverflowError](https://docs.python.org/3.6/library/exceptions.html#OverflowError)。注意，即使输入是一个 aware 对象也不调整时区。

* 2.计算 datetime2 以使 datetime2 + timedelta == datetime1。至于加法，结果与输入的 datetime 拥有相同的 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 属性且不调整时区，即使输入是 aware。这不完全等同于 datetime1 + (-timedelta)，因为孤立的 -timedelta 可能会溢出而 datetime1 - timedelta 则不会。

* 3.从一个 [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) 减去另一个 [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) 只有当两个运算对象都是 naive 或者都是 aware 时才被定义。如果一个是 aware 而另一个是 naive，则抛出 [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)。

如果两者都是 naive 或者都是 aware 且拥有相同的 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 属性，则 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 属性被忽略，且结果是一个 [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta) 对象 *t* 如此以致 `datetime2 + t == datetime1`。在这种情况下不调整时区。

如果两者都是 aware 且拥有不同的 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 属性，`a-b` 的行为就好像 *a* 和 *b* 首先被转换成 naive UTC datetimes。The result is `(a.replace(tzinfo=None) - a.utcoffset()) - (b.replace(tzinfo=None) - b.utcoffset())` except that the implementation never overflows.

* 4.当 *datetime1* 在时间上早于 *datetime2* 时，*datetime1* 被认为小于 *datetime2*。

如果一个比较数是 naive 而另一个是 aware，如果试图对两者的顺序进行比较会抛出 [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)。为平等比较，naive 实例永远不等于 aware 实例。

如果两个比较数都是 aware，且拥有相同的 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 属性，则共同的 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 属性被忽略且 base datetimes 被比较。如果两个比较数都是 aware 但拥有不同的 [tzinfo](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo) 属性，则比较数首先被调整，通过减去它们的 UTC 偏移量 (从 `self.utcoffset()` 获得)。

*在版本3.3中发生变化：* naive 和 aware [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime) 实例之间的等式比较（equality comparisons）不会抛出 [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)。

**注意：** In order to stop comparison from falling back to the default scheme of comparing object addresses, datetime comparison normally raises [TypeError](https://docs.python.org/3.6/library/exceptions.html#TypeError) if the other comparand isn’t also a [datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) object. However, `NotImplemented` is returned instead if the other comparand has a `timetuple()` attribute. This hook gives other kinds of date objects a chance at implementing mixed-type comparison. 不然的话，当一个 [datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) 对象与另一个不同类型的对象比较时，会抛出 [TypeError](https://docs.python.org/3.6/library/exceptions.html#TypeError) 除非比较是 `==` 或 `!=`。后一种情况分别返回 [False](https://docs.python.org/3.6/library/constants.html#False) 或 [True](https://docs.python.org/3.6/library/constants.html#True)。

[datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) 对象可以用作字典的键。在布尔上下文中，所有的 [datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) 对象都被认为是真。

**实例方法：**

datetime.**replace**(_year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0_)  
返回一个拥有相同属性的 datetime，除了由关键字参数指定新值的那些属性。注意可以通过指定 `tzinfo=None` 从一个 aware datetime 创建一个 naive datetime而无需转换日期和时间数据。

*在版本3.6中新增：* 增加了 `fold` 参数。

datetime.**utcoffset()**  
如果 [tzinfo](https://docs.python.org/3.6/library/datetime.html#datetime.datetime.tzinfo) 是 `None`，返回 `None`，否则返回 `self.tzinfo.utcoffset(self)`，且如果后者不返回 `None` 或一个总的分钟数小于一天的一个 timedelta 对象则抛出一个异常。

datetime.**strftime**(*format*)  
返回一个代表日期和时间的字符串，由一个明确的格式字符串所控制。完整的格式化指令列表，参见 [strftime() 和 strptime() 的行为](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)。

```python
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2018, 8, 2, 12, 23, 31, 980032)
>>> datetime.datetime.now().strftime('%Y%m%d%H%M%S')
'20180802122335'
>>>
```

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

## 12. 数据持久性
这章描述的模块支持将 Python 数据以持久性的形式储存到磁盘上。[pickle](https://docs.python.org/3/library/pickle.html#module-pickle) 和 [marshal](https://docs.python.org/3/library/marshal.html#module-marshal) 模块能将许多 Python 数据类型转换成字节流并且之后可以从这些字节流中重新创建那些对象。

### 12.1. pickle — Python对象序列化
**源代码：** [Lib/pickle.py](https://github.com/python/cpython/tree/3.7/Lib/pickle.py)

[pickle](https://docs.python.org/3/library/pickle.html#module-pickle) 模块为序列化和反序列化一个 Python 对象结构实现了二进制协议。*“Pickling”* 是一个 Python 对象层次结构被转换成一个字节流的过程，而 *“unpickling”* 是反操作，一个字节流 (从一个 [二进制文件](https://docs.python.org/3/glossary.html#term-binary-file) 或 [bytes-like 对象](https://docs.python.org/3/glossary.html#term-bytes-like-object) ) 被转换回一个对象层次结构。Pickling (和 unpickling) 也被称为 “序列化”, “marshalling,” (不要把这个与 [marshal](https://docs.python.org/3/library/marshal.html#module-marshal) 模块混淆) 或 “flattening”; 然而，为避免混淆，这里所使用的术语是 “pickling” 和 “unpickling”。

**警告：** 针对错误的或恶意的结构化数据 [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) 模块是不安全的。永远不要 unpickle 从一个不信任的或未认证的源接收的数据。

#### 12.1.3. 模块接口
序列化一个对象层次结构，你可以简单地调用 [dumps()](https://docs.python.org/3/library/pickle.html#pickle.dumps) 函数。相似地，反序列化一个数据流，你可以调用 [loads()](https://docs.python.org/3/library/pickle.html#pickle.loads) 函数。然而，如果你想更多地控制序列化和反序列化，你可以分别创建一个 [Pickler](https://docs.python.org/3/library/pickle.html#pickle.Pickler) 或一个 [Unpickler](https://docs.python.org/3/library/pickle.html#pickle.Unpickler) 对象。

[pickle](https://docs.python.org/3/library/pickle.html#module-pickle) 模块提供了下面的函数以使 pickling 过程更加的方便：

pickle.**dumps**(*obj, protocol=None, \*, fix_imports=True*)  
返回对象的 pickled 表示形式作为一个字节对象，而不是将它写入到一个文件。

参数 *protocol* 和 *fix_imports* 的含义同 [dump()](https://docs.python.org/3/library/pickle.html#pickle.dump) 函数中这两个参数的含义。

pickle.**load**(*file, \*, fix_imports=True, encoding="ASCII", errors="strict"*)  
从打开的 [文件对象](https://docs.python.org/3/glossary.html#term-file-object) *file* 中读取一个 pickled 对象的表示形式并返回其中指定的复原的对象层次结构。这等同于 `Unpickler(file).load()`。

pickle.**loads**(*bytes_object, \*, fix_imports=True, encoding="ASCII", errors="strict"*)  
从一个[字节](https://docs.python.org/3/library/stdtypes.html#bytes)对象读取一个 pickled 对象层次结构并返回其中指定的对象层次结构的复原。

## 13. 数据压缩和归档
这章描述的模块支持用zlib，gzip，bzip2和lzma算法对数据进行压缩，及创建ZIP和tar格式的归档。另请参见 [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) 模块提供的[归档操作](https://docs.python.org/3/library/shutil.html#archiving-operations)。

### 13.1. zlib — 与gzip兼容的压缩
对于要求数据压缩的应用，使用zlib库，这个模块中的函数允许压缩和解压缩。zlib库有它自己的主页 [http://www.zlib.net](http://www.zlib.net/)。Python 模块和版本早于1.1.3的zlib库存在已知的不兼容性；1.1.3 有一个安全隐患，所以我们推荐使用 1.1.4 或更新版本。

zlib.**compress**(*data, level=-1*)  
压缩 *data* 中的字节，返回一个包含压缩数据的字节对象。*level* 是一个从`0`到`9`的整型数或者`-1`，它控制压缩的级别；`1` (Z_BEST_SPEED) 速度最快但压缩率最低，`9` (Z_BEST_COMPRESSION) 速度最慢但压缩率最高。`0` (Z_NO_COMPRESSION) 是不压缩。默认值是 `-1` (Z_DEFAULT_COMPRESSION)。Z_DEFAULT_COMPRESSION 表示一个默认的在速度和压缩之间的折衷 (当前等同于级别6)。如果出现任何错误则抛出 [error](https://docs.python.org/3/library/zlib.html#zlib.error) 异常。**_data_ 要求是一个bytes-like对象。**

*在版本3.6中发生变化：* *level* 现在可以被用作一个关键字参数。

```python
>>> from urllib.request import urlopen
>>> import zlib
>>> html = urlopen('http://example.webscraping.com').read()
>>> len(html)
7902
>>> html_compressed = zlib.compress(html)
>>> len(html_compressed)
2456
>>> html_decompressed = zlib.decompress(html_compressed)
>>> len(html_decompressed)
7902
>>>
```

zlib.**decompress**(*data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE*)  
解压 *data* 中的字节，返回一个包含未压缩的数据的字节对象。

**注意：当要压缩的数据足够小的时候，会出现压缩后的数据比压缩前更大的情况。**

```python
>>> from urllib.request import urlopen
>>> import zlib
>>> html = b'http://example.webscraping.commmmmmmmmm'
>>> len(html)
39
>>> html_compressed = zlib.compress(html)
>>> len(html_compressed)
39
>>> html_decompressed = zlib.decompress(html_compressed)
>>> len(html_decompressed)
39
>>>
```

在上面的例子中，如果html变量的长度小于39，则会出现压缩后的数据比压缩前的数据更大的情况。

### 13.5. zipfile — 与ZIP归档一起工作
**源代码：** [Lib/zipfile.py](https://github.com/python/cpython/tree/3.7/Lib/zipfile.py)

ZIP文件格式是一个普遍的归档和压缩标准。这个模块提供工具创建，读，写，附加，和列出一个ZIP文件。这个模块的任何高级用法都要求理解 [PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT) 中定义的格式。

#### 13.5.1. ZipFile对象
*class* zipfile.**ZipFile**(*file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None*)  
打开一个ZIP文件，其中 *file* 可以是一个指向一个文件的路径 (一个字符串)，一个 file-like 对象或者一个 [path-like 对象](https://docs.python.org/3/glossary.html#term-path-like-object)。

ZipFile也是一个上下文管理器因而支持 [with](https://docs.python.org/3/reference/compound_stmts.html#with) 语句。在下面的例子中，当 [with](https://docs.python.org/3/reference/compound_stmts.html#with) 语句的套件完成的时候 *myzip* 被关闭——即使出现一个异常：

```python
from zipfile import ZipFile
with ZipFile('spam.zip', 'w') as myzip:
    myzip.write('eggs.txt')
```

在上面的代码中，因为本地没有eggs.txt文件，所以抛出了一个 `FileNotFoundError` ，但该代码块依然创建一个名为spam.zip的空的归档文件。

ZipFile.**close()**  
关闭归档文件。在退出你的程序前你必须调用 [close()](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.close) 否则至关重要的记录将不会被写入。

ZipFile.**namelist()**  
返回一个归档成员的名称列表。

ZipFile.**open**(*name, mode='r', pwd=None, \*, force_zip64=False*)  
访问归档的一个成员作为一个二进制 file-like 对象。*name* 可以是归档里面的一个文件的名字或者一个 [ZipInfo](https://docs.python.org/3/library/zipfile.html#zipfile.ZipInfo) 对象。*mode* 参数，如果包含，必须是 `'r'` (默认) 或 `'w'`。*pwd* 是用于解密加密ZIP文件的密码。

[open()](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open) 也是一个上下文管理器因而支持 [with](https://docs.python.org/3/reference/compound_stmts.html#with) 语句：

```sh
$ cat eggs.txt
这是一个测试文件
```

```python
>>> from zipfile import ZipFile
>>> with ZipFile('spam.zip') as myzip:
...     with myzip.open('eggs.txt') as myfile:
...         print(myfile.read().decode('gb2312'))
...
这是一个测试文件
>>>
```

ZipFile.**write**(*filename, arcname=None, compress_type=None, compresslevel=None*)  
将名为 *filename* 的文件写入到归档中，指定归档名 *arcname* (默认，这同 *filename*，但不带驱动器号且移除前导路径分隔符)。如果指定，*compress_type* 将覆盖构造函数为新的条目指定的 *compression* 参数的值。类似地，如果指定 *compresslevel* 的话，将覆盖构造函数中的 *compresslevel* 参数的值。打开归档的模式必须是 `'w'`, `'x'` 或 `'a'`。

**注意：** ZIP文件没有官方的文件名编码。如果你有 unicode 文件名，在将它们传递给 [write()](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.write) 你必须用你期望的编码将它们转换成字节字符串。WinZip用CP437编码解释所有文件名，也被称为 DOS Latin。

**注意：** 归档名应该相对于归档根目录，就是说，它们不应该以一个路径分隔符开头。

**注意：** 如果 `arcname` (或 `filename`, 如果没有指定 `arcname`) 包含一个空字节，归档中的文件的名称将在空字节处被截断。

*在版本3.6中发生变化：* 对一个以 `r` 模式创建的ZipFile或一个关闭的ZipFile调用 [write()](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.write) 将抛出一个 [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)。之前，是抛出一个 [RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError)。

```python
>>> import csv
>>> from io import BytesIO, StringIO
>>> from urllib.request import urlopen
>>> from zipfile import ZipFile
>>> zipped_data = urlopen('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip').read()
>>> urls = []
>>> with ZipFile(BytesIO(zipped_data)) as zf:
...     csv_filename = zf.namelist()[0]
...     for rank, website in csv.reader(StringIO(zf.open(csv_filename).read().decode())):
...         urls.append('http://' + website)
... 
>>> len(urls)
1000000
>>> urls[0]
'http://google.com'
>>> 
```

**注意：** 下载得到的压缩数据是在使用BytesIO封装之后，才传给ZipFile的。这是因为ZipFile需要一个类似文件的接口，而不是字节。

## 14. 文件格式
本章描述的模块解析各种既不是标记语言也与e-mail无关的其它文件格式。

### 14.1. csv — CSV文件读写
**源代码：** [Lib/csv.py](https://github.com/python/cpython/tree/3.7/Lib/csv.py)

所谓的 CSV (Comma Separated Values) 格式是表和数据库最常见的导入和导出格式。

csv 模块的 [reader](https://docs.python.org/3/library/csv.html#csv.reader) 和 [writer](https://docs.python.org/3/library/csv.html#csv.writer) 对象读和写序列。程序员也可以使用 [DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader) 和 [DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter) 类来读写字典形式中的数据。

#### 14.1.1. 模块内容
[csv](https://docs.python.org/3/library/csv.html#module-csv) 模块定义了下列函数：

csv.**reader**(*csvfile, dialect='excel', \*\*fmtparams*)  
返回一个将遍历给定的 *csvfile* 文件中的行的 reader 对象。*csvfile* 可以是支持[迭代器](https://docs.python.org/3/glossary.html#term-iterator)协议及每次调用它的 `__next__()` 方法都返回一个字符串的任意对象 — [文件对象](https://docs.python.org/3/glossary.html#term-file-object) 和列表对象都是适合的。如果 *csvfile* 是一个文件对象，打开它时必须带有 `newline=''`。（如果没有指定 `newline=''`，新行嵌入引用字段后将不能被正确解释，且在以 `\r\n` 作为行结束符的平台会写入一个额外的 `\r`。总是指定 `newline=''` 应该是安全的，因为 csv 模块执行自己的 ([universal](https://docs.python.org/3/glossary.html#term-universal-newlines)) 新行处理方法。）

```sh
$ cat club.csv
113,菲比酒吧
114,哥弟KTV
```

```python
>>> import csv
>>> with open('club.csv', newline='') as csvfile:
...     content = csv.reader(csvfile)
...     for item in content:
...         print(item)
...
['113', '菲比酒吧']
['114', '哥弟KTV']
>>>
```

```python
>>> import csv
>>> with open('club.csv', newline='') as csvfile:
...     content = csv.reader(csvfile)
...     for id, name in content:
...         print(name)
...
菲比酒吧
哥弟KTV
>>>
```

```python
>>> _list = ['a', 'b', 'c']
>>> content = csv.reader(_list)
>>> for item in content:
...     print(item)
...
['a']
['b']
['c']
>>>
```

csv.**writer**(_csvfile, dialect='excel', \*\*fmtparams_)  
Return a writer object responsible for converting the user’s data into delimited strings on the given file-like object. *csvfile* 可以是带有一个 `write()` 方法的任意对象。如果 *csvfile* 是一个文件对象，打开它时必须带有 `newline=''`。（如果没有指定 `newline=''`，新行嵌入引用字段后将不能被正确解释，且在以 `\r\n` 作为行结束符的平台会写入一个额外的 `\r`。总是指定 `newline=''` 应该是安全的，因为 csv 模块执行自己的 ([universal](https://docs.python.org/3/glossary.html#term-universal-newlines)) 新行处理方法。）

```python
>>> import csv
>>> with open('school.csv', 'w', newline='') as csvfile:
...     writer = csv.writer(csvfile)
...     writer.writerow(['班级', '姓名', '学号'])
...     writer.writerow([181, '成龙', 20181801])
...     writer.writerow([181, '李连杰', 20181802])
...
10
17
18
>>>
```

#### 14.1.4. Writer对象
`Writer` 对象 ([DictWriter](https://docs.python.org/3/library/csv.html#csv.DictWriter) 实例和 [writer()](https://docs.python.org/3/library/csv.html#csv.writer) 函数返回的对象) 有下列公共方法。

csvwriter.**writerow**(*row*)  
将 *row* 参数写入到 writer 的文件对象中，并根据当前的 dialect 进行格式化。

*在版本3.5中发生变化：* 支持任意可迭代对象。

##### 16.2.2.1. 内存流
使用一个 [str](https://docs.python.org/3/library/stdtypes.html#str) 或 [bytes-like 对象](https://docs.python.org/3/glossary.html#term-bytes-like-object) 作为一个文件用于读写也是可能的。对字符串来说可以像一个文件以文本模式打开一样使用 [StringIO](https://docs.python.org/3/library/io.html#io.StringIO)。可以像一个文件以二进制模式打开一样使用 [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO)。两者都提供完整的随机读写的能力。

**另请参见：**

[sys](https://docs.python.org/3/library/sys.html#module-sys)  
包含标准IO流：[sys.stdin](https://docs.python.org/3/library/sys.html#sys.stdin)，[sys.stdout](https://docs.python.org/3/library/sys.html#sys.stdout)，和 [sys.stderr](https://docs.python.org/3/library/sys.html#sys.stderr)。

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

*class* io.**BytesIO**(**[**_initial_bytes_**]**)  
使用内存中的一个字节缓冲区实现一个流。它继承 [BufferedIOBase](https://docs.python.org/3/library/io.html#io.BufferedIOBase)。当 [close()](https://docs.python.org/3/library/io.html#io.IOBase.close) 方法被调用时缓冲区被丢弃。

可选参数 *initial_bytes* 是一个包含初始化数据的 [bytes-like 对象](https://docs.python.org/3/glossary.html#term-bytes-like-object)。

除了那些从 [BufferedIOBase](https://docs.python.org/3/library/io.html#io.BufferedIOBase) 和 [IOBase](https://docs.python.org/3/library/io.html#io.IOBase) 继承的方法，[BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO) 提供或重写了这些方法：

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

*class* io.**StringIO**(*initial_value='', newline='\n'*)  
一个用于文本I/O的内存中的流。当 [close()](https://docs.python.org/3/library/io.html#io.IOBase.close) 方法被调用时文本缓冲区被丢弃。

缓冲区的初始值可以通过提供的 *initial_value* 参数继续设置。如果新行转化被启用，newlines will be encoded as if by [write()](https://docs.python.org/3/library/io.html#io.TextIOBase.write)。流被放在缓冲区的起始位置。

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

## 22. 互联网协议和支持
这章描述的模块实现了互联网协议和相关技术的支持。它们在Python中全被实现了。大多数这些模块都要求系统相关的模块 [socket](https://docs.python.org/3/library/socket.html#module-socket) 存在，目前大多数流行的平台都支持 [socket](https://docs.python.org/3/library/socket.html#module-socket)。下面是一个概述：

### 22.12. http.client — HTTP协议客户端
**Source code:** [Lib/http/client.py](https://github.com/python/cpython/tree/3.6/Lib/http/client.py)

这个模块定义实现HTTP和HTTPS协议客户端的类。它通常不被直接使用 — 模块 [urllib.request](https://docs.python.org/3.6/library/urllib.request.html#module-urllib.request) 使用它处理HTTP和HTTPS URLs。

**另请参阅：** 更高层次的HTTP客户端接口推荐 [Requests package](http://docs.python-requests.org/)。

**注意：** 如果Python编译了SSL支持 (通过 [ssl](https://docs.python.org/3.6/library/ssl.html#module-ssl) 模块)，HTTPS支持才可用。

这个模块提供了下面的类：

*class* http.client.**HTTPResponse**(*sock, debuglevel=0, method=None, url=None*)  
Class whose instances are returned upon successful connection. Not instantiated directly by user.

*在版本3.4中发生变化：* *strict* 参量被移除了。HTTP 0.9 风格 “Simple Responses” 不再支持。

#### 22.12.2. HTTPResponse对象
An [HTTPResponse](https://docs.python.org/3.6/library/http.client.html#http.client.HTTPResponse) instance wraps the HTTP response from the server. It provides access to the request headers and the entity body. The response is an iterable object and can be used in a with statement.

*在版本3.5中发生变化：* 现在实现了 [io.BufferedIOBase](https://docs.python.org/3.6/library/io.html#io.BufferedIOBase) 接口，它的所有的读操作都支持。

HTTPResponse.**read**([*amt*])  
读取并返回响应正文，或者直到下一个 *amt* 字节。

HTTPResponse.**version**  
服务器使用的HTTP协议版本。HTTP/1.0 为 10，HTTP/1.1 为 11。

HTTPResponse.**status**  
服务器返回的状态代码。

实例属性：

**code**  
返回类型为int，返回HTTP Response状态代码

```python
>>> import http.client
>>> import urllib.error
>>> from urllib.request import urlopen
>>> dir(http.client.HTTPResponse)
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'close', 'closed', 'detach', 'fileno', 'flush', 'getcode', 'getheader', 'getheaders', 'geturl', 'info', 'isatty', 'isclosed', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> hasattr(http.client.HTTPResponse, 'code')
False
>>> type(urlopen('http://example.webscraping.com'))
<class 'http.client.HTTPResponse'>
>>> isinstance(urlopen('http://example.webscraping.com'), http.client.HTTPResponse)
True
>>> hasattr(urlopen('http://example.webscraping.com'), 'code')
True
>>> dir(urlopen('http://example.webscraping.com'))
['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method', '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked', '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp', 'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'reason', 'seek', 'seekable', 'status', 'tell', 'truncate', 'url', 'version', 'will_close', 'writable', 'write', 'writelines']
>>> type(urlopen('http://example.webscraping.com').code)
<class 'int'>
>>> urlopen('http://example.webscraping.com').code
200
>>> try:
...     print(urlopen('https://python.org/java').code)
... except urllib.error.HTTPError as e:
...     print(e.code)
...
404
>>>
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

# Python语言参考
## 3. 数据模型
### 3.2. 标准类型层次结构
**模块**  
　　模块是 Python 代码的基本组织单元，模块由 [import](https://docs.python.org/3/reference/simple_stmts.html#import) 语句 (参见 [import](https://docs.python.org/3/reference/simple_stmts.html#import))，或通过调用函数如 [importlib.import_module()](https://docs.python.org/3/library/importlib.html#importlib.import_module) 和内置的 [\_\_import\_\_()](https://docs.python.org/3/library/functions.html#__import__) 调用 [导入系统](https://docs.python.org/3/reference/import.html#importsystem) 所创建。每个模块对象都有一个通过一个字典对象实现的命名空间 (这就是模块中定义的函数的 `__globals__` 属性所引用的字典)。属性引用被转换为在字典中查找，例如，`m.x` 等同于 `m.__dict__["x"]`。模块对象不包含用于初始化模块的代码对象 (因为一旦初始化完成就不需要它了)。

属性赋值更新模块的命名空间字典，例如，`m.x = 1` 等价于 `m.__dict__["x"] = 1`。

预定义的 (可写的) 属性： [\_\_name\_\_](https://docs.python.org/3/reference/import.html#__name__) 是模块的名字；\_\_doc\_\_ 是模块的文档字符串，如不可用则为 `None`；\_\_annotations\_\_ (可选的) 是一个包含模块正文执行期间收集的变量注释的字典；如果模块是从一个文件加载，则 [\_\_file\_\_](https://docs.python.org/3/reference/import.html#__file__) 是该文件的路径名。

特殊的只读属性：[\_\_dict\_\_](https://docs.python.org/3/library/stdtypes.html#object.__dict__) is the module’s namespace as a dictionary object.

### 3.3. 特殊方法名
#### 3.3.6. 仿真可调用对象
object.**\_\_call\_\_**(*self*__\[__*, args...*__\]__)  
当实例作为一个函数被“调用”时调用；如果定义了这个方法，则 `x(arg1, arg2, ...)` 是 `x.__call__(arg1, arg2, ...)` 的缩写。

## 7. 简单语句
### 7.3. assert语句
将调试断言插入到一个程序中，assert 语句是一种方便的方式：

**assert_stmt** ::=  "assert" [expression](https://docs.python.org/3/reference/expressions.html#grammar-token-expression) \["," [expression](https://docs.python.org/3/reference/expressions.html#grammar-token-expression)\]

简单形式，`assert expression`，等同于

```python
if __debug__:
    if not expression: raise AssertionError
```

### 7.12. global语句
**global_stmt** ::=  "global" [identifier](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-identifier) ("," [identifier](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-identifier))*

[global](https://docs.python.org/3/reference/simple_stmts.html#global) 语句是一个适用于整个当前代码块的公告。它意味着global语句中的identifiers都将被解释为全局变量。

## 8. 复合语句
一个复合语句由一个或多个“子句”构成。一个子句由一个头部和一个“套件”构成。一个具体的复合语句的子句头部拥有相同的缩进级别。每个子句头部以一个唯一的标识关键字开始及以一个冒号结尾。一个套件是由一个子句控制的一组语句。一个套件可以是与头部处于同一行且位于头部的冒号之后的一个或多个由分号分隔的简单语句，或者它可以是随后的行中的一个或多个缩进的语句。只有后面这种形式的套件可以包含嵌套的复合语句；下面是非法的，主要是因为接下来的 [else](https://docs.python.org/3/reference/compound_stmts.html#else) 子句属于哪一个 [if](https://docs.python.org/3/reference/compound_stmts.html#if) 子句不清晰：

```python
if test1: if test2: print(x)
```

还要注意在这个上下文中分号比冒号捆绑得更紧密，所以在下面的例子中，要么所有的 [print()](https://docs.python.org/3/library/functions.html#print) 调用都被执行，要么一个都没有：

```python
if x < y < z: print(x); print(y); print(z)
```

总结：

**compound_stmt ::**=&nbsp;&nbsp;[if_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-if_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [while_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-while_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [for_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-for_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [try_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-try_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [with_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-with_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [funcdef](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-funcdef)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [classdef](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-classdef)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [async_with_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-async_with_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [async_for_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-async_for_stmt)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| [async_funcdef](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-async_funcdef)  
**suite&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::**=&nbsp;&nbsp;[stmt_list](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-stmt_list) NEWLINE | NEWLINE INDENT [statement](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-statement)+ DEDENT  
**statement&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::**=&nbsp;&nbsp;[stmt_list](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-stmt_list) NEWLINE | [compound_stmt](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-compound_stmt)  
**stmt_list&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;::**=&nbsp;&nbsp;[simple_stmt](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-simple_stmt) (";" [simple_stmt](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-simple_stmt))* [";"]

### 8.5. with语句
The [with](https://docs.python.org/3.6/reference/compound_stmts.html#with) statement is used to wrap the execution of a block with methods defined by a context manager (参见 [With语句上下文管理器](https://docs.python.org/3.6/reference/datamodel.html#context-managers) 章节).

**with_stmt ::=**&nbsp;&nbsp;"with" with_item ("," with_item)* ":" [suite](https://docs.python.org/3.6/reference/compound_stmts.html#grammar-token-suite)  
**with_item ::=**&nbsp;&nbsp;[expression](https://docs.python.org/3.6/reference/expressions.html#grammar-token-expression) \["as" [target](https://docs.python.org/3.6/reference/simple_stmts.html#grammar-token-target)\]

当不止一个 with_item 时，上下文管理器的处理就好像有多个 [with](https://docs.python.org/3.6/reference/compound_stmts.html#with) 语句嵌套似的。

```python
with A() as a, B() as b:
    suite
```

等同于

```python
with A() as a:
    with B() as b:
        suite
```

*在版本3.1中发生变化：* 支持多个上下文表达式。

# Python教程
## 2. 使用Python解释器
### 2.1. 调用解释器
Typing an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. 如果无效，你可以通过输入下面的命令：`quit()` 退出解释器。

## 4. 更多控制流工具
Besides the [while](https://docs.python.org/3/reference/compound_stmts.html#while) statement just introduced, Python knows the usual control flow statements known from other languages, with some twists.

### 4.3. range() 函数
如果你需要遍历一个数字序列，内置函数 [range()](https://docs.python.org/3/library/stdtypes.html#range) 派得上用场。它生成等差数列：

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

给定的结束点永远都不是生成的序列的一部分；一个长度为10的序列的项的合法索引，`range(10)` 生成 10 个值。让 range 以另一个数开始是可能的，或者指定一个不同的增量(即使为负；有时这被称为 ‘step’):

```python
>>> range(5, 10)
range(5, 10)
>>> for i in range(5, 10):
...     print(i)
...
5
6
7
8
9
>>> for i in range(0, 10, 3):
...     print(i)
...
0
3
6
9
>>> for i in range(-10, -100, -30):
...     print(i)
...
-10
-40
-70
```

遍历一个序列的索引，你可以联合 [range()](https://docs.python.org/3/library/stdtypes.html#range) 和 [len()](https://docs.python.org/3/library/functions.html#len) 如下：

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
>>>
```

In most such cases, however, it is convenient to use the [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) function, 请看 [Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms)。

如果你仅打印一个range，将发生一件奇怪的事情：

```python
>>> print(range(0, 10))
range(0, 10)
>>>
```

在很多方面 [range()](https://docs.python.org/3/library/stdtypes.html#range) 返回对象的行为就好像它是一个列表，但实际上它不是。当你遍历它时，它是一个返回预期的序列中的连续的项的对象，但它实际上不制造列表，从而节省空间。

我们说这样的对象是*可迭代的*，也就是说，suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted. 我们已经见过 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 语句就是这样一个*迭代器*。[list()](https://docs.python.org/3/library/stdtypes.html#list) 函数是另一个；它从可迭代对象创建列表：

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
>>>
```

稍后我们将看到更多返回可迭代对象和使用可迭代对象作为参数的函数。

### 4.4. break 和 continue 语句, 和循环中的 else 子句
[break](https://docs.python.org/3/reference/simple_stmts.html#break) 语句，与 C 中相似，摆脱封闭它的最内层的 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 或者 [while](https://docs.python.org/3/reference/compound_stmts.html#while) 循环。

循环语句可能含有一个 `else` 子句；当循环通过耗尽列表 (with [for](https://docs.python.org/3/reference/compound_stmts.html#for)) 或者当条件变为 false (with [while](https://docs.python.org/3/reference/compound_stmts.html#while)) 而结束时执行 else 子句，当循环被一个 [break](https://docs.python.org/3/reference/simple_stmts.html#break) 语句终止时则不执行 else 子句。通过下面这个搜索质数的循环来举例说明：

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
>>>
```

(是的，这是正确的代码。仔细看：`else` 子句属于 [for](https://docs.python.org/3/reference/compound_stmts.html#for) 循环，**而不是** [if](https://docs.python.org/3/reference/compound_stmts.html#if) 语句。)

当与循环一起使用时，比起 [if](https://docs.python.org/3/reference/compound_stmts.html#if) 语句中的 `else` 子句，循环中的 `else` 子句与 [try](https://docs.python.org/3/reference/compound_stmts.html#try) 语句中的 `else` 子句有更多的共同点：当没有异常发生时执行 [try](https://docs.python.org/3/reference/compound_stmts.html#try) 语句的 `else` 子句，当没有 `break` 发生时执行循环的 `else` 子句。关于 [try](https://docs.python.org/3/reference/compound_stmts.html#try) 语句和异常的更多信息，请看 [处理异常](https://docs.python.org/3/tutorial/errors.html#tut-handling)。

[continue](https://docs.python.org/3/reference/simple_stmts.html#continue) 语句，也是从 C 借鉴来的，继续循环的下一次迭代：

```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print('Found an even number', num)
...         continue
...     print('Found a number', num)
...
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
>>>
```

## 7. 输入和输出
有几种方式呈现一个程序的输出；数据可以被以易于人阅读的形式打印出来，或者写入到一个文件中以备将来使用。这章将讨论一些可能性。

### 7.2. 读和写文件
[open()](https://docs.python.org/3/library/functions.html#open) 返回一个[文件对象](https://docs.python.org/3/glossary.html#term-file-object)，最常见的用法是带两个参数：`open(filename, mode)`。

```python
>>> f = open('workfile', 'w')
```

#### 7.2.1. 文件对象的方法
这节剩下的例子将假设一个名为 `f` 的文件对象已经被创建。

`f.write(string)` 写入 *string* 的内容到文件中，返回写入的字符数。

```python
>>> f = open('workfile', 'w')
>>> f.write('This is a test\n')
15
```

其它类型的对象在写入他们以前必须被转换成一个字符串 (文本模式) 或者一个字节对象 (二进制模式)：

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
>>> f.closed
False
>>> f.close()
>>> f.closed
True
>>> with open('workfile', 'r') as f:
...     f.read()
...
"This is a test\n('the answer', 42)"
>>> f.closed
True
>>> with open('workfile', 'r') as f:
...     print(f.read())
...
This is a test
('the answer', 42)
>>> f.closed
True
>>>
```

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

# Beautiful Soup
## 输出
### Pretty-printing
`prettify()` 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行

```python
>>> from bs4 import BeautifulSoup
>>> html = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
>>> soup = BeautifulSoup(html, 'lxml')
>>> print(soup.prettify())
<html>
 <body>
  <a href="http://example.com/">
   I linked to
   <i>
    example.com
   </i>
  </a>
 </body>
</html>
>>>
```

`BeautifulSoup` 对象和它的tag节点都可以调用 `prettify()` 方法:

```python
>>> print(soup.a.prettify())
<a href="http://example.com/">
 I linked to
 <i>
  example.com
 </i>
</a>
>>> print(soup.i.prettify())
<i>
 example.com
</i>
>>>
```

# cssselect
cssselect: 适用于Python的CSS选择器  
[https://cssselect.readthedocs.io/en/latest/](https://cssselect.readthedocs.io/en/latest/)

*cssselect* 解析 [CSS3 选择器](https://www.w3.org/TR/selectors-3/) 并将它们转换成 [XPath 1.0](https://www.w3.org/TR/xpath/) 表达式。这些表达式可以被用在 [lxml](http://lxml.de/) 或另一个 XPath 引擎中，用于在XML或HTML文档中查找匹配的元素。

在它被提取出来作为一个独立的项目以前，这个模块过去一直作为 `lxml.cssselect` 存在于lxml中。

安装  
`pip install cssselect`

# lxml
[https://lxml.de](https://lxml.de)

## lxml.html
从版本2.0开始，lxml 与一个用于处理 HTML 的独立的 Python 包（lxml.html）一起发布了。它基于 lxml 的 HTML 解析器，但它提供一个特殊的元素API用于 HTML 元素，以及一些用于常见HTML处理任务的工具。

### 解析HTML
#### 解析HTML片段
有几个可用于解析HTML的函数：

**fromstring(string):**  
返回 document_fromstring 或者 fragment_fromstring，基于字符串看起来是否像是一个完整的文档，或者仅仅是一个片段。

### HTML元素方法
HTML元素除了拥有ElementTree的所有方法，还包含一些额外的方法：

**.text_content():**  
返回元素及其子元素的内容，且不带标记。

**.cssselect(expr):**  
使用一个CSS选择器表达式，从这个元素和它的子元素中选择元素。(注意 .xpath(expr) is also available as on all lxml elements.)【该方法返回的是一个由 lxml.html.HtmlElement 类型的元素构成的列表】

```python
>>> import lxml.html
>>> from urllib.request import urlopen
>>> html = urlopen('http://example.webscraping.com/places/default/view/Afghanistan-1').read().decode()
>>> tree = lxml.html.fromstring(html)
>>> type(tree)
<class 'lxml.html.HtmlElement'>
>>> area = tree.cssselect('table > tr#places_area__row > td.w2p_fw')
>>> type(area)
<class 'list'>
>>> area = tree.cssselect('table > tr#places_area__row > td.w2p_fw')[0]
>>> type(area)
<class 'lxml.html.HtmlElement'>
>>> area = tree.cssselect('table > tr#places_area__row > td.w2p_fw')[0].text_content()
>>> type(area)
<class 'lxml.etree._ElementUnicodeResult'>
>>> print(area)
647,500 square kilometres
>>>
```

# Python Codes
Python代码块

## download.py
最简单的下载函数  

```python
from urllib.request import urlopen


def download_simple(url):  # url(str)
    """The simplest download function
    """
    html = urlopen(url).read().decode()
    return html


print(download_simple('http://example.webscraping.com').strip())

```

## ssh.py
paramiko——SSH协议的Python实现

```python
import paramiko


def ssh(command):
    global client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('211.211.211.211', 1999,
                   username='username', password='password')
    stdin, stdout, stderr = client.exec_command(command)
    result = stdout.read().decode() if stdout else stderr.read().decode()
    return result


print(ssh('ls -alh').strip())
client.close()

```