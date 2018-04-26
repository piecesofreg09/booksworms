# bookworms

Book recommendation system

## Getting Started

Make sure Python3.6 or higher is installed. Or the package might not work.

### Installation

Install by package. After downloading and extracting the package, direct into the directory with the file `setup.py`. Then install the module by

```
python -m pip install .
```

### Uninstall

To uninstall, type in the command window

```
python -m pip uninstall bookworms
```

## Module Usage

After installation, the module has two main functionality, training and visulization. 

1. For training, add the following code in your script

```
from bookworms.train import train
train(['input.json'], support, variable) 

# input must be list, with file names as string in it. Empty list is allowed.
# suppor is the variable for ARM training
# variable is currently an arbitrary variable
```

2. For visualization, add the following code in your script

```
from bookworms.visualize import visualize
visualize()
```

## Script Usage

After installation, the file can also be used as a script. Type in the following command in command window will result in the same result as in Module Usage.

1. For training
```
python -m bookworms train -f input.json -s support
```

2. For visualization
```
python -m bookworms visualization
```

Type in `python -m bookworms -h` for more help.

## Running the tests

Test function and a small dataset is included in the `.test\` directory. Running the following command in the command window directory will show the process of training and visualization.

```
python test.py
```

## Authors

See also the list of [contributors](https://github.gatech.edu/hlu82/bookworms/settings/collaboration) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* Data is scraped from Goodreads.com, only for academic research purpose, and will be deleted after the project due.
* suppress_output() is shared from https://thesmithfam.org/blog/2012/10/25/temporarily-suppress-console-output-in-python/.

