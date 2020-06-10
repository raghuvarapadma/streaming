import numpy as numpy
import pandas as pd
from functions.basic_functions import *
from functions.user_selection import *

def movies_or_shows():
    while True:
        try:
            choice = input('Would you like to search for movies or TV shows? Search by Movies or Shows. ' )
        except:
            print('Please enter a valid response!')
            continue
        else:
            if choice.lower() == 'movies':
                print('You chose movies!')
                return choice
                break
            elif choice.lower() == 'shows':
                print('You chose TV shows!')
                return choice
                break
            else:
                print('Please enter a valid response!')
                continue

def choice_movies():
    data = pd.read_csv('MoviesOnStreamingPlatforms_updated.csv')
    data['Platform'] = data.apply(plat,axis=1)
    data.drop(columns=['Netflix','Hulu','Prime Video','Disney+','Type','Unnamed: 0','ID'],axis=1,inplace=True)
    data['Age'] = data['Age'].map({'18+':'NC-17','16+':'R','13+':'PG-13','7+':'PG','all':'G'})
    data['Age'] = data['Age'].fillna('NONE')
    data['Rotten Tomatoes'] = data['Rotten Tomatoes'].fillna(0.0)
    data['Rotten Tomatoes'] = data['Rotten Tomatoes'].apply(lambda x: int(x[:-1]) if x !=0 else 0)
    data['IMDb'] = data['IMDb'].fillna(0.0)
    data['Directors'] = data['Directors'].fillna('NONE')
    data['Genres'] = data['Genres'].fillna('NONE')
    data['Country'] = data['Country'].fillna('NONE')
    data['Language'] = data['Language'].fillna('NONE')
    data['Runtime'] = data['Runtime'].fillna(0.0)
    
    # array defining the paramters the user wants to go through
    parameters_user_search = []
    user_search_limits = {}
    
    # recursive function asking what parameters the user wants
    taking_input_movies(parameters_user_search,data)
    
    # entering in specific values and storing it in the dictionary
    value_input_dict(parameters_user_search,user_search_limits,data)
    for i in range(len(parameters_user_search)):
        if parameters_user_search[i] == 'Title':
            data = data[data['Title_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Title_TRUEFALSE',inplace=True)
        elif parameters_user_search[i] == 'IMDb':
            data = data[data['IMDb']>=user_search_limits[parameters_user_search[i]]]
        elif parameters_user_search[i] == 'Rotten Tomatoes':
            data = data[data['Rotten Tomatoes']>=user_search_limits[parameters_user_search[i]]]
        elif parameters_user_search[i] == 'Directors':
            data = data[data['Directors_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Directors_TRUEFALSE',inplace=True)
        elif parameters_user_search[i] == 'Genres':
            data = data[data['Genres_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Genres_TRUEFALSE',inplace=True)
        elif parameters_user_search[i] == 'Country':
            data = data[data['Country_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Country_TRUEFALSE',inplace=True)
        elif parameters_user_search[i] == 'Language':
            data = data[data['Language_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Language_TRUEFALSE',inplace=True)
        elif parameters_user_search[i] == 'Runtime':
            data = data[data['Runtime']<=user_search_limits[parameters_user_search[i]]]
        elif parameters_user_search[i] == 'Platform':
            data = data[data['Platform_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Platform_TRUEFALSE',inplace=True)
        else:
            data = data[data[parameters_user_search[i]]==user_search_limits[parameters_user_search[i]]]
    
    sort_data = sorting_data_movies(data)
    data.sort_values(sort_data,axis=0,ascending=False,inplace=True)
    
    data['IMDb'] = data['IMDb'].replace(0.0,'NONE')
    data['Rotten Tomatoes'] = data['Rotten Tomatoes'].replace(0,'NONE')
    data['Runtime'] = data['Runtime'].replace(0.0,'NONE')
    
    data.set_index('Title',inplace=True)
    
    data_to_csv(data)
    
    print(data)
    
    
def choice_shows():
    data = pd.read_csv('tv_shows.csv')
    data['Platform'] = data.apply(plat,axis=1)
    data.drop(columns=['Netflix','Hulu','Prime Video','Disney+','type','Unnamed: 0'],axis=1,inplace=True)
    data['Age'] = data['Age'].map({'18+':'TV-MA','16+':'TV-MA','13+':'TV-14','7+':'TV-PG','all':'TV-Y'})
    data['Age'] = data['Age'].fillna('NONE')
    data['Rotten Tomatoes'] = data['Rotten Tomatoes'].fillna(0.0)
    data['Rotten Tomatoes'] = data['Rotten Tomatoes'].apply(lambda x: int(x[:-1]) if x !=0 else 0)
    data['IMDb'] = data['IMDb'].fillna(0.0)
    
    # array defining the paramters the user wants to go through
    parameters_user_search = []
    user_search_limits = {}
    
    # recursive function asking what parameters the user wants
    taking_input_shows(parameters_user_search,data)
    
    # entering in specific values and storing it in the dictionary
    value_input_dict(parameters_user_search,user_search_limits,data)
    for i in range(len(parameters_user_search)):
        if parameters_user_search[i] == 'Title':
            data = data[data['Title_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Title_TRUEFALSE',inplace=True)
        elif parameters_user_search[i] == 'IMDb':
            data = data[data['IMDb']>=user_search_limits[parameters_user_search[i]]]
        elif parameters_user_search[i] == 'Rotten Tomatoes':
            data = data[data['Rotten Tomatoes']>=user_search_limits[parameters_user_search[i]]]
        elif parameters_user_search[i] == 'Platform':
            data = data[data['Platform_TRUEFALSE']==user_search_limits[parameters_user_search[i]]]
            data.drop(columns='Platform_TRUEFALSE',inplace=True)
        else:
            data = data[data[parameters_user_search[i]]==user_search_limits[parameters_user_search[i]]]
            
    sort_data = sorting_data_shows(data)
    data.sort_values(sort_data,axis=0,ascending=False,inplace=True)
    
    data['IMDb'] = data['IMDb'].replace(0.0,'NONE')
    data['Rotten Tomatoes'] = data['Rotten Tomatoes'].replace(0,'NONE')
    
    data.set_index('Title',inplace=True)
    
    data_to_csv(data)
    
    print(data)