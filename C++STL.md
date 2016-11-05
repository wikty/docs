# STL

The Standard Template Library provides a set of well structured
generic C++ components that work together in a seamless way.

* [Helper Classes](#helper-classes)
* [Container Classes](#container-classes)
* [Iterator Classes](#iterator-classes)



## <a name="function-templates"></a>function templates

## <a name="generic-algorithms"></a>generic algorithms

Mutating, non-mutating, sorting, numeric

## <a name="helper-classes"></a>helper classes

#### pair

1. Definition
 		
		// don't need to include header
		template <class U, class V>
		struct pair {
			U first;
			V second;
			pair(const U& first = U(), const V& second = V()) :
			first(first), second(second) {}
		};
		
		template <class U, class Y>
		pair<U, V> make_pair(const U& first, const V& second);

2. Description

	`pair` is the basis for the `map` dnd `set` associative containers because it stores (potentially) heterogeneous pairs of data together, A pair binds a key (known as the first element) with an associated value (known as the second element)
	
	`pair` is a struct rather than a class, so you're free to directly access the `first` and `second` fields

	many other STL classes depend on the `pair` container class, all of the associative containers(`map`, `hash_map`, and `multimap`) require a `pair` be used to insert new data

## <a name="container-classes"></a>container classes

1. STL containers are Abstract Data Types (ADTs)
2. All containers are parameterized by the type(s) they contain
3. Each container declares various traits
4. Each container provides factory methods for creating iterators(i.e, `begin`, `end`, `rbegin`, `rend`)

### Sequential: vector, deque, list

1. arrange the data they contain in a linear manner
2. element order has nothing to do with their values
3. don't need to be stored contiguous

#### vector

1. Definition
		
		#include <vector>
		using namespace std;
		
		template <class T>
		class vector {
			public:
				vector();
				vector(const vector<T>& originalMap);
				
				typedef implementation_specific_class_1 iterator;
				typedef implementation_specific_class_2 const_iterator;

				bool empty() const; // true if logical length is 0
				long size() const; // returns logical length of vector
				void clear(); // empties the vector, sets size to 0

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
		

2. Description

	`vector` behaves like an array, you can set the size of the `vector` up front, you can use operator[] to access and modify its entries, and you can insert/erase element in anywhere you want and let the `vector` do all of the shifting to you(`vector` will grow and shrink automatically)

	`push_back` tacks something new to the end of the vector, the object argument pass to `push_back` will be deep copied into vector, the pointer argument pass to `push_back` will referenc the same memory from within the vector as well

		static void readFile(ifstream& infile, vector<string>& lines)
		{
			assert(lines.size() == 0); // assert aborts program if test fails
			assert(infile.good()); // verify ifstream refers to legit file

			string line;
			while (ifstream.peek() != EOF) {
				getline(ifstream, line); // reassign line to be next line of file
				lines.push_back(line); // append
			}
			cout << "All done! (Number of lines: " << lines.size() << ")" << endl;
		}	

		The STL’s intent is to provide an iterator with each and every container type it defines, making it the responsibility of the iterator to mimic the behavior of true pointers while providing sequential access to all contained elements

		iterate over the vector using the same semantics normally used to traverse traditional arrays, or using `begin` and `end` methods

		vector<double> transactionAmounts;
		// initialization code omitted

		double totalSales = 0.0;
		for (int i = 0; i < transactionAmounts.size(); i++)
			totalSales += transactionAmounts[i];
	
		vector<double> transactionAmounts;
		// initialization code omitted

		double totalSales = 0.0;
		vector<double>::const_iterator curr = transactionAmounts.begin();
		vector<double>::const_iterator end = transactionAmouts.end();
		for (; curr != end; ++curr)
			totalSales += *curr;


#### deque

1. Definition

2. Description

	`deque` is a double-ended queue, efficient insertion/removal elements at the beginning/end of the sequence

#### list

1. Definition

2. Description

	`list` has constant time insertion & deletion at any point in the sequence (not just at the beginning/end), but does not support random access. `list` is implemented as doubly-linked list

### Associative: set, multiset, map, multimap

1. maintain the data in structures suitable for fast associative operations
2. implemented as balanced binary trees

#### set

1. Definition
	

2. Description

	`set` is an ordered collection of unique kekys

#### map

1. Definition

		#include <map>
		using namespace std;

		template <class Key, class Value>
		class map {
			public:
				map();
				map(const map<Key, Value>& originalMap);
				
				// typedefs for iterator and const_iterator

				pair<iterator, bool> insert(const pair<Key, Value>& newEntry);
				iterator find(const Key& key);
				const_iterator find(const Key& key) const;

				Value& operator[](const Key& key);

				iterator begin();
				iterator end();
				const_iterator begin() const;
				const_iterator end() const;
		};
		

2. Description

	The `map` is the STL’s generic symbol table, and it allows you to specify the data type for both the key and the value

	The `insert` method is stubborn, because it doesn’t permit existing keys to be reassigned to new values, return value is a pair, the first field of the pair stores an iterator addressing the argument pair stored inside the map on behalf of the key, the second field of the pair to report whether or not the key is already bound to some other value 

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

	`find` a key whether or not already inside the map. The comparison of the return value to jazzChords.end() might. We’re used to sentinel values of NULL and –1, but the STL has each instance of each container define its own sentinel value, and that value is categorically reported by the container’s end method. The check against end() should generally be made—particularly if you’re not sure the key is even present.

		chordMap::const_iterator found = jazzChords.find("F# minor 11");
		if (found == jazzChords.end())
			cout << "Chord was never recorded." << endl;

	`[]` operator allows you access and even update a map using array-like semantics

		map<string, int> portfolio;
		// portfolio.insert(make_pair(string("LU"), 400));
		portfolio["LU"] = 400;
		portfolio["AAPL"] = 80;
		portfolio["GOOG"] = 6500;
		// operator[] allows us to update an existing value to something new—something the insert operation doesn’t allow
		portfolio["GOOG"] += 30

	iterate map

		int stockCount = 0;
		map<string, int>::const_iterator curr = stocks.begin();
		while (curr != stocks.end()) {
			stockCount += curr->second;
			++curr;
		}

#### multimap

1. Definition

2. Description

	`multimap` can support multiple equivalent (non-unique) keys

### Adapters: stack, queue, priority queue
 
## <a name="iterator-classes"></a>iterator classes

1. STL iterators are a C++ implementation of the Iterator pattern
2. STL iterators are a generalization of pointers
3. Iterators are often used to iterate over a range of objects
4. Iterators are central to generic programming because they are an interface between containers and algorithms
		
### input iterator
input iterators are used to read values from a sequence

They may be dereferenced to refer to some object & may be incremented to obtain the next iterator in a sequence

	// Fill a vector with values read from standard input.
	std::vector<int> v;
	for (istream_iterator<int> i = cin; i != istream_iterator<int> (); ++i)
		v.push_back (*i);

	// Fill vector with values read from stdin using std::copy()
	std::vector<int> v;
	std::copy (std::istream_iterator<int>(std::cin), std::istream_iterator<int>(), std::back_inserter(v));

### output iterator
output iterator is a type that provides a mechanism for storing (but not necessarily accessing) a sequence of values

Intuitively, an output iterator is like a tape where you can write a value to the current location & you can advance to the next location, but you cannot read values & you cannot back up or rewind

	// Copy a file to cout via a loop.
	std::ifstream ifile ("example_file");
	int tmp;
	while (ifile >> tmp) std::cout << tmp;
	// Copy a file to cout via input & output iterators
	std::ifstream ifile ("example_file");
	std::copy (std::istream_iterator<int> (ifile), std::istream_iterator<int> (), std::ostream_iterator<int> (std::cout));

### forward iterator
