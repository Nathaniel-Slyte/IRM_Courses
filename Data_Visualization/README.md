# Data Visualization: Compelling Data-Driven Stories

[Fundamentals of Data Visualization - Claus O.Wilke](http://dl.booktolearn.com/ebooks2/computer/graphics/9781492031086_Fundamentals_of_Data_Visualization_0a8c.pdf)

## Table of Content

* I. Introduction
* II. Visualization
    * a. Type of Data and Aesthetics
    * b. Type of Graphs
* III. Principles of Design
    * a. Minimalism and Proportional Ink
    * b. Contextualization
* IV. Story Telling
* V. Workshop
* VI. Assignement

---

## I. Introduction

**Why you should care:**

* Reporting implies making clear, attractive and convincing data visualizations
* Needs to carry the weight of an argumentation
* Develop an eye for compelling graphics

* [What is Data Visualization in 3 min?](https://www.youtube.com/watch?v=VyhLRJVoIrI)
* [Creating Beautiful and Meaningful Visualizations with Big Data](https://www.youtube.com/watch?v=Z8E4_rOpbyw)

**Differentiate between Good, Ugly, Bad and Wrong figures:**

* Ugly: Clear and Informative but Aesthetic issues
* Bad: Perception issues, unclear, confusing or complicated
* Wrong: Mathematical, Objectivity issues

## II. Visualization

### a. Type of Data and Aesthetics

**Data:**

|              |Quantitative|Qualitative        |
|--------------|------------|-------------------|
|**Discrete**  |1, 2, 3     |dog, cat, good, bad|
|**Continuous**|1.3, 1e-2   |                   |
Text, Date, Time, ... etc

**Aesthetics:**

* Position ((x, y) 2D, (x, y, z) 3D, (radius, theta) 2D Polar, ...)
* Shape (Circle, Square, Triangle, ...)
* Size (Large, Medium, Small, ...)
* Color (Hue, Value, Saturation, Opacity, ...)
* Line Width (Thick, Thin, ...)
* Line Type (Continuous, Dotted, Dashed, ...)

**Link data to aesthetics:**

* The most impactful feature needs to be more important visually
* Ordered Data Need to be Ordered in Position
* Equal spacing for discrete vairables
* Axis and scales should be appropriate
* Colors as a tool to classify
* Color as a value
* Color to highlight


### b. Type of Graphs

|Data Types   |Graphs                                                                                      |
|-------------|--------------------------------------------------------------------------------------------|
|Amounts      |Bars, Grouped/Stacked Bars, Heatmap                                                         |
|Distributions|Histogram, Density, Box, Violins, Overlapping Density, Stacked Histogram, Rigideline, Sina  |
|Proportions  |Pie, Bars, Stacked Bars, Stacked Densities, Mosaic, Treemap, Parallel Sets                  |
|Relationships|Scatter, Bubble, Paired Scatter, Slopegraph, Desnity Contours, Bins, Correlogram, Line Graph|
|Geospatial   |Map, Choropleth, Cartogram, Cartogram Heatmap                                               |
|Uncertainty  |Error Bars, Eyes, Half-Eyes, Confidence Band                                                |

## III. Principles of Design

### a. Minimalism and Proportional Ink

> "When a shaded region is used to represent a numerical value, the area of that shaded
> region should be directly proportional to the corresponding value." -- Bergstrom and West 2016

* Maximize Data-Ink Ratio
* Accessibility first
* Avoid using too many colours
* Minimalism should be a goal
* [Data to Ink Ratio (Tufte principle of Data Visualization)](https://www.youtube.com/watch?v=JIMUzJzqaA8)

### b. Contextualization

* Choose the target
* Considere color blind people (Solved by choosing good color palettes and using redundancy)
* Always order legend in the same order of the compared value
* Armonize colours between correlated data between graphs
* Add Legend, Title, Tables, ... etc
* Weight the amount of context necessary, do not over do it

## IV. Story Telling

* [The Largest Vocabulary in Hip Hop](https://pudding.cool/projects/vocabulary/)
* [The Dawn Wall](https://www.nytimes.com/interactive/2015/01/09/sports/the-dawn-wall-el-capitan.html?_r&_r=0)
* [After Babylon](http://snip.ly/pJsZ#http://www.puffpuffproject.com/languages.html)
* [This is every Active Satellite Orbiting Earth](https://qz.com/296941/interactive-graphic-every-active-satellite-orbiting-earth/)
* [Where We Came From and Where We Went, State by State](https://www.nytimes.com/interactive/2014/08/13/upshot/where-people-in-each-state-were-born.html?abt=0002&abg=0&mtrref=undefined&assetType=REGIWALL)
* [Selfie City](http://selfiecity.net/)

---

## V. Workshop

**Requirements**:

* Libraries: [Python3](https://www.python.org/), [Pip3](https://pypi.org/), [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/3.1.1/index.html)
* Dataset: [Marble Racing](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-06-02/readme.md)

**Tasks**:

* Load and Explore data with Pandas
* Explore the different type of Graphs and Aesthetics
* Export Graphs to `.eps` format

---

## VI. Assignements

**Requirements**:

* Libraries: [Python3](https://www.python.org/), [Pip3](https://pypi.org/), [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/3.1.1/index.html)
* Datasets: [Animal Crossing](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-05-05/readme.md), [Beer Production](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-03-31/readme.md), [Australia Fires](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-07/readme.md)

**Objectives**:

* Explore a Dataset with a complete statistical analysis using Graphs
* Organize the graphs and build Slides for a convincing Story Telling