import os
import sys

# ensure that imports are possible from the src folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '../src/')))
