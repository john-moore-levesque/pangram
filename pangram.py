from nltk.corpus import words

word_list = words.words()

fourOrMore = [ word for word in word_list if len(word) > 3 ]
sevenOrMore = [ word for word in fourOrMore if len(word) > 6 ]

def findPangrams(letters, required):
    def _isPangram(word, letters, required):
        allLetters = set(letters + required)
        wordSet = set(word)
        if required not in word:
            return False
        if len(set(word)) < 7:
            return False
        if wordSet.difference(allLetters) or allLetters.difference(wordSet):
            return False
        return True

    pangrams = []
    for word in sevenOrMore:
        if _isPangram(word, letters, required):
            pangrams.append(word)
    return pangrams

def findWords(letters, required):
    def _addWord(word, letters, required):
        allLetters = set(letters + required)
        if required not in word:
            return False
        for letter in word:
            if letter not in allLetters:
                return False
        return True

    pangrams = findPangrams(letters, required)
    otherWords = []
    for word in fourOrMore:
        if word not in pangrams:
            if _addWord(word, letters, required):
                otherWords.append(word)
    return pangrams, otherWords
