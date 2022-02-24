names = {'Мужской': {"Санкт-Петербург": ["Саша"], 
                    "Мосва": ["Вадим", "Паша"], 
                    "Омск": ["Денис", "Костя", "Стас"],
                     "Сочи": ["Вася", "Никита"]},
        'Женский': {"Санкт-Петербург": ["Юля", "Наташа"], 
                    "Москва": ["Настя", "Ася", "Маша"],
                    "Крым": ["Лиза", "Вероника"],
                    "Омск": ["Ксюша", "Катя"]}}


def fas_search(names):

    for gender in names:
        print(f"Пол загаданного человека {gender}?")
        if input() == "да":
            for citis in names[gender]:
                print(f"Он живет в городе {citis}?")
                if input() == "да":
                    for name in names[gender][citis]:
                        print(f"Это он - {name}?")

                        if input() == "да":
                            print('Ответ:', name)
                            return
                    break


fas_search(names)
