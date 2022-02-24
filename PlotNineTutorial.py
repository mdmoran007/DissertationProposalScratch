# PlotNine Tutorial:
#   - https://towardsdatascience.com/how-to-use-ggplot2-in-python-74ab8adec129
# This is placed on ggplot2, and is often described as the closest to it in the Python ecosystem.

# The Grammar of Graphics creates a visual language for presentations.
# It sees a chart as a series of layers (building from the bottom):
#   - Theme (legend, background, annotations, etc.)
#   - Coordinates (Which coordinate system to use)
#   - Statistical Transformations (mainly summary statistics to include, like mean or percentiles)
#   - Facets (dealing with sub-plots)
#   - Geometric objects (the elements in the chart) <==Required
#   - Aesthetics (the axes) <==Required
#   - Data (required) <==Required

# MatPlotLib does have a ggplot style, but it is not as full of an implementation.
# Syntax is very similar to ggplot.

import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from plotnine import *
from plotnine.data import mpg # familiar sample data set.
#%matplotlib inline # does not work in PyCharm

# Basic Plot
p = (ggplot(mpg)         # defining what data to use
      + aes(x='class')    # defining what variable to use
      + geom_bar(size=20) # defining the type of plot to use
)

print (p)

# Change the orientation
p = (ggplot(mpg)
    + aes(x='class')
    + geom_bar(size=20)
    + coord_flip()        # flipping the x- and y-axes
    + labs(title='Number of Vehicles per Class', x='Vehicle Class', y='Number of Vehicles') # customizing labels
    )
print (p)

# Multi-dimensional Data
p =  (ggplot(mpg)
     + aes(x='displ', y='hwy', color='class')
     + geom_point()
     + labs(title='Engine Displacement vs. Highway Miles per Gallon', x='Engine Displacement, in Litres', y='Highway Miles per Gallon')
)

print (p)

# These are very familiar charts with a very familiary feel.
# Here's another chart from:
#   - https://plotnine.readthedocs.io/en/stable/

from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

p = (ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
    + geom_point()
    + stat_smooth(method='lm')
    + facet_wrap('~gear'))

print(p)