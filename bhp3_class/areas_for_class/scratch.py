from collections import dequeue
import queue

print(f'my name is {__name__}')

def get_words():
    
    def extend_words(word):
        if "." in word:
            words.put(f'/{word}')
        else:
            words.put(f'/{word}/')

        for extension in EXTENSIONS:
            words.put(f'/{word}{extension}')
    
    with open(WORDLIST) as f:
        raw_words = f.read()

    words = queue.Queue()
    for word in raw_words.split():
        extend_words(word)
            
    return words

def main():
    print('see how that\' different?')

if __name__ == '__main__':
    main()
