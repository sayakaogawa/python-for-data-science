#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:35:42 2021

Using Numpy, Pandas, and Matplotlib to analyze COVID-19 data.

Project: COVID-19 Trend Analysis
@author: sayaka.ogawa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

def read_file(path):
    
    df = pd.read_csv(path)
    
    return df


def clean_data(df):
    
    df.drop(['SNo','Last Update'], axis=1, inplace=True)
    df.rename(columns={'ObservationDate':'Date',
                       'Province/State':'State',
                       'Country/Region':'Country'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # imputer with constant strategy.
    imputer = SimpleImputer(strategy='constant')
    
    # impute all missing values by the constant strategy of the imputer
    df2 = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    
    # group by country and date, find sum of all all columns, and reset index
    df3 = df2.groupby(['Country','Date'])[['Country','Date','Confirmed','Deaths','Recovered']].sum().reset_index()
    
    return df3


def country_data(df):
    
    countries = df['Country'].unique()
    l = len(countries)
    
    # find trend in confirmed, deaths, and recovered cases with respect to the date
    # find and plot data for each country's trend
    for i in range(0,l):
        # find indices for country at i
        c = df[df['Country']==countries[i]].reset_index()
        
        # create a new plot each iteration.
        plt.figure()
        
        plt.scatter(np.arange(0,len(c)), c['Confirmed'],
                    color='blue', label='Confirmed')
        plt.scatter(np.arange(0,len(c)), c['Recovered'],
                    color='green', label='Recovered')
        plt.scatter(np.arange(0,len(c)), c['Deaths'],
                    color='red', label='Deaths')
        
        # format title and axis labels
        plt.title(countries[i])
        plt.xlabel('Days since the first case')
        plt.ylabel('Number of cases')
        
        # add legend
        plt.legend()
        
    # show all plots after all iterations
    plt.show
    

def world_data(df):
    
    df = df.groupby(['Date'])[['Date', 'Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
    
    plt.scatter(np.arange(0,len(df)), df['Confirmed'],
                color='blue', label='Confirmed')
    plt.scatter(np.arange(0,len(df)), df['Recovered'],
                color='green', label='Recovered')
    plt.scatter(np.arange(0,len(df)), df['Deaths'],
                color='red', label='Deaths')
    plt.title('World')
    plt.xlabel('Days since first case')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()
    

def main():
    
    path = '/Users/sayaka.ogawa/Desktop/python-for-data-science/covid_19_data.csv'
    file = read_file(path)
    df = clean_data(file)
    # country_data(df)
    world_data(df)
    

main()
