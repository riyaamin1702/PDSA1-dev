This is the basic harness for the first practical data science
assessment.

# Create working environment. 
conda create -n PDSA1 python=3.8
pip install -r requirements.txt

# This will install everything you need to run jupyter or the
# command line options.

# You can start the notebook with:
jupyter notebook A1.ipynb

# The notebook can be used to get the functions working you
# need. Once you have them working, you need to copy your
# functions into the 3 script files, one per challenge so
# that they can be automatically ran against the regression
# harness.

# Files included.

- README.md : This file.
- requirements.txt : pip requirements file.
- A1.ipynb : jupyter notebook template
- data/*.m : The semistructured input files you will process.
- aflutil/helper.py : Several helper utility functions that
                      are provided to read / write files in
                      a specific format. You should look at
                      all of these functions carefully as 
                      they will help you solve the challenges.
- aflutil/AFLGame.py : This is a helper class that is used only
                       in the third challenge.
- create_afl_tsv.py : The main script for the first challenge.
- validate_afl_tsv.py : The main script for the second challenge.
- find_topfive_wins.py : The main script for the third challenge.
