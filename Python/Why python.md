# Why Python
I love this question.  I really do.  Mostly because I asked myself this question over, and over, and over some more throughout my time in high school, college, and at my first job as a software engineer.  And I have poured countless hours doing research, watching informative and in depth presentations on things like the GIL, etc. etc. etc. just to figure out when/how/if I would run into a major problem because Python was "slow".

So before I start writing out this huge answer (mostly for my own benefit since it has been thoroughly answered by many others already) let's examine the two most common reasons that lead people to (rightfully) claim Python is **slow** and/or it is not **high performance**:

* **Interpreted**
* **The GIL**

The first is fairly straight forward, but at a high level [compilers](https://en.wikipedia.org/wiki/Compiler) translate higher level languages into lower-level (faster) languages so a compiled language will almost always execute faster than non-compiled ones.  There are some exceptions to this rule-of-thumb (such as situations where [JIT can be faster than AOT compiling](http://stackoverflow.com/questions/1878696/why-is-java-faster-when-using-a-jit-vs-compiling-to-machine-code)), but they are distraction to this discussion.

The second is a bit more notorious, but Python has something called the [*Global Interpreter Lock*](https://en.wikipedia.org/wiki/Global_interpreter_lock) which basically prevents multi-threading by mandating the interpreter only execute a single thread within a single process (instance of the Python interpreter) at a time.  How this works can be [pretty interesting](https://www.google.com/url?bvm=bv.110151844,d.cGc&cad=rja&cd=2&esrc=s&q=&rct=j&sa=t&sig2=_c7-oLnbY2oyXAdHYT9HGw&source=web&uact=8&url=https://www.youtube.com/watch?v%3Dph374fJqFPE&usg=AFQjCNHLoAIxYMQIF1omshcBMV7BT0HwPQ&ved=0ahUKEwjXuuK1wObJAhUG1mMKHQ8jA80QtwIIITAB) as well, but also a tangential rabbit hole like compilers.

**9/10 times the slower performance of Python does not matter.**

Over time I have come to the opinion that there are two main reasons for this.

The first is that what matters is not code execution time, but end-user experience.  It doesn't *usually* matter if a function takes 0.001 seconds or 0.01 to execute.  In this vein, for most problems horizontal scaling can be used to solve many bottlenecks that would have been created by Python.

Take for example [these benchmarks](https://www.techempower.com/benchmarks/#section=data-r10&hw=peak&test=json) for popular web frameworks.  The best one using Python came in at 650.5K req/s while the best number was 2.2M.  Purely from a performance perspective, you are probably wondering why you wouldn't just pick the fastest, but then you look at that #1 spot and realize it is using C.  C is a great language (IMO), but Python is a lot more expressive and has a larger eco-system with pre-built tools you could choose to use.  So instead of squeezing every last bit of computing power out of your server while sacrificing development time/scope, you could instead get 4 servers for Python for every 1 needing C and save many times that in developer productivity and development time.  This is obviously a dramatized and drastically simplified example, but the point being illustrated I think is sound.

Which brings us to the second realization surrounding the *GIL* and my conclusion that it really **isn't that bad**.

By not allowing multi-threading (or simultaneous execution within the same process) Python drastically simplifies programming complexity faced by developers.  [Common](http://www.drdobbs.com/tools/avoiding-classic-threading-problems/231000499) [issues](http://stackoverflow.com/questions/461896/what-is-the-most-frequent-concurrency-issue-youve-encountered-in-java) and optimizations for multi-threaded processes can just be ignored en-masse by the developer because the Python interpreter will only ever execute a single piece of logic at a time.

This also doesn't usually matter much for the same horizontal reasoning as point 1.  Instead of tackling issues with multi-threading, you can choose to tackle issues with [*multi-processing*](https://en.wikipedia.org/wiki/Multiprocessing).  Instead of managing multiple threads in a single process you can spin up multiple processes and communicate between them.  The difference is subtle, but again, for 9/10 of those cases the performance overhead of multi-processing vs. threading doesn't matter.

In the cases where the performance over head *does* matter, you can always "glue" a different language into your Python logic.  The classic example is how [Numpy](http://www.numpy.org/) brings high performance array data structures to Python by dropping into C.

**So what's the take away from all of this?**

With computational power (# of processor cores, speed of individual cores, $ cost of server hardware, etc.) getting cheaper all the time, most performance issues can usually be solved somewhat by horizontal scaling.

For the things you can't really solve horizontally, you can write something in a different language and "glue it" into your Python logic (play on the saying that Python is a "glue" language).

So if ultimately performance can be augmented/handled, you are left with the main reasons Python is desirable as a language:

* *Simple*
* *Productive*
* *Readable (and thereby more* maintainable)

There is countless more we could talk about with regards to the strengths and weaknesses of Python and we could go into ever more detail, but I think this is a good start at tackling the question of why Python interpreter performance hasn't affected its popularity.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgzOTQyNDQzXX0=
-->
