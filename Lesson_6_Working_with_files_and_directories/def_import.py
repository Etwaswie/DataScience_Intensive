set_words = set()
array_words = []


def read_file(file_with_list):
    lines = file_with_list.readlines()
    for line in lines:
        words = line.split(' ')
        for word in words:
            set_words.add(word.strip('\n').lower())
    for _ in set_words:
        array_words.append(_)
    array_words.sort()


def save_file(file_write):
    file_write.write(f'Всего в файле уникальных слов: {len(set_words)}\n')
    for word in array_words:
        file_write.write(word + '\n')


if __name__ == '__main__':
    print('fkdjfdk')
