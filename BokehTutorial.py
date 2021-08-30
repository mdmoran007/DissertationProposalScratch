# Bokeh Tutorial from:
#   - https://docs.bokeh.org/en/latest/docs/first_steps/first_steps_1.html

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