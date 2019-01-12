############################################################################################
##############                                                                ##############
##############          COMPOUND WORDS SPLITTER                               ##############
##############                                                                ##############
##############          1) install NLTK                                       ##############
##############              - `sudo pip install -U nltk`                      ##############
##############                                                                ##############
##############          2) edit files:                                        ##############
##############              - compounds.txt                                   ##############
##############              with your list of compound words                  ##############
##############              - removed_words.txt                               ##############
##############              with your list of components exceptions           ##############
##############                                                                ##############
##############          3) run `python compounds_splitter.py`                 ##############
##############                                                                ##############
##############          Lexicon taken from various public sources             ##############
##############          including NLTK and UPenn                              ##############
##############                                                                ##############
############################################################################################


# FUNCTIONS

## split_compound - parameters: list of components, compound words, accumulator for tail recursion (empty string), stored results
def split_compound(components, compound, acc, results):
    for c in components:
        if compound == '':
            results.append(acc)
            return
        elif compound.startswith(c):
            split_compound(components, compound[len(c):], acc + " " + c, results)
        else:
            pass

## process_all_compounds - main loop
def process_all_compounds(is_direct_match_excluded):

    ### results as a pass-by-reference type variable: a list
    results = []
    
    ### main cycle through compounds (eliminates duplicates, required for correct output)
    for compound in sorted(set(compounds), key=compounds.index):
        ### insert compound in results
        results.append(">" + compound)
        ### call to main logic function
        split_compound(english_words, compound, '', results)
        ### get solution for current compound by slicing results from the current compound on
        current_compound_solutions = [r.strip() for r in results[results.index(">" + compound)+1:] if not (r.strip() == compound and is_direct_match_excluded)]
        ### print output
        print("{} solutions for '{}':".format(len(current_compound_solutions), compound))
        print("{}".format(", ".join(current_compound_solutions)), end="\n\n")

    ### save to file
    with open(results_file, 'w') as f:
        for o in results:
            f.write(o + "\n")

## print header
def print_header(header):
    print('\n'.join(header), end='\n\n')


# PYTHONIC MAIN (taking care of Pytests too)
import __main__
if __name__ == "__main__" or 'test' in __main__.__file__:


    # IMPORTS

    import string, os
    from nltk.corpus import words
    import argparse 


    # SETUP

    ## job, blacklist, output files and vocabularies folder
    compounds_file = './compounds.txt'
    removed_words = './removed_words.txt'
    results_file = './results.txt'
    vocabularies_folder = './vocabularies/'

    ## POS categories
    POS_categories = {'P': 'prepositions', 'PRO': 'pronouns', 'ADV': 'adverbs', 'ADJ': 'adjectives', 'V': 'verbs', 'N': 'nouns', 'CONJ': 'conjunctions', 'INTJ': 'interjections', 'D': 'determiners'}

    ## vocabularies folder and files
    vocabulary_files = {}
    vocabulary_files['prepositions'] = vocabularies_folder + '50_top_English_prepositions'
    vocabulary_files['pronouns'] = vocabularies_folder + '60_top_English_pronouns'
    vocabulary_files['adverbs'] = vocabularies_folder + '250_top_English_adverbs'
    vocabulary_files['adjectives'] = vocabularies_folder + '500_top_English_adjectives'
    vocabulary_files['verbs'] = vocabularies_folder + '1000_top_English_verbs'
    vocabulary_files['nouns'] = vocabularies_folder + '1500_top_English_nouns'
    vocabulary_files['conjunctions'] = vocabularies_folder + '25_top_English_conjunctions'
    vocabulary_files['interjections'] = vocabularies_folder + '100_top_English_interjections'
    vocabulary_files['uncategorized_english_words'] = vocabularies_folder + '10000_uncategorized_English_words_filtered' # filtered: POS vocabularies have been already excluded
    vocabulary_files['nltk_words'] = vocabularies_folder + '235000_nltk_English_words_filtered' # filtered: POS vocabularies have been already excluded. 
    vocabulary_files['determiners'] = vocabularies_folder + 'English_determiners'

    ## minimum uncategorized words length default value
    MIN_LENGTH_DEFAULT = 3

    ## exclude uncategorized words default value
    EXCLUDE_UNCATEGORIZED = False

    ## exclude direct matches default value
    EXCLUDE_DIRECT_MATCHES = False


    # INIT

    ## initialise output header
    output_header = []

    ## argument parser setup
    parser = argparse.ArgumentParser(description='English compound words splitter')
    parser.add_argument('--exclude-less-than', '-l', action='store', dest='min_uncategorized_words_length', type=int, default=MIN_LENGTH_DEFAULT, help='Excludes uncategorized words components with less than the specified number of letters (default: {})'.format(MIN_LENGTH_DEFAULT))
    parser.add_argument('--exclude-POS', '-p', dest='user_selected_vocabularies', default='', nargs='+', help='Exclude selected POS categories from components. Choose any of the following: P (prepositions), PRO (pronouns), ADV (adverbs), ADJ (adjectives), V (verbs), N (nouns), CONJ (conjunctions), INTJ (interjections), D (determiners). All of the above are selected by default')
    parser.add_argument('--exclude-uncategorized', '-u', action="store_true", dest="exclude_uncategorized_words", default=EXCLUDE_UNCATEGORIZED, help='Exclude uncategorized words from components. Included by default')
    parser.add_argument('--exclude-direct-match', '-d', action="store_true",  dest="exclude_direct_matches", default=EXCLUDE_DIRECT_MATCHES, help='Exclude direct matches from results. E.g.: "sunflower" only yields "sun flower" and not "sunflower, sun flower". Included by default')
    arguments = parser.parse_args()

    ### check wrong POS argument. Legal POS are: P (prepositions), PRO (pronouns), ADV (adverbs), ADJ (adjectives), V (verbs), N (nouns), CONJ (conjunctions), INTJ (interjections), D (determiners)
    wrong_POS = [v for v in arguments.user_selected_vocabularies if v not in POS_categories]
    if len(wrong_POS) > 0:
        exit('Wrong POS selected: ' + ' '.join(wrong_POS) + '. Please choose from:\n' + '\n'.join('- {!s} ({!r})'.format(key,val) for (key,val) in POS_categories.items()))
    
    ### add lines to output header if user excluded categories
    if len(arguments.user_selected_vocabularies) > 0:
        output_header.append('Excluding: ' + ', '.join([POS_categories[v] for v in arguments.user_selected_vocabularies]))
    
    ### copy exclude_direct_matches argument into a global variable
    is_direct_match_excluded = arguments.exclude_direct_matches

    ## load compounds to be analyzed
    with open(compounds_file, 'r') as f:
        compounds = [(x.strip()) for x in f.readlines() if x.strip() != '']

    ## load components' blacklist: these words won't be used for splitting
    with open(removed_words, 'r') as f:
        removed_words = [(x.strip()) for x in f.readlines() if x.strip() != '']

    ## build vocabulary
    vocabulary = {}
    for category in vocabulary_files:
        with open(vocabulary_files[category]) as vf:
            vocabulary[category] = [(x.strip()) for x in vf.readlines() if x.strip() != '']

    ## build components list
    english_words = []

    ## select uncategorized words from vocabularies
    if not arguments.exclude_uncategorized_words:
        english_words += vocabulary['nltk_words']
        english_words += vocabulary['uncategorized_english_words']

        ### remove all n-letters acronyms and abbreviations from general lexicon (see: MIN_LENGTH_DEFAULT)
        english_words = [w for w in english_words if len(w) >= arguments.min_uncategorized_words_length]

    ## select POS-categories
    for key, val in POS_categories.items():
        if key not in arguments.user_selected_vocabularies:
            english_words += vocabulary[val]

    ## make the components distinct (because there may be intersections between vocabularies)
    english_words = set(english_words)

    ## remove components in blacklist from selected components
    english_words = [c for c in english_words if c not in removed_words]


    # MAIN SECTION

    print_header(output_header)
    process_all_compounds(is_direct_match_excluded)
