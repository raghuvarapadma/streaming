# sets specific values of parameters entered by user
def value_input_dict(user_arr,user_dict, data):
    if 'Title' in user_arr:
        title_value(user_dict, data)
    if 'Year' in user_arr:
        year_value(user_dict, data)
    if 'Age' in user_arr:
        age_value(user_dict, data)
    if 'Rating' in user_arr:
        rating_value(user_arr,user_dict, data)
    if 'Directors' in user_arr:
        directors_value(user_dict, data)
    if 'Genres' in user_arr:
        genres_value(user_dict, data)
    if 'Country' in user_arr:
        country_value(user_dict, data)
    if 'Language' in user_arr:
        language_value(user_dict, data)
    if 'Runtime' in user_arr:
        runtime_value(user_dict, data)
    if 'Platform' in user_arr:
        platform_value(user_dict, data)
        
def title_value(user_dict, data):
    while True:
        try:
            title = input("What show/movie are you looking for? ")
        except:
            print("Please enter a valid movie!")
            continue
        else:
            data['Title_TRUEFALSE'] = data['Title'].str.contains(title)
            user_dict['Title'] = True
            break
            
def year_value(user_dict, data):
    while True:
        try:
            year = int(input('What year do you want search shows/movies from? '))
        except TypeError:
            print("Please enter a valid year!")
            continue
        else:
            if year not in data['Year'].values.tolist():
                print("Please enter a valid year!")
                continue
            else:
                print("You chose " + str(year) + "!")
                user_dict['Year'] = year
                break
                
def age_value(user_dict, data):
    while True:
        try:
            age = input('What is the age rating of the shows/movies you are seeking for? ')
        except TypeError:
            print('Please enter a valid rating!')
            continue
        else:
            if age not in data['Age'].values.tolist():
                print('Please enter a valid age rating!')
                continue
            else:
                print('You chose ' + age + " movies!")
                user_dict['Age'] = age
                break
                
def rating_value(user_arr,user_dict, data):
    while True:
        try:
            rating_sys = input('What system do you want to use to evaluate the rating of the shows/movies? Choose IMDb or Rotten Tomatoes. ')
        except TypeError:
            print('Please enter a valid rating system!')
            continue
        else:
            if (rating_sys == 'Rotten Tomatoes') or (rating_sys == 'IMDb'):
                while True:
                    try:
                        rating = float(input('What rating would you like your movie to meet? '))
                    except TypeError:
                        print('Please enter a valid rating!')
                        continue
                    else:
                        if rating_sys == 'Rotten Tomatoes':
                            if (rating > 100):
                                print('Please enter a valid rating input!')
                                continue
                            else:
                                print('You chose to use the ' + rating_sys + ' system!')
                                print('You would like the rating of your movie to be greater than or equal to ' + str(rating) + '!')
                                index = user_arr.index('Rating')
                                user_dict[rating_sys] = rating
                                user_arr.insert(index,'Rotten Tomatoes')
                                user_arr.pop(index+1)
                                break
                        elif rating_sys == 'IMDb':
                            if (rating > 10):
                                print('Please enter a valid rating input!')
                                continue
                            else:
                                print('You chose to use the ' + rating_sys + ' system!')
                                print('You would like the rating of your movie to be greater than or equal to ' + str(rating) + '!')
                                index = user_arr.index('Rating')
                                user_dict[rating_sys] = rating
                                user_arr.insert(index,'IMDb')
                                user_arr.pop(index+1)
                                break
                break
            else:
                print('Please enter a valid rating system!')
                continue
                
def directors_value(user_dict,data):
    while True:
        try:
            director = input('Please enter the name of the director you would like to search for. ')
        except:
            print('Please enter a valid input!')
            continue
        else:
            data['Directors_TRUEFALSE'] = data['Directors'].str.contains(director)
            user_dict['Directors'] = True
            break
            
def genres_value(user_dict,data):
    while True:
        try:
            genre = input('Please enter the genre of the movie you would like to search for. ')
        except:
            print('Please enter a valid input!')
            continue
        else:
            data['Genres_TRUEFALSE'] = data['Genres'].str.contains(genre)
            user_dict['Genres'] = True
            break
            
def country_value(user_dict,data):
    while True:
        try:
            country = input('Please enter the country of the movie you would like to search for. ')
        except:
            print('Please enter a valid input!')
            continue
        else:
            data['Country_TRUEFALSE'] = data['Country'].str.contains(country)
            user_dict['Country'] = True
            break

def language_value(user_dict,data):
    while True:
        try:
            language = input('Please enter the language of the movie you would like to search for. ')
        except:
            print('Please enter a valid input!')
            continue
        else:
            data['Language_TRUEFALSE'] = data['Language'].str.contains(language)
            user_dict['Language'] = True
            break
            
def runtime_value(user_dict,data):
    while True:
        try:
            runtime = int(input('Please enter the maximum runtime of the movie you would like to search for. '))
        except:
            print('Please enter a valud input!')
            continue
        else:
            max_runtime=int(data['Runtime'].max())
            if (runtime > max_runtime):
                print('Please enter a valid runtime value!')
                continue
            elif (runtime < 0):
                print('Please enter a valud runtime value!')
            else:
                print('The maximum runtime you chose for your movie is ' + str(runtime) + '!')
                user_dict['Runtime'] = runtime
                break
            
def platform_value(user_dict,data):
    while True:
        try:
            platform = input('Please enter the platform of the shows/movies you would like to watch. ')
        except:
            print('Please enter a valid input!')
            continue
        else:
            data['Platform_TRUEFALSE'] = data['Platform'].str.contains(platform)
            user_dict['Platform'] = True
            break