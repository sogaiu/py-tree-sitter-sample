# py-tree-sitter-sample

## Setup

Clone this repository and cd to the resulting directory:

```
git clone https://github.com/sogaiu/py-tree-sitter-sample
cd py-tree-sitter-sample
```

Once in the cloned directory, clone the [tree-sitter-java grammar
repository](https://github.com/tree-sitter/tree-sitter-java):

```
git clone https://github.com/tree-sitter/tree-sitter-java
```

Setup a "virtual" environment for python to isolate things ("virtual"
here really means something like "project-specific"):

```
python -m venv venv
```

Activate the environment (use `deactivate` to exit later) [1]:

```
source ./venv/bin/activate
```

Install
[py-tree-sitter](https://github.com/tree-sitter/py-tree-sitter/) using
python's `pip` program -- note that when installing, the name to use
really is `tree-sitter`:

```
pip install tree-sitter
```

## Verify

Try the sample code:

```
python sample.py
```

Output should look something like:

```
<Node type=program, start_point=(1, 0), end_point=(6, 0)>
program
(1, 0)
(6, 0)
<Node type=class_declaration, start_point=(1, 0), end_point=(5, 1)>
class_declaration
(1, 0)
(5, 1)
```

Note that to work with the code again at a later time (say after
rebooting or via another command prompt), remember to "activate" the
environment as explained in the Setup section above.

## Footnotes

[1] For Windows, use the following to activate the environment
instead:

```
.\venv\Scripts\activate.bat
```

To deactivate the environment, do:

```
.\venv\Scripts\deactivate.bat
```
