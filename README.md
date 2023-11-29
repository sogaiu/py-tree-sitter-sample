# py-tree-sitter-sample

## Setup

```
git clone https://github.com/sogaiu/py-tree-sitter-sample
cd py-tree-sitter-sample

# clone the tree-sitter-java grammar
git clone https://github.com/tree-sitter/tree-sitter-java

# setup a "virtual" environment for python to isolate things
python -m venv venv

# activate the environment (use `deactivate` to exit later) [1]
source ./venv/bin/activate

# install py-tree-sitter
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
