def word_frequency(sentence):
    words = sentence.split()
    word_freq_dict = {}
    for word in words:
        if word in word_freq_dict:
            word_freq_dict[word] += 1
        else:
            word_freq_dict[word] = 1
    return word_freq_dict