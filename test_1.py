# TEST PRECONDITIONS: no optional command-line arguments, empty 'removed_words.txt' #
## check ./test_support/ for support functions

import unittest
import compounds_splitter
import test_support.support

# TEST CASES

def test_sunflower():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "sunflower", '', results)
    assert "sun flower, sunflower" == test_support.support.prepare_result(results)

def test_cockroach():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "cockroach", '', results)
    assert "cock roach, cockroach" == test_support.support.prepare_result(results)

def test_pleasecretin():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "dropin", '', results)
    assert "drop in" == test_support.support.prepare_result(results)

def test_doorin():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "doorin", '', results)
    assert "do or in, door in" == test_support.support.prepare_result(results)