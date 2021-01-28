words = ['asdf', 'kkk',' ','']
##words = ' '.join(words).split()
while '' in words:
    words.remove('')
while ' ' in words:
    words.remove(' ')
print(words)