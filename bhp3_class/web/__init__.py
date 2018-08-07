

def get_words(wordlist, resume=None):
    with open(wordlist) as f:
        raw_words = f.read()
    found_resume = False
    words = list()
    for word in raw_words.split():
        if resume is not None:
            if found_resume:
                words.append(word)
            else:
                if word == resume:
                    found_resume = True
                    print(f'Resuming wordlist from: {resume}')
        else:
            words.append(word)
    return words