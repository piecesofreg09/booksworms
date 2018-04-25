1. Put the training part of CF and Ricky's alg in the file train.py. Specify the output to match the book recommendation alg from Zefang.

2. Add the additional required packages needed for Ricky's alg or CF in setup.py, so that when the bookworms module is installed, the required packages will be installed at the same time.

3. Put the visualization method into the visualize.py, where it is lablled with # NEEDS IMPLEMENTATION on line 41. The visualization component should be working with the local recommendation algorithm.

4. When import inside the ./bookworms/ package, use 'from .file import func' instead of 'from file import func', the latter would trigger package not found error. 

5. The main two portals of the module bookworms is train and visualize. They are all written in the bookworms/__main__.py file.
