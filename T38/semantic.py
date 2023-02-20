import spacy
nlp = spacy.load('en_core_web_md')

# ------ Similarity with Spacy code extract ------
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# ------ Working with vectors code extract ------
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# ------ Working with vectors code extract ------
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

#--------- Similarity with Spacy code extract --------
print("Own Example")
word4 = nlp("dog")
word5 = nlp("bull")
word6 = nlp("meat")
print(f"{word4} compared to {word5}: {word4.similarity(word5)}")
print(f"{word6} compared to {word5}: {word6.similarity(word5)}")
print(f"{word6} compared to {word4}: {word6.similarity(word4)}")