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

A good tool for creating annotated text corpora is called Brat, and available from <http://brat.nlplab.org/>.

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

	import random
	
	def generate_model(cfd, word, num=20, k=5):
		for i in range(num):
			print(word, end=' ')
			# word = cfd[word].max()
			word = random.choice(cfd[word].most_common(k))[0]

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
	wn.synset('tree.n.01').part_holonyms()	

There are also relationships between verbs. For example, the act of walking involves the act of stepping, so walking entails stepping. Some verbs have multiple entailments

此外动词之间还有构成关系，比如走路由迈步构成;吃有咀嚼和吞咽构成；挑逗有高兴和失望构成

	wn.synset('walk.v.01').entailments()
	wn.synset('eat.v.01').entailments()
	wn.synset('tease.v.03').entailments()

由lemmas构成的词汇关系

	wn.lemma('horizontal.a.01.horizontal').antonyms()


We have seen that synsets are linked by a complex network of lexical relations. Given a particular synset, we can traverse the WordNet network to find synsets with related meanings. Knowing which words are semantically related is useful for indexing a collection of texts, so that a search for a general term like *vehicle* will match documents containing specific terms like *limousine*.

WordNet通过同义词集间的词汇关系构成了复杂的网络关系，知道同义词集语义上的关联性对检索一段文本很有用处，比如检索vehicle时，会返回包含limousine的文档（因为limousine是一种vehicle）

查看两个同义词集最近公共父同义词集：

	one_synset.lowest_common_hypernyms(another_synset)

度量同义词集所有路径中离根节点最近的路径长度，也即反应同义词集在概念上的具体程度：

	wn.synset('vertebrate.n.01').min_depth() # 8
	wn.synset('entity.n.01').min_depth() # 0

查看两个同义词集到根节点上路径的相似度：

	one_synset.path_similarity(another_synset) # [0, 1] or -1

### VerbNet

 NLTK also includes VerbNet, a hierarhical verb lexicon linked to WordNet. It can be accessed with `nltk.corpus.verbnet`.



## Zipf's Law
 
Let f(w) be the frequency of a word w in free text. Suppose that all the words of a text are ranked according to their frequency, with the most frequent word first. Zipf's law states that the frequency of a word type is inversely proportional to its rank (i.e. f × r = k, for some constant k). For example, the 50th most common word type should occur three times as frequently as the 150th most common word type.

将一段文本中的单词按照其在该文本中的出现次数进行排序，根据Zipf's Law 单词出现次数和单词排名是成反比的，也就是说对于任意单词，该单词排名*该单词出现次数应该是一个常量

1. Write a function to process a large text and plot word frequency against word rank using `pylab.plot`. Do you confirm Zipf's law? (Hint: it helps to use a logarithmic scale). What is going on at the extreme ends of the plotted line? 绘制大段文本的单词出现次数以及单词排名，看是否符合Zipf's Law
    
2. Generate random text, e.g., using `random.choice("abcdefg ")`, taking care to include the space character. You will need to import random first. Use the string concatenation operator to accumulate characters into a (very) long string. Then tokenize this string, and generate the Zipf plot as before, and compare the two plots. What do you make of Zipf's Law in the light of this? 随机生成大量的文本并切分为单词，对其进行分析，看是否符合Zipf's Law

## Text Sources 文本数据来源

The processing pipeline of source text to the available corpus material

从文本数据来源到生成语料数据的过程：

1. 从网络下载或从本地加载特定格式的数据，这里要注意编码问题
2. 根据数据格式提取其中的文本内容，并对数据一般化并进行清理
3. 对文本内容tokenization，生成token list
4. 将token list装换为Text对象，该对象支持各种分析文本的方法

### Electronic Books

A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from [Project Gutenberg](http://www.gutenberg.org/). Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages.

NLTK 语料库中只含有古登堡项目的一小部分文本，我们可以从利用古登堡项目的其他电子书数据来作为我们文本的数据来源



	from urllib import request
	import nltk
	url = "http://www.gutenberg.org/files/2554/2554.txt"
	response = request.urlopen(url)
	raw = response.read().decode('utf8')
	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	text.collocations()

### HTML Documents

Much of the text on the web is in the form of HTML documents. You can use a web browser to save a page as text to a local file, then access this as described in the section on files below. However, if you're going to do this often, it's easiest to get Python to do the work directly. To get text out of HTML we will use a Python library called *BeautifulSoup*.

使用BeautifulSoup库来解析HTML文档中的文本数据

	from bs4 import BeautifulSoup
	url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html).get_text()
	tokens = nltk.word_tokenize(raw)
	text = nltk.Text(tokens)
	text.concordance('gene')

### Search Engine Results

The web can be thought of as a huge corpus of unannotated text. Web search engines provide an efficient means of searching this large quantity of text for relevant linguistic examples. The main advantage of search engines is size: since you are searching such a large set of documents, you are more likely to find any linguistic pattern you are interested in.  A second advantage of web search engines is that they are very easy to use. Thus, they provide a very convenient tool for quickly checking a theory, to see if it is reasonable.

搜索引擎可以用来查询语义相关的词汇，因为文本基数大，搜索引擎返回的结果是十分丰富的，即词汇多样性足够强。

### RSS Feeds

The blogosphere is an important source of text, in both formal and informal registers. With the help of a Python library called the *Universal Feed Parser*, we can access the content of a blog

博客是因为同时含有正式以及非正式文本，所以博客是很好的文本来源，借助于feedparser库，可以很方便的从博客的RSS中提取文本数据

	import feedparser
	llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
	llog['feed']['title']
	post = llog.entries[2]
	post.title
	content = post.content[0].value
	raw = BeautifulSoup(content).get_text()
	
### Local Files

	path = nltk.data.find('corpora/gutenberg/melville-moby_dick.txt') # NLTK 语料库中文件的位置
	f = open(path, 'rU') # 'U' 用来表明，打开文件时忽略换行符的差异，\r\n, \r, \n
	raw = f.read()

### PDF MSWord and other Binary Formats

Text often comes in binary formats — like PDF and MSWord — that can only be opened using specialized software. Third-party libraries such as *pypdf* and *pywin32* provide access to these formats. Extracting text from multi-column documents is particularly challenging.

从二进制文件中解析文本数据可以借助pypdf，pywin32，即使这样，从二进制中解析文本数据也是充满挑战的，也许更好的办法是自己手动用应用程序打开文件后导出文本数据

### Char Encoding/Decoding

文本数据的处理往往涉及到编码解码的问题,python支持unicode字符集,可以使用`\uxxxx`来表示任何unicode字符，在内部python将字符当成unicode字符进行处理，但是当涉及到跟外部数据交互时，我们需要考虑文件、网页数据或者命令行终端的编码是怎样的，当从外部读取时需要解码为unicode，当写入外部时需要将数据编码成外部适应的格式。

一个常见的问题是，从特定编码的文件中读出数据无法在命令行终端显示，这一般是由于命令行的编码格式无法解读文件中的字符数据，此时可以将不可编码字符以unicode代码格式输出`line.encode('unicode_escape')`

### Normalizing Text 文本一般化

we want to convert uppercase into lowercase char, and strip off any affixes, a task known as stemming. A further step is to make sure that the resulting form is a known word in a dictionary, a task known as lemmatization.

通常我们要对文本进行某些预处理，比如转换大小写以及移除后缀，这个任务被叫做提取词根，更进一步的，我们希望提取的词是字典中的合法单词，该任务叫做lemmatization

NLTK includes several off-the-shelf stemmers, and if you ever need a stemmer you should use one of these in preference to crafting your own using regular expressions, since these handle a wide range of irregular cases.

NLTK 自带了很多用于提取词根的工具，不同提取词根工具使用的规则不同，所以产生的结果也不同，在提取词根时工具无所谓好坏，只是不同的工具有不同的适应情形

	raw = 'a mandate from the masses, not from some farcical aquatic ceremony'
	tokens = nltk.word_tokenize(raw)	
	porter = nltk.PorterStemmer()
	lancaster = nltk.LancasterStemmer()
	[porter.stem(t) for t in tokens]
	[lancaster.stem(t) for t in tokens]	

lemmatization只有在移除词缀后单词合法，才会移除词缀

	wnl = nltk.WordNetLemmatizer()
	[wnl.lemmatize(t) for t in tokens]

Another normalization task involves identifying non-standard words including numbers, abbreviations, and dates, and mapping any such tokens to a special vocabulary.

此外文本的一般化处理还包括对数字，缩写，日期等非标准token的处理

### Tokenization

The very simplest method for tokenizing text is to split on whitespace.

最简单tokenization的方法，文本根据空白分割
	
	re.split(r'\s+', raw) # 没有考虑标点符号

根据单词边界分割

	re.split(r'\W+', raw)

考虑了连字符以及标点符号
	
	re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)

NLTK 自带支持使用正则表达式tokenization的工具

	text = 'That U.S.A. poster-print costs $12.40...'
	pattern = r'''(?x)    # set flag to allow verbose regexps
		([A-Z]\.)+        # abbreviations, e.g. U.S.A.
		| \w+(-\w+)*        # words with optional internal hyphens
		| \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
		| \.\.\.            # ellipsis
		| [][.,;"'?():-_`]  # these are separate tokens; includes ], [
	'''

	tokens = nltk.regexp_tokenize(text, pattern)
	#set(tokens).difference(nltk.corpus.words.words('en'))

Tokenization turns out to be a far more difficult task than you might have expected. No single solution works well across-the-board, and we must decide what counts as a token depending on the application domain.

When developing a tokenizer it helps to have access to raw text which has been manually tokenized, in order to compare the output of your tokenizer with high-quality (or "gold-standard") tokens. The NLTK corpus collection includes a sample of Penn Treebank data, including the raw Wall Street Journal text (nltk.corpus.treebank_raw.raw()) and the tokenized version (nltk.corpus.treebank.words()).

tokenization并没有针对所有情形下一致的解决方案，我们通常需要根据不同应用场景来设计不同的tokenization策略，NLTK 语料库提供了人工tokenization后的数据和原始的文本数据，这样有利于程序员比对自己的tokenizatin是否精准

### Segmentation 分割问题

Tokenization is an instance of a more general problem of segmentation. 

tokenizatin只是分割问题的特例

### Sentence Segmentation 句子分割

Manipulating texts at the level of individual words often presupposes the ability to divide a text into individual sentences. As we have seen, some corpora already provide access at the sentence level. 

将文本分割为单词通常以将文本分割为句子为基础，NLTK的部分语料库提供了从语句级别访问数据的方法

	len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents())

In other cases, the text is only available as a stream of characters. Before tokenizing the text into words, we need to segment it into sentences. NLTK facilitates this by including the Punkt sentence segmenter

而在另外一些情形下我们得到的仅仅只是字符数据流，需要我们自己将其分割为语句，NLTK同样提供了语句分割工具

	text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
	sents = nltk.sent_tokenize(text)

Sentence segmentation is difficult because period is used to mark abbreviations, and some periods simultaneously mark an abbreviation and terminate a sentence, as often happens with acronyms like U.S.A.

语句分割是比较困难的问题，因为句点常用作语句结尾，但同时也会被用在单词简写中

### Word Segmentation

For some writing systems, tokenizing text is made more difficult by the fact that there is no visual representation of word boundaries. A similar problem arises in the processing of spoken language, where the hearer must segment a continuous speech stream into individual words.

像中文词之间没有明显的边界，所以分词是更难的，同时像手写识别以及语音识别中也面临同样单词边界模糊的问题

Our first challenge is simply to represent the problem: we need to find a way to separate text content from the segmentation. We can do this by annotating each character with a boolean value to indicate whether or not a word-break appears after the character. Now the segmentation task becomes a search problem: find the bit string that causes the text string to be correctly segmented into words. With enough data, it is possible to automatically segment text into words with a reasonable degree of accuracy. Such methods can be applied to tokenization for writing systems that don't have any visual representation of word boundaries.

让我们先来形式化这个问题，给定一个文本字符串，再给定一个二进制串，二进制串的意思是当前位置如果为1则表示相应位置字符为分词的边界，如果当前位置为0则表示处于单词内部。因此问题转换为寻找合适的二进制串使得得到的分词结果尽可能的好，如何评价分词结果呢？给定特定的二进制串后可以推导出由该二进制串分割文本产生的单词表以及表示句子的单词表索引序列，然后我们定义一个objective function，该函数值为单词表中所有词汇字符数（额外加1表示单词边界字符）之和加上单词索引序列长度来表示，我们的目标是求objective function的最小值。只要给的数据足够充分，可以使用该分词方法可以给出较好的结果。

Simulated annealing is a heuristic for finding a good approximation to the optimum value of a function in a large, discrete search space, based on an analogy with annealing in metallurgy

模拟退火是用来在较大离散空间中搜索近似最优化问题的启发式方法

	# 根据二进制串分词
	def segment(text, segs):
	    words = []
	    last = 0
	    for i in range(len(segs)):
	        if segs[i] == '1':
	            words.append(text[last:i+1])
	            last = i+1
	    words.append(text[last:])
	    return words

	# 评价分词结果
	def evaluate(text, segs):
	    words = segment(text, segs)
	    text_size = len(words)
	    lexicon_size = sum(len(word) + 1 for word in set(words))
	    return text_size + lexicon_size

	# 查找使得objective function最小化的二进制串（基于非确定性的模拟退火）
	from random import randint

	def flip(segs, pos):
	    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

	def flip_n(segs, n):
	    for i in range(n):
	        segs = flip(segs, randint(0, len(segs)-1))
	    return segs

	def anneal(text, segs, iterations, cooling_rate):
	    temperature = float(len(segs))
	    while temperature > 0.5:
	        best_segs, best = segs, evaluate(text, segs)
	        for i in range(iterations):
	            guess = flip_n(segs, round(temperature))
	            score = evaluate(text, guess)
	            if score < best:
	                best, best_segs = score, guess
	        score, segs = best, best_segs
	        temperature = temperature / cooling_rate
	        print(evaluate(text, segs), segment(text, segs))
	    print()
	    return segs

	# 运行结果
	text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
	seg1 = "0000000000000001000000000010000000000000000100000000000"
	anneal(text, seg1, 5000, 1.2)

## Tagging Words

Back in elementary school you learnt the difference between nouns, verbs, adjectives, and adverbs. These "word classes" are not just the idle invention of grammarians, but are useful categories for many language processing tasks.

我们在语文课本上学到的动词，名词，形容词等并非单纯语法上的发明，它们在自然语言处理中具有特定的作用。

 We will also see how tagging is the second step in the typical NLP pipeline, following tokenization. The process of classifying words into their parts of speech and labeling them accordingly is known as part-of-speech tagging, POS-tagging, or simply tagging. Parts of speech are also known as word classes or lexical categories. The collection of tags used for a particular task is known as a tagset. Our emphasis in this chapter is on exploiting tags, and tagging text automatically.

单词标记通常在自然语言处理第一步-tokenization之后进行。对单词根据词性进行分类的过程通常被称为词性标注或者tagging，词性也即词类别。我们想要实现的就是文本的自动标注

### Part-Of-Speech Tagger

A part-of-speech tagger, or POS-tagger, processes a sequence of words, and attaches a part of speech tag to each word 

NLTK 词性标注器为单词附加一个表示词性的字段。

	text = nltk.word_tokenize("And now for something completely different")
	nltk.pos_tag(text)
	nltk.help.upenn_tagset('RB') # 查询tag的意义

词性标注之所以重要，是因为相同词性的单词在文本中具有相似的分布性质，比如NLTK提供了一个`Text.similar(word)`方法，用来统计在文本中同word类似的单词，所谓类似是指当文本出现word1wordword2序列时，如果同时出现word1wdword2序列，则单词wd跟word类似，即寻找具有相同上下文环境的单词，利用该函数我们可以发现一般具有相同上下文的单词会具有相同的词性

		text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
		text.similar('woman')
		text.similar('the')
### Representing Tagged Tokens

在nltk中tagged token被写作tuple，其中包含token和tag，并且支持我们用特定语法来创建tagged token

	tagged_token = nltk.tag.str2tuple('fly/NN') # ('fly', 'NN')

### Reading Tagged Corpora
nltk中的某些语料库是经过标注的，并一致的提供了方法`tagged_words`来访问被标注的单词，并且当语料库提供了分割的语句时，则可以通过`tagged_sents`来访问标注后的语句

	nltk.corpus.brown.tagged_words()
	nltk.corpus.brown.tagged_words(tagset='universal')
	nltk.corpus.nps_chat.tagged_words()
	nltk.corpus.conll2000.tagged_words()
	nltk.corpus.treebank.tagged_words()

### Tagset

下面是一个简单的标注集

	Tag 	Meaning 	English Examples
	ADJ 	adjective 	new, good, high, special, big, local
	ADP 	adposition 	on, of, at, with, by, into, under
	ADV 	adverb 	really, already, still, early, now
	CONJ 	conjunction 	and, or, but, if, while, although
	DET 	determiner, article 	the, a, some, most, every, no, which
	NOUN 	noun 	year, home, costs, time, Africa
	NUM 	numeral 	twenty-four, fourth, 1991, 14:24
	PRT 	particle 	at, on, out, over per, that, up, with
	PRON 	pronoun 	he, their, her, its, my, I, us
	VERB 	verb 	is, say, told, given, playing, would
	. 	punctuation marks 	. , ; !
	X 	other 	ersatz, esprit, dunno, gr8, univeristy

统计哪些标注用的比较多


	from nltk.corpus import brown
	brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
	tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
	tag_fd.plot(cumulative=True)
	
### Nouns

Nouns generally refer to people, places, things, or concepts, e.g.: woman, Scotland, book, intelligence. Nouns can appear after determiners and adjectives, and can be the subject or object of the verb

名词通常用来表示人，物或地点等，名词可以出现在冠词和形容词后，名词可以充当动词的主语或者宾语，普通名词标注为N，专有名词标注为NP

统计名词经常出现在什么词后面

	from nltk.corpus import brown
	brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
	word_tag_pairs = nltk.bigrams(brown_news_tagged) # 构造经过标注后的单词二元组
	noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN'] # 统计名词前面单词的词性
	fdist = nltk.FreqDist(noun_preceders)
	fdist.most_commont() # 根据结果可知名词经常出现在冠词，形容词，动词后面




## Examples

统计文本中双元音出现频率

	import re
	import nltk

	fd = nltk.FreqDist(i for word in nltk.corpus.words.words('en') for i in re.findall(r'[aeiou]{2,}', word))

英文单词通常是冗余的，一般来说去掉单词中间（单词开头和尾部的元音字母不能去掉）的元音字母也不会影响阅读，下面是一个对文本去冗余的程序

	import re, nltk

	def compress(word):
		regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]+'
		pieces = re.findall(regexp, word)
		return ''.join(pieces)

	english_udhr = nltk.corpus.udhr.words('English-Latin1')
	print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))

英语单词存在词根问题，一个单词往往会有多个形式，在搜索引擎中我们常常想将用户提供的单词提取词根后再进行文档的搜索，下面是一个提取单词词根的程序

	import re, nltk

	def stem(word):
		regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
		stem, suffix = re.findall(regexp, word)[0]
		return stem

	raw = 'government moving proxies happily'
	[stem(word) for word in nltk.word_tokenize(raw)]

从文本中查找潜在的具有包含概念的单词（即具有父类子类关系的单词）

	from nltk.corpus import brown
	hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
	hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>") # 注这里的findall方法是Text对象提供的

为文本基于词根构建索引工具

	class IndexedText(object):

	    def __init__(self, stemmer, text):
	        self._text = text
	        self._stemmer = stemmer
	        self._index = nltk.Index((self._stem(word), i)
	                                 for (i, word) in enumerate(text))

	    def concordance(self, word, width=40):
	        key = self._stem(word)
	        wc = int(width/4)                # words of context
	        for i in self._index[key]:
	            lcontext = ' '.join(self._text[i-wc:i])
	            rcontext = ' '.join(self._text[i:i+wc])
	            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
	            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
	            print(ldisplay, rdisplay)

	    def _stem(self, word):
	        return self._stemmer.stem(word).lower()


	porter = nltk.PorterStemmer()
	grail = nltk.corpus.webtext.words('grail.txt')
	text = IndexedText(porter, grail)
	text.concordance('lie')

自己格式化显示统计数据

	def tabulate(cfdist, words, categories):
	    print('{:16}'.format('Category'), end=' ')                    # column headings
	    for word in words:
	        print('{:>6}'.format(word), end=' ')
	    print()
	    for category in categories:
	        print('{:16}'.format(category), end=' ')                  # row heading
	        for word in words:                                        # for each word
	            print('{:6}'.format(cfdist[category][word]), end=' ') # print table cell
	        print()                                                   # end the row

	from nltk.corpus import brown
	cfd = nltk.ConditionalFreqDist(
		(genre, word)
		for genre in brown.categories()
		for word in brown.words(categories=genre))

	genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
	modals = ['can', 'could', 'may', 'might', 'must', 'will']
	tabulate(cfd, modals, genres)

Soundex算法,根据英语单词的发音来索引单词,将发音类似的单词编码为同一代码，代码格式为一个英文字母跟随三个数字（许多数据库内置对该算法的支持）


	def soundex(word):
		tbl = {}
		tbl['b'] = 1
		tbl['f'] = 1
		tbl['p'] = 1
		tbl['v'] = 1
		tbl['c'] = 2
		tbl['g'] = 2
		tbl['j'] = 2
		tbl['k'] = 2
		tbl['q'] = 2
		tbl['s'] = 2
		tbl['x'] = 2
		tbl['z'] = 2
		tbl['d'] = 3
		tbl['t'] = 3
		tbl['l'] = 4
		tbl['m'] = 5
		tbl['n'] = 5
		tbl['r'] = 6
		word = word.lower()
		first = word[0]
		word = ''.join([c for c in word if c != 'h' and c != 'w'])
		word = ''.join([str(tbl.get(c, c)) for c in word])
		s = ''
		last = ''	
		for i in range(len(word)):
			if word[i] == last:
				continue
			s += word[i]
			last = word[i]
		word = s
		word = ''.join([word[0]]+[c for c in word[1:] if c not in 'aeiouy'])
		if word[0].isdigit():
			word = first + word[1:]
		if len(word) < 4:
			word += '0000'
		return word[:4].upper()

n-grams提取文本中相邻词对

	nltk.bigrams(text)
	nltk.trigrams(text)
	nltk.ngrams(text, n)

	n = 3
	[text[i:i+n] for i range(len(text)-n+1)]

trie树

	def insert(trie, key, value):
	    if key:
	        first, rest = key[0], key[1:]
	        if first not in trie:
	            trie[first] = {}
	        insert(trie[first], rest, value)
	    else:
	        trie['value'] = value

	trie = {}
	insert(trie, 'chat', 'cat')
	insert(trie, 'name', 'wen')

多文档检索，建立了关键字到文档路径列表的索引表

	def raw(file):
	    contents = open(file).read()
	    contents = re.sub(r'<.*?>', ' ', contents)
	    contents = re.sub('\s+', ' ', contents)
	    return contents

	def snippet(doc, term):
	    text = ' '*30 + raw(doc) + ' '*30
	    pos = text.index(term)
	    return text[pos-30:pos+30]

	print("Building Index...")
	files = nltk.corpus.movie_reviews.abspaths()
	idx = nltk.Index((w, f) for f in files for w in raw(f).split())

	query = ''
	while query != "quit":
	    query = input("query> ")     # use raw_input() in Python 2
	    if query in idx:
	        for doc in idx[query]:
	            print(snippet(doc, query))
	    else:
	        print("Not found")

单词到id对应，将文本转换为id数据

	def preprocess(tagged_corpus):
	    words = set()
	    tags = set()
	    for sent in tagged_corpus:
	        for word, tag in sent:
	            words.add(word)
	            tags.add(tag)
	    wm = dict((w, i) for (i, w) in enumerate(words))
	    tm = dict((t, i) for (i, t) in enumerate(tags))
	    return [[(wm[w], tm[t]) for (w, t) in sent] for sent in tagged_corpus]

利用matplotlib绘制条形图

	from numpy import arange
	from matplotlib import pyplot

	colors = 'rgbcmyk' # red, green, blue, cyan, magenta, yellow, black

	def bar_chart(categories, words, counts):
	    "Plot a bar chart showing counts for each word by category"
	    ind = arange(len(words))
	    width = 1 / (len(categories) + 1)
	    bar_groups = []
	    for c in range(len(categories)):
	        bars = pyplot.bar(ind+c*width, counts[categories[c]], width,
	                         color=colors[c % len(colors)])
	        bar_groups.append(bars)
	    pyplot.xticks(ind+width, words)
	    pyplot.legend([b[0] for b in bar_groups], categories, loc='upper left')
	    pyplot.ylabel('Frequency')
	    pyplot.title('Frequency of Six Modal Verbs by Genre')
	    pyplot.show()

	genres = ['news', 'religion', 'hobbies', 'government', 'adventure']
	modals = ['can', 'could', 'may', 'might', 'must', 'will']
	cfdist = nltk.ConditionalFreqDist(
		(genre, word)
		for genre in genres
		for word in nltk.corpus.brown.words(categories=genre)
		if word in modals)
	counts = {}
	for genre in genres:
		counts[genre] = [cfdist[genre][word] for word in modals]
	bar_chart(genres, modals, counts)

利用networkx操纵图数据

	# https://networkx.lanl.gov/
	import networkx as nx
	import matplotlib
	from nltk.corpus import wordnet as wn

	def traverse(graph, start, node):
	    graph.depth[node.name] = node.shortest_path_distance(start)
	    for child in node.hyponyms():
	        graph.add_edge(node.name, child.name)
	        traverse(graph, start, child)

	def hyponym_graph(start):
	    G = nx.Graph()
	    G.depth = {}
	    traverse(G, start, start)
	    return G

	def graph_draw(graph):
	    nx.draw_graphviz(graph,
	         node_size = [16 * graph.degree(n) for n in graph],
	         node_color = [graph.depth[n] for n in graph],
	         with_labels = False)
	    matplotlib.pyplot.show()

	dog = wn.synset('dog.n.01')
	graph = hyponym_graph(dog)
	graph_draw(graph)