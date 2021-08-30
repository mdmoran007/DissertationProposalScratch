# Bokeh Tutorial from:
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