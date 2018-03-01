languages = ['Java', 'Python', 1, 2]
for language in languages:
    if isinstance(language, str):
        print(True, language)
    else:
        print(False, language)
