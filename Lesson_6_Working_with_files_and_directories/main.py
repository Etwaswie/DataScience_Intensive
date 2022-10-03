import def_import as defs


with open('data.txt', 'r', encoding='UTF-8') as file, open('unique_words.txt', 'w+',
                                                           encoding='UTF-8') as file_for_write:
    defs.read_file(file)
    defs.save_file(file_for_write)



