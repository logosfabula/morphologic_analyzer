# Simple Morphologic Analyzer 

A handy tool for splitting English compounds into their components. It makes use of a set of public English language corpora and NLTK.

## Getting Started

Type:
`git clone https://github.com/logosfabula/morphologic_analyzer.git`

### Prerequisites

You need NLTK.

`sudo pip install -U nltk`

### Installing

No need of installation.

### Setup

Fill in: 
`./compounds.txt`
with the compound words to be analyzed.

Then add the components you don't want to take into account in: 
`./removed_words.txt`

### Use

`./python compounds_splitter.py`

Results will appear on screen and in `./results.txt`

### Testing

Follow instructions on preconditions in `test_*.py`
Run `Py.test`
Support functions for tests are in `./test_support/`

## Authors

* **Anton Maria Prati** - *Initial work* - [logosfabula](https://github.com/logosfabula)

See also the list of [contributors](https://github.com/logosfabula/morphologic_analyzer/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments




