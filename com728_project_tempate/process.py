"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 24 - 28: Write suitable functions to process the data as follows:

Retrieve the total number of movies
Retrieve an individual movie
Retrieve specific data for an individual movie
Retrieve all movies for a specified release year
Retrieve all movies in the specified genres

Each function for the above should follow the pattern below:
- Take a list of movies (where a movie is a list of data values) as a parameter.
- You may name this parameter records.
- Process the list of movies appropriately.  You may use the module tui to retrieve any 
additional information required to complete the processing.
- Return a suitable result
 
"""

# TODO: Your code here

import tui


def total_num_of_movies(records):
    tui.total_movies(len(records))

def individual_movie(records):
    name = tui.movie_name()
    for movies in range(len(records)):
        if records == name:
            tui.display_movie(records)

def specific_individual_movie(records):
    name, cols = tui.movie_details()
    for i in range(len(records)):
        if records[i][1] == name:
            tui.display_movie(records[i], cols)

def specific_release_year(records):
    year = tui.movie_year()

    for i in range(len(records)):
        if records[i][3] == year:
            tui.movie_year.append(records[i])
            tui.display_movies()


def specific_genre(records):
    genre = tui.movie_genres()
    for i in range(len(records)):
        if (len(records [4])):
            tui.movie_genres.append(records)

    tui.display_movies()