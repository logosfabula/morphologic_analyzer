from nltk.corpus import words
import string, os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open('./compounds.txt', 'r') as f:
    compounds = [(x.strip()) for x in f.readlines() if x.strip() != '']

vocabulary_files = {}
vocabulary_files['prepositions'] = '/vocabularies/50_top_English_prepositions'
vocabulary_files['pronouns'] = '/vocabularies/60_top_English_pronouns'
vocabulary_files['adverbs'] = '/vocabularies/250_top_English_adverbs'
vocabulary_files['adjectives'] = '/vocabularies/500_top_English_adjectives'
vocabulary_files['verbs'] = '/vocabularies/1000_top_English_verbs'
vocabulary_files['nouns'] = '/vocabularies/1500_top_English_nouns'
vocabulary_files['conjunctions'] = '/vocabularies/25_top_English_conjunctions'
vocabulary_files['interjections'] = '/vocabularies/100_top_English_interjections'
vocabulary_files['most_common_english_words'] = '/vocabularies/10000_most_common_English_words'
vocabulary_files['nltk_words'] = '/vocabularies/235000_nltk_English_words'

vocabulary = {}
for pos in vocabulary_files:
    with open(dir_path + vocabulary_files[pos]) as vf:
        vocabulary[pos] = [(x.strip()) for x in vf.readlines() if x.strip() != '']

english_words = []
english_words += vocabulary['nltk_words']
english_words += vocabulary['most_common_english_words']
english_words = [w for w in english_words if len(w) > 2]
english_words += vocabulary['prepositions']
english_words += vocabulary['pronouns']
english_words += vocabulary['adverbs']
english_words += vocabulary['adjectives']
english_words += vocabulary['verbs']
english_words += vocabulary['nouns']
english_words += vocabulary['conjunctions']
english_words += vocabulary['interjections']
english_words += vocabulary['articles']
english_words = set(english_words)

removed_words = []
english_words = [c for c in english_words if c not in removed_words]

out = ''

def fun(components, compound, acc):
    global out
    for c in components:
        if compound == '':
            print(acc)
            out += acc + '\n'
            return
        elif compound.startswith(c):
            fun(components, compound[len(c):], acc + " " + c)
        else:
            pass

for compound in compounds:    
    print("\n[" + compound + "]")
    out += "\n[" + compound + "]"
    fun(english_words, compound, '')

with open('./results.txt', 'w') as f:
    f.write(out)