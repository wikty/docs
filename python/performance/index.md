## CPython 和 PyPy

CPython作为最流行的Python环境，对于CPU密集型任务（CPU bound tasks）较慢，而 [PyPy](http://pypy.org/) 则较快。

可以使用的 [David Beazley的](http://www.dabeaz.com/GIL/gilvis/measure2.py) CPU密集测试代码进行比较。

## GIL 去性能的限制

[GIL](http://wiki.python.org/moin/GlobalInterpreterLock) (全局解释器锁)是Python支持多线程并行操作的方式。Python的内存管理不是 线程安全的，所以GIL被创造出来避免多线程同时运行同一个Python代码。

David Beazley 有一个关于GIL如何工作的 [指导](http://www.dabeaz.com/python/UnderstandingGIL.pdf) 。他也讨论了 Python3.2中的 [新GIL](http://www.dabeaz.com/python/NewGIL.pdf) 他的结论是为了最大化一个Python程序的性能，应该对GIL工作方式有一个深刻的理解 ——— 它如何影响您的特定程序，您拥有多少核，以及您程序瓶颈在哪。

## C 扩展提升性能

[Cython](http://cython.org/) 是Python语言的一个超集，对其您可以为Python写C 或C++模块。Cython也使得您可以从已编译的C库中调用函数。使用Cython让您得以发挥Python 的变量与操作的强类型优势。

这是一个Cython中的强类型例子。

```
def primes(int kmax):
"""有一些Cython附加关键字的素数计算 """

    cdef int n, k, i
    cdef int p[1000]
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result

```

将这个有一些附加关键字的寻找素数算法实现与下面这个纯Python实现比较：

```
def primes(kmax):
"""标准Python语法下的素数计算"""

    p = range(1000)
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result
```

## 多线程/进程并发

[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) 模块是标准库中的一个模块，它提供了一个“用于异步调用的高级接口”。 它抽象了许多关于使用多个线程或进程并发的更复杂的细节，并允许用户专注于完成手头的任务。

[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) 模块提供了两个主要的类，即 ThreadPoolExecutor 和 ProcessPoolExecutor 。 ThreadPoolExecutor将创建一个用户可以提交作业的工作线程池。当下一个工作线程可用时， 这些作业将在另一个线程中执行。

ProcessPoolExecutor以相同的方式工作，它使用多进程而不是多线程作为工作池。这就可以避开 GIL的问题，但是由于传递参数给工作进程的工作原理，只有可序列化的对象可以执行并返回。

由于GIL的工作原理，一个很好的经验法则是当执行涉及很多阻塞（如通过网络发出请求）的任务时 使用ThreadPoolExecutor，而对高计算开销的任务使用ProcessPoolExecutor执行器。

使用两个执行器并行执行有两个主要方法。一个是使用 map(func, iterables) 方法。 这个函数除了能并行执行一切，它几乎和内置的 map() 函数一模一样 ：

```
from concurrent.futures import ThreadPoolExecutor
import requests

def get_webpage(url):
    page = requests.get(url)
    return page

pool = ThreadPoolExecutor(max_workers=5)

my_urls = ['http://google.com/']*10  # Create a list of urls

for page in pool.map(get_webpage, my_urls):
    # 处理结果
    print(page.text)

```

为了进一步的控制，submit(func, *args, **kwargs) 方法将调度一个可执行的调用 （如 func(*args, **kwargs) ），并返回一个代表可调用的执行的 [Future](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future) 对象。

Future对象提供了可用于检查计划可调用进程的各种方法。这些包括：

cancel()     尝试取消调用。 cancelled()     如果调用被成功取消，返回True。 running()     如果当前正在执行调用而且没被取消，则返回True done()     如果调用被成功取消或完成运行，返回True。 result()     返回调用返回的值。请注意，此调用将阻塞到默认情况下调度的可调用对象的返回。 exception()     返回调用抛出的异常。如果没有抛出异常，将返回 None 。请注意，这和 result() 一样会阻塞。 add_done_callback(fn)     添加回调函数函数，在所调用的可调用对象执行返回时执行（如 fn(future) ）。     预定可回拨。

```
from concurrent.futures import ProcessPoolExecutor, as_completed

def is_prime(n):
    if n % 2 == 0:
        return n, False

    sqrt_n = int(n**0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return n, False
    return n, True

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

futures = []
with ProcessPoolExecutor(max_workers=4) as pool:
    # Schedule the ProcessPoolExecutor to check if a number is prime
    # and add the returned Future to our list of futures
    for p in PRIMES:
        fut = pool.submit(is_prime, p)
        futures.append(fut)

# As the jobs are completed, print out the results
for number, result in as_completed(futures):
    if result:
        print("{} is prime".format(number))
    else:
        print("{} is not prime".format(number))

```

[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) 模块包含两个帮助函数来处理Futures。as_completed(futures) 函数 返回futures列表的的迭代器，在futures结束时yield。

而 wait(futures) 函数则简单地阻塞，直到列表中所有的futures完成。

有关使用 [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) 模块的更多信息，请参阅官方文档。

## 线程管理

标准库带有一个 [threading](https://docs.python.org/3/library/threading.html) 模块，允许用户手动处理多个线程。

在另一个线程中运行一个函数就如传递一个可调用对象以及它的参数到 Thread 的构造函数中， 然后调用 start() 一样简单：

```
from threading import Thread
import requests

def get_webpage(url):
    page = requests.get(url)
    return page

some_thread = Thread(get_webpage, 'http://google.com/')
some_thread.start()

```

调用 join() 来等待线程终止：

```
some_thread.join()

```

调用 join() 后，检查线程是否仍然存在（因为join调用超时）总是一个好主意：

```
if some_thread.is_alive():
    print("join() must have timed out.")
else:
    print("Our thread has terminated.")

```

由于多个线程可以访问相同的内存部分，有时可能会出现两个或多个线程尝试同时写入同一资源的情况， 或者输出取决于某些事件的顺序或时序。 这被称为 数据竞争 或竞争条件。当这种情况发生时， 输出将会出现乱码，或者可能会遇到难以调试的问题。 [stackoverflow post](http://stackoverflow.com/questions/26688424/python-threads-are-printing-at-the-same-time-messing-up-the-text-output) 是个很好的例子。

可以避免的方法是每个线程在写入共享资源之前获取 [Lock](https://docs.python.org/3/library/threading.html#lock-objects) 。 锁可以通过环境上下文协议 （ with 语句）或直接使用 acquire() 和 release() 来获取和释放。 以下是一个（颇有争议的）例子：

```
from threading import Lock, Thread

file_lock = Lock()

def log(msg):
    with file_lock:
        open('website_changes.log', 'w') as f:
            f.write(changes)

def monitor_website(some_website):
    """
    Monitor a website and then if there are any changes,
    log them to disk.
    """
    while True:
        changes = check_for_changes(some_website)
        if changes:
            log(changes)

websites = ['http://google.com/', ... ]
for website in websites:
    t = Thread(monitor_website, website)
    t.start()

```

在这里，我们有一堆线程检查站点列表中的更改，每当有任何更改时，它们尝试通过调用 log(changes) 将这些更改写入文件。 当调用 log() 时，它在 with file_lock: 处等待获取锁。 这样可以确保在任何时候只有一个线程正在写入文件。

## 进程管理

Multiprocessing 模块