# Bokeh Tutorial starting from:
#   - https://docs.bokeh.org/en/latest/docs/first_steps/first_steps_1.html
#
# I am making some changes and consolidating some sections, but it will give me a good basis to learn.

# First Steps 1: Creating a simple line chart ---------------------

# 1. Import the necessary functions
import bokeh.io
from bokeh.plotting import figure, show

# Define two lists containing the data for your line chart:

# 2. Make two lists.
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# 3. Use the figure () function to creat the plot.
# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')

# 4. add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Temp.", line_width=2)

# 5. show the results
# Defaults to making an html file in this directory.
bokeh.io.output_file('BokehTutorial-1A.html')
show(p)

# Combining multiple graphs -------------------
# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

# create a new plot with a title and axis labels
p = figure(title="Multiple line example", x_axis_label='x', y_axis_label='y')

# add multiple renderers
p.line(x, y1, legend_label="Temp.", line_color="blue", line_width=2)
p.line(x, y2, legend_label="Rate", line_color="red", line_width=2)
p.line(x, y3, legend_label="Objects", line_color="green", line_width=2)

# show the results]
bokeh.io.output_file('BokehTutorial-1B.html')
show(p)

# Re-cap:
#  1: Prep the data
#  2: Call the figure() fxn to create the plot
#  3: Add renderers.
#  4: show() or save() the plot.

# First Steps 2: Adding and customizing renderers ------------------------------
# In part 1, we used figure() to render line charts.
# In this section, we'll use other functions to render other types of charts.

# Just added the circle and the vbar to the previous instructions.
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

# create a new plot with a title and axis labels
p = figure(title="Multiple glyphs example", x_axis_label="x", y_axis_label="y")

# add multiple renderers
p.line(x, y1, legend_label="Temp.", line_color="blue", line_width=2)
p.vbar(x=x, top=y2, legend_label="Rate", width=0.5, bottom=0, color="red")
p.circle(x, y3, legend_label="Objects", line_color="yellow", size=12)

# show the results
bokeh.io.output_file('BokehTutorial-2A.html')
show(p)

# Customizing Glyphs.
# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a new plot with a title and axis labels
p = figure(title="Glyphs properties example", x_axis_label="x", y_axis_label="y")

# add circle renderer with additional arguments
circle = p.circle(
    x,
    y,
    legend_label="Objects",
    fill_color="green",
    fill_alpha=0.5,
    line_color="orange",
    size=80,
)

# change color of previously created object's glyph
glyph = circle.glyph
glyph.fill_color = "blue"
glyph.line_alpha=0.75

# show the results
bokeh.io.output_file('BokehTutorial-2B.html')
show(p)

# First Steps 3: Adding legends, text, and annotations -----------------------
# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [4, 5, 5, 7, 2]
y2 = [2, 3, 4, 5, 6]

# create a new plot
p = figure(title="Headline Example")

# Change and enhance the plot title
p.title_location = 'left'
p.title.text = ' New Headline Text '

# style the headline
p.title.text_font_size = "25px"
p.title.align = "right"
p.title.background_fill_color = "darkgrey"
p.title.text_color = "white"

# add circle renderer with legend_label arguments
line = p.line(x, y1, legend_label="Temp.", line_color="blue", line_width=2)
circle = p.circle(
    x,
    y2,
    legend_label="Objects",
    fill_color="red",
    fill_alpha=0.5,
    line_color="blue",
    size=80,
)

# display legend in top left corner (default is top right corner)
p.legend.location = "top_left"

# add a title to your legend
p.legend.title = "Obervations"

# change appearance of legend text
p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"

# change border and background of legend
p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.8
p.legend.background_fill_color = "navy"
p.legend.background_fill_alpha = 0.2

# show the results
bokeh.io.output_file('BokehTutorial-3A.html')
show(p)

# Using Annotations
import random

from bokeh.models import BoxAnnotation
from bokeh.plotting import figure, show

# generate some data (1-50 for x, random values for y)
x = list(range(0, 51))
y = random.sample(range(0, 100), 51)

# create new plot
p = figure(title="Box annotation example")

# add line renderer
line = p.line(x, y, line_color="blue", line_width=2)

# add box annotations
low_box = BoxAnnotation(top=20, fill_alpha=0.1, fill_color="red")
mid_box = BoxAnnotation(bottom=20, top=80, fill_alpha=0.1, fill_color="green")
high_box = BoxAnnotation(bottom=80, fill_alpha=0.1, fill_color="red")

# add boxes to existing figure
p.add_layout(low_box)
p.add_layout(mid_box)
p.add_layout(high_box)

# show the results
bokeh.io.output_file('BokehTutorial-3B.html')
show(p)

# First Steps 4: Customizing Your Plot ---------------------------------------

# In the previous first steps guides, we generated different glyphs
# and added more information such as a title, legend, and annotations.
#
# In this section, we will customize the appearance of the plot as a whole.
# This includes resizing your plot, changing its lines and colors, and customizing the axes and tools.

# Using Themes
# With Bokeh’s themes, you can quickly change the appearance of your plot.
# Themes are a set of pre-defined design parameters such as colors, fonts, or line styles.
#
# Bokeh comes with five built-in themes:
#   - caliber
#   - dark_minimal
#   - light_minimal
#   - night_sky
#   - contrast
# Additionally, you can define your own custom themes.
#
# To use one of the built-in themes, assign the name of the theme to the theme property of the document

from bokeh.io import curdoc

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# apply theme to current document
curdoc().theme = "dark_minimal"

# create a plot
p = figure(sizing_mode="stretch_width", max_width=500, plot_height=250)

# add a renderer
p.line(x, y)

# show the results
bokeh.io.output_file('BokehTutorial-4A.html')
show(p)

# Resizing your plot¶
# Bokeh’s Plot objects have various attributes that influence the way your plot looks.
#
# Setting width and height
# To set the size of your plot, use the attributes plot_height and plot_width when calling the figure() function:

# First, re-set the theme
curdoc().theme = 'caliber'

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a new plot with a specific size
p = figure(
    title="Plot sizing example",
    plot_width=350,
    plot_height=250,
    x_axis_label="x",
    y_axis_label="y",
)

# add circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

# show the results
bokeh.io.output_file('BokehTutorial-4B.html')
show(p)

# chage plot size
p.plot_width = 450
p.plot_height = 150

# add circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

# show the results

bokeh.io.output_file('BokehTutorial-4C.html')
show(p)

# Make the plot responsive to the size of the browser:

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a new plot with responsive width
p = figure(
    title="Plot responsive sizing example",
    sizing_mode="stretch_width",
    plot_height=250,
    x_axis_label="x",
    y_axis_label="y",
)

# add circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

# show the results
bokeh.io.output_file('BokehTutorial-4D.html')
show(p)

# Customizing axes
# You can set various attributes to change the way the axes in your plot work and look.
#
# Setting your axes’ appearance
# Options for customizing the appearance of your plot include:
#   - setting labels for your axes
#   - styling the numbers displayed with your axes
#   - defining colors and other layout properties for the axes themselves

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a plot
p = figure(
    title="Customized axes example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=350,
)

# add a renderer
p.circle(x, y, size=10)

# change some things about the x-axis
p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"

# change some things about the y-axis
p.yaxis.axis_label = "Pressure"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"

# change things on all axes
p.axis.minor_tick_in = -3
p.axis.minor_tick_out = 6

# show the results
bokeh.io.output_file('BokehTutorial-4E.html')
show(p)

# create a new plot with responsive width
p = figure(
    y_range=(0, 25),
    title="Axis range example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add circle renderer with additional arguments
circle = p.circle(x, y, size=8)

# show the results
bokeh.io.output_file('BokehTutorial-4F.html')
show(p)

# Formatting axis ticks
from bokeh.models import NumeralTickFormatter
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")

bokeh.io.output_file('BokehTutorial-4F.html')
show(p)

# Logarithmic Axes
# prepare some data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y0 = [i**2 for i in x]
y1 = [10**i for i in x]
y2 = [10**(i**2) for i in x]

# create a new plot with a logarithmic axis type
p = figure(
    title="Logarithmic axis example",
    sizing_mode="stretch_width",
    plot_height=300,
    max_width=500,
    y_axis_type="log",
    y_range=[0.001, 10 ** 11],
    x_axis_label="sections",
    y_axis_label="particles",
)

# add some renderers
p.line(x, x, legend_label="y=x")
p.circle(x, x, legend_label="y=x", fill_color="white", size=8)
p.line(x, y0, legend_label="y=x^2", line_width=3)
p.line(x, y1, legend_label="y=10^x", line_color="red")
p.circle(x, y1, legend_label="y=10^x", fill_color="red", line_color="red", size=6)
p.line(x, y2, legend_label="y=10^x^2", line_color="orange", line_dash="4 4")

# show the results
bokeh.io.output_file('BokehTutorial-4G.html')
show(p)

# Date-Time Axes
import random
from datetime import datetime, timedelta

from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.plotting import figure, show

# generate list of dates (today's date in subsequent weeks)
dates = [(datetime.now() + timedelta(day * 7)) for day in range(0, 26)]

# generate 25 random data points
y = random.sample(range(0, 100), 26)

# create new plot
p = figure(
    title="datetime axis example",
    x_axis_type="datetime",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add renderers
p.circle(dates, y, size=8)
p.line(dates, y, color="navy", line_width=1)

# format axes ticks
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

# show the results
bokeh.io.output_file('BokehTutorial-4H.html')
show(p)

# Customizing the Grid
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a plot
p = figure(
    title="Customized grid lines example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add a renderer
p.line(x, y, line_color="green", line_width=2)

# change just some things about the x-grid
p.xgrid.grid_line_color = "red"

# change just some things about the y-grid
p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [6, 4]

# show the results
bokeh.io.output_file('BokehTutorial-4I.html')
show(p)

# Adding bands and bounds to the grid
# create a plot
p = figure(
    title="Bands and bonds example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add a renderer
p.line(x, y, line_color="green", line_width=2)

# add bands to the y-grid
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

# define vertical bonds
p.xgrid.bounds = (2, 4)

# show the results
bokeh.io.output_file('BokehTutorial-4J.html')
show(p)

# Set the background color
# create a plot
p = figure(
    title="Background colors example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add a renderer
p.line(x, y, line_color="green", line_width=2)

# change the fill colors
p.background_fill_color = (204, 255, 255)
p.border_fill_color = (102, 204, 255)
p.outline_line_color = (0, 0, 255)

# show the results
bokeh.io.output_file('BokehTutorial-4K.html')
show(p)

# Customizing the toolbar

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a plot
p = figure(
    title="Toolbar autohide example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# Change Location and activate toolbar autohide
p.toolbar_location = "below" # Use None to hide altogether
p.toolbar.autohide = True
p.toolbar.logo = None # De-activate the logo

# add a renderer
p.line(x, y)

# show the results
bokeh.io.output_file('BokehTutorial-4L.html')
show(p)

# Customizing the Available Tools in the Toolbar
# To customize tools, first you import the  tools that you want:
# Then make those attributes for the figure.

from bokeh.models.tools import BoxZoomTool, PanTool, ResetTool

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a plot
p = figure(
    title="Modifying tools example",
    tools=[BoxZoomTool(), ResetTool()],
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add an additional pan tool
# only vertical panning is allowed
p.add_tools(PanTool(dimensions="width"))

# add a renderer
p.circle(x, y, size=10)

# show the results
bokeh.io.output_file('BokehTutorial-4M.html')
show(p)

# Adding Tooltips
# There are several ways to do this in Bokeh. This is the quickest.

from bokeh.models.tools import HoverTool
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

p = figure(
    y_range=(0, 10),
    toolbar_location=None,
    tools=[HoverTool()],
    tooltips="Data point @x has the value @y",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add renderers
p.circle(x, y, size=10)
p.line(x, y, line_width=2)

# show the results
bokeh.io.output_file('BokehTutorial-4N.html')
show(p)

# First Steps 5: Vectorizing glyph properties -------------------------------------
# In the previous first steps guide, you customized various aspects of your plot by adding and changing attributes.
# In this section, you will use vectors of data to influence aspects of your plot and its elements.

# Vectorizing colors
# So far, you have assigned specific colors to a glyph by using properties such as fill_color.
# To change colors depending on values in a variable,
# pass a variable containing color information to the fill_color attribute:

# generate some data (1-10 for x, random values for y)
x = list(range(0, 26))
y = random.sample(range(0, 100), 26)

# generate list of rgb hex colors in relation to y
colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

# create new plot
p = figure(
    title="Vectorized colors example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add circle and line renderers
line = p.line(x, y, line_color="blue", line_width=1)
circle = p.circle(x, y, fill_color=colors, line_color="blue", size=15)

# show the results
bokeh.io.output_file('BokehTutorial-5A.html')
show(p)

# Vectorizing Colors and Sizes
# Here, apply the same principle to the radius

import numpy as np

# generate some data
N = 1000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100

# generate radii and colors based on data
radii = y / 100 * 2
colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

# create a new plot with a specific size
p = figure(
    title="Vectorized colors and radii example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# add circle renderer
p.circle(
    x,
    y,
    radius=radii,
    fill_color=colors,
    fill_alpha=0.6,
    line_color="lightgrey",
)

# show the results
bokeh.io.output_file('BokehTutorial-5B.html')
show(p)

# Color mapping with palettes
# Bokeh comes with dozens of pre-defined color palettes that you can use to map colors to your data.Th
# is includes palettes from Brewer, D3, or Matplotlib.
#
# First, use the linear_cmap() function to create a color map for your data.
# The required attributes for this function are:
#   - field_name: the data sequence to map colors to
#   - palette: the palette to use
#   - low: the lowest value to map a color to
#   - high: the highest value to map a color to
# Then assign your color mapper to the color parameter of your renderer:

from bokeh.palettes import Turbo256
from bokeh.plotting import figure
from bokeh.transform import linear_cmap

# generate data
x = list(range(-32, 33))
y = [i**2 for i in x]

# create linear color mapper
mapper = linear_cmap(field_name="y", palette=Turbo256, low=min(y), high=max(y))

# create plot
p = figure(plot_width=500, plot_height=250)

# create circle renderer with color mapper
p.circle(x, y, color=mapper, size=10)

bokeh.io.output_file('BokehTutorial-5C.html')
show(p)

# First steps 6: Combining plots -----------------------------------------------
# In the previous first steps guides, you created individual plots.
# In this section, you will combine several plots into different kinds of layouts.

# Creating rows, columns, and grids
# The easiest way to combine individual plots is to assign them to rows or columns.

from bokeh.layouts import row
from bokeh.plotting import figure, show

# prepare some data
x = list(range(11))
y0 = x
y1 = [10 - i for i in x]
y2 = [abs(i - 5) for i in x]

# create three plots with one renderer each
s1 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s1.circle(x, y0, size=12, color="#53777a", alpha=0.8)

s2 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s2.triangle(x, y1, size=12, color="#c02942", alpha=0.8)

s3 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s3.square(x, y2, size=12, color="#d95b43", alpha=0.8)

# put the results in a row and show
# To display several plots in a vertical column layout, use the column() function instead.
# A more flexible way to arrange elements in Bokeh is to use the gridplot() function.
bokeh.io.output_file('BokehTutorial-6A.html')
show(row(s1, s2, s3))

# You can also make it more responive to the browser.
# create three plots with one renderer each
s1 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s1.circle(x, y0, size=12, color="#53777a", alpha=0.8)

s2 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s2.triangle(x, y1, size=12, color="#c02942", alpha=0.8)

s3 = figure(plot_width=250, plot_height=250, background_fill_color="#fafafa")
s3.square(x, y2, size=12, color="#d95b43", alpha=0.8)

# put the results in a row that automatically adjusts
# to the browser window's width
bokeh.io.output_file('BokehTutorial-6B.html')
show(row(children=[s1, s2, s3], sizing_mode="scale_width"))

# First steps 7: Displaying and exporting ----------------------------------------------------
# This section will work with formatting, exporting, and saving the visualizations.
# THe ability to do it in a png requires a driver that the M1 does not appear to have yet, but I can export.

from bokeh.plotting import figure, output_file, save, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# set output to static HTML file
output_file(filename="BokehTutorial-7A.html", title="Your Title Here")

# create a new plot with a specific size
p = figure(sizing_mode="stretch_width", max_width=500, plot_height=250)

# add a circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

# save the results to a file
save(p) # Without showing
# Show (and save) the results
show(p) # Will also work directly in a Jupyter notebook.

# This section had to be customized to check hardware since it does not work on the native M1 architecture.
# This requires selenium be installed to work. It also looks like it needs a chromedriver.
import platform
from bokeh.io import export_png
from bokeh.plotting import figure

if platform.machine() == 'arm64':
    print('The right drivers don\'t exist to run this on native MacOS arm64')
else:
    # prepare some data
    x = [1, 2, 3, 4, 5]
    y = [4, 5, 5, 7, 2]

    # create a new plot with fixed dimensions
    p = figure(plot_width=350, plot_height=250)

    # add a circle renderer
    circle = p.circle(x, y, fill_color="red", size=15)

    # save the results to a file
    export_png(p, filename='BokenTutorial-7B.png')

# First steps 8: Providing and filtering data --------------------------------
# In this section, we will use various sources and structures to import and filter data.

from bokeh.models import ColumnDataSource

# create dict as basis for ColumnDataSource
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

# create ColumnDataSource based on dict
source = ColumnDataSource(data=data)
# You could also convert a pandas dataframe with a command like:
# source = ColumnDataSource(df)

# create a plot and renderer with ColumnDataSource data
p = figure()
p.circle(x='x_values', y='y_values', source=source)

bokeh.io.output_file(filename="BokehTutorial-8A.html")
show(p)

# Filtering Data
from bokeh.layouts import gridplot
from bokeh.models import CDSView, ColumnDataSource, IndexFilter
from bokeh.plotting import figure, show

# create ColumnDataSource from a dict
source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]))

# create a view using an IndexFilter with the index positions [0, 2, 4]
view = CDSView(source=source, filters=[IndexFilter([0, 2, 4])])

# setup tools
tools = ["box_select", "hover", "reset"]

# create a first plot with all data in the ColumnDataSource
p = figure(plot_height=300, plot_width=300, tools=tools)
p.circle(x="x", y="y", size=10, hover_color="red", source=source)

# create a second plot with a subset of ColumnDataSource, based on view
# There are other filters. This just filters out the data points at that index position.
p_filtered = figure(plot_height=300, plot_width=300, tools=tools)
p_filtered.circle(x="x", y="y", size=10, hover_color="red", source=source, view=view)

# show both plots next to each other in a gridplot layout
bokeh.io.output_file(filename="BokehTutorial-8B.html")
show(gridplot([[p, p_filtered]]))

# First steps 9: Using widgets -----------------------------------------------
# To make a more interactive html viz, you can use widgets.
# This can also be done with a bokeh server.

from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

# create plot with circle glyphs
p = figure(x_range=(1, 9), plot_width=500, plot_height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")

# set up textarea (div)
div = Div(
    text="""
          <p>Select the circle's size using this control element:</p>
          """,
    width=200,
    height=30,
)

# set up spinner
spinner = Spinner(
    title="Circle size",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    width=200,
)
spinner.js_link("value", points.glyph, "size")

# set up RangeSlider
range_slider = RangeSlider(
    title="Adjust x-axis range",
    start=0,
    end=10,
    step=1,
    value=(p.x_range.start, p.x_range.end),
)
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

# create layout
layout = layout(
    [
        [div, spinner],
        [range_slider],
        [p],
    ]
)

# show result
bokeh.io.output_file('BokehTutorial-9A.html')
show(layout)