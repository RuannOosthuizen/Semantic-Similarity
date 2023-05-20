import spacy


nlp = spacy.load('en_core_web_md')

# First extraction

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# Second extraction

"""
tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# Third extraction
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
"""

####-----NOTES-----#####
"""
Based on the codes when runned I found it interesting about the following similarities
1. The similarity bewteen "cat" and "monkey" is apporoximately 0.502 which suggests a moderate similarity bwteen the two words which can been seen as both the words referes to an animal.
2. The similarity bewteen "banana" and "monkey" is apporoximately 0.429 this would suggest a moderate similarity as well, which can be due to the stereotype of monkeys eat bananas.
3. The similarity bewteen "banana" and "cat" is apporoximately 0.318 indicating that the program does not explixitly seem to transitive relationships with the calculations.
"""
