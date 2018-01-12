# Python文档
Python官方文档不完全翻译。  

* [Python 3标准库](#python-3标准库)
	* [4.](#4)
		* [4.6](#46)
			* [4.6.4. 列表](#464-列表)
		* [4.7. 文本序列类型 — str](#47-文本序列类型--str)

[Python 2标准库](https://github.com/godontop/pythondocs/blob/master/python2/README.md)
# Python 3标准库
Python版本：3.6.4
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