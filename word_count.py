def count_words(string):
    '''
    Count the words present in a string
    INPUT: string
    OUTPUT: dictionary
    '''
    output = {}
    words = string.split()
    for word in words:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    return output

if __name__ == '__main__':
    test_string = 'i love cheese so much wow oh god'
    print count_words(test_string)
