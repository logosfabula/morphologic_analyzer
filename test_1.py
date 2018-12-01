# TEST PRECONDITIONS: no optional command-line arguments, empty 'removed_words.txt' #

import unittest
import compounds_splitter

# utilities

def prepare_result(results):
    return str(sorted(results)).strip('][').replace("'","").replace("  "," ").strip()

# TEST CASES

def test_sunflower():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "sunflower", '', results)
    assert "sun flower, sunflower" == prepare_result(results)

def test_cockroach():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "cockroach", '', results)
    assert "cock roach, cockroach" == prepare_result(results)

def test_pleasecretin():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "dropin", '', results)
    assert "drop in" == prepare_result(results)

def test_doorin():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "doorin", '', results)
    assert "do or in, door in" == prepare_result(results)