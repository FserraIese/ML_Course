### Assignment 1

#### Introduction

The file `airbnb.csv` contains data on the Airbnb listings in New York City: the host identification, a short description, the neighborhood, the price and other attributes. The data can be imported to a Pandas data frame using the function `read_csv`. Using the Pandas tools for data analysis, you have to address the following questions.

#### Questions

1. The attribute `host_since` is the date of the host's first listing in Airbnb. How can you count the listings whose host started before 2010? And the hosts that started before that year? Note that this column has been imported to string data type, but an expression like `host_since < '2010-01-01'` still makes sense, so you don't need to change the data type.

2. What is the proportion of listings whose rating is missing? Note that some of the columns of your data frame contain `NaN` values. These values are created every time that `read_csv` finds a missing value in the data file. The corresponding column is imported then as `float`, even if the input data do not have decimals. By applying `isna()` to any Pandas series, you can create a boolean series (`True`/`False`) which can be used to count the missing values.

3. Use a histogram to explore the distribution of the price. Is it useful? Not much, because some very expensive listings distort the whole picture. How can you trim the data, dropping the most expensive listings, to get a better picture?

4. What is the average price per room type? Given that the distribution of the price is quite skewed, Is it better to use the median?

5. Explore the variation of median price across neighborhoods using a two-way pivot table.

6. Some of the combinations of room type and neighbourhood can have a small number of observations, so these statistics may not be informative. In your pivot table, replace the median price by number of listings, to find the rare combinations.

#### Submission

1. Submit a text file containing the responses to these questions and the Python code used to respond every question.

2. Put your name on top of the document.

#### Deadline

February 2 (Sunday), 24:00.
