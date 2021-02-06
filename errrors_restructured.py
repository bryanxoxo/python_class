#this function breaks up text into words for us
def break_words(text_argument):
    words_to_break = text_argument.split()
    return words_to_break

#This function Counts the number of words
def count_words(counted_words):
    len(words)

#This function sorts the words alphabetically
def alpha_words(alpha_argument):
    words_to_alpha.sort()
    return words_to_alpha

def sort_sentence(sentence):
    sorted_words = break_words(sentence)
    return sorted_words(sentence)

#This function prints the first word after popping it off
def print_first_word(firstie):
    first_word = firstie.pop(0)
    print(first_word)

#This function prints the last word after popping it off
def print_last_word(lastie):
    last_word = lastie.pop()
    print(last_word)

#This function prints the first and last words of the sentence
def print_first_and_last_word(first_n_last):
    sentence = break_words(first_n_last)
    print_first_word(sentence)
    print_last_word(sentence)

sentence = "I think it's interesting that 'cologne' rhymes with 'alone'"

words = break_words(sentence)
sorted_words = sort_sentence(sentence)

print(words)
print(sort_sentence)