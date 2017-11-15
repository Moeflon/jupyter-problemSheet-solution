# jupyter-problemSheet-solution

## Introduction
The following is a 4th year in-class assignment for Emerging technologies. These problems relate to Jupyter, numpy, and pyplot. We will use the famous iris data set, and plot some graphs to give a visual representation of the data.

### What is the IRIS data set?

The IRIS data set consists of 50 samples from each of 3 species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

For more info see : [IRIS](https://archive.ics.uci.edu/ml/datasets/iris)

## Getting started

To be able to run these scripts we have a bit of setup to do first. Firstly we will need to have python installed you can get it here:

[Python](https://www.python.org/downloads/)

Once the download & installation of Python is finished we are ready to go!

You might need to install some dependencies.

Open a CMD / Terminal window on your system and type in the following:

##### Installing Jupyter Notebook

First, ensure that you have the latest pip; older versions may have trouble with some dependencies:

```pip3 install --upgrade pip```

Then install the Jupyter Notebook using:

```pip3 install jupyter```

For more informaton about Jupyter Notebook you can find it [HERE](http://jupyter.org/install.html)

##### Other Dependencies

1. Seaborn -> ```pip install seaborn```
2. Numpy -> ```pip install numpy```
3. MatPlotlib -> ```pip install matplotlib```
4. Scipy -> ```pip install scipy``` 

With that out of the way we can go to the directory of the project

```cd path/to/directory```

Once in the project directory we will use the following commands to run the scripts

```python iris.py```

This will run the python version of the script from the Command line or Terminal

Other wise we can view this using Jupyter Notebook

```jupyter notebook```

This will open a webpage where you can then view the irisDataSet.ipynb file

## Assignment Specification

### 1. Get and load the data

Search online for Fisher’s iris data set, find a copy of the data, download it and save it to your repository. If it is not in CSV format, use whatever means (Excel, notepad++, visual studio code, python) to convert it to CSV and save the CSV version to your repository also. Open your Jupyter notebook for this problem sheet, creating a new one if needed, and load the CSV file into a numpy array.

### 2. Write a note about the data set

In a markdown cell at the start of your notebook, write a short description of the iris data set, complete with references.

### 3. Create a simple plot

The dataset contains five variables: sepal length, sepal width, petal length, petal width, and species. Use pyplot to create a scatter plot of sepal length on the x-axis versus sepal width on the y-axis. Add axis labels and a title to the plot.

### 4. Create a more complex plot

Re-create the above plot, but this time plot the setosa data points in red, the versicolor data point in green, and the virginica data points in blue. Setosa, versicolor, and virginica are the three possible values of the species variable. Add a legend to the plot showing which species is in which colour.

### 5. Use seaborn

Use the seaborn library to create a scatterplot matrix of all five variables.

### 6. Fit a line

Fit a straight line to the variables petal length and petal width for the whole data set. Plot the data points in a scatter plot with the best fit line shown.

### 7. Calculate the R-squared value

Calculate the R-squared value for your line above.

### 8. Fit another line

Use numpy to select only the data points where species is setosa. Fit a straight line to the variables petal length and petal width. Plot the data points in a scatter plot with the best fit line shown.

### 9. Calculate the R-squared value

Calculate the R-squared value for your line above.

### 10. Use gradient descent

Use gradient descent to approximate the best fit line for the petal length and petal width setosa values. Compare the outputs to your calculations above.
