# Python文档
Python相关文档。  

* [Python 3 标准库](#python-3-标准库)
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