# Python语法

1. yield的用法:使函数变为生成器,即迭代器
   https://www.runoob.com/w3cnote/python-yield-used-analysis.html
   
2. 迭代器:函数类型的生成器的特点是：在每次调用 next() 的时候执行，遇到 yield 语句就完成一个元素的推导并返回，
   再次执行 next() 时从上次返回的 yield 语句处继续向后执行
   https://www.cnblogs.com/licongyu/p/5768141.html

3. python range() 函数可创建一个整数列表，一般用在 for 循环中。**故for循环是针对一个已经初始化之后的列表进行循环的**

4. classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的
    属性，类的方法，实例化对象等。(类似Java的静态方法)