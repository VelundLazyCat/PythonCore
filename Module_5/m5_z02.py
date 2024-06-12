articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]
key = 'Ocean'


def find_articles(key, letter_case=False):
    new_articles = []
    if letter_case:
        for articles in articles_dict:
            for val in articles.values():
                titles = str(val)
                if titles.find(key) >= 0:
                    new_articles.append(articles)
                    break
    else:
        for articles in articles_dict:
            for val in articles.values():
                titles = str(val)
                titles = titles.lower()
                if titles.find(key.lower()) >= 0:
                    new_articles.append(articles)
                    break
    return new_articles


print(find_articles(key))
