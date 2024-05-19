#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo">
#     </a>
# </p>
# 
# 
# # Exploring and pre-processing a dataset using Pandas 
# 
# 
# Estimated time needed: **30** minutes
#     
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * Explore the dataset
# * Pre-process dataset as required (may be for visualization)
# 

# ## Introduction
# 
# The aim of this lab is to provide you a refresher on the **Pandas** library, so that you can pre-process and anlyse the datasets before applying data visualization techniques on it. This lab will work as acrash course on *pandas*. if you are interested in learning more about the *pandas* library, detailed description and explanation of how to use it and how to clean, munge, and process data stored in a *pandas* dataframe are provided in our course [**Data Analysis with Python**](https://www.coursera.org/learn/data-analysis-with-python?specialization=ibm-data-analyst) and [**Python for Applied Data Science**](https://www.coursera.org/learn/python-for-applied-data-science-ai?specialization=ibm-data-analyst)
# 
# ------------
# 

# ## Table of Contents
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 
# 1. [Exploring Datasets with *pandas*](#0)<br>
# 2. [The Dataset: Immigration to Canada from 1980 to 2013](#1)<br>
# 3. [*pandas* Basics](#2) <br>
# 4. [*pandas* Intermediate: Indexing and Selection](#3) <br>
# 5. [*pandas* Filtering based on a criteria](#4)<br>
# 6. [*pandas* Sorting Values](#5)
# 
# </div>
# 

# # Exploring Datasets with *pandas* <a id="0"></a>
# 
# *pandas* is an essential data analysis toolkit for Python. From their [website](http://pandas.pydata.org/):
# >*pandas* is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, **real world** data analysis in Python.
# 
# The course heavily relies on *pandas* for data wrangling, analysis, and visualization. We encourage you to spend some time and familiarize yourself with the *pandas* API Reference: http://pandas.pydata.org/pandas-docs/stable/api.html.
# 

# ## The Dataset: Immigration to Canada from 1980 to 2013 <a id="1"></a>
# 

# Dataset Source: [International migration flows to and from selected countries - The 2015 revision](https://www.un.org/development/desa/pd/data/international-migration-flows).
# 
# The dataset contains annual data on the flows of international immigrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals. The current version presents data pertaining to 45 countries.
# 
# In this lab, we will focus on the Canadian immigration data.
# 
# ![Data Preview](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%201/images/DataSnapshot.png)
# 
#  The Canada Immigration dataset can be fetched from <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx">here</a>.
# 
# ---
# 

# ## *pandas* Basics<a id="2"></a>
# 

# The first thing we'll do is install **openpyxl** (formerly **xlrd**), a module that *pandas* requires to read Excel files.
# 

# In[2]:


get_ipython().system('pip install mamba')


# Next, we'll do is import two key data analysis modules: *pandas* and *numpy*.
# 

# In[6]:


get_ipython().system('pip install openpyxl')
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# Let's download and import our primary Canadian Immigration dataset using *pandas*'s `read_excel()` method.
# 

# In[7]:


df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')


# Let's view the top 5 rows of the dataset using the `head()` function.
# 

# In[8]:


df_can.head()
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10) 


# We can also view the bottom 5 rows of the dataset using the `tail()` function.
# 

# In[9]:


df_can.tail()


# When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe. We can do this by using the `info()` method.
# 
# This method can be used to get a short summary of the dataframe.
# 

# In[10]:


df_can.info(verbose=False)


# To get the list of column headers we can call upon the data frame's `columns` instance variable.
# 

# In[11]:


df_can.columns


# Similarly, to get the list of indices we use the `.index` instance variables.
# 

# In[12]:


df_can.index


# Note: The default type of intance variables `index` and `columns` are **NOT** `list`.
# 

# In[13]:


print(type(df_can.columns))
print(type(df_can.index))


# To get the index and columns as lists, we can use the `tolist()` method.
# 

# In[14]:


df_can.columns.tolist()


# In[15]:


df_can.index.tolist()


# In[16]:


print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))


# To view the dimensions of the dataframe, we use the `shape` instance variable of it.
# 

# In[17]:


# size of dataframe (rows, columns)
df_can.shape


# **Note**: The main types stored in *pandas* objects are `float`, `int`, `bool`, `datetime64[ns]`, `datetime64[ns, tz]`, `timedelta[ns]`, `category`, and `object` (string). In addition, these dtypes have item sizes, e.g. `int64` and `int32`.
# 

# Let's clean the data set to remove a few unnecessary columns. We can use *pandas* `drop()` method as follows:
# 

# In[18]:


# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)


# Let's rename the columns so that they make sense. We can use `rename()` method by passing in a dictionary of old and new names as follows:
# 

# In[19]:


df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns


# We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013, as follows:
# 

# In[20]:


df_can['Total'] = df_can.sum(axis=1)
df_can['Total']


# We can check to see how many null objects we have in the dataset as follows:
# 

# In[21]:


df_can.isnull().sum()


# Finally, let's view a quick summary of each column in our dataframe using the `describe()` method.
# 

# In[22]:


df_can.describe()


# ---
# ## *pandas* Intermediate: Indexing and Selection (slicing)<a id="3"></a>
# 

# ### Select Column
# **There are two ways to filter on a column name:**
# 
# Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.
# ```python
#     df.column_name               # returns series
# ```
# 
# Method 2: More robust, and can filter on multiple columns.
# 
# ```python
#     df['column']                  # returns series
# ```
# 
# ```python 
#     df[['column 1', 'column 2']]  # returns dataframe
# ```
# ---
# 

# Example: Let's try filtering on the list of countries ('Country').
# 

# In[23]:


df_can.Country  # returns a series


# Let's try filtering on the list of countries ('Country') and the data for years: 1980 - 1985.
# 

# In[24]:


df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.


# ### Select Row
# 
# There are main 2 ways to select rows:
# 
# ```python
#     df.loc[label]    # filters by the labels of the index/column
#     df.iloc[index]   # filters by the positions of the index/column
# ```
# 

# Before we proceed, notice that the default index of the dataset is a numeric range from 0 to 194. This makes it very difficult to do a query by a specific country. For example to search for data on Japan, we need to know the corresponding index value.
# 
# This can be fixed very easily by setting the 'Country' column as the index using `set_index()` method.
# 

# In[25]:


df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()


# In[26]:


df_can.head(3)


# In[27]:


# optional: to remove the name of the index
df_can.index.name = None


# Example: Let's view the number of immigrants from Japan (row 87) for the following scenarios:
#     1. The full row data (all columns)
#     2. For year 2013
#     3. For years 1980 to 1985
# 

# In[28]:


# 1. the full row data (all columns)
df_can.loc['Japan']


# In[29]:


# alternate methods
df_can.iloc[87]


# In[30]:


df_can[df_can.index == 'Japan']


# In[31]:


# 2. for year 2013
df_can.loc['Japan', 2013]


# In[32]:


# alternate method
# year 2013 is the last column, with a positional index of 36
df_can.iloc[87, 36]


# In[33]:


# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]


# In[34]:


# Alternative Method
df_can.iloc[87, [3, 4, 5, 6, 7, 8]]


# **Exercise:** Let's view the number of immigrants from **Haiti** for the following scenarios: <br>1. The full row data (all columns) <br>2. For year 2000 <br>3. For years 1990 to 1995
# 

# In[35]:


df_can.loc['Haiti']
df_can.loc['Haiti', 2000]
df_can.loc['Haiti', [1990, 1991, 1992, 1993, 1994, 1995]]


# <details><summary>Click here for a sample python solution</summary>
# 
# ```python
#    # 1. the full row data (all columns)
#     df_can.loc['Haiti']
#     #or
#     df_can[df_can.index == 'Haiti']
# 
#     # 2. for year 2000
#     df_can.loc['Haiti', 2000]
#            
#     #  3. for years 1990 to 1995
#     df_can.loc['Haiti', [1990, 1991, 1992, 1993, 1994, 1995]]
#  ```
# 
# </details>
# 

# Column names that are integers (such as the years) might introduce some confusion. For example, when we are referencing the year 2013, one might confuse that when the 2013th positional index. 
# 
# To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.
# 

# In[36]:


df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers


# Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years:
# 

# In[37]:


# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years


# **Exercise:** Create a list named 'year' using map function for years ranging from 1990 to 2013. <br>Then extract the data series from the dataframe df_can for Haiti using year list. 
# 

# In[40]:


years = list(map(str, range(1990, 2014)))
Haiti= df_can.loc['Haiti', years]


# <details><summary>Click here for a sample python solution</summary>
# 
# ```python
#     #The correct answer is:
#     year = list(map(str, range(1990, 2014)))
#     haiti = df_can.loc['Haiti', year] # passing in years 1990 - 2013
#     
# ```
# </details>
# 

# ### Filtering based on a criteria <a id="4"></a>
# To filter the dataframe based on a condition, we simply pass the condition as a boolean vector. 
# 
# For example, Let's filter the dataframe to show the data on Asian countries (AreaName = Asia).
# 

# In[41]:


# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)


# In[42]:


# 2. pass this condition into the dataFrame
df_can[condition]


# In[43]:


# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses


# **Exercise:** Fetch the data where AreaName is 'Africa' and RegName is 'Southern Africa'. <br>Display the dataframe and find out how many instances are there?
# 

# In[ ]:





# <details><summary>Click here for a sample python solution</summary>
# 
# ```python
#     df_can[(df_can['Continent']=='Africa') & (df_can['Region']=='Southern Africa')]
# ```
# </details>
# 

# ### Sorting Values of a Dataframe or Series <a id="5"></a><br>
# You can use the `sort_values()` function is used to sort a DataFrame or a Series based on one or more columns. <br>You to specify the column(s) by which you want to sort and the order (ascending or descending). Below is the syntax to use it:-<br><br>
# ```df.sort_values(col_name, axis=0, ascending=True, inplace=False, ignore_index=False)```<br><br>
# col_nam - the column(s) to sort by. <br>
# axis - axis along which to sort. 0 for sorting by rows (default) and 1 for sorting by columns.<br>
# ascending - to sort in ascending order (True, default) or descending order (False).<br>
# inplace - to perform the sorting operation in-place (True) or return a sorted copy (False, default).<br>
# ignore_index - to reset the index after sorting (True) or keep the original index values (False, default).<br>
# 

# Let's sort out dataframe df_can on 'Total' column, in descending order to find out the top 5 countries that contributed the most to immigration to Canada. 
# 

# In[ ]:


df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
top_5 = df_can.head(5)
top_5


# **Exercise:** Find out top 3 countries that contributes the most to immigration to Canda in the year 2010. <br> Display the country names with the immigrant count in this year
# 

# In[ ]:





# <details><summary>Click here for a sample python solution</summary>
# 
# ```python
#     df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
#     top3_2010 = df_can['2010'].head(3)
#     top3_2010
# ```
# </details>
# 

# Congratulations! you have learned how to wrangle data with Pandas. You will be using alot of these commands to preprocess the data before its can be used for data visualization.
# 

# ### Thank you for completing this lab!
# 
# 
# ## Author
# 
# <a href="https://www.linkedin.com/in/aklson/" target="_blank">Alex Aklson</a>
# 
# 
# ### Other Contributors
# [Jay Rajasekharan](https://www.linkedin.com/in/jayrajasekharan),
# [Ehsan M. Kermani](https://www.linkedin.com/in/ehsanmkermani),
# [Slobodan Markovic](https://www.linkedin.com/in/slobodan-markovic),
# [Weiqing Wang](https://www.linkedin.com/in/weiqing-wang-641640133/),
# [Dr. Pooja](https://www.linkedin.com/in/p-b28802262/)
# 
# 
# ## Change Log
# 
# 
# |  Date (YYYY-MM-DD) | Version | Changed By    |  Change Description                   |
# |--------------------|---------|---------------|---------------------------------------|
# | 2023-06-08         | 2.5     | Dr. Pooja         |  Separated from original lab        |
# | 2021-05-29         | 2.4     | Weiqing Wang  |  Fixed typos and code smells.         |
# | 2021-01-20         | 2.3     | Lakshmi Holla |  Changed TOC cell markdown            |
# | 2020-11-20         | 2.2     | Lakshmi Holla |  Changed IBM box URL                  |
# | 2020-11-03         | 2.1     | Lakshmi Holla |  Changed URL and info method          |
# | 2020-08-27         | 2.0     | Lavanya       |  Moved Lab to course repo in GitLab   |
# 
# 
# 
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 

# In[ ]:




