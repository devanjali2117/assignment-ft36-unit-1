def reverseSentence(sentence):
    words = sentence.split()  
    reversed_words = [word[::-1] for word in words]      reversed_sentence = ' '.join(reversed_words)  
    return reversed_sentence

