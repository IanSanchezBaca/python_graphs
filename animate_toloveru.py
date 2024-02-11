#!/usr/bin/env python3
# LIBRARIES
import os 
import math 
from fractions import Fraction # prob dont need this
import warnings
import pygraphviz as pgv

warnings.simplefilter("ignore", RuntimeWarning)
mygraph = pgv.AGraph()

if not os.path.exists(""):
    os.makedirs("uwu")
    print("new directory \"uwu\" created")
