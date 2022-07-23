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
* [PEPs](#peps)
    * [PEP 453 -- Explicit bootstrapping of pip in Python installations](#pep-453----explicit-bootstrapping-of-pip-in-python-installations)
        * [在Windows下执行脚本](#在windows下执行脚本)
* [术语表](#术语表)
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
一个 [datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) 对象是包含一个 [date](https://docs.python.org/3.6/library/datetime.html#datetime.date) 对象和一个 [time](https://docs.python.org/3.6/library/datetime.html#datetime.time) 对象的所有信息的一个单一对象。与一个 [date](https://docs.python.org/3.6/library/datetime.html#datetime.date) 对象相似，[datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) assumes the current Gregorian calendar extended in both directions; 与一个 time 对象相似，[datetime](https://docs.python.org/3.6/library/datetime.html#datetime.datetime) 假定每一天都精确地含有 3600\*24 秒。

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