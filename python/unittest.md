## test fixture
A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process

Such a working environment for the testing code is called a fixture.

If the setUp() method raises an exception while the test is running, the framework will consider the test to have suffered an error, and the test method will not be executed. If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.



## test case
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

The basic building blocks of unit testing are test cases ¡ª single scenarios that must be set up and checked for correctness.

Note that in order to test something, we use one of the assert*() methods provided by the TestCase base class. If the test fails, an exception will be raised, and unittest will identify the test case as a failure. Any other exceptions will be treated as errors.
assert*() methods are used instead of the assert statement so the test runner can accumulate all test results and produce a report.

Some users will find that they have existing test code that they would like to run from unittest, without converting every old test function to a TestCase subclass.

For this reason, unittest provides a FunctionTestCase class. This subclass of TestCase can be used to wrap an existing test function. Set-up and tear-down functions can also be provided.

In some cases, the existing tests may have been written using the doctest module. If so, doctest provides a DocTestSuite class that can automatically build unittest.TestSuite instances from the existing doctest-based tests.


## test suite
A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together
test case instances are grouped together according to the features they test. unittest provides a mechanism for this: the test suite, represented by unittest¡¯s TestSuite class.

## test runner
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

unittest.main() provides a command-line interface to the test script

The unittest module can be used from the command line to run tests from modules, classes, even individual test methods or specified by file path:

python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
python -m unittest tests/test_something.py


## test discovery
Unittest supports simple test discovery. In order to be compatible with test discovery, all of the test files must be modules or packages (including namespace packages) importable from the top-level directory of the project (this means that their filenames must be valid identifiers).

python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"

## test skipping and expected failures
Unittest supports skipping individual test methods and even whole classes of tests. In addition, it supports marking a test as an ¡°expected failure,¡± a test that is broken and will fail, but shouldn¡¯t be counted as a failure on a TestResult.

## Distinguishing test iterations using subtests
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

## example

For example for a directory structure like this:

new_project
©À©¤©¤ antigravity.py
©¸©¤©¤ test_antigravity.py
You can just run:

$ cd new_project
$ python -m unittest test_antigravity
For a directory structure like yours:

new_project
©À©¤©¤ antigravity
©¦   ©À©¤©¤ __init__.py         # make it a package
©¦   ©¸©¤©¤ antigravity.py
©¸©¤©¤ test
    ©À©¤©¤ __init__.py         # also make test a package
    ©¸©¤©¤ test_antigravity.py
And in the test modules inside the test package, you can import the antigravity package and its modules as usual:

# import the package
import antigravity

# import the antigravity module
from antigravity import antigravity

# or an object inside the antigravity module
from antigravity.antigravity import my_object
Running a single test module:

To run a single test module, in this case test_antigravity.py:

$ cd new_project
$ python -m unittest test.test_antigravity
Just reference the test module the same way you import it.

Running a single test case or test method:

Also you can run a single TestCase or a single test method:

$ python -m unittest test.test_antigravity.GravityTestCase
$ python -m unittest test.test_antigravity.GravityTestCase.test_method
Running all tests:

You can also use test discovery which will discover and run all the tests for you, they must be modules or packages named test*.py (can be changed with the -p, --pattern flag):

$ cd new_project
$ python -m unittest discover
This will run all the test*.py modules inside the test package


## notes
You can place the definitions of test cases and test suites in the same modules as the code they are to test (such as widget.py), but there are several advantages to placing the test code in a separate module, such as test_widget.py:

The test module can be run standalone from the command line.
The test code can more easily be separated from shipped code.
There is less temptation to change test code to fit the code it tests without a good reason.
Test code should be modified much less frequently than the code it tests.
Tested code can be refactored more easily.
Tests for modules written in C must be in separate modules anyway, so why not be consistent?
If the testing strategy changes, there is no need to change the source code.