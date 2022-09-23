import re


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
                file.readline()
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
            year = re.search(r'\(\d\d\d\d[^,]', row)[0][1:5] \
                    if re.search(r'\(\d\d\d\d[^,]', row) != None else None
            if year in release_years:
                release_years[year] += 1
            else:
                release_years[year] = 1
        release_years = dict(sorted(release_years.items(), key=lambda x: x[1], reverse=True))
        return release_years
    
    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
        Sort it by counts descendingly.
        """
        genres = {}
        for row in self.get_generator_file():
            genres_list = row.split(',')[-1].split('|')
            for genre in genres_list:
                genre = genre.strip()
                if genre in genres:
                    genres[genre] += 1
                else:
                    genres[genre] = 1
        genres = dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))
        return genres
        
    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        movies = {}
        for row in self.get_generator_file():
            row = row.split(',')
            genres_count = len(row[-1].split('|'))
            title = row[1]
            movies[title] = genres_count
        movies = dict(sorted(movies.items(), key=lambda x: x[1], reverse=True)[:n])
        return movies


# if __name__ == '__main__':
#     obj = Movies('ml-latest-small/movies.csv')
#     print(obj.most_genres(5))
#     print(obj.dist_by_genres())
#     print(obj.dist_by_release())