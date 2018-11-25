############################################################################################
##############          COMPOUND WORDS SPLITTER                               ##############
##############                                                                ##############
##############          1) install NLTK                                       ##############
##############              - `sudo pip install -U nltk`                      ##############
##############                                                                ##############
##############          2) edit files:                                        ##############
##############              - compounds.txt                                   ##############
##############              with your list of compound words                  ##############
##############              - removed_words.txt                               ##############
##############              with your list of components' exceptions          ##############
##############                                                                ##############
##############          3) run `python compounds_splitter.py`                 ##############
############################################################################################


# IMPORTS

import string, os
from nltk.corpus import words


# CONFIG

compounds_file = './compounds.txt'
removed_words = './removed_words.txt'
vocabularies_folder = './vocabularies/'
results_file = './results.txt'

vocabulary_files = {}
vocabulary_files['prepositions'] = vocabularies_folder + '50_top_English_prepositions'
vocabulary_files['pronouns'] = vocabularies_folder + '60_top_English_pronouns'
vocabulary_files['adverbs'] = vocabularies_folder + '250_top_English_adverbs'
vocabulary_files['adjectives'] = vocabularies_folder + '500_top_English_adjectives'
vocabulary_files['verbs'] = vocabularies_folder + '1000_top_English_verbs'
vocabulary_files['nouns'] = vocabularies_folder + '1500_top_English_nouns'
vocabulary_files['conjunctions'] = vocabularies_folder + '25_top_English_conjunctions'
vocabulary_files['interjections'] = vocabularies_folder + '100_top_English_interjections'
vocabulary_files['most_common_english_words'] = vocabularies_folder + '10000_most_common_English_words'
vocabulary_files['nltk_words'] = vocabularies_folder + '235000_nltk_English_words'
vocabulary_files['articles'] = vocabularies_folder + 'English_articles'


# SETUP

## load compounds to be analyzed
with open(compounds_file, 'r') as f:
    compounds = [(x.strip()) for x in f.readlines() if x.strip() != '']

## load components' blacklist: these words won't be used for splitting
with open(removed_words, 'r') as f:
    removed_words = [(x.strip()) for x in f.readlines() if x.strip() != '']

## build vocabulary
vocabulary = {}
for pos in vocabulary_files:
    with open(vocabulary_files[pos]) as vf:
        vocabulary[pos] = [(x.strip()) for x in vf.readlines() if x.strip() != '']

## select words from vocabularies
english_words = []
english_words += vocabulary['nltk_words']
english_words += vocabulary['most_common_english_words']

## remove all 2-letters acronyms and abbreviations from general lexicon
english_words = [w for w in english_words if len(w) > 2]

## select POS-categories
english_words += vocabulary['prepositions']
english_words += vocabulary['pronouns']
english_words += vocabulary['adverbs']
english_words += vocabulary['adjectives']
english_words += vocabulary['verbs']
english_words += vocabulary['nouns']
english_words += vocabulary['conjunctions']
english_words += vocabulary['interjections']
english_words += vocabulary['articles']

## make the components distinct (because there are intersections with general vocabularies)
english_words = set(english_words)

## remove components in blacklist from selected components
english_words = [c for c in english_words if c not in removed_words]


# MAIN LOGIC

## parameters: list of components, compound words, accumulator for tail recursion (empty string), stored results
def split_compound(components, compound, acc, results):
    for c in components:
        if compound == '':
            results.append(acc)
            return
        elif compound.startswith(c):
            split_compound(components, compound[len(c):], acc + " " + c, results)
        else:
            pass

def main():

    ### results as a pass-by-reference type variable: a list
    results = []
    
    ### main cycle through compounds (eliminates duplicates, required for correct output)
    for compound in sorted(set(compounds), key=compounds.index):
        ### insert compound in results
        results.append(">" + compound)
        ### call to main logic function
        split_compound(english_words, compound, '', results)
        ### get solution for current compound by slicing results from the current compound on
        current_compound_solutions = [r.strip() for r in results[results.index(">" + compound) +1:] if r.strip() != compound]
        ### print output
        print("{} solutions for '{}':".format(len(current_compound_solutions), compound))
        print("{}.".format(", ".join(current_compound_solutions)), end="\n\n")

    ### save to file
    with open(results_file, 'w') as f:
        for o in results:
            f.write(o + "\n")


# MAIN

## 
if __name__ == "__main__":
    main()