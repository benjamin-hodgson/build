`build`
=======

[![Build Status](https://travis-ci.org/benjamin-hodgson/build.svg?branch=master)](https://travis-ci.org/benjamin-hodgson/build)
[![Documentation Status](https://readthedocs.org/projects/build/badge/?version=v1.0.1)](https://readthedocs.org/projects/build/?badge=v1.0.1)

A tiny base class for fluent builders, harvested from Huddle's test code.


Installation
------------

```bash
$ pip install build
```

Example
-------

```python
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
