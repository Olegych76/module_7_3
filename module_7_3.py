class WordsFinder:

    def __init__(self, *file_name):
        self.file_names = file_name

    def get_all_words(self):
        all_words = {}
        p = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                lst = []
                for i in f:
                    s = i.lower()  # переводим строку в нижний регистр
                    for j in s:  # удаляем пунктуацию
                        if j in p:
                            s = s.replace(j, '')
                    lst += s.split()  # добавляем слова в список
                all_words[file_name] = lst  # добавляем список-значение в словарь для конкретного ключа
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_[name] = words.index(word.lower()) + 1
        return dict_

    def count(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            dict_[name] = words.count(word.lower())
        return dict_


finder1 = WordsFinder('test_file.txt')

finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')

print(finder1.get_all_words())
print(finder1.find("text"))
print(finder1.count('teXT'))

print(finder2.get_all_words())
print(finder2.find("ThE"))
print(finder2.count('tHe'))


