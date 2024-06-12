from datetime import date, datetime


def get_birthdays_per_week(users):

    if not len(users):  # Перевіряємо на пустий список користувачів
        return {}

# Якщо список не пустий створюємо змінні

    # Кортеж з якого формуємо ключі питомого словника
    week_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

    current_datetime = datetime.now()    # День відліку нашого тижневого списку
    next_week_dict = {}                  # Словник з іменинниками починаючи від дня запиту
    # Визначаємо який день тижня для дня запиту
    this_day = current_datetime.weekday()

    this_day = 2                        # тестовий день тижня для випадку кінця року
    # тестовий дата запата для випадку кінця року
    current_datetime = datetime(year=2023, month=12, day=27)

#  Створюємо словник іменинників починаючи від дня тижня запиту
    for days in range(len(week_tuple)):

        if this_day == 5:
            next_week_dict.update({week_tuple[0]: []})
            this_day = 1
            continue
        else:
            next_week_dict.update({week_tuple[this_day]: []})
        this_day += 1
    # print(next_week_dict)
#  перебираемо вхідний список претендентів на торт
    for user in users:
       # створюємо тичасову дату для випалку ДР у цьому році
        temp = datetime(current_datetime.year,
                        user["birthday"].month, user["birthday"].day)
   # створюємо тичасову дату для випалку ДР вже минув в цьому році
        temp_future = datetime(current_datetime.year+1,
                               user["birthday"].month, user["birthday"].day)
   # вираховуємо різницю між сьогодні і днем наролдення для двох випадків окремо
        time_delta = temp.date() - current_datetime.date()
        time_delta_future = temp_future.date() - current_datetime.date()

   # Відокремлюємо випадки коли день народження нвступні 7 днів. випадок ДР в цьому році не минув
        if time_delta.days >= 0 and time_delta.days <= 7:
            # Оголошуємо змінну яка показує чи випадає ДР на вихідні
            what_the_day = this_day + time_delta.days
            if what_the_day > 6:  # відокремлюємо дні після неділі
                what_the_day = (what_the_day-7) % 5
            elif what_the_day == 6:  # Випадок якшо ДР в неділю
                what_the_day = 0
            else:
                what_the_day = what_the_day % 5  # Випадки якшо ДР випадає до суботи включно
        # приеднуемо юбіляра до списку по ключу того дня коли поздоровляти враховуючи перенос вихідних днів
            next_week_dict[week_tuple[what_the_day]].append(user["name"])

   # Відокремлюємо випадки коли день народження нвступні 7 днів. випадок ДР вже минув цьому році
        if time_delta_future.days >= 0 and time_delta_future.days < 7:
           # Оголошуємо змінну яка показує чи випадає ДР на вихідні
            what_the_day_future = this_day + time_delta_future.days
            if what_the_day_future > 6:  # відокремлюємо дні після неділі
                what_the_day_future = (what_the_day_future-7) % 5
            elif what_the_day_future == 6:  # Випадок якшо ДР в неділю
                what_the_day_future = 0
            else:
                # Випадки якшо ДР випадає до суботи включно
                what_the_day_future = what_the_day_future % 5
        # приеднуемо ювіляра до списку по ключу того дня коли поздоровляти враховуючи перенос вихідних днів
            next_week_dict[week_tuple[what_the_day_future]].append(
                user["name"])

    # Почистимо наш словник від ключів з порожніми значеннями
    new_week_dict = {}
    for keys, values in next_week_dict.items():

        if len(values):
            new_week_dict.update({keys: values})

    return new_week_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 27).date()},
        {"name": "Bart Simson", "birthday": datetime(1976, 12, 30).date()},
        {"name": "Takeshi Kovac", "birthday": datetime(1976, 12, 31).date()},
        {"name": "Alan Rickman", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Cat Stepan", "birthday": datetime(1986, 1, 2).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
