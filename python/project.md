http://infinitemonkeycorps.net/docs/pph/

# Example: how to make a quality Python software

## project directory
googlemaps/ # Project root directory

	.svn/ # Version Control

	googlemaps/ # Quality Code

		googlemaps.py

	test/ # Unit Testing

		test_googlemaps.py

	doc/ # Documentation

		index.rst

		html/

			index.html

	README.txt

	LICENSE.txt # Licensing

	setup.py # Packaging

	MANIFEST.in

## project hosting

### Choose a Host

Your code needs a home on the Internet: a website where people can download your software, learn how to use it, and provide feedback. There are several websites that will host your open-source project for free; some popular choices are listed below. The basic requirements are web page hosting, a version control system, and a user feedback system. Feedback mechanisms include bug trackers, forums, and mailing lists. If you’re not sure which host to use, Sourceforge is one of the oldest and best-known hosts; I’ll be using Sourceforge in the examples below.

### Choose a Project Name

You’ll need a project name in order to register. Your project’s name is important, but don’t spend too much time obsessing over it. It’s worth doing a quick search on [Google](http://www.google.com/), [The Python Package Index](http://pypi.python.org/) and [freshmeat](http://www.freshmeat.net/) to see if someone else already has a software product by that name. If it’s something totally unrelated, it’s probably not a problem (but watch out for trademarks). If your name is taken, consider tacking on “Py” or “Python” or a clever [Monty Python](http://en.wikipedia.org/wiki/Monty_Python) reference.

> Note
>
> Your project name or “short name” may be taken on your host; this may affect the URL of your project’s homepage and detract from its “findability.” Your project’s actual name doesn’t have to match the project name you use on your host, but it helps. Decide whether that’s important; if so, consider whether you want to change your project’s name, live with a mismatched host project name, or find another hosting service that has your name available.
>
> Note
>
> You *can* set up a project on your own website and host things yourself, but it’s more work.

Sign up for an account on your chosen host. Register your project, and take a few minutes to fill in your project’s metadata. Including a brief description, category, tags or keywords, programming language, etc. will make your software easier for people to find and grok. (If your host requires you to choose a license for your software up front, have a look at the [licensing](http://infinitemonkeycorps.net/docs/pph/#id9) section.)

### Open-Source Project Hosts[¶](http://infinitemonkeycorps.net/docs/pph/#open-source-project-hosts)

- Bitbucket: [http://bitbucket.org/](http://bitbucket.org/)
- CodePlex: [http://www.codeplex.com/](http://www.codeplex.com/)
- Freepository: [https://freepository.com/](https://freepository.com/)
- GitHub: [http://github.com/](http://github.com/)
- Gitorious: [http://gitorious.org/](http://gitorious.org/)
- Google Code: [http://code.google.com/projecthosting/](http://code.google.com/projecthosting/)
- Launchpad: [https://launchpad.net/](https://launchpad.net/)
- Sourceforge: [http://www.sourceforge.net/](http://www.sourceforge.net/)
- Tuxfamily: [http://www.tuxfamily.org/](http://www.tuxfamily.org/)

## Version Control

### Create a Repository

You will need to set up a version control system (VCS; also called a revision control or source code mangagement system) to hold your code on the Internet. This is practically what it means to be an open source project: anybody can easily download your code at any time. It also has the practical benefit of keeping backup copies of every version of your code you check in.

Subversion is probably the most widely-known VCS, and something of a lowest common denominator. It’s a good default choice, supported by many project hosts, and available on all platforms. I’ll be using Subversion for the examples in this article, but feel free to choose one of the newer, sexier VCSes below. They are all functionally identical for the basics, and most have facilities to import from or export to Subversion if you decide you want to change later.

Note that your choice of project host may limit your choice of VCS, or vice versa.

Create a SVN (or git, or hg, or bzr, or...) repository at your project host’s website.

### Back Up Your Code

Backing up is always a good idea; we’ll just make a quick tarball in case something gets hosed.

> Note
>
> I’m using Unix command lines and pathnames in this document, but the concepts easily map to other operating systems.

In what follows, I’m going to assume your Python source currently lives at `*/path/to/googlemaps/googlemaps.py*`. You’ll need to replace `*/path/to/*` with the appropriate path on your system, and everywhere you see `*googlemaps*`, replace it with the appropriate name for your project. Now, about that tarball:

> `$ cd */path/to/*`
>
> `$ tar czvf *googlemaps*.tgz *googlemaps/*`

While you’re at it, you should clean out your source directory, remove any compiled/binary files (such as `*.pyc`), clean out any hidden settings files or directories (you have a backup!), and remove anything sensitive or private; everything in there is about to be shared with the world.

Now we’ll move your code directory aside for the new one we’re about to create:

> `$ mv *googlemaps*/ *googlemaps*-backup/`

### Check out the repository

Your host should give you a URL or command to check out the repository. Here’s what it looks like for **svn** from Sourceforge:

> `$ cd */path/to/googlemaps*`
>
> `$ svn co https://*googlemaps*.svn.sourceforge.net/svnroot/*googlemaps* *googlemaps*`

This should give you a new `googlemaps` directory containing a hidden `.svn` directory (or whatever VCS you’re using).

### Copy your code into your working repo copy

Your new `googlemaps` directory will soon contain other things besides source code (remember: it’s a *project* now!), so we are going to make a new subdirectory for your code. Source files go in a subdirectory with the same name as the project or package.

> `$ svn mkdir */path/to/googlemaps/googlemaps*` (note the **svn**!)
>
> `$ cp -a */path/to/googlemaps*-backup/* */path/to/googlemaps*/`

### Add your code to the repository

> `$ cd */path/to/googlemaps/*`
>
> `$ svn add *`

### Commit your changes

> `$ svn commit -m "Initial import."`

That’s it. The master copy of the code now lives on your project host’s servers.. You’ll do all of your coding in this new working directory on your machine, and periodically commit changes to the server. If you’re new to version control, refer to the appropriate link below, but basically: you’ll need to tell your VCS whenever you’re adding, moving, or deleting a file from your source. Here are the basics for **svn**:

> **svn stat** - Show what’s added or changed
>
> **svn commit** - Save a snapshot of your code to the repo
>
> **svn add** - Put a new file under version control
>
> **svn mv** - Tell svn when you’re moving a file (use instead of **/bin/mv**)
>
> **svn rm** - Tell svn you’re removing a file (use instead of **/bin/rm**)
>
> **svn mkdir** - Create a new directory in your working copy (use instead of **/bin/mkdir**)
>
> **svn update** - Download any changes from the repo into your working copy

### Version Control Systems

- Bazaar (bzr): [http://bazaar-vcs.org/](http://bazaar-vcs.org/)
- Git (git): [http://git-scm.com/](http://git-scm.com/)
- Mercurial (hg): [http://mercurial.selenic.com/wiki/](http://mercurial.selenic.com/wiki/)
- Subversion (svn): [http://subversion.tigris.org/](http://subversion.tigris.org/)

## Quality Code

Writing good code is a journey. [The Pragmatic Programmer](http://www.pragprog.com/the-pragmatic-programmer) by Andrew Hunt and David Thomas is a good first step. [Code Complete](http://cc2e.com/) by Steve McConnell is another. A good sense of design and implementation can be learned, but you still have to use it. Probably the single biggest driver of open source code quality is knowing that other hackers will be looking at and using your code. Write code for other humans to read: your peers, your clients, your potential employers... your open source projects become a part of your reputation, your resume. Invest the effort to write good code. (Did I mention it will save you time and grief in the long run?)

Writing good code is an art. Aesthetics are subjective, but in Python, there is a generally accepted standard for formatting your code: [PEP 8](http://python.org/dev/peps/pep-0008/). Read it. There is a tool, [pep8](http://pypi.python.org/pypi/pep8/), for checking your code against it.

Writing good code is a science. There are (semi-) objective means of measuring code quality. First, your code should work, which we can verify with [unit testing](http://infinitemonkeycorps.net/docs/pph/#id5). Second, your code should look and [smell](http://en.wikipedia.org/wiki/Code_smell) good, which we can check with [Pylint](http://www.logilab.org/857).

### Pylint

> `$ sudo easy_install pylint`
>
> `$ pylint mymodule.py`

Pylint warns you about many potential problems with your code. The first you’ll probably notice are naming conventions. The short of it is that pretty much all identifiers should be `lowercase_with_underscores`, with the exception of `ClassNames` and `ExceptionNames`, which are CamelCased (and exception names should generally end with Error). “Constants” are `UPPER_CASE_UNDERSCORE`.`_private_identifiers` can be prefixed with a leading underscore, but for modules, there’s a better way: list all public classes, functions, and data as strings in a global list called `__all__`:

```
__all__ = ['GoogleMaps', 'GoogleMapsError']

```

A quick advice rundown: One- and two-character variable names are generally too short to be meaningful. Indent with 4 spaces. Put whitespace around operators and after commas. Give everything a docstring. Don’t shadow variables. Use `is` to compare with `None`, `True`, and `False`. Make your own exceptions subclass `Exception`. Limit `try` clauses to the bare minimum amount of code; catch the most specific exception possible (i.e., not `Exception`). Keep it simple. Last but very first: don’t use global variables.

Look at and learn about the warnings Pylint produces. Know when to ignore them; it can produce false positives. If Pylint complains and you are really sure that your code is safe, indicate to Pylint (and anyone reading your code) that you know what you’re doing:

```
def fetch_json(query_url, params={}, headers={}):       # pylint: disable-msg=W0102
    ...

```

Try for a Pylint score of at least 8. Personally, I try to fix or shush all messages except those about long line length in code (I do keep docstrings trimmed for people using the interactive help).

### Prepare For The Future

The Python world is starting to make a leisurely transition to [Python 3](http://docs.python.org/dev/3.0/whatsnew/3.0.html), which is not backwards compatible with Python 2. You can prepare your code for the future by running your [unit tests](http://infinitemonkeycorps.net/docs/pph/#unittesting) under Python 2.6+ with the `-3` switch:

> `$ python -3 test/test_mymodule.py`

This will warn you about things that will change in Python 3. If you really want to make sure your code works in Python 3, use the [2to3](http://docs.python.org/library/2to3.html)tool to translate your code to Python 3, then install Python 3 (keep your Python 2!) and run your unit tests under it. Don’t try to maintain both versions; just keep running your 2.x source through **2to3**.

Quality code is the most important part of an open source project. Once your package is set up, this is where you should spend most of your time.

### Python code quality tools

- Pylint, [lint](http://en.wikipedia.org/wiki/Lint_(software)) for Python: [http://www.logilab.org/857](http://www.logilab.org/857)
- PEP 8, Style Guide for Python Code: [http://python.org/dev/peps/pep-0008/](http://python.org/dev/peps/pep-0008/)
- pep8, code formatting checker: [http://pypi.python.org/pypi/pep8/](http://pypi.python.org/pypi/pep8/)
- Pyntch, a static type checker (for a dynamic language!): [http://www.unixuser.org/~euske/python/pyntch/index.html](http://www.unixuser.org/~euske/python/pyntch/index.html)
- PyFlakes, a fast lint-like tool for Python: [http://divmod.org/trac/wiki/DivmodPyflakes](http://divmod.org/trac/wiki/DivmodPyflakes)
- PyChecker, a Python source code checking tool: [http://pychecker.sourceforge.net/](http://pychecker.sourceforge.net/)
- PyMetrics, code statistics including cyclomatic complexity: [http://sourceforge.net/projects/pymetrics/](http://sourceforge.net/projects/pymetrics/)
- 2to3, Automated Python 2 to 3 code translation: [http://docs.python.org/library/2to3.html](http://docs.python.org/library/2to3.html)

## Unit Testing

A good way to check whether your code works is to try it. A great way is to try it automatically, every time it changes. That’s the premise of [unit testing](http://en.wikipedia.org/wiki/Unit_testing): write code to test your code, so that it’s easy, so that you’ll do it often. In this context, unit means module, class, or function; we test each unit of functionality separately, so we have more confidence everything will work when we put it all together.

### doctest

Python has two standard unit testing modules, `doctest` and `unittest` (it’s that important!). `doctest` is a fantastic way to kill two birds with one stone: demonstrating how to use your code by example, and making sure it gives the answers you expect. You can literally run your code in an interactive session, check if its working, and then paste the session into a docstring:

```
def local_search(self, query, numresults=_LOCAL_RESULTS_PER_PAGE, **kwargs):
    """
    Searches Google Local for the string `query` and returns a
    dictionary of the results.

    >>> gmaps = GoogleMaps()
    >>> local = gmaps.local_search('sushi san francisco, ca')
    >>> result = local['responseData']['results'][0]
    >>> print result['titleNoFormatting']
    Sushi Groove
    """

```

Then, by putting this in your main routine:

```
if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

`doctest` will automatically pull the code out of your docstring, run it, and compare the output to that present in the docstring whenever your module is run as a script.

Writing examples is an important part of [good documentation](http://infinitemonkeycorps.net/docs/pph/documentation) anyway, and with `doctest` it takes almost no extra effort to turn those docs into tests.

### unittest

`unittest` is Python’s standard “heavyweight” unit testing framework. It’s a bit more flexible and a bit more powerful that `doctest`, but it takes a bit more doing to use. Here is the same test using `unittest`:

```
import unittest
from googlemaps import GoogleMaps

class Test(unittest.TestCase):
    """Unit tests for googlemaps."""

    def test_local_search(self):
        """Test googlemaps local_search()."""
        gmaps = GoogleMaps(GMAPS_API_KEY, referrer_url='http://www.google.com/')
        local = gmaps.local_search('sushi san francisco, ca')
        result = local['responseData']['results'][0]
        self.assertEqual(result['titleNoFormatting'], 'Sushi Groove')

if __name__ == "__main__":
    unittest.main()

```

This would go in a file called `test/test_googlemaps.py`, and this is a general rule: tests go in a directory called `test` at the root level of your package, and are named `test_*modulename*.py`. All of the tests for module modulename go in this file, and this file tests all of the functionality in modulename.

Even if you are only using doctests, you should still have a `test/test_*modulename*.py` that runs your doctests:

```
import unittest
import doctest

import googlemaps

class Test(unittest.TestCase):
    """Unit tests for googlemaps."""

    def test_doctests(self):
        """Run googlemaps doctests"""
        doctest.testmod(googlemaps)

if __name__ == "__main__":
    unittest.main()

```

This is because `unittest` is the standard for Python unit testing, and many tools, IDEs, and people expect to find and interface with `unittest` tests in the standard place.

### Create your tests

Tell your VCS to create a new `test` directory under your project root:

> `$ cd */path/to/googlemaps/*`
>
> `$ svn mkdir test`

Create a `test_*modulename*.py` file and put your `unittest` tests in it. Since the test modules are in a separate directory from your code, you may need to add your module’s parent directory to your **PYTHONPATH** in order to run them:

> `$ cd */path/to/googlemaps*`
>
> `$ export PYTHONPATH=$PYTHONPATH:/path/to/*googlemaps*/*googlemaps*`
>
> `$ python test/test_*googlemaps*.py`

Finally, there is one more popular unit testing framework for Python (it’s that important!), [nose](http://somethingaboutorange.com/mrl/projects/nose/). `nose` helps simplify and extend the builtin `unittest` framework (it can, for example, automagically find your test code and setup your **PYTHONPATH** for you), but it is not included with the standard Python distribution.

In conclusion: Write unit tests. Run them. Often. It will make you feel MUCH more confident about releasing your code to the world.

### Unit Testing Resources

- unittest, Python’s builtin unit testing framework: [http://docs.python.org/library/unittest.html](http://docs.python.org/library/unittest.html)
- doctest, Test interactive Python examples in docstrings: [http://docs.python.org/library/doctest.html](http://docs.python.org/library/doctest.html)
- nose, “is nicer testing for python”: [http://somethingaboutorange.com/mrl/projects/nose/](http://somethingaboutorange.com/mrl/projects/nose/)
- coverage.py, test coverage measurement: [http://nedbatchelder.com/code/coverage/](http://nedbatchelder.com/code/coverage/)
- Python Testing Tools Taxonomy, including web app and GUI testing tools: [http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy](http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy)

## Documentation

Good documentation is important for showing others how to use your code as well as for keeping *you* straight on what it’s supposed to do. With the `doctest` module, you can even use it to test your code. Python makes it easy to insert documentation right into the code with [docstrings](http://docs.python.org/tutorial/controlflow.html#documentation-strings); they often even do triple-duty as comments. With just a little extra formatting in your docstrings, you can automatically produce beautiful web or print documentation for your project.

I even suggest writing the documentation *before* writing the code (or at least concurrently). This is a great way to employ user-centered design. You are going to have to explain how to use your code at some point; what design would be the easiest to explain? I’d wager that design would also be in the running for “easy to implement, test and maintain” as well. Writing up the docs first will let you figure out how it all works together before committing to the code.

This works just as well if a module is written by you, for you as a component of a higher-level program. Ask yourself: if I were looking for a module to do XYZ, what would I want it to look like? How would I want to use it? What would I want to know first? What examples would I like to see? Have compassion on yourself: write good documentation (and code) for *you*. Write out the docs for this awesome hypothetical module, see if it “coheres,” then fill in the code.

### Use reStructuredText in docstrings

The Python community is gravitating toward [reStructuredText](http://docutils.sourceforge.net/rst.html) for docstring markup; it’s the equivalent of Javadoc for Python. It’s easy to write and read:

```
def reverse_geocode(self, lat, lng, sensor='false', oe='utf8', ll='', spn='', gl=''):
    """
    Converts a (latitude, longitude) pair to an address.

    Interesting bits:

    >>> gmaps = GoogleMaps()
    >>> reverse = gmaps.reverse_geocode(38.887563, -77.019929)
    >>> address = reverse['Placemark'][0]['address']
    >>> print address
    200 6th St SW, Washington, DC 20024, USA
    >>> accuracy = reverse['Placemark'][0]['AddressDetails']['Accuracy']
    >>> print accuracy
    8

    :param lat: latitude
    :type lat: float
    :param lng: longitude
    :type lng: float
    :return: `Reverse geocoder return value`_ dictionary giving closest
        address(es) to `(lat, lng)`
    :rtype: dict
    :raises GoogleMapsError: If the coordinates could not be reverse geocoded.

    Keyword arguments and return value are identical to those of :meth:`geocode()`.

    .. _`Reverse geocoder return value`:
        http://code.google.com/apis/maps/documentation/geocoding/index.html#ReverseGeocoding

    """

```

It can automatically generate HTML like this:

> - `GoogleMaps.``reverse_geocode`(*lat*, *lng*, *sensor='false'*, *oe='utf8'*, *ll=''*, *spn=''*, *gl=''*)
>
>   Converts a (latitude, longitude) pair to an address.Interesting bits:`>>> gmaps = GoogleMaps()>>> reverse = gmaps.reverse_geocode(38.887563, -77.019929)>>> address = reverse['Placemark'][0]['address']>>> print address200 6th St SW, Washington, DC 20024, USA>>> accuracy = reverse['Placemark'][0]['AddressDetails']['Accuracy']>>> print accuracy8`Parameters:*lat* (float) – latitude*lng* (float) – longitudeReturns:[Reverse geocoder return value](http://code.google.com/apis/maps/documentation/geocoding/index.html#ReverseGeocoding) dictionary giving closest address(es) to (lat, lng)Return type:dictRaises GoogleMapsError: If the coordinates could not be reverse geocoded.Keyword arguments and return value are identical to those of `geocode()`.

Take-home points:

- Normal docstring formatting conventions apply: see [PEP 257](http://www.python.org/dev/peps/pep-0257/).
- Identifier references go in `backticks`.
- `:param lat: latutide` documents parameters
- `:type lat: float` documents parameter types
- `:return: dictionary giving closest addresses...` documents return values
- `:rtype: dict` documents return type
- `:raises GoogleMapsError: If coordinates could not...` documents exceptions raised
- `>>>` starts a doctest and is automatically formatted as code; code can also be indicated by indenting four spaces or preceding with `::` and a blank line
- Link to other methods, functions, classes, modules with `:meth:`*mymethod*``, `:func:`*myfunc*``, `:class:`*myclass*``, and `:mod:`*mymodule*``.
- Hyperlink names go in backticks with a trailing underscore: ``Google`_`, and targets can be defined anywhere with `.. _Google:http://www.google.com/`.
- See the [reStructuredText](http://docutils.sourceforge.net/rst.html) documentation for much more.

### Generate docs with Sphinx

The documentation above, and the present Howto, were rendered with [Sphinx](http://sphinx.pocoo.org/). Sphinx is the official document processor for Python itself and many Python projects. You’ve probably seen its handiwork at [http://docs.python.org/](http://docs.python.org/). Setting up Sphinx to automatically generate documentation for your module is easy. First tell your VCS to create a `doc/` directory under your project root (this is the the standard place for documentation), and then run **sphinx-quickstart**:

> `$ cd */path/to/googlemaps*`
>
> `$ svn mkdir doc`
>
> `$ cd doc`
>
> `$ sudo easy_install sphinx`
>
> `$ sphinx-quickstart`

Answer the questions (the defaults are fine, except be sure to say ‘yes’ to the autodoc extension). Then, edit the generated `index.rst`file to add this:

> `.. automodule:: *googlemaps*`

This is the place to put any extra documentation that’s not in your docstrings. Be sure to put `index.rst` and Sphinx’ `conf.py` under version control:

> `$ svn add index.rst conf.py`

You can generate your documentation by running **sphinx-build** in the `doc/` directory:

> `$ sphinx-build . html/`

(You will need to have `*/path/to/googlemaps/googlemaps*` in your **PYTHONPATH** for this to work.)

This will put the HTML documentation in `doc/html/`. Sphinx generates very nice documentation. Open it up with your web browser and look at it. It will encourage you to write better documentation if you see that you’re making something beautiful as you write.

### README

In addition to the docstrings in your code and the resulting HTML documentation, you should create a `README.txt` file in the top level of your directory structure. Put it under version control. Your `README.txt` should contain the following:

- Name, version, and release date of the package
- Brief description of the package
- Any dependencies or required versions of Python
- How to install the package (ideally just `easy_install *packagename*`)
- How to run the program(s), if your package contains scripts
- Package author and contact information
- Copyright and [licensing](http://infinitemonkeycorps.net/docs/pph/#id9) terms
- Pointer to full documentation

Some people like to break a few of these out into separate files (`INSTALL`, `AUTHORS`, `ANNOUNCE`...), but personally I prefer to keep it simple.

If you already have this information in your docstrings or somewhere else, by all means, [don’t repeat yourself](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself): either use Sphinx, which can also produce plain (reStructured) text, or whip up a script to pull out the information and write your `README.txt` for you. You can extract the docstring from any module, class, or function with, e.g., `*mymodule*.__doc__`. Here’s how to make Sphinx output plain (reStructured) text to the `text/` directory:

> `$ sphinx-build -b text . text/`

### Documentation Resources

- PEP 257, Docstring Conventions: [http://www.python.org/dev/peps/pep-0257/](http://www.python.org/dev/peps/pep-0257/)
- reStructuredText markup: [http://docutils.sourceforge.net/rst.html](http://docutils.sourceforge.net/rst.html)
- Sphinx, Python Documentation Generator: [http://sphinx.pocoo.org/](http://sphinx.pocoo.org/)

## Licensing

You will need to decide on a license for your code. Popular open-source licenses include the GPL and LGPL, BSD, MIT/X11, Apache, Eclipse, and Mozilla. There are several resources listed below to help guide you in choosing a license. Your choice has implications for who can use your code under what circumstances, including which other open source projects can incorporate it. Your choice of license may also have implications for your choice of project host, since some hosts only permit software under some licenses. Take the time to learn a bit about licensing, and decide how you would like your code to be used.

Once you have chosen a license, you can find the complete text at the [Open Source Initiative](http://www.opensource.org/licenses). Read through the text to ensure you agree with its terms. Copy the complete text into a file called `LICENSE.txt` at the top level of your project (and put it under version control). Then, you will need to put a copyright notice in a comment at the top of each source file, and a brief statment of the licensing terms including where to find the license. You do not have to include the full license directly in your source; see the resources below for suggestions. If you have considerable documentation, consider licensing the documentation itself under one of the available [free documentation licenses](http://www.dreamsongs.com/IHE/IHE-50.html).

### Licensing Resources

- Open Source Licenses at OSI: [http://www.opensource.org/licenses](http://www.opensource.org/licenses)
- Open Source Licenses on Wikipedia: [http://en.wikipedia.org/wiki/Open_source_license](http://en.wikipedia.org/wiki/Open_source_license)
- zooko Quick Reference for Choosing a Free Software License: [http://zooko.com/licence_quick_ref.html](http://zooko.com/licence_quick_ref.html)
- KDE Open Source License Comparison: [http://developer.kde.org/documentation/licensing/licenses_summary.html](http://developer.kde.org/documentation/licensing/licenses_summary.html)
- New Media Rights’ Open Source Licensing Guide: [http://www.newmediarights.org/open_source/new_media_rights_open_source_licensing_guide](http://www.newmediarights.org/open_source/new_media_rights_open_source_licensing_guide)
- Groklaw - Understanding Open Source Software: [http://www.groklaw.net/article.php?story=20031231092027900](http://www.groklaw.net/article.php?story=20031231092027900)
- Innovation Happens Elsewhere’s Licenses for Docmentation: [http://www.dreamsongs.com/IHE/IHE-50.html](http://www.dreamsongs.com/IHE/IHE-50.html)
- Creative Commons ‘Choose a License’ (for documentation): [http://creativecommons.org/choose/](http://creativecommons.org/choose/)
- Free Software Foundation’s Various Licenses and Comments About Them: [http://www.gnu.org/philosophy/license-list.html](http://www.gnu.org/philosophy/license-list.html)

## Packaging

Packaging takes the files in your carefully crafted directory layout and bundles them up for easy download and use by others. The standard way to do this in Python is with [distutils](http://docs.python.org/distutils/index.html). Creating a simple file, `setup.py`, will give you your own **easy_install**-able package.

### setup.py

Here is an example `setup.py`:

```
from distutils.core import setup
import sys

sys.path.append('googlemaps')
import googlemaps


setup(name='googlemaps',
      version='1.0',
      author='John Kleint',
      author_email='py-googlemaps-general@lists.sourceforge.net',
      url='http://sourceforge.net/projects/py-googlemaps/',
      download_url='https://sourceforge.net/projects/py-googlemaps/files/',
      description='Easy geocoding, reverse geocoding, driving directions, and local search in Python via Google.',
      long_description=googlemaps.GoogleMaps.__doc__,
      package_dir={'': 'googlemaps'},
      py_modules=['googlemaps'],
      provides=['googlemaps'],
      keywords='google maps local search ajax api geocode geocoding directions navigation json',
      license='Lesser Affero General Public License v3',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Scientific/Engineering :: GIS',
                  ],
     )

```

Don’t worry if you don’t have a `download_url` yet. Notice that we import our own module in order to pull in the `__doc__` string for the `long_description`; you are free to use whatever text is appropriate. If you have a package instead of a module, you’d replace `py_modules` with `packages` and remove the `package_dir`. You can find the list of `classifiers` at PyPI’s list of [trove classifiers](http://pypi.python.org/pypi?%3Aaction=list_classifiers). If your code depends on other third-party packages/modules, you can specify those with a `required` keyword argument.

This covers our code, but we need one more file to pull in the documentation: `MANIFEST.in` in the package root:

```
recursive-include doc/html *
prune doc/html/.doctrees/
exclude doc/html/.buildinfo
include LICENSE.txt
```

Now, to build your package, you just run **setup.py sdist**:

> `$ python setup.py sdist`

If all goes well, this will create a tarball in `dist/*googlemaps*-1.0.tar.gz`. Let’s make sure there are no problems installing it and verify the presence of important files with **cheesecake_index**:

> `$ sudo easy_install cheesecake`
>
> `$ cheesecake_index --path=dist/*googlemaps*-1.0.tar.gz`

Ensure at the minimum that your package is able to be installed. Notice that the cheesecake index includes Pylint as one component, so you’re already ahead of the game. Personally I think the score is weighted a bit heavily toward installability and documentation, but a relative [cheesecake index](http://pycheesecake.org/#algorithm-for-computing-the-cheesecake-index) of at least 70% seems like a reasonable target.

### Packaging Resources

- distutils, the standard Python Distribution Utilities: [http://docs.python.org/distutils/index.html](http://docs.python.org/distutils/index.html)
- setuptools, an enhanced, extended distutils and home of **easy_install**: [http://peak.telecommunity.com/DevCenter/setuptools](http://peak.telecommunity.com/DevCenter/setuptools)
- Cheesecake, package “kwalitee” checker: [http://pycheesecake.org/](http://pycheesecake.org/)
- PyPI’s list of trove classifiers: [http://pypi.python.org/pypi?%3Aaction=list_classifiers](http://pypi.python.org/pypi?%3Aaction=list_classifiers)

## Release

Now that we’ve built the “golden master” in `dist/*googlemaps*-1.0.tar.gz`, it’s time to upload it. Your project host should have instructions for uploading files for release; most hosts let you do this via the web, SCP/SFTP, or FTP. Once you’ve uploaded the package, upload the documentation in `docs/html` to your project’s website (don’t forget the subdirectories). Take a moment to update your project’s metadata with things that may have changed, such as the license. If your program has a GUI, take a few screenshots and add them to your project metadata and/or web page.

Copy the URL where your file can be downloaded (the page containing the link is fine), and put it in the `download_url` argument of your `setup.py`.

### PyPI

You’ll likely want to register your package with the [Python Package Index](http://pypi.python.org/pypi). This enables people to automatically download and install your package with [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall) or [pip](http://pip.openplans.org/). You will need to sign up for a PyPI account (it’s free). You can do this either on the PyPI website, or via the command line and have your password mailed to you. Either way:

> `$ python setup.py sdist register upload`

This will build your packages, prompt you for your username/password, register your package (and its metadata) with PyPI, and then upload your package to PyPI. Uploading your package itself is not strictly necessary, but it may make it easier to find.

While you’re at it, you can also create a Windows installer to make it easy for Windows users to get your package:

> `$ python setup.py bdist_wininst upload`

This will create a file `dist/*googlemaps*-1.0.win32.exe` that you can also upload to your project host. (Note that Python 2.6 has a bug that may give the installer the wrong name, but you can simply rename it.)

Visit your project’s PyPI page at `http://pypi.python.org/pypi/*projectname*/`; you’ll notice that your `setup.py` `long_description` text has become the text of the web page. PyPI understands [reStructuredText](http://docutils.sourceforge.net/rst.html), so go ahead and tweak your `long_description` to your liking. Remeber that `sphinx-build -b text . text/` will “flatten” your documentation to reStructuredText, if you want to put the whole thing on PyPI. You can re-register a revised project without changing the version number. You can also edit your project’s metadata via the PyPI website.

- PyPI, the Python Package Index: [http://pypi.python.org/pypi](http://pypi.python.org/pypi)
- Registering with the Package Index: [http://docs.python.org/distutils/packageindex.html](http://docs.python.org/distutils/packageindex.html)
- Easy Install, automatically download and install Python packages: [http://peak.telecommunity.com/DevCenter/EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall)
- pip, “pip installs packages”: [http://pip.openplans.org/](http://pip.openplans.org/)
- freshmeat.net, Open source project index: [http://freshmeat.net/](http://freshmeat.net/)

### Epilogue

Congratulations on the release of your Python package! Your code may grow from these humble beginnings, but it has a good foundation, and you are now familiar with the mechanics of open source Python projects. In parting, I woluld be remiss not to mention a great resource on all aspects of the open-source project lifecycle, the free book [Producing Open Source Software](http://www.producingoss.com/), by Karl Fogel. Best of luck. And...

> *Always look on the bright side of life...*
>
> *Always look on the bright side of life...*