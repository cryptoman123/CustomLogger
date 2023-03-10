# CustomLogger
Custom Logger is a Python library which you can use if you don't want to get into the nitty–gritty of writing your own logger. I made this Custom Logger so I don't have to create a logger for each project.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install custom logger
```



## Usage
mkdir docs
cd docs
sphinx-quickstart <defaults>

Edit Conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
extensions = [
   'sphinx.ext.duration',
   'sphinx.ext.doctest',
   'sphinx.ext.autodoc',
   'sphinx.ext.autosummary',
]
html_theme = 'sphinx_rtd_theme'

sphinx-apidoc -o . ..
creates .rst for each python file
make html


```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## TODO

1. Add tests in the documentation.
2. Add usage in documentation.
3. Write test cases.
4. Correct README.md

## License

[MIT](https://choosealicense.com/licenses/mit/)

# Reference
Sajip, V. (n.d.). Logging HOWTO. Python Documentation. Retrieved March 7, 2023, from https://docs.python.org/3/howto/logging.html

The Python Software Foundation (n.d.). Logging facility for Python. Python Documentation. Retrieved March 7, 2023, from https://docs.python.org/3/library/logging.html

Ajitsaria, A. (n.d.). Logging in Python. Retrieved March 7, 2023, from https://realpython.com/python-logging/

YouTube. (2022, October 6). Sphinx - how to generate documentation from python DOC strings - five + minutes on tips and tricks. YouTube. Retrieved March 7, 2023, from https://www.youtube.com/watch?v=BWIrhgCAae0&amp;ab_channel=LearnProgrammingwithJoel 

Toptal.com, 2023, https://www.toptal.com/developers/gitignore/api/python. Accessed 7 Mar. 2023.

# Test Environment
![](https://img.shields.io/badge/Python%203.7-14354C?style=for-the-badge&logo=python&logoColor=white) ![](https://img.shields.io/badge/NVIDIA-RTX3060-76B900?style=for-the-badge&logo=nvidia&logoColor=white) ![](https://img.shields.io/badge/Windows%2011-Dell_G15_5511-0078D6?style=for-the-badge&logo=windows&logoColor=white)