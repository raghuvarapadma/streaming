# adds in Platform column into datatable which represents on what platforms the show or movie is availble on
def plat(row):
    string = ''
    if row['Netflix'] == 1:
        if string == '':
            string+='Netflix'
        else:
            string+=',Netflix'
    if row['Hulu'] == 1:
        if string == '':
            string+='Hulu'
        else:
            string+=',Hulu'
    if row['Prime Video'] == 1:
        if string == '':
            string+='Prime Video'
        else:
            string+=',Prime Video'
    if row['Disney+'] == 1:
        if string == '':
            string+='Disney+'
        else:
            string+=',Disney+'
    return string

def taking_input_movies(user_arr,data):
    while True:
        try:
            param = input('Which parameter would you like to search by? Search by Title, Year, Age, Rating, Directors, Genres, Country, Language, Runtime, Platform. ')
        except TypeError:
            print('Please input a valid answer!')
            continue
        else:
            if (param in data.columns) or (param == 'Rating'):
                user_arr.append(param)
                while True:
                    try:
                        repeat = input('Would you like to search for another parameter? ')
                    except TypeError:
                        print('Please input an integer!')
                        continue
                    else:
                        if repeat.lower() == 'yes':
                            return taking_input_movies(user_arr,data)
                            break
                        elif repeat.lower() == 'no':
                            return user_arr
                            break
                        else:
                            print('Please enter a valid input!')
                            continue
            else:
                print('Please enter a valid input!')
                continue
    return user_arr

def taking_input_shows(user_arr,data):
    while True:
        try:
            param = input('Which parameter would you like to search by? Search by Title, Year, Age, Rating, Platform. ')
        except TypeError:
            print('Please input a valid answer!')
            continue
        else:
            if (param in data.columns) or (param == 'Rating'):
                user_arr.append(param)
                while True:
                    try:
                        repeat = input('Would you like to search for another parameter? ')
                    except TypeError:
                        print('Please input an integer!')
                        continue
                    else:
                        if repeat.lower() == 'yes':
                            return taking_input_shows(user_arr,data)
                            break
                        elif repeat.lower() == 'no':
                            return user_arr
                            break
                        else:
                            print('Please enter a valid input!')
                            continue
            else:
                print('Please enter a valid input!')
                continue
    return user_arr

def sorting_data_movies(data):
    while True:
        try:
            param = input('Which parameter would you like to sort the data by? Search by Title, Year, Age, IMDb, Rotten Tomatoes, Directors, Genres, Country, Language, Runtime, Platform. ')
        except TypeError:
            print('Please input a valid answer!')
            continue
        else:
            if param in data.columns:
                return param
                break
            else:
                print('Please input a valid answer!')
                continue

def sorting_data_shows(data):
    while True:
        try:
            param = input('Which parameter would you like to sort the data by? Search by Title, Year, Age, IMDb, Rotten Tomatoes, Platform. ')
        except TypeError:
            print('Please input a valid answer!')
            continue
        else:
            if param in data.columns:
                return param
                break
            else:
                print('Please input a valid answer!')
                continue
                
def data_to_csv(data):
    while True:
            try:
                copy = input('Do you want to copy to a .csv file? ')
            except:
                print('Please enter a valid input!')
            else:
                if copy.lower() == 'yes':
                    print('Here is your .csv file!')
                    data.to_csv('Movies and Streaming.csv')
                    break
                elif copy.lower() == 'no':
                    print('You did not want to convert to a .csv file!')
                    break
                else:
                    print('Please enter a valid input!')
                    continue