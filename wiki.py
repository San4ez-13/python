import wikipedia
wikipedia.set_lang('ru')
search = input('Что ищем?\n')
s = wikipedia.search(search)
print(s)