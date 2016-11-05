## XPath
A simple way to access like XML documents

## Basic Notation

Begin with a node-set so far. A new node-set is selected based on the original node-set, and condition is checked on this new node-set.

## Condition Checked

### Steps & Predicate
Steps go down to the next level to fetch the now node-set, but Predicate just test current node-set and discard the unmatched nodes from node-set

Each predicate can itself be just as complex as any expression: it can itself contain steps and predicates of its own.

### Example

`/foo/bar`

1. start with the node-set(only has the root node for now)
2. `/foo` for each node in original node-set(only has the root node), fetch its child nodes that are `foo` elements, and take those as the new node-set
3. `/bar` for each node in original node-set(all of `foo` elements), fetch its child nodes thar are `bar` elements, and take those as the new node-set

`/foo[bar]`

1. start with the node-set(only has the root node for now)
2. `/foo` for each node in original node-set(only has the root node), fetch its child nodes that are `foo` elements, and take those as the new node-set
3. `[bar]` for each node in origianl node-set, if it doesn't have child `bar` element, then discard the node

## Axes
Axes specify which set of nodes to select **before** checking the condition – it doesn’t have to be the child nodes of the current set, that’s just the default axis (which you don’t need to write) called `child::`


### Example

`/foo/following-sibling::bar`

1. start with the root node
2. `/foo` for each node in original node-set(only has the root node), fetch its child nodes that are `foo` elements, and take those as the new node-set
3. `/following-sibling::bar` for each node in original node-set(all of `foo` elements), fetch its sibling nodes thar are `bar` elements, and take those as the new node-set


1. The ancestors of the context node, consist of the parent of the context node and the parent's parent and so on

		ancestor::

2. The context node and its ancestors.

		ancestor-or-self::

3. The attributes of the context node, will be empty unless the context node is an node element

		attribute::

4. The children of the context node. A child is any node immediately below the context node in the tree.

		child::

5. The descendants of the context node. A descendant is a child or a child of a child and so on

		descendant-or-self::

6. All nodes that are after the context node in the tree, excluding any descendants, attribute nodes, and namespace nodes.

		following::

7. All the following siblings of the context node. The following-sibling:: axis identifies just those children of a parent node who appear in the tree after the context node. This axis excludes all other children that appear before the context node.

		following-sibling::

8. The namespace nodes of the context node

		namespace::

9. The parent of the context node, if there is one. The parent is the node immediately above the context node in the tree

		parent::

10. All nodes that are before the context node in the tree, excluding any ancestors, attribute nodes, and namespace nodes.

		preceding::

11. All the preceding siblings of the context node. The preceding-sibling:: axis identifies just those children of a parent node who appear in the tree before the context node. This axis excludes all other children that appear after the context node.

		preceding-sibling::

14. Just the context node itself

		self::


## Syntactic Shortcuts

1. `child` is the default axis, so you no need to write `child::` before the condition if you want go down into children elements
2. `/attribute::href` can write as `/@href` (for each node in the node-set, fetch its `href` attribute)
3. `/descendant-or-self::foo` can write as `//foo` (for each node in the node-set, fetch its descendant or self elements named `foo`)
4. `[position() = 1]` can write as `[1]` (for each node in the node-set, discard nodes that their position in the node-set is not 1, in another word just fetch the node-set's first element)
5. current node `.`
6. parent node `..`


## Syntax Reference

### Simple XML Document


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
	</root>


### syntax

1. Select the document node

		/

2. Select the 'root' element

		/root

3. Select all 'actor' elements that are direct children of the 'actors' element.

		/root/actors/actor

4. Select all 'singer' elements regardless of their positions in the document.

		//foo:singer

5. Select the 'id' attributes of the 'singer' elements regardless of their positions in the document.

		//foo:singer/@id

6. Select the textual value of first 'actor' element.

		//actor[1]/text()

7. Select the last 'actor' element. Select the second last 'actor' element.

		//actor[last()]
		//actor[last() - 1]

8. Select the first and second 'actor' elements using their position.

		//actor[position() < 3]

9. Select all 'actor' elements that have an 'id' attribute.

		//actor[@id]

10. Select the 'actor' element with the 'id' attribute value of '3'.

		//actor[@id='3']

11. Select all 'actor' nodes with the 'id' attribute value lower or equal to '3'.

		//actor[@id<=3]

12. Select all the children of the 'singers' node.

		/root/foo:singers/*

13. Select all the elements in the document.
	
		//*

14. Select all the 'actor' elements AND the 'singer' elements.

		//actor|//foo:singer

15. Select the name of the first element in the document.

		name(//*[1])

16. Select the numeric value of the 'id' attribute of the first 'actor' element.

		number(//actor[1]/@id)

17. Select the string representation value of the 'id' attribute of the first 'actor' element.

		string(//actor[1]/@id)

18. Select the length of the first 'actor' element's textual value.

		string-length(//actor[1]/text())

19. Select the local name of the first 'singer' element, i.e. without the namespace.

		local-name(//foo:singer[1])

20. Select the number of 'singer' elements.

		count(//foo:singer)

21. Select the sum of the 'id' attributes of the 'singer' elements.

		sum(//foo:singer/@id)

### Simple XML Document

	<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="myfile.xsl" ?>
	<bookstore specialty="novel">
	  <book style="autobiography">
	    <author>
	      <first-name>Joe</first-name>
	      <last-name>Bob</last-name>
	      <award>Trenton Literary Review Honorable Mention</award>
	    </author>
	    <price>12</price>
	  </book>
	  <book style="textbook">
	    <author>
	      <first-name>Mary</first-name>
	      <last-name>Bob</last-name>
	      <publication>Selected Short Stories of
	        <first-name>Mary</first-name>
	        <last-name>Bob</last-name>
	      </publication>
	    </author>
	    <editor>
	      <first-name>Britney</first-name>
	      <last-name>Bob</last-name>
	    </editor>
	    <price>55</price>
	  </book>
	  <magazine style="glossy" frequency="monthly">
	    <price>2.50</price>
	    <subscription price="24" per="year"/>
	  </magazine>
	  <book style="novel" id="myfave">
	    <author>
	      <first-name>Toni</first-name>
	      <last-name>Bob</last-name>
	      <degree from="Trenton U">B.A.</degree>
	      <degree from="Harvard">Ph.D.</degree>
	      <award>Pulitzer</award>
	      <publication>Still in Trenton</publication>
	      <publication>Trenton Forever</publication>
	    </author>
	    <price intl="Canada" exchange="0.7">6.50</price>
	    <excerpt>
	      <p>It was a dark and stormy night.</p>
	      <p>But then all nights in Trenton seem dark and
	      stormy to someone who has gone through what
	      <emph>I</emph> have.</p>
	      <definition-list>
	        <term>Trenton</term>
	        <definition>misery</definition>
	      </definition-list>
	    </excerpt>
	  </book>
	  <my:book xmlns:my="uri:mynamespace" style="leather" price="29.50">
	    <my:title>Who's Who in Trenton</my:title>
	    <my:author>Robert Bob</my:author>
	  </my:book>
	</bookstore>

### Syntax

1. All 'author' elements within the current context. Note that this is equivalent to the expression in the next row.

		./author

2. All 'author' elements within the current context.

		author

3. All 'first.name' elements within the current context.

		first.name

4. The document element ('bookstore') of this document.

		/bookstore

5. All 'author' elements in the document

		//author

6. All 'book' elements whose style attribute value is equal to the specialty attribute value of the 'bookstore' element at the root of the document.

		book[/bookstore/@specialty=@style]

7. All 'first-name' elements that are children of an 'author' element.

		author/first-name

8. All 'title' elements one or more levels deep in the 'bookstore' element (arbitrary descendants). Note that this is different from the expression in the next row.

		bookstore//title

9. All 'title' elements that are grandchildren of 'bookstore' elements.

		bookstore/*/title

10. All 'title' elements one or more levels deep in the current context.

		.//title

11. All elements that are the children of 'author' elements

		author/*

12. All 'last-name' elements that are grandchildren of 'book' elements

		book/*/last-name

13. All grandchildren elements of the current context

		*/*

14. All elements with the 'specialty` attribute

		*[@specialty]

15. The 'style' attribute of the current context

		@style

16. The 'exchange' attribute on 'price' elements within the current context

		price/@exchange

17. All 'price' elements with 'exchange' attributes of the current context

		price[@exchange]

18. All attributes of the current element context

		@*

19. All 'first-name' elements in the current context node. Note that this is equivalent to the expression in the next row.

		./first-name

20. All 'first-name' elements in the current context node.

		first-name

21. The first 'author' element in the current context node

		author[1]

22. The third 'author' element that has a 'first-name' child

		author[first-name][3]

23. The 'book' element from the 'my' namespace

		my:book

24. All elements from the 'my' namespace

		my:*

25. All attributes from the my namespace

		@my:*

26. The last 'author' child of each 'book' element of the current context node

		book/author[last()]

27. The last 'author' element from the entire set of 'author' children of 'book' elements of the current context node.

		(book/author)[last()]

28. All 'author' elements that contain at least one 'degree' element child, and that are children of 'book' elements that also contain at least one 'excerpt' element.

		book[excerpt]/author[degree]

29. All 'book' elements that contain 'author' children that in turn contain at least one 'degree' child.

		book[author/degree]

30. All 'author' elements that contain at least one 'degree' element child and at least one 'award' element child.

		author[degree][award]
		author[degree and award]

31. All 'author' elements that contain at least one 'degree' or 'award' and at least one 'publication' as the children

		author[(degree or award) and publication]

32. All 'author' elements that contain at least one 'degree' element child and that contain no 'publication' element children.

		author[degree and not(publication)]

33. All 'author' elements that contain at least one 'publication' element child and contain neither 'degree' nor 'award' element children.


		author[publication and not(degree or award)]

34. All 'author' elements that contain at least one 'last-name' element child with the value "Bob".

		author[last-name="Bob"]

34. All 'author' elements where the first 'last-name' child element has the value "Bob"

		author[last-name[1]="Bob"]

35. All 'degree' elements where the 'from' attribute is not equal to "Harvard".

		degree[@from != "Harvard"]

36. All 'author' elements whose value is "Bob"

		author[. = "Bob"]

37. All 'author' elements that contain a 'last-nam' child element whose value is Bob, and a 'price' sibling element whose value is greater than 50. 

		author[last-name="Bob" and ../price > 50]

38. The first three books

		book[position <= 3]

39. All 'author' elements that do no contain 'last-name' child elements with the value "Bob"

		author[not(last-name="Bob")]

40. All 'author' elements containing any child element whose value is "Bob"

		author[*="Bob"]

41. The second text node in each 'p' element in the current context node

		p/text()[2]

42. The nearest 'book' ancestor of the context node

		ancestor::book[1]

43. The nearest 'author' ancestor in the current context and this 'author' element is a child of a 'book' element

		ancestor::author[parent::book][1]
