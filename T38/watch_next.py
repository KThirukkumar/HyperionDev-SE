import spacy
nlp = spacy.load('en_core_web_md')

movie_desc = {}

with open('movies.txt', 'r') as m: 
    for line in m.readlines():
        movie_desc[line[:8]] = line[9:]

def movie_comparison(description):
    # Initialise similar_movie and similarity_score value for use later
    similar_movie = ""
    similarity_score = 0

    print("-----------Movie similarity-----------")
    # Iterate through movie's descriptions from movies.txt
    for movie in list(movie_desc.keys()):

        movie_des_nlp = nlp(movie_desc[movie])

        # Compare similarity score of current movie with current highest similarity
        # Updates similar movie and similarity score to current iteration if a higher score is present
        if nlp(description).similarity(movie_des_nlp) > similarity_score:
            similarity_score = nlp(description).similarity(movie_des_nlp)
            similar_movie = movie
    
    return f"The most similar movie is: {similar_movie}"

sample_desc = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk in to a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

print(movie_comparison(sample_desc))

"""
Expected output:
-----------Movie similarity-----------
The most similar movie is: Movie C 
"""
    

    

