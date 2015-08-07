try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

    from setuptools import setup, find_packages


setup(
    name='build',
    version='1.0.1',
    author="Benjamin Hodgson",
    author_email="benjamin.hodgson@huddle.net",
    url="https://github.com/benjamin-hodgson/build",
    description="A tiny base class for fluent builders",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=["setuptools"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
