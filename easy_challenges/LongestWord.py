def LongestWord(sen):

    #remove punctuation
    characters = "!?.@#$%&*/:;,~`^´[]{}"
    
    for i in range(len(characters)):
        sen = sen.replace(characters[i],"")

    #split sentence in list of words

    sen = sen.split(" ")

    len_longest_word = 0
    longest_word = ""

    #longest word
    
    for j in range(len(sen)):
        l=len(sen[j])
        if l > len_longest_word:
            len_longest_word = l
            longest_word = sen[j]

    Longest_Word = longest_word.replace('"','')

    return Longest_Word
