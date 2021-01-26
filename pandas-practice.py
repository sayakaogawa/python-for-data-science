#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:50:38 2021

@author: sayaka.ogawa
"""

import pandas as pd

def series():
    
    data = pd.Series([2, 3, 4, 5], index=['a','b','c', 'd'])
    
    # explicit slicing, inclusive of last element
    data['a':'c']
    
    # implicit slicing, exclusive of last element
    data[0:2] 
    
    # passing a dictionary as series argument
    grades_dict = {'A':4, 'B':3.5, 'C':3, 'D':2.5}
    grades = pd.Series(grades_dict)
    
    marks_dict = {'A':85, 'B':75, 'C':65, 'D':55}
    marks = pd.Series(marks_dict)
    
    return grades, marks


def data_frame(grades, marks):
    
    # create a DataFrame passing the grades and marks series
    df = pd.DataFrame({'Marks':marks, 'Grades':grades})
    
    # transposing the dataframe
    df.T 
    
    # access values of the df - will not include indices
    df.values[2, 0] # access third row, first column value
    
    # accesses the indices for the columns
    df.columns
    
    # add column to df, just like a dictionary
    df['ScaledMarks'] = 100*(df['Marks']/90)
    
    # delete column
    del df['ScaledMarks']
    
    # access all data above a certain threshold
    df[df['Marks']>70]   # aka masking
    
    # NaN / None-type values - df with missing values.
    df2 = pd.DataFrame([{'a':1, 'b':4}, {'b':-3, 'c':9}])
    
    # fill NaN with 0s
    df2.fillna(0)
    
    # indexing
    df3 = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
    df3[1] # explicit index
    df3[1:3] # implicit index
    df3.loc[1:3] # explicit indices
    df3.iloc[1:3]    # impliict indices
    
    # implicit index for record at 2nd row, all columns
    df.iloc[2, :]
    
    # reverse all the rows, include all columns
    df.iloc[::-1, :]
    

def csv_files():
    """Learning how to load a data set and handling the data set. """
    
    # read in a csv file
    df = pd.read_csv('/Users/sayaka.ogawa/Desktop/python-for-data-science/covid_19_data.csv')

    # get the first several records at the top
    df.head()   # can specify the number of records
    
    # deleting columns. axis=1 indicates column, 
    # inplace tells to do this update to df itself.
    df.drop(['SNo', 'Last Update'], axis=1, inplace=True)
    
    # rename columns {before:after}
    df.rename(columns={'ObservationDate':'Date', 'Province/State':'Province',
                       'Country/Region':'Country'}, inplace=True)
    
    # reformat date to internal Pandas day format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # describe data
    df.describe()
    
    # info function that will tell you how many records for each column
    df.info()
    
    # fill empty cells with 'NA'
    df = df.fillna('NA')
    
    # see how many total confirmed cases and deaths in each country, take sum, and reset index
    df2 = df.groupby('Country')[['Country','Confirmed','Deaths']].sum().reset_index()
    
    # group by country and date, and see sum of confirmed cases
    df2 = df.groupby(['Country', 'Date'])[['Country','Date','Confirmed']].sum().reset_index()
    
    # find all records for which the confirmed cases are > 100
    df3 = df2[df2['Confirmed'] > 100]
    
    return df3
    

def main():
    
    # grades, marks = series()

    # dataframe = data_frame(grades, marks)
    
    # df = csv_files()
    
    
main()
    