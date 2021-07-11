class Unscrable(object):
    """
     Takes in a file to create a dictionary.
     Finds words that have the same 
     greedy 
    """

    def __init__(self, file="wordlist.txt"):
        file = open(file, 'r')

        # key lower case -> sorted word
        # value -> list holding original word
        self.dictionary = {}
        self.fill_dictionary(file.readlines())
        file.close()

    def fill_dictionary(self, list_of_words):
        count = 0

        def clean_data(string):
            """
            """
            word_to_examine = word.strip().lower()

            # remove parenthesis
            index = 0 
            for letter in word_to_examine:
                if letter == '(':
                    word_to_examine = word_to_examine[: index]
                    break
                index += 1
            
            #sort word to use as key
            sorted_word = list(word_to_examine)
            sorted_word.sort()
            sorted_word = ''.join(sorted_word)
            return sorted_word, word_to_examine, string.strip()

        for word in list_of_words:
            word_to_put = clean_data(word)

            # see it it exist in dic
            if word_to_put[0] in self.dictionary:
                # add the current word to the list
                get_value = self.dictionary[word_to_put[0]]
                get_value.append(word_to_put[2])
            else:
                # add it to the dictionary
                self.dictionary[word_to_put[0]] = [word_to_put[2]]

    def unscramble(self, string):
        sorted_word = list(string.strip().lower())
        sorted_word.sort()
        sorted_word = ''.join(sorted_word)

        if sorted_word in self.dictionary:
            return self.dictionary[sorted_word]
        return "Not found"


if __name__ == "__main__":
    m = Unscrable()
    print(m.unscramble("eilnst"))
    # inlets wasn't in dataset?