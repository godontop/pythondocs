* [Python标准库](#python标准库)  
	* [2 内置函数](#2-内置函数)  

# Python文档
Python官方文档不完全翻译。  
# Python标准库
Python版本：2.7.4
## 2 内置函数
**input**([*prompt*])  
等同于 eval(raw_input(prompt))。  

常规用户输入请考虑使用 [raw_input()](https://docs.python.org/2.7/library/functions.html#raw_input) 函数。

**raw_input**([*prompt*])  
如果 *prompt* 参数存在，它将被写到标准输出且不带尾部换行符。接着函数从输入读取一行，将其转化为一个字符串(stripping a trailing newline), 并返回该字符串。当读到 EOF 时，抛出[EOFError](https://docs.python.org/2.7/library/exceptions.html#exceptions.EOFError) 。