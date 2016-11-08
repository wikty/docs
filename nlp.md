# Natural Language Processing 自然语言处理
By "natural language" we mean a language that is used for everyday communication by humans. In contrast to artificial languages such as programming languages and mathematical notations, natural languages have evolved as they pass from generation to generation, and are hard to pin down with explicit rules.

自然语言是人类同于交流的语言，是不同于编程语言、数学公式这类人造语言的


## Python for NLP

1. Install NLTK

		pip install nltk

2. Download NLTK data resource

		import nltk
		nltk.download()

### Frequency Distribution 单词的频率分布
It tells us the frequency of each vocabulary item in the text. It is a "distribution" because it tells us how the total number of word tokens in the text are distributed across the vocabulary items.

文本中单词的总次数在所有词汇项上的分布次数

NLTK provides built-in support for frequency distribution: 

	fd = FreqDist(text1)
	print(fd['house']) # how many times does house appear in the text1
	print(fd.most_common(50)) # the 50 most frequent words of text1
	fd.plot(50, cumulative=True) # generate a cumulative frequency plot for the 50 most frequent words
	fd.hapaxes() # hapaxes are words that occur once only

	fd = FreqDist([len(w) for w in text1]) # distribution of word length
	print(fd.most_common()) # the most frequent word lengths of text1
	fd.max() # the most word length
	fd[5] # the occurences of 5 word-length
	fd.freq(5) # the 

How can we automatically identify the words of a text that are most informative about the topic and genre of the text? the 50 most frequent words don't help us, and those words that occur once only, the so-called **hapaxes**, don't help too. Since neither frequent nor infrequent words help, we need to try something else.

文本中的高频词和低频词都不能有效的反应文本的有用信息

How about the long words of the text? Because long words are often hapaxes, so it would be better to consider with the frequently occuring of those long words.(i.e, eliminates frequent short words and infrequent long words)

		fd = FreqDist(text1)
		sorted(w for w in set(text1) if len(w) > 7 and fd[w] > 10)

如果同时考虑词长度以及词频率，效果会稍微好一些


	fdist = FreqDist(samples) 	create a frequency distribution containing the given samples
	fdist[sample] += 1 	increment the count for this sample
	fdist['monstrous'] 	count of the number of times a given sample occurred
	fdist.freq('monstrous') 	frequency of a given sample
	fdist.N() 	total number of samples
	fdist.most_common(n) 	the n most common samples and their frequencies
	for sample in fdist: 	iterate over the samples
	fdist.max() 	sample with the greatest count
	fdist.tabulate() 	tabulate the frequency distribution
	fdist.plot() 	graphical plot of the frequency distribution
	fdist.plot(cumulative=True) 	cumulative plot of the frequency distribution
	fdist1 |= fdist2 	update fdist1 with counts from fdist2
	fdist1 < fdist2 	test if samples in fdist1 occur less frequently than in fdist2


### Collocation 固定搭配

A collocation is a sequence of words that occur together unusually often. A characteristic of collocations is that they are resistant to substitution with words that have similar senses; for example, maroon wine sounds definitely odd.

固定搭配就是经常在一起出现的词。固定搭配的一个特性是，对使用同义词进行替换具有抗性

To get a handle on collocations, we start off by extracting from a text a list of word pairs, also known as **bigrams**. Collocations are essentially just frequent bigrams.

固定搭配必然是高频的bigram，获取文本中所有的bigram以及获取文本中所有固定搭配

	>>> list(bigrams(['more', 'is', 'said', 'than', 'done']))
	[('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]
	>>> text1.collocations()
	
You should know that collocations that emerge are very specific to the genre of the texts.


## Tokenization
A token is the technical name for a sequence of characters — such as hairy, his, or :) — that we want to treat as a group.

A word type is the form or spelling of the word (include punctuation symbols)independently of its specific occurrences in a text — that is, the word considered as a unique item of vocabulary.



## Words Model

## Train a model and predict scores


### Word Sense Disambiguation 词二义性消除
In word sense disambiguation we want to work out which sense of a word was intended in a given context.

词在不同上下文中往往具有不同的含义，确定特定上下文环境中某个词的含义就是消除二义性的过程

### Pronoun Resolution 代词解析
A deeper kind of language understanding is to work out "who did what to whom" — i.e., to detect the subjects and objects of verbs. Answering this question involves finding the antecedent of pronoun, **anaphora resolution** — identifying what a pronoun or noun phrase refers to — and **semantic role labeling** — identifying how a noun phrase relates to the verb

自然语言处理中经常需要理解“谁对谁做了什么”，其中的关键是要理解文本中的主语和宾语。主要涉及到找代词的先行词，利用对照分析识别代词名字的含义，以及利用语义角色标注识别名词短语如何同动词关联

### Machine Traslation
Machine translation is difficult because a given word could have several possible translations (depending on its meaning), and because word order must be changed in keeping with the grammatical structure of the target language. Today these difficulties are being faced by collecting massive quantities of parallel texts from news and government websites that publish documents in two or more languages. Given a document in German and English, and possibly a bilingual dictionary, we can automatically pair up the sentences, a process called **text alignment**. Once we have a million or more sentence pairs, we can detect corresponding words and phrases, and build a model that can be used for translating new text.

### Spoken Dialog Systems

	nltk.chat.chatbots()

### Textual Entailment

The challenge of language understanding has been brought into focus in recent years by a public "shared task" called Recognizing Textual Entailment (RTE).

### Limitations of NLP 自然语言处理不能什么

Despite the research-led advances in tasks like RTE, natural language systems that have been deployed for real-world applications still cannot perform common-sense reasoning or draw on world knowledge in a general and robust manner. We can wait for these difficult artificial intelligence problems to be solved, but in the meantime it is necessary to live with some severe limitations on the reasoning and knowledge capabilities of natural language systems. Accordingly, right from the beginning, an important goal of NLP research has been to make progress on the difficult task of building technologies that "understand language," using superficial yet powerful techniques instead of unrestricted knowledge and reasoning capabilities.

自然语言处理不能以鲁棒的方式进行推理或者理解现实世界的知识，这些人工智能的问题需要留待以后解决。对自然语言处理的定位应该在于，利用相关技术来理解自然语言，而不是解决推理或者知识理解方面的问题

## Text Corpora 语料库
Practical work in Natural Language Processing typically uses large bodies of linguistic data, or **corpora**. A text corpus is a large body of text. Many corpora are designed to contain a careful balance of material in one or more genres.

语料库是进行自然语言处理的数据基础，一般来说语料库会包含各种不同类型的大量文本

### Gutenberg Corpus 古登堡语料库

NLTK includes a small selection of texts from the Project Gutenberg electronic text archive, which contains some 25,000 free electronic books, hosted at <http://www.gutenberg.org>.

NLTK含有古登堡电子书计划的部分语料数据

	nltk.corpus.gutenberg.fileids() # the file identifiers in the Gutenberg corpus
	nltk.corpus.gutenberg.words('austen-emma.txt') # the words in the austen-emma.txt, return back a list to hold words
	nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')) # return back as Text object

Do some statistics for Gutenberg corpus:

	for fileid in gutenberg.fileids():
		num_chars = len(gutenberg.raw(fileid)) [1]
		num_words = len(gutenberg.words(fileid))
		num_sents = len(gutenberg.sents(fileid))
		num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
		print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

1. average word length 单词平均长度
2. average sentence length 句子平均长度
3. lexical diversity score(the number of times each vocabulary item appears in the text on average) 词汇平均出现次数 即词汇多样性评分

Observe that average word length appears to be a general property of English, since it has a recurrent value of 4. (In fact, the average word length is really 3 not 4, since the num_chars variable counts space characters.) By contrast average sentence length and lexical diversity appear to be characteristics of particular authors.

由分析可知，英语中单词的平均长度为3，而句子长度和词汇多样性评分则因文章而异

### Web & Chat Corpus 网络和聊天语料库

Although Project Gutenberg contains thousands of books, it represents established literature. It is important to consider less formal language as well. NLTK's small collection of web text from some web site. There is also a corpus of instant messaging chat sessions, originally collected by the Naval Postgraduate School for research on automatic detection of Internet predators.

除了上面的古登堡电子书外，NLTK还提供了别的语料库，毕竟古登堡文本太过书面式，webtext和nps chat语料库内容分别采集自网上论坛以及即时通讯工具

	nltk.corpus.webtext.fileids()
	nltk.corpus.webtext.raw('grail.txt')
	nltk.corpus.nps_chat.fileids()
	nltk.corpus.nps_chat.posts('10-19-20s_706posts.xml')

### Brown Corpus 布朗语料库

The Brown Corpus was the first million-word electronic corpus of English, created in 1961 at Brown University. This corpus contains text from 500 sources, and the sources have been categorized by genre, such as news, editorial, reviews, hobbies, fiction, and so on.(a complete list of its genre, see <http://icame.uib.no/brown/bcm-los.html>)

布朗语料库十分庞大，收录内容都根据流派进行了分类，因此布朗语料库很适合用于研究不同流派文本的差异

	from nltk.corpus import brown
	brown.categories() # text categories of the brown corpus
	brown.words(categories='news') # words belong to the news category
	brown.words(categories=['news', 'reviews'])
	brown.sents(categories='news')
	brown.fileids()
	brown.words(fileids=['cg62']) # words belong to the cg62 file


The usage of modal verbs in the news genre text:
新闻类别中情态动词的出现次数：

	fd = nltk.FreqDist(w.lower() for w in brown.words(categories='news'))
	modals = ['can', 'could', 'may', 'might', 'must', 'will']
	for m in modals:
		print(m+':', fd[m], end=' ')

The usage of modal verbs in the each genre text:
情态动词在各类文本中使用次数的对比：

	cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
	 genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
	modals = ['can', 'could', 'may', 'might', 'must', 'will']
	cfd.tabulate(conditions=genres, samples=modals)

### Reuters Corpus 路透语料库

The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. The documents have been classified into 90 topics, and grouped into two sets, called "training" and "test"; thus, the text with fileid 'test/14826' is a document drawn from the test set. This split is for training and testing algorithms that automatically detect the topic of a document. Unlike the Brown Corpus, categories in the Reuters corpus overlap with each other, simply because a news story often covers multiple topics.

路透语料库含有大量的新闻文档，文档被分成90个话题类别，并且被分成了训练组和测试组。一篇新闻往往会涉及到若干个话题，因此不同话题的文档会有重叠。我们可以查看文档包含哪些话题，也可以查看谈及某个话题的有哪些文档

	from nltk.corpus import reuters
	reuters.fileids()
	reuters.categories() # all of the avaiable topics
	reuters.categories('training/9865') # topcis covered by the document training/9865
	reuters.categories(['training/9865', 'training/9890'])
	reuters.fileids('barley') # all of files belong to the topic barley
	reuters.fileids(['barley', 'corn'])
	reuters.words('training/9865')
	reuters.words(['training/9865', 'training/9880'])
	reuters.words(categories='barley')
	reuters.words(categories=['barley', 'corn'])

### Inaugural Address Corpus 总统就职演说语料库

this corpus is actually a collection of 55 texts, one for each presidential address. An interesting property of this collection is its time dimension, its fileid's first 4 chars is the year of the text

绘制单词america和citizen在语料库文本中的使用次数（注：这里没有对文档长度归一化）

	from nltk.corpus import inaugural
	cfd = nltk.ConditionalFreqDist((target, fileid[:4]) for fileid in inaugural.fileids() for w in inaugural.words(fileid) for target in ['america', 'citizen'] if w.lower().startswith(target))
	cfd.plot()

### Annotated Text Corpora 文本注释语料库

Many text corpora contain linguistic annotations, representing POS tags, named entities, syntactic structures, semantic roles, and so forth. NLTK provides convenient ways to access several of these corpora, and has data packages containing corpora and corpus samples, freely downloadable for use in teaching and research(<http://nltk.org/data>)

NLTK 提供了很多注释型语料库，可供免费下载使用，这些语料库一般含有句法结构，语义角色等注释

### Corpora in Other Languages 非英语语料库

NLTK comes with corpora for many languages. there is a example, the corpora named *udhr*, contains the Universal Declaration of Human Rights in over 300 languages. Let's use a conditional frequency distribution to examine the differences in word lengths for a selection of languages included in the udhr corpus.

NLTK 提供了很多非英语语料库，这里以udhr语料库为例，该语料库包含300多种语言的人权申明文本，我们可以使用条件频率分布来观察，不同语言单词长度的分布情况

	from nltk.corpus import udhr
	languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
	cfd = nltk.ConditionalFreqDist((lang, len(word)) for lang in languages for word in udhr.words(lang + '-Latin1'))
	cfd.plot(cumulative=True)

### Basic Corpus Functionality 语料库对象常用方法

	fileids() 	the files of the corpus
	fileids([categories]) 	the files of the corpus corresponding to these categories
	categories() 	the categories of the corpus
	categories([fileids]) 	the categories of the corpus corresponding to these files
	raw() 	the raw content of the corpus
	raw(fileids=[f1,f2,f3]) 	the raw content of the specified files
	raw(categories=[c1,c2]) 	the raw content of the specified categories
	words() 	the words of the whole corpus
	words(fileids=[f1,f2,f3]) 	the words of the specified fileids
	words(categories=[c1,c2]) 	the words of the specified categories
	sents() 	the sentences of the whole corpus
	sents(fileids=[f1,f2,f3]) 	the sentences of the specified fileids
	sents(categories=[c1,c2]) 	the sentences of the specified categories
	abspath(fileid) 	the location of the given file on disk
	encoding(fileid) 	the encoding of the file (if known)
	open(fileid) 	open a stream for reading the given corpus file
	root 	if the path to the root of locally installed corpus
	readme()
	help(nltk.corpus.reader)	more documentation

### Corpus Structure 语料库的结构
Common Structures for Text Corpora: The simplest kind of corpus is a collection of isolated texts with no particular organization; some corpora are structured into categories like genre (Brown Corpus); some categorizations overlap, such as topic categories (Reuters Corpus); other corpora represent language use over time (Inaugural Address Corpus).

语料库的组织结构一般有一下几种：简单的文本聚合；按照genre，source，author，language等分类组织，并且有时这类方式会在不同类别间存在重叠；具有时间结构的特征，比如新闻语料库

### Loading Your Corpus

If you have your own collection of text files that you would like to access using the above methods, you can easily load them with the help of NLTK's *PlaintextCorpusReader*.

NLTK支持加载用户自定义语料库：

	from nltk.corpus import PlaintextCorpusReader
	corpus_root = '/usr/share/dict'
	fileids_regx = '*.txt' # a regular expression
	c = PlaintextCorpusReader(corpus_root, fileids_regx)
	c.fileids()

	# load your local copy of PennTreeBank
	from nltk.corpus import BracketParseCorpusReader
	corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj"
	file_pattern = r".*/wsj_.*\.mrg"
	ptb = BracketParseCorpusReader(corpus_root, file_pattern)
	ptb.fileids()

## Conditional Frequency Distribution 条件频率分布

When the texts of a corpus are divided into several categories, by genre, topic, author, etc, we can maintain separate frequency distributions for each category. This will allow us to study systematic differences between the categories.  A conditional frequency distribution is a collection of frequency distributions, each one for a different "condition". The condition will often be the category of the text.

所谓条件频率分布，就是每个项都有一个“条件”，一般来说“条件”是类别信息，在统计频率时，会依照不同条件分别计算对应条件下的频率分布。语料库往往会被组织成若干分类，如果可以对照不同分类下的分布情况，对研究分类间的差异很有意思。

In the plot() and tabulate() methods, we can optionally specify which conditions to display with a conditions= parameter. When we omit it, we get all the conditions. Similarly, we can limit the samples to display with a samples= parameter. This makes it possible to load a large quantity of data into a conditional frequency distribution, and then to explore it by plotting or tabulating selected conditions and samples.

NLTK 支持对条件频率分布以图表形式展示，分别对应方法`plot`，`tabulate`，这两个方法默认会展示所有类别中的所有项的频率分布，此外可以提供参数`conditions`，`samples`来限制展示的类别以及项

	cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre)) # (condition, event) as basic input item

	cfd.conditions() # input conditions
	cfd['news'] # the news condition is just a frequency distribution
	cfd['romance'].most_common(50)
	cfd['romance']['could'] 
	 
	genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor'] # conditions to be display
	
	modals = ['can', 'could', 'may', 'might', 'must', 'will'] # events to be display
	
	cfd.tabulate(conditions=genres, samples=modals) # display a table consist of the above conditions&events

## Generating Random Text with Bigrams 利用词对生成随机文本

### Bigrams & Conditional Distribution

The bigrams() function takes a list of words and builds a list of consecutive word pairs.

函数`bigrams`利用语句生成连续的词对序列

Use a conditional frequency distribution to create a table of bigrams, the first item of bigram as condition, the second item of bigram as event

将bigram的第一项当成condition，第二项当成event，对上面生成的词对序列进行条件频率建模。假设当前输出的单词（既是当前条件，又是当前上下文环境）是home，直观上来看CFD建模后，下一个输出的单词应该是在条件home下，频率最高的那个单词，以此类推直到生成了预定数目的单词


### Example

	def generate_model(cfd, word, num=20):
		for i in range(num):
			print(word, end=' ')
			word = cfd[word].max()

	words = nltk.corpus.genesis.words('english-kjv.txt')
	bigrams = nltk.bigrams(words)
	cfd = nltk.ConditionalFreqDist(bigrams)
	
	generate_model(cfd, 'home')


## Lexical Resources
A lexicon, or lexical resource, is a collection of words and/or phrases along with associated information such as part of speech and sense definitions. Lexical resources are secondary to texts, and are usually created and enriched with the help of texts. A lexical entry consists of a headword (also known as a lemma) along with additional information such as the part of speech and the sense definition. Two distinct words having the same spelling are called homonyms.

词典就是一系列单词和短语的集合。一般来说一条词汇项由：词条，读法，词性，含义组成。拼写一致的不同单词被叫做homonyms

### Wordlist Corpora 单词表语料库

#### Wordlist ship with Unix

The Words Corpus is the /usr/share/dict/words file from Unix, used by some spell checkers. We can access the wordlist by NLTK `nltk.corpus.words.words()`

Unix自带的单词表可以通过NLTK直接访问，下面是利用该单词表实现不常见单词过滤：

  	

	def unusual_words(text):
    	text_vocab = set(w.lower() for w in text if w.isalpha())
    	english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    	unusual = text_vocab - english_vocab
    	return sorted(unusual)
	
	unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))

### Stopwords

There is also a corpus of stopwords, that is, high-frequency words like the, to and also that we sometimes want to filter out of a document before further processing. 

通常对文本进行进一步处理前，我们都要过滤掉文本中的停止词，因此停止词数量少且出现频率高

	nltk.corpus.stopwords.words('english')

### FirstNames

The names corpus contains 8,000 first names categorized by gender. 

NLTK 含有第一名字的词典，该词典根据性别分类，下面我们要找出具有性别二义性的第一名字（即男女都有使用的名字）：

	names = nltk.corpus.names
	[w for w in names.words('male.txt') if w in names.words('female.txt')]

名字中最后字母在男女名字中使用情况的分布：

	cfd = nltk.ConditionalFreqDist((fileid, name[-1]) for fileid in nltk.corpus.names.fileids() for name in nltk.corpus.names.words(fileid))
	cfd.plot()

## Pronouncing Dictionary

A slightly richer kind of lexical resource is a table (or spreadsheet), containing a word plus some properties in each row. NLTK includes the CMU Pronouncing Dictionary for US English, which was designed for use by speech synthesizers.

NLTK 含有针对美式英语的带有读音的词典

	entries = nltk.corpus.cmudict.entries()
	entries[42379] # ('fireball', ['F', 'AY1', 'ER0', 'B', 'AO2', 'L'])

For each word, this lexicon provides a list of phonetic codes — distinct labels for each contrastive sound — known as phones. The symbols in the CMU Pronouncing Dictionary are from the Arpabet, described in more detail at <http://en.wikipedia.org/wiki/Arpabet>

每个词汇项含有单词以及读音代码表，读音代码表采用Arpabet

The following program finds all words whose pronunciation ends with a syllable sounding like nicks. You could use this method to find rhyming words.

查找尾音相同的单词，可以利用该方法查找押韵的单词：

	syllable = ['N', 'IH0', 'K', 'S']
	entries = nltk.corpus.cmudict.entries()
	[word for word, pron in entries if pron[-4:] == syllable]

we define a function to extract the stress digits and then scan our lexicon to find words having a particular stress pattern.

发现具有特定重音模式的单词：

	def stree(pron):
		return [char for phone in pron for char in phone if char.isdigit()]
	
	[w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]

## Comparative wordlist 多语言对照词典

Another example of a tabular lexicon is the comparative wordlist. NLTK includes so-called Swadesh wordlists, lists of about 200 common words in several languages. The languages are identified using an ISO 639 two-letter code.

NLTK 含有多语言对照词典，语言使用ISO-639两字符标识

	from nltk.corpus import swadesh
	swadesh.fileids()
	swadesh.words('en') # english wordlist
	swadesh.entries(['fr', 'en']) # comparative wordlist

## Toolbox

Perhaps the single most popular tool used by linguists for managing data is Toolbox, previously known as Shoebox since it replaces the field linguist's traditional shoebox full of file cards. Toolbox is freely downloadable from <http://www.sil.org/computing/toolbox/>.

A Toolbox file consists of a collection of entries, where each entry is made up of one or more fields. Most fields are optional or repeatable, which means that this kind of lexical resource cannot be treated as a table or spreadsheet.

Toolbox是一个有力的语言数据工具，每个toolbox文件含有很多entries，且每个entry含有不定数目的fields，因此不能将其当成表结构来处理，更适合用XML进行处理

		nltk.corpus.toolbox.entries('rotokas.dic')

## WordNet

WordNet is a semantically-oriented dictionary of English, similar to a traditional thesaurus but with a richer structure. NLTK includes the English WordNet, with 155,287 words and 117,659 synonym sets. We'll begin by looking at synonyms and how they are accessed in WordNet.

WordNet 是一个基于语义的英语词典，不同于传统词典的是它含有更加丰富的结构，NLTK 包含了WordNet的155,287个单词以及117,659个同义词集

### Synonyms

Explore synonyms with the help of WordNet:

1. 查找单词对应的所有同义词集合
2. 查看同义词集合中的单词
3. 查看同义词集的定义
4. 查看同义词集的例句
5. 查看同义词集中的所有lemmas（lemma同义词集中唯一标识一个词）

	from nltk.corpus import wordnet as wn
	wn.synsets('motorcar') # synonyms sets, output [Synset('car.n.01')]
	wn.synset('car.n.01').lemma_names() # synonymous words or lemmas
	wn.synset('car.n.01').definition() # definition
	wn.synset('car.n.01').examples() # example sentences
	wn.synset('car.n.01').lemmas()
	wn.lemma('car.n.01.automobile')
	wn.lemma('car.n.01.automobile').synset()
	wn.lemma('car.n.01.automobile').name()

	wn.synsets('car') # car has several synonyms sets
	wn.lemmas('car') #  all the lemmas involving the word car

### WordNet Hierarchy

First you should to know that synsets in WordNet are linked by a complex network of lexical relations.

WordNet synsets correspond to abstract concepts, and they don't always have corresponding words in English. These concepts are linked together in a hierarchy. Some concepts are very general, such as Entity, State, Event — these are called unique beginners or root synsets. Others, such as gas guzzler and hatchback, are much more specific. 

WordNet 的同义词集以层级树状结构进行组织，节点是同义词集，边表示同义词集从抽象到具体的关联，越位于上层的集概念越抽象，位于下层的是概念越具体

访问同义词集的子集

	wn.synset('car.n.01').hyponyms()
	[lemma.name() for s in wn.synset('car.n.01').hyponyms() for lemma in s.lemmas()]

访问同义词集的父集，也许含有多个父集

	wn.synset('car.n.01').hypernyms()
	wn.synset('car.n.01').hypernym_paths() # synset paths to root
	wn.synset('car.n.01').root_hypernyms() # the root synsets

Hypernyms and hyponyms are called lexical relations because they relate one synset to another. These two relations navigate up and down the "is-a" hierarchy. Another important way to navigate the WordNet network is from items to their components (meronyms) or to the things they are contained in (holonyms)

除了上面提到的从抽象概念到具体概念，以及从具体概念到抽象概念的同义词集访问方法外，还有从部分到整体以及从整体到部分的方法，比如树含有树干，树枝等部分`part_meronyms()`；树由心材和边材构成`substance_meronyms()`；一些树构成了森林`member_holonyms()`

	wn.synset('tree.n.01').part_meronyms()
	wn.synset('tree.n.01').substance_meronyms()
	wn.synset('tree.n.01').member_holonyms()

There are also relationships between verbs. For example, the act of walking involves the act of stepping, so walking entails stepping. Some verbs have multiple entailments

此外动词之间还有构成关系，比如走路由迈步构成;吃有咀嚼和吞咽构成；挑逗有高兴和失望构成

	wn.synset('walk.v.01').entailments()
	wn.synset('eat.v.01').entailments()
	wn.synset('tease.v.03').entailments()

由lemmas构成的词汇关系

	wn.lemma('horizontal.a.01.horizontal').antonyms()


	

