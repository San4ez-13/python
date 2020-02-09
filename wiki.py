import wikipedia
wikipedia.set_lang('ru')

while True:

    try:
        search = input('Что ищем?\n')
        s = wikipedia.page(search)
        print(s.content)
    except:
        print('По вашему запросу ничего не найдено!')
        print()
        print('Допустимые варианты:')
        print('====================')
        s = wikipedia.search(search)
        for item in s:
            print(item)
        print('=====================')
        print()    
