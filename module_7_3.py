import io
class WordsFinder():
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                words =[]
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in punctuation:
                        line = line.replace(symbol, "")
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        dict_find ={}
        for file_name, words in self.get_all_words().items():
            if word in words:
                dict_find[file_name] = words.index(word) + 1
        return dict_find

    def count(self, word):
        word = word.lower()
        dict_count = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                dict_count[file_name] = words.count(word)
        return dict_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



