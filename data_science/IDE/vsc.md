## Keyboard shortcuts

Being able to keep your hands on the keyboard when writing code is crucial for high productivity. VS Code has a rich set of default keyboard shortcuts as well as allowing you to customize them.

- [Keyboard Shortcuts Reference](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference) - Learn the most commonly used and popular keyboard shortcuts by downloading the reference sheet.
- [Install a Keymap extension](https://code.visualstudio.com/docs/getstarted/keybindings#_keymap-extensions) - Use the keyboard shortcuts of your old editor (such as Sublime Text, Atom, and Vim) in VS Code by installing a Keymap extension.
- [Customize Keyboard Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings#_customizing-shortcuts) - Change the default keyboard shortcuts to fit your style.

## 多光标同时编辑

这里有几种方式支持多光标同时编辑：

* 通过按下 `Alt` 并单击，可以在任意位置插入额外的光标。当在键盘上键入内容时，这些内容会同时出现在所有光标的后面。

* 按下 `CTRL` + `D`，则当前光标所在的单词会被选中，继续按下该快捷键则后面出现的该单词也会被选中并且在后面插入光标，然后就可以同时编辑这些单词了。当在键盘上键入内容时，这些被选中的所有单词将被键入内容替换，如果不想要替换它们，而是希望在后面追加内容，就先按下 `CTRL` + `SHIFT` + `L` 后，再输入内容。

注：进入多光标编辑模式时，可以通过按下 `ESC` 来返回普通模式。

## 块选择

* 扩展选择区域：按下 `ALT` + `SHIFT`，再通过上下左右键来控制选择区域的扩展和收缩
* 矩形区域选择：按下 `ALT` + `SHIFT`，再通过 `CTRL` + 上下左右键来选择矩形区域或者可以通过鼠标拖拽





It leverages all of VS Code's power to provide auto complete and IntelliSense, linting, debugging, and unit testing, along with the ability to easily switch between Python environments, including virtual and conda environments.



打开命令面板：按下 `F1` 或者 `CTRL` + `SHIFT` + `P`



文件内跳转窗口：按下 `CTRL` + `P` 后，可以使用 `:` 跳转到特定行，`@` 跳转到特定变量。



选择 Python 版本（或虚拟环境）：

窗口左下角有一个显示当前使用 Python 版本的区域，单击它可以选择不同的版本。

或者打开命令面板，使用 `Python: Select Interpreter` 来切换版本



运行 Python 代码：

* 编辑窗口右击，从菜单中选择运行文件还是选中的部分代码
* 文件窗口中右击脚本文件，运行该脚本
* 命令面板中使用 `Python: Create Terminal` 打开当前环境的新终端，来运行代码



## Autocomplete and IntelliSense

The Python extension supports code completion and Intellisense using the currently selected interpreter. [Intellisense](https://code.visualstudio.com/docs/editor/intellisense) is a general term for a number of features, including intelligent code completion (in-context method and variable suggestions) across all your files and for built-in and third-party modules.

IntelliSense quickly shows methods, class members, and documentation as you type, and you can trigger completions at any time with Ctrl+Space.



## Linting

Linting analyzes your Python code for potential errors, making it easy to navigate to and correct different problems.

The Python extension can apply a number of different linters including Pylint, Pep8, Flake8, mypy, pydocstyle, prospector, and pylama. See [Linting](https://code.visualstudio.com/docs/python/linting).



## Debugging

No more `print` statement debugging! Set breakpoints, inspect data, and use the debug console as you run your program step by step. Debug a number of different type of Python applications, including multi-threaded, web, and remote applications.

For Python-specific details, including setting up your `launch.json` configuration and remote debugging, see [Debugging](https://code.visualstudio.com/docs/python/debugging).



## Snippets

Snippets take productivity to the next level. You can configure [your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets) and use snippets provided by an extension. Snippets appear in the same way as code completion Ctrl+Space.



## Environments

The Python extension automatically detects Python interpreters that are installed in standard locations. It also detects conda environments as well as virtual environments in the workspace folder. See [Configuring Python environments](https://code.visualstudio.com/docs/python/environments). You can also use the `python.pythonPath` setting to point to an interpreter anywhere on your computer.

### Installing packages

Packages are installed using the **Terminal** panel and commands like `pip install <package_name>`(Windows) and `pip3 install <package_name>` (macOS/Linux). VS Code installs that package into your project along with its dependencies.



## Unit testing

The Python extension supports [unit testing](https://code.visualstudio.com/docs/python/unit-testing) with the unittest, pytest, and nose test frameworks.

To run unit tests, you enable one of the frameworks in settings. Each framework also has specific settings, such as arguments that identify paths and patterns for test discovery.

Once discovered, VS Code provides a variety of commands (on the Status Bar, the Command Palette, and elsewhere) to run and debug tests, including ability to run individual test files and individual methods.



## 代码编辑

### 运行

在编辑窗口中通过快捷键 `SHIFT` + `ENTER` 可以运行选中的代码（如果没有选中的话，就运行整个文件）

### 自动完成和智能感知

Autocomplete 和 IntelliSense 默认支持位于当前工作目录中所有文件中引用到的安装于 Python 标准位置的任何包。此外还可以通过以下配置来优化此项功能：

* 使 IntelliSens 支持安装于非标准位置的包：将安装于非标准位置包的路径添加到配置项 `python.autoComplete.extraPaths` 。

* 通过预加载来加快对某些包的 Autocomplete 速度：例如 `"python.autoComplete.preloadModules": ["numpy", "pandas", "matplotlib"],`
* 自动完成函数名时，添加括号：例如 `"python.autoComplete.addBrackets": true,`

### 排版

**配置**

指定使用哪种工具来对进行自动排版。配置项为 `python.formatting.provider`，可以选的内容有：`autopep8`, `black`, `yapf`。

* 这几个排版工具可能需要通过 `pip` 来安装。
* 它们有各自专门的配置项来进行配置：`python.formatting.autopep8Args`, `python.formatting.blackArgs`, `python.formatting.yapfArgs`。

### 重构

可以使用编辑器中的 **Extract Variable**, **Extract Method**, 和 **Sort Imports** 这些功能来进行代码重构。

#### Extract Variable

选中一段代码后，右击选择 “Extract Variable”，编辑器会自动将被选中代码所在作用域中的重复类似内容，提取为一个变量。

例如原始代码如下：

```
import math

a = math.sin(math.sqrt(2 * math.pi + 5))  # 选中其中的 
b = math.cos(math.sqrt(2 * math.pi + 5))
```

