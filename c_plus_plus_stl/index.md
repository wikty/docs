---
title: C++ Standard Template Library
author: Xiao wenbin
date: 2016/11/08
category: C++
---

# STL简介

C++标注库（The Standard Template Library）提供了丰富的泛型组件，包括常用数据结构、算法、容器类、迭代类等模板。

*目录*

[TOC]

# Helper Classes

## Pair

* 定义

  ```c++
  // don't need to include header
  template <class U, class V>
  struct pair {
  	U first;
  	V second;
  	pair(const U& first = U(), const V& second = V())
        :first(first), second(second) {}
  };

  template <class U, class Y>
  pair<U, V> make_pair(const U& first, const V& second);Description
  ```

* 描述

  `pair` 是 `map` 和 `set`这类关联容器数据结构的基础，可以将`pair`的第一个元素当作键，第二个元素当作关联的值。此外要注意`pair`不是类而是一个结构体，因此成员变量是公开的，可以在外部直接访问。 

# Container Classes

* 容器类是抽象数据结构（Abstract Data Types ）
* 容器类是泛型的，因此要通过类型参数来初始化
* 容器类提供了工厂方法来创建迭代器，以供遍历容器中的元素

## Sequential

* 常用序列类有：`vector`，`deque`，`list`等
* 以线性方式组织容器中的数据
* 线性方式组织并不意味着物理储存是线性的

### Vector

* 定义

  ```c++
  #include <vector>
  using namespace std;

  template <class T>
  class vector {
  	public:
  		vector();
  		vector(const vector<T>& originalMap);
  		
  		typedef implementation_specific_class_1 iterator;
  		typedef implementation_specific_class_2 const_iterator;

  		bool empty() const;
  		long size() const;
  		void clear();

  		void push_back(const T& elem);
  		void pop_back();

  		T& operator[](int i);
  		const T& operator[](int i) const;
  		iterator insert(iterator where, const T& elem);
  		iterator erase(iterator where);

  		iterator begin();
  		iterator end();
  		const_iterator begin() const;
  		const_iterator end() const;
  };
  ```

* 描述

  `vector` 有点像动态数组，可以使用`[]`操作符访问以及修改元素，也可以使用成员方法`insert`和`erase`来在任何地方插入删除元素（内部自动完成空间的伸缩以及元素的移动）。

  	// 将文件流读入到vector中
  	static void readFile(ifstream& infile, vector<string>& lines)
  	{
  		assert(lines.size() == 0);
  		assert(infile.good());
  	
  		string line;
  		while (infile.peek() != EOF) {
  			getline(infile, line); // reassign line to be next line of file
  			lines.push_back(line); // append
  		}
  		cout << "All done! (Number of lines: " << lines.size() << ")" << endl;
  	}
  	
  	// 数组方式访问
  	vector<double> transactionAmounts;
  	double totalSales = 0.0;
  	for (int i = 0; i < transactionAmounts.size(); i++)
  		totalSales += transactionAmounts[i];
  	
  	// 迭代器方式访问
  	vector<double>::const_iterator curr = transactionAmounts.begin();
  	vector<double>::const_iterator end = transactionAmouts.end();
  	for (; curr != end; ++curr)
  		totalSales += *curr;

### Deque

`deque` 是双端队列，可以高效（常量时间）的在队列两端插入删除元素。

### List

`list` 可以在任何位置高效（常量时间）的插入删除元素（底层用双向链表实现），不支持随机访问。

## Associative

* 支持数据的关联存储（即键-值存储）
* 底层使用平衡二叉树实现

### Set

`set` 中元素的键唯一

### Map

* 定义

  ```c++
  #include <map>
  using namespace std;

  template <class Key, class Value>
  class map {
  	public:
    		map();
    		map(const map<Key, Value>& originalMap);        
    		pair<iterator, bool> insert(const pair<Key, Value>& newEntry);
    		iterator find(const Key& key);
    		const_iterator find(const Key& key) const;
    		Value& operator[](const Key& key);
    		iterator begin();
    		iterator end();
    		const_iterator begin() const;
    		const_iterator end() const;
  };
  ```

* 描述

  `map`是泛型符号表，键和值的类型都允许用户来指定

* Description

  The `map` is the STL’s generic symbol table, and it allows you to specify the data type for both the key and the value

  ```c++
  // insert是非强制插入，返回值pair的第二个元素用来解释插入是否成功
  typedef map<string, vector<string> > chordMap;
  chordMap jazzChords;
  vector<string> cmajor;
  cmajor.push_back("C");
  cmajor.push_back("E");
  cmajor.push_back("G");
  pair<chordMap::iterator, bool> result = jazzChords.insert(make_pair(string("C Major"), cmajor));

  if(result.second)
  	cout << "\" << result.first->first << "\" was successfully inserted." << endl;
  else
  	cout << "\" << result.first->first << "\" already present." << endl;

  // find查找是否含有某个键
  // 在C语言中，当查找不存在是会返回NULL或者-1，
  // 而容器类则通过定义了一个特殊值用来标识未找到
  chordMap::const_iterator found = jazzChords.find("F# minor 11");
  if (found == jazzChords.end()) // container.end()表示未找到的标识
  	cout << "Chord was never recorded." << endl;

  // []操作符允许访问修改value by key
  map<string, int> portfolio;
  // portfolio.insert(make_pair(string("LU"), 400));
  portfolio["LU"] = 400;
  portfolio["AAPL"] = 80;
  portfolio["GOOG"] = 6500;
  portfolio["GOOG"] += 30

  // 迭代访问
  int stockCount = 0;
  map<string, int>::const_iterator curr = stocks.begin();
  while (curr != stocks.end()) {
  	stockCount += curr->second;
  	++curr;
  }
  ```


### Multimap

`multimap` 支持插入相同键，即键不唯一

## Adapter 

* stack
* queue
* priority
* queue

# Iterator Classes

* STL迭代器可以看成指针的推广
* 迭代器一般用来遍历访问一些对象
  * 迭代器是泛型编程的核心，充当容器类和算法类的桥梁

## Input Iterator

输入迭代器用来序列数据的读取。支持解引用操作来访问被引用的对象，递增操作来访问下一个迭代器

```c++
// Fill a vector with values read from standard input.
std::vector<int> v;
for (istream_iterator<int> i = cin; i != istream_iterator<int> (); ++i)
	v.push_back (*i);

// Fill vector with values read from stdin using std::copy()
std::vector<int> v;
std::copy (std::istream_iterator<int>(std::cin), std::istream_iterator<int>(), std::back_inserter(v));
```

## Output Iterator

输出迭代器用来序列数据的写入。可以将输出迭代器想象成磁带，支持在当前位置读取、写入、移动到一下位置，但是不能回退。

```c++
// Copy a file to cout via a loop.
std::ifstream ifile ("example_file");
int tmp;
while (ifile >> tmp) std::cout << tmp;
// Copy a file to cout via input & output iterators
std::ifstream ifile ("example_file");
std::copy (std::istream_iterator<int> (ifile), std::istream_iterator<int> (), std::ostream_iterator<int> (std::cout));
```

## Forward Iterator

前向迭代器必须同时实现了输入输出迭代器

```c++
template <typename ForwardIterator, typename T>

void replace (ForwardIterator first, ForwardIterator last, const T& old_value, const T& new_value) {
	for (; first != last; ++first)
		if (*first == old_value) *first = new_value;
}

std::vector<int> v (3, 1); // 1, 1, 1
v.push_back (7); // 1, 1, 1, 7
replace (v.begin(), v.end(), 7, 1);
assert (std::find (v.begin(), v.end(), 7) == v.end());
```

## Bidirectional Iterator

双向迭代器支持向前和向后访问操作，许多容器类均支持双向迭代，例如：`list`，`set`， `multiset`，`map`，`multimap`

```c++
template <typename BidirectionalIterator, typename Compare>
void bubble_sort (BidirectionalIterator first, BidirectionalIterator last, Compare comp) {
	BidirectionalIterator left_el = first, right_el = first;
	++right_el;
	while (first != last)
	{
		while (right_el != last) {
			if (comp(*right_el, *left_el)) std::swap (left_el, right_el);
			++right_el;
			++left_el;
		}
		--last;
		left_el = first, right_el = first;
		++right_el;
	}
}
```

## Random Access Iterator

随机访问迭代器允许随机的访问容器中的元素，所谓随机就是可以直接访问容器中任意位置的元素，容器类`vector`，`deque`都实现了随机访问

```c++
std::vector<int> v (1, 1);
v.push_back (2); v.push_back (3); v.push_back (4); // vector v: 1 2 3 4
std::vector<int>::iterator i = v.begin();
std::vector<int>::iterator j = i + 2; cout << *j << " ";
i += 3; std::cout << *i << " ";
j = i - 1; std::cout << *j << " ";
```

# Generic Algorithms

算法不是直接作用于容器而是作用于迭代器。每个容器类都通过Trait来声明迭代器，`vector`和`deque`声明了随机访问迭代器，`list`、`map`、`set`、`multimap`、`multiset`等声明了双向迭代器，可以调用容器类的工厂方法`begin`、`end`、`rbegin`、`rend`来访问迭代器。算法在实现时，通过调用容器类的迭代器来访问容器元素的，一致的容器类迭代器接口使得算法的泛型成为了可能。所谓算法泛型是指，算法不是针对特定容器类而编写的，而是面向迭代器编写的，不同的容器类只要实现了相同的迭代器，就都可以使用相同的算法。

## Find

返回被查找元素第一次出现位置的前向迭代器

```c++
#include <vector>
#include <algorithm>
#include <assert>
#include <string>

int main (int argc, char *argv[]) {
	std::vector <std::string> projects;
	for (int i = 1; i < argc; ++i)
		projects.push_back (std::string (argv [i]));
	std::vector<std::string>::iterator j = std::find (projects.begin (), projects.end (), std::string ("Lab8"));
	if (j == projects.end ()) return 1;
	assert ((*j) == std::string ("Lab8"));
	return 0;
}
```

## Copy

从输入迭代器复制到输出迭代器

```c++
std::vector<int> v;
std::copy (std::istream_iterator<int>(std::cin), std::istream_iterator<int>(), std::back_inserter(v));
std::copy (v.begin (), v.end (), std::ostream_iterator<int> (std::cout));
```

## Fill

将序列的值都赋值为某个值

```c++
int a[10];
std::fill (a, a + 10, 100);
std::fill_n (a, 10, 200);
std::vector<int> v (10, 100);
std::fill (v.begin (), v.end (), 200);
std::fill_n (v.begin (), v.size (), 200);
```

## Replace

替换

```c++
std::vector<int> v;
v.push_back(1);
v.push_back(2);
v.push_back(3);
v.push_back(1);
std::replace (v.begin (), v.end (), 1, 99);
assert (V[0] == 99 && V[3] == 99);
```

## Remove

移除

```c++
int *nend = std::remove (pbegin, pend, 20);
// 根据测试条件移除元素
pend = std::remove_if (pbegin, pend, is_odd ());
```
## Transform

```c++
std::transform
```
## For each

```c++
std::for_each
```

