---
title: XPath参考手册
author: Xiao Wenbin
date: 2016/11/06
category: xpath
---

## XPath简介

网络上许多文档都是结构化的，最常见的HTML文档就是典型的结构化文档，结构化文档因其自身内容组织具有良好的结构特征，使得这类文档可以灵活的用于数据存储，而XPath正是用于高效访问like-XML文档的语言，XPath语言虽然简单，但却可以编写出非常复杂的文档访问逻辑。

XPath工作流程：从一个初始节点集开始，然后通过条件测试来筛选新的节点集，不断如此，最后得到结果的节点集。

*目录*

[TOC]



## 轴

轴体现了节点跟文档中其它节点的关系，比如节点间的父子关系、兄弟关系、祖先关系等，所以在对节点集进行**条件测试之前**，可以先用轴来从节点集中进行筛选。默认的轴是`child::`，也即语法中忽略轴信息时，就认为筛选出当前节点集的子节点集以进行后续的条件测试。


### 样例

XPath：`/foo/following-sibling::bar`

1. 以文档根节点作为初始节点集（仅含根节点）
2. `/foo`表示遍历当前节点集，将节点的子节点中名称为`foo`的节点作为新节点集的元素
3. `/following-sibling::bar`表示遍历当前节点集，将节点的后续兄弟节点中名称为`bar`的节点作为新节点集的元素

### 常用轴

1. 祖先轴，当前节点的祖先节点

   	ancestor::element-name

2. 祖先轴+当前节点

   	ancestor-or-self::element-name

3. 属性轴，当前节点的属性

   	attribute::attr-name

4. 孩子轴，当前节点的儿子节点

   	child::element-name

5. 后代轴，当前节点的后代节点

   	descendant::element-name

6. 后代轴+当前节点

   	descendant-or-self::element-name

7. 节点树中位于当前节点之后的所有节点，不包括后代节点、属性节点、名称空间节点

   	following::element-name

8. 节点树中位于当前节点之后的所有兄弟节点

   	following-sibling::element-name

9. 名称空间轴

   	namespace::

10. 父亲轴，当前节点的父节点

   	parent::element-name

11. 节点树中位于当前节点之前的所有节点，不包括祖先节点、属性节点、名称空间节点

   	preceding::element-name

12. 节点树中位于当前节点之前的所有兄弟节点

   	preceding-sibling::element-name

13. 指向当前节点自身的轴

   	self::


## 条件测试

条件测试主要分为step和predicate两个动作。step就是进入下一层级元素以获得新节点；predicate则是对当前节点进行测试，保留通过测试的，丢掉测试失败的。*注*：predicate中又包含step和predicate

### 样例

XPath：`/foo/bar`

1. 以文档根节点作为初始节点集（仅含根节点）
2. `/foo`表示遍历当前节点集，将节点的子节点中名称为`foo`的节点作为新节点集的元素
3. `/bar`表示遍历当前节点集，将节点的子节点中名称为`bar`的节点作为新节点集的元素

XPath：`/foo[bar]`

1. 以文档根节点作为初始节点集（仅含根节点）
2. `/foo`表示遍历当前节点集，将节点的子节点中名称为`foo`的节点作为新节点集的元素
3. `[bar]` 表示遍历当前节点集，将含有`bar`子节点的节点作为新节点集的元素，不含有`bar`子节点的节点则被丢弃

## XPath的Shortcut

1. `child` 是默认轴，如果意图运用测试来筛选节点集的子节点，则可以在条件测试的前面忽略`child::`
2. 属性轴的简写，`attribute::href` 可以简写为`@href`
3. 后代轴的简写，`/descendant-or-self::foo`可以简写为`//foo`
4. 位置筛选简写，`[position() = 1]`可以简写为`[1]`
5. 当前节点`.`
6. 父节点`..`

## 语法参考

### 样例文档


	<root xmlns:foo="http://www.foo.org/" xmlns:bar="http://www.bar.org">
		<actors>
			<actor id="1">Christian Bale</actor>
			<actor id="2">Liam Neeson</actor>
			<actor id="3">Michael Caine</actor>
		</actors>
		<foo:singers>
			<foo:singer id="4">Tom Waits</foo:singer>
			<foo:singer id="5">B.B. King</foo:singer>
			<foo:singer id="6">Ray Charles</foo:singer>
		</foo:singers>
		<description>
			<profile refid="1">Christian Bale is a man</profile>
			<profile refid="2">Liam Neeson is a man</profile>
			<profile refid="3">Michael Caine is a woman</profile>
		</decription>
		
	    <bookstore specialty="novel">
	      <book style="autobiography">
	        <author>
	          <username>Joe Bob</username>
	          <award>Trenton Literary Review Honorable Mention</award>
	        </author>
	        <price>12</price>
	      </book>
	      <book style="textbook">
	        <author>
	          <username>Mary Bob</username>
	          <publication>Turing</publication>
	        </author>
	        <editor>
	          <username>Britney Bob</username>
	        </editor>
	        <price>55</price>
	      </book>
	      <book style="novel" id="myfave">
	        <author>
	          <username>Toni Bob</username>
	          <degree from="Trenton U">B.A.</degree>
	          <degree from="Harvard">Ph.D.</degree>
	          <award>Pulitzer</award>
	          <publication>Still in Trenton</publication>
	          <publication>Trenton Forever</publication>
	        </author>
	        <price intl="Canada" exchange="0.7">6.50</price>
	        <excerpt>
	          <p>It was a dark and stormy night.</p>
	        </excerpt>
	      </book>
	    </bookstore>
	</root>

### 语法

1. 文档节点

   	/

2. 文档最高层次节点`root`

   	/root

3. 文档中`root`节点的子节点`actors`的所有`actor`儿子节点

   	/root/actors/actor

4. 文档中在名称空间`foo`下的`singer`节点且不考虑其在文档中的位置

   	//foo:singer

5. 节点`root`下的所有后代`actor`节点

   	/root//actor

6. 文档中所有的`foo:singer`节点的`id`属性值

   	//foo:singer/@id

7. 文档中从前往后第一个`actor`节点的文本内容

   	//actor[1]/text()

8. 文档中从前往后最后一个`actor`和倒数第二个`actor`

   	//actor[last()]
   	//actor[last() - 1]

9. 文档中每个`actors`的最后一个`actor`子节点

   	//actors/actor[last()]

10. 文档中所有`actors`的所有`actor`子节点的最后一个

   	//(actors/actor)[last()]

11. 文档中从前往后第一个和第二个`actor`节点

   	//actor[position() < 3]

12. 文档中含有属性`id`的所有`actor`节点

   	//actor[@id]

13. 文档中属性`id`值等于3的所有`actor`节点

   	//actor[@id='3']

14. 文档中属性`id`值小于等于3的所有`actor`节点

   	//actor[@id<=3]

15. 文档中`foo:singers`节点的所有儿子节点

   	/root/foo:singers/*

16. 文档中`root`所有的孙子节点`actor`

   	/root/*/actor

17. 文档中含有属性`id`的所有节点

   	//*[@id]

18. 文档中的所有节点

   	//*

19. 文档中所有`actor`和`foo:singer`节点

   	//actor|//foo:singer

20. 文档中第一个元素的名称

   	name(//*[1])

21. 文档第一个`actor`节点的属性`id`的数值表示

   	number(//actor[1]/@id)

22. 文档第一个`actor`节点的属性`id`的字符串表示

   	string(//actor[1]/@id)

23. 文档第一个`actor`节点的内容长度

   	string-length(//actor[1]/text())

24. 文档中第一个`foo:singer`的名称（不含名称空间）

   	local-name(//foo:singer[1])

25. 文档中`foo:singer`节点的数目

   	count(//foo:singer)

26. 文档中`foo:singer`节点的所有属性

   	//foo:singer/@*

27. 名称空间`foo`下的所有属性

   	@foo:*

28. 文档中的跟第一个`actor`相关的`profile`节点

   	//profile[@refid=//actor[1]/@id]

29. 文档中含有`actor`的第一个`actors`节点

   	//actors[actor][1]

30. 从当前节点上下文中获取子节点`actor`

   	actor
   	./actor

31. 对文档中所有`foo:singer`节点的`id`属性值求和

   	sum(//foo:singer/@id)

32. 文档中含有`author/degree`的`book`节点

   	book[author/degree]

33. 文档中所有含有`degreee`和`award`子节点的`author`节点

   	author[degree][award]
   	author[degree and award]

34. 文档中含有子节点`degree`或`award`且同时含有`publication`的`author`节点

   	author[(degree or award) and publication]

35. 文档中含有子节点`degree`且不含有`publication`的`author`节点

   	author[degree and not(publication)]


36.    文档中含有值等于`Bob`的子节点`username`的节点`author`

       	author[username="Bob"]

37.    文档中所有值不等于`Bob`的节点`author`

                 author[. != "Bob"]

38.    文档中含有值等于`Bob`的`username`子节点的`author`节点，且其兄弟节点`price`大于50

                 author[username="Bob" and ../price > 50]

39.    文档中含有任意子节点值等于`Bob`的`author`节点

                 author[*="Bob"]

40.    节点`p`的第二个文本节点内容

                 p/text()[2]

41.    当前节点最近的`book`祖先节点

                 ancestor::book[1]

42.    当前节点最近的`author`祖先节点，且其父亲节点是`book`

                 ancestor::author[parent::book][1]

43.    当前节点的所有儿子节点（不含文本节点）

                 /*

44.    当前节点的所有儿子节点（含有文本节点）

                 /child::node()

45.    当前节点所有不含文本的儿子节点

                 /child::node()[not(text())]

46.    当前节点的所有儿子节点（不含文本节点）

                 /child::node()[not(self::text())]