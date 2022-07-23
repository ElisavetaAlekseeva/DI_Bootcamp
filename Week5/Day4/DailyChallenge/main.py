# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# Implement a classmethod that returns a Text instance but with a text file:
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
# Now, use the provided the_stranger.txt file and try using the class you created above.



from cgitb import text


class Text:
    def __init__(self, string = '') -> None:
        self.string = string
        self.string_list = self.string.split()

    def frequency(self,word):
        count = 0
        x = 0
        while x < len(self.string_list):
            for words in self.string_list:
                x += 1
                if words == word:
                    count += 1
                else:
                    continue
        if count == 0:
            return None
        dict = {word: count}
        return dict


    def common_word(self):
        words_count_dict = {}
        for word in self.string.split():
            if word in words_count_dict.keys():
               words_count_dict[word] += 1
            else:
                words_count_dict[word] = 1
        max_value = max(words_count_dict.values())
        return [k for k,v in words_count_dict.items() if v == max_value] 
        

    def unique_words(self):
        unique_list = []
        for word in self.string.split():
            if word in unique_list:
                unique_list.remove(word)
            else:
                unique_list.append(word)
        return unique_list


    def from_file(self, path):
        text = ''
        f = open(path, 'r')
        for x in f:
            text += x
        return Text(text)
        
            



string = Text('A good book would sometimes cost as much as a good house.')
print(string.frequency('good'))
print(string.common_word())
print(string.unique_words())

string2 = Text().from_file('the_stranger.txt')
print(string2)




