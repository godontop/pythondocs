# Python文档
Python官方文档不完全翻译。  

* [Python 3标准库](#python-3标准库)
	* [4.](#4)
		* [4.6](#46)
			* [4.6.4. 列表](#464-列表)

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

To remind users that it operates by side effect, 它不返回排序后的序列(使用 sorted() 明确地请求一个新的排序的列表实例).  
```python3  
letters = ['d', 'a', 'e', 'c', 'b']
print(letters.sort())
```
**Result:**  
None

list.sort()方法的返回值是None，要打印排序后的列表，应使用下面的代码：
```python3
letters = ['d', 'a', 'e', 'c', 'b']
letters.sort()
print(letters)
```
**Result:**  
['a', 'b', 'c', 'd', 'e']