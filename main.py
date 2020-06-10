# main function
import numpy as numpy
import pandas as pd
from movies_shows_selection import *

def main():
    # asks the user if they want to sort through shows or movies
    choose_option = movies_or_shows()

    # depending on selection, either sorts through tv shows or movies
    if choose_option == 'movies':
        # sorting through movies
        choice_movies()
    else:
        #sorting through tv shows
        choice_shows()

if __name__ == '__main__':
    main()