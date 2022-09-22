import os, sys, urllib, requests, json, pytest, collections, functools, datetime, re


class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.file_path = path_to_the_file

    def get_generator_file(self):
        try:
            with open(self.file_path, 'r') as file:
                for row in file:
                    yield row
        except OSError as e:
            print(f'ERROR: {e}')


    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        release_years = {}
        for row in self.get_generator_file():
            year = re.search(r'(\d\d\d\d)', row)[0]
            if year in release_years:
                release_years[year] += 1
            else:
                release_years[year] = 0
            pass
        return release_years
    
    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """
        return genres
        
    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        return movies


# for i in Movies('ml-latest-small/movies.csv').get_generator_file():
#     print(i)