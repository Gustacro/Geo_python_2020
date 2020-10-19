#!/usr/bin/env python
# coding: utf-8

# # Exercise 6 - Data analysis with Pandas
#
# In this week's exercise we will continue developing our skills using Pandas to analyze climate data.
#
# After making your changes, you will need to upload your changes to GitHub.
# The answers to the questions in this week's exercise should be given by modifying the document in the requested places.
#
# If you are uncertain about **the style of your code**, take a look at the **[PEP 8 - Style guide for Python code](https://www.python.org/dev/peps/pep-0008/)**.
#
#  - **Exercise 6 is due by 16:00 on 17.10.**
#  - Don't forget to check out the [hints for this week's exercise](https://geo-python.github.io/2018/lessons/L6/exercise-6.html) if you're having trouble.
#  - Scores on this exercise are out of 20 points.
#  - There are altogether 3 problems that you should solve. The fourth problem is optional (Problem 4) for more advanced students (does not affect grading)
#
# ## Data
#
# For problems 1-3 in this exercise we will be using climate data from the Helsinki-Vantaa airport station.
# For these problems, we have daily observations obtained from the [NOAA Global Historical Climatology Network](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND).
# The file was downloaded using the "Custom GHCN-Daily Text" output format, including following attributes:
#
# | Attribute                | Description                      |
# |--------------------------|----------------------------------|
# | `STATION`                | Unique ID of the weather station |
# | `ELEVATION`              | Elevation of the station         |
# | `LATITUDE` , `LONGITUDE` | Coordinates of the station       |
# | `DATE`                   | Date of the measurement          |
# | `PRCP`                   | Precipitation                    |
# | `TAVG`                   | Average temperature              |
# | `TMAX`                   | Maximum temperature              |
# | `TMIN`                   | Minimum temperature              |
#
# The file for this problem is exactly as available from the NOAA website. You can take a [look of the data](data/1091402.txt).
#
# **Note**: once again that temperatures in this dataset are given in degrees Fahrenheit.
#
# Additional information about the data format can be found in the [hints for Exercise 6](https://geo-python.github.io/2018/lessons/L6/exercise-6-hints.html).
#

# # Problem 1 - Reading in a tricky data file (5 points)
#
# #### Overview
#
# You first task for this exercise is to read in the data file (`data/1091402.txt`) to a variable called **`data`**.
# This should be done using the `read_csv()` -function in Pandas, and the resulting DataFrame should have the following attributes:
#
#   - The numerical values for rainfall and temperature read in as numbers
#   - The second row of the datafile should be skipped, but the text labels for the columns should be from the first row
#   - The no-data values (assigned with value **`-9999`**) should properly be converted to `NaN`
#
# After successfully reading the data file, you should find answers programmably to specific questions below, and upload your notebook to **your own repository** for this week's exercise.
#
# You can find hints about how to do these things in the [description of Exercise 5 Problem 1](https://github.com/Geo-Python-2018/Exercise-5/blob/master/Pandas/Exercise-5-problem1.ipynb) and the [hints for Exercise 6](https://geo-python.github.io/2018/lessons/L6/exercise-6.html).
#

# 1. Read the file into variable **data**
#    - Skip the second row
#    - Convert the no-data values into `NaN` (values -9999)

# In[1]:


# YOUR CODE HERE
# raise NotImplementedError()
import pandas as pd


# In[2]:


fp = r"data/1091402.txt"
data = pd.read_csv(fp, sep='\s+', skiprows=[1], na_values=-9999) # sep= '\s+' means that the data is separeted by 1 single white space or more.

# Data columns
print(data.columns)
# dataframe shape
print(data.shape)


# In[3]:


# Test print that should work
print(data.head(1))


# - How many no-data values (NaN) are there for **`TAVG`**?
#   - Assign your answer into a variable called **`tavg_nodata_count`**
#

# In[4]:


# How many no-data values?
tavg_nodata_count = data.TAVG.isna().sum() # isna() search for NaN values, sum() wil sum those values together
# YOUR CODE HERE
# raise NotImplementedError()


# In[5]:


# This test print should print a number
print(tavg_nodata_count)


# - How many no-data values (NaN) are there for `TMIN`?
#   - Assign your answer into a variable called **`tmin_nodata_count`**
#

# In[6]:


# How many no-data values?
tmin_nodata_count = data['TMIN'].isna().sum()

# YOUR CODE HERE
# raise NotImplementedError()


# In[7]:


# This test print should print a number
print(tmin_nodata_count)


# - How many days total are covered by this data file?
#   - Assign your answer into a variable called **`day_count`**
#

# In[8]:


# How many days?
day_count = data.DATE.count() # count() will coint the number of dates in the data set

# YOUR CODE HERE
# raise NotImplementedError()


# In[9]:


# This test print should print a number
print(day_count)


# - When was the first observation made (i.e. the oldest)?
#   - Assign your answer into a variable called **`first_obs`**
#

# In[10]:


# YOUR CODE HERE
# raise NotImplementedError()
# Sort the data in ascending order
data = data.sort_values(by = 'DATE', ascending = True)

# Use iloc[<index_num>, dataframe.columns.get_loc(<'column'>)] to return the value of specific column cell
# first_obs = data.iloc[0, data.columns.get_loc('DATE')]
first_obs = data['DATE'].min()


# In[11]:


# This test print should print a number
print(first_obs)


# - When was the last observation made (i.e. the most recent)?
#   - Assign your answer into a variable called **`last_obs`**

# In[12]:


# YOUR CODE HERE
# raise NotImplementedError()

# Sort the data in descending order
# last_obs = data.sort_values(by='DATE', ascending=False).iloc[0, data.columns.get_loc('DATE')] # all in one column
last_obs = data['DATE'].max()


# In[13]:


# This test print should print a number
print(last_obs)


# - What was the average temperature of the whole data file (all years)?
#   - Assign your answer into a variable called **`avg_temp`**

# In[14]:


# YOUR CODE HERE
# raise NotImplementedError()
avg_temp = data.TAVG.mean()


# In[15]:


# This test print should print a number
print(avg_temp)


# - What was the **`TMAX`** temperature of the ``Summer 69`` (i.e. including months May, June, July, August of the year 1969)?
#   - Assign your answer into a variable called **`avg_temp_69`**

# In[16]:


# YOUR CODE HERE
# raise NotImplementedError()

# define condition for DATE column in order to filter the data in the dataframe
avg_temp_69 = data.loc[(data.DATE >= 19690501) & (data.DATE<= 19690831)]

# Asign the  mean value of column TAVG to a variable
avg_temp_69 = avg_temp_69.TAVG.mean()


# In[17]:


# This test print should print a number
print(avg_temp_69)


# # Problem 2 - Calculating monthly average temperatures (7.5 points)
#
# For this problem your goal is to calculate monthly average temperature values in degrees Celsius from the daily values we have in the data file. You can use the approaches taught in Lessons 4,5 and 6 to solve this.
# You can again consult the [hints for Exercise 6](https://geo-python.github.io/2018/lessons/L6/exercise-6-hints.html) if you are stuck.
#
# **You can continue working with the same data that you used in Problem 1.**
#
# #### For this problem you should modify:
#
# 1. Calculate the monthly average temperatures for the entire data (i.e. for each year separately) file using the approach taught in the lecture.
#     - You should store the average temperatures into a new Pandas DataFrame called **`monthly_data`**.
# 2. Create a new column called **`temp_celsius`** into the **`monthly_data`** DataFrame that has the monthly temperatures in Celsius.
#    - Store also the information about the date into column **`DATE_m`** (which should be a string column with month and year info) and the **`TAVG`** values into the `monthly_data` DataFrame.
# 3. Update and commit your changes to the notebook in your **own repository** of this week's exercise.

# In[18]:


# Print first five rows of the dataframe to review the structure of it
data.head()


# In[19]:


# YOUR CODE HERE
# raise NotImplementedError()

# Create year-month, month columns
data['YM'] = (data['DATE'].astype(str)).str.slice(start=0, stop= 6)
data['monthNumber'] = (data['DATE'].astype(str)).str.slice(start=4, stop= 6)

# print head of the new column
print(data['YM'].head())

# Check the data type for the column 'DATE_m' is string
print('\nData type of the column YM is:')
print(type(data.iloc[0, data.columns.get_loc('YM')]))


# In[20]:


# Crete function to convert Fahrenheits to Celsuis
def fahrToCelsius(temp_fahrenheit):
    """
    Function to convert Fahrenheit temperature into Celsius.

    Parameters
    ----------

    temp_fahrenheit: int | float
        Input temperature in Fahrenheit (should be a number)

    Returns
    -------

    Temperature in Celsius (float)
    """

    # Convert the Fahrenheit into Celsius and return it
    converted_temp = (temp_fahrenheit - 32) / 1.8
    return converted_temp



# In[21]:


""" Create a new column called temp_celsius containing monthly temperatures in Celsius """
# Convert Temperatures to Celsius
data['TAVG_Celsius'] = fahrToCelsius(data['TAVG'])

# In[22]:


# Create a new empty Dataframe
monthly_data = pd.DataFrame()


# Ahaa! As we can see, a single group contains a **DataFrame** with values only for that specific month.
# This is really useful, because now we can calculate e.g. the average values for all weather measurements (+ month or even hour if we want to) that we have (you can use any of the statistical functions that we have seen already, e.g. mean, std, min, max, median, etc.).
#
# We can do that by using the **`mean()`** -function that we already used during the Lesson 5.
#
# - Let's calculate the mean for following attributes (let's see how to do them all at once!):
#    - ``PRCP``,
#    - ``TAVG``,
#    - ``TMAX``,
#    - ``TMIN``,
#    - ``Celsius``.

# <b>Great!...</b>
#
# Let's add these values to the dataframe created a few steps above.

# In[23]:
monthlyData = pd.DataFrame() # Create empty dataframe

grouped_month = data.groupby('YM') # Group data dataframe by 'YM' column

# Aggregate data
for key, group in grouped_month: # Iterate over dataframe
    mean_value = group[['TAVG_Celsius']].mean() # Calculate mean() value for columns
    mean_value['YM'] = key # Define key as new column 'YM'
    mean_value['monthNumber'] = key[4:6] # Define new column 'monthNumber'
    monthlyData = monthlyData.append(mean_value, ignore_index=True) # append new columns to dataframe


monthlyData = monthlyData[['YM', 'monthNumber', 'TAVG_Celsius']] # re-organize dataframe

monthlyData.head()



# # Problem 3 - Calculating temperature anomalies (7.5 points)
#
# Our goal in this problem is to calculate monthly temperature anomalies in order to see how temperatures have changed over time, relative to the observation period between 1952-1980.
#
# We will again continue working with this same notebook.
#
# In order to complete the problem, you must do following things:
#
# - You need to calculate a mean temperature ***for each month*** over the period 1952-1980 using the data in the data file.
#  As a result, you should end up with 12 values, 1 mean temperature for each month in that period, and store them in a new Pandas DataFrame called **`reference_temps`**.
#    - The columns in the new DataFrame should be titled `Month` and `ref_temp`.
#
# For example, your `reference_temps` data should be something like that below, 1 value for each month of the year (12 total):
#
# | Month    | ref_temp         |
# |----------|------------------|
# | 01       | -5.350916        |
# | 02       | -5.941307        |
# | 03       | -2.440364        |
# | ...      | ...              |
#
# *Remember, these temperatures should be in degrees Celsius.*
#
# - Once you have the monthly mean values for each of the 12 months, you can then calculate a temperature anomaly for every month in the `monthly_data` DataFrame.
# - The temperature anomaly we want to calculate is simply the temperature for one month in `monthly_data` (`temp_celsius` -column) minus the corresponding monthly reference temperature in `ref_temp` column of `reference_temps` DataFrame.
#     - Hint: You need to make a table join (see hints for this week)
# - You should thus end up with three new columns in the `monthly_data` DataFrame:
#
#     1. **`Diff`**  showing the temperature anomaly, the difference in temperature for a given month (e.g., February 1960) compared to the average (e.g., for February 1952-1980),
#     2. **`Month`** indicating the month, and
#     3. **`ref_temp`** indicating the (monthly) reference temperature.
# - Update and commit your changes to the notebook in your **own repository** of this week's exercise.
#

# ### Get the month from the year_month column called **`data['DATE_m']`**

# In[24]:


# # Create a datetype column
# data['DATE_datetime'] = pd.to_datetime(data['DATE'], format='%Y%m%d')

# # Create datatime index
# timeindex = pd.DatetimeIndex(data['DATE_datetime'])

# # Create copy Dataframe with certain columns
# monthlyData = pd.Series(list(data['TAVG']), index= timeindex)

# # Resample by month
# ts = monthlyData.resample('1M',).mean()

# print(ts.head())


# In[25]:


# Create months dictionary
months_dict = pd.DataFrame({'monthNumber': ['01','02','03','04','05','06','07','08','09','10','11','12']
                            ,'month': ['January','February','March','April','May','June','July','August','September','October','November','December']})

# Choose period
period = data.loc[data['DATE']<19810101]

# Reset index for period
period = period.reset_index(drop=True)


# In[26]:
# Create a empty dataframe
referenceTemps = pd.DataFrame()

# Group by month
grouped_period = period.groupby('monthNumber')

# Iterate over groups
for key, group in grouped_period:
    row = group[['TAVG_Celsius']].mean()
    row['monthNumber'] = key
    referenceTemps = referenceTemps.append(row, ignore_index= True)

# Rename columns
referenceTemps = referenceTemps.rename(columns= {'TAVG_Celsius': 'avgTempsC'})


# In[27]:
referenceTemps.head()
monthlyData.head()


# In[28]:

# Merge columns
referenceTemps = referenceTemps.merge(months_dict, on= 'monthNumber')

# Join monthyData and referenceTemps

monthlyData = monthlyData.merge(referenceTemps, how= 'left', on='monthNumber', sort=False) # NOT WORKING

# Compare temperatures
monthlyData['Diff'] = monthlyData['TAVG_Celsius'] - monthlyData['avgTempsC']



# In[32]:


print(f'MonthlyData sample:\n{monthlyData.head()}')
# monthlyData.columns


# In[ ]:





# ### <i>Let's filter the data to be only between 1952 and 1980...</i>

# Now we can see that we have a new dataframe called 'reference_month', a new object called grouped with type **`DataFrameGroupBy`**. it contains 12 individual groups in the data. <b>One group for each month</b>
#
# Let's see what we have on month grouped variable. on the first month **`01`**. we can get the value of the month from the **`DataFrameGroupBy`** -object with **`get_group()`** function

# Great... we can see that a single group contains a <b>DataFrame</b> with values only for a specific month. now we can calculate the average values for all weather mesurenments (+ month) that we have
#
# Let's caluclate all the mean values for all the groups (1 months per group) for all those weather attributes that we were interested that are between 1952 and 1980.

# In[31]:


# lets print a sample of both dataframes
print('\n', (monthlyData.dtypes))

print('\n', referenceTemps.dtypes)


# - What is the highest value in `Diff` column?
#    - Print the answer in the cell below

# In[ ]:





# #### Done!
#
# That's it. Now you are ready with Problems 1-3. If you want, you can still continue with an optional [Problem 4.](Exercise-6-problem-4.ipynb)
