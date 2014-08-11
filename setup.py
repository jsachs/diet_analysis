from distutils.core import setup

setup(
    name = "diet_analysis",
    packages = ["diet_analysis"],
    version = "0.1",
    description = "Curses-based diet logging tool",
    author = "Jacob Sachs",
    author_email = "jacob.s.sachs@gmail.com",
    url = "https://github.com/jsachs/diet_analysis",
    download_url = "https://github.com/jsachs/diet_analysis/archive/master.zip",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        ],
    requires=['numpy', 'matplotlib', 'tinydb']
)