I'm not maintaining this, and it has been removed from PyPI. It's only one file. You're welcome to copy it
==========================================================================================================



`build`
=======

[![Build Status](https://travis-ci.org/benjamin-hodgson/build.svg?branch=master)](https://travis-ci.org/benjamin-hodgson/build)
[![Documentation Status](https://readthedocs.org/projects/build/badge/?version=v1.0.1)](https://readthedocs.org/projects/build/?badge=v1.0.1)
[![Coverage Status](https://coveralls.io/repos/benjamin-hodgson/build/badge.svg?branch=master&service=github)](https://coveralls.io/github/benjamin-hodgson/build?branch=master)
[![Requirements Status](https://requires.io/github/benjamin-hodgson/build/requirements.svg?branch=master)](https://requires.io/github/benjamin-hodgson/build/requirements/?branch=master)

A tiny base class for fluent builders, harvested from Huddle's test code.


Installation
------------

```bash
$ pip install build
```

Example
-------

```python
from build import Builder

class MyBuilder(Builder):
    # declare the defaults for the builder
    defaults = [
        ("abc", 123),
        ("def", 456),
        ("xyz", 789)
    ]

    def build(self):
        # convert self.data into the object you're building
        return self.data

MyBuilder().with_abc(-1).with_def(-2).build() # {'xyz': 789, 'def': -2, 'abc': -1}
```
