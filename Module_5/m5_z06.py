text = r'You’re decent, but you seem like a mismAtch.'
spam_words = ['Match']
space_around_c = True


def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    for sp in spam_words:
        spam0 = sp.lower()
        spam1 = sp.lower()+' '
        spam2 = ' '+sp.lower()+' '
        spam3 = ' '+sp.lower()+'.'

        if space_around:
            if text.find(spam1) >= 0 or text.find(spam2) >= 0 or text.find(spam3) >= 0:
                return True
            else:
                return False

        else:
            if text.find(spam0) >= 0:
                return True
            else:
                return False


print(is_spam_words(text, spam_words, space_around_c))
