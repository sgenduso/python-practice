pyg_suffix = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first_letter = word[0]
    new_word = word[1:len(word)] + first_letter + pyg_suffix
    print new_word
else:
    print 'please provide a valid word'
