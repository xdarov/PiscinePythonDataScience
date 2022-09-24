
class Tags:
    """
    Analyzing data from tags.csv
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

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        big_tags = {}
        for row in self.get_generator_file():
            tag = row.split(',')[2]
            if tag in big_tags:
                continue
            big_tags[tag] = len(tag.split(' '))
        big_tags = dict(sorted(big_tags.items(), key=lambda x: x[1], reverse=True)[:n])
        return big_tags

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        tag_list = [row.split(',')[2] for row in self.get_generator_file()]
        big_tags = sorted(set(tag_list),
                          key=lambda x: len(x), reverse=True)[:n]
        return big_tags

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        tags_most_words = list(self.most_words(n).keys())
        tags_longest = self.longest(n)
        big_tags = list(set(tags_most_words + tags_longest))
        return big_tags
        
    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        popular_tags = {}
        for row in self.get_generator_file():
            tag = row.split(',')[2]
            if tag in popular_tags:
                popular_tags[tag] += 1
            else:
                popular_tags[tag] = 1
        popular_tags = dict(sorted(popular_tags.items(), key=lambda x: x[1], reverse=True)[:n])
        return popular_tags
        
    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        tags_with_word = []
        for row in self.get_generator_file():
            tag = row.split(',')[2]
            if word in tag and tag not in tags_with_word:
                tags_with_word.append(tag)
        tags_with_word = sorted(tags_with_word)
        return tags_with_word

