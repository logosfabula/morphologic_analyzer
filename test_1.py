# TEST PRECONDITIONS: no optional command-line arguments, empty 'removed_words.txt' #
## check ./test_support/ for support functions

import unittest
import compounds_splitter
import test_support.support

# TEST CASES

def test_sunflower():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "sunflower", '', results)
    expected = ['sun flower', 'sunflower']
    results = test_support.support.prepare_result(results).split(',')
    assert sorted(expected) == sorted(results)

def test_cockroach():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "cockroach", '', results)
    expected = ['cock roach', 'cockroach']
    results = test_support.support.prepare_result(results).split(',')
    assert sorted(expected) == sorted(results)

def test_pleasecretin():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "pleasecretin", '', results)
    expected = ['plea sec ret in', 'plea sec retin', 'plea secre tin', 'plea secret in', 'plea secretin', 'please cretin']
    results = test_support.support.prepare_result(results).split(',')
    assert sorted(expected) == sorted(results)

def test_doorin():
    results = []
    compounds_splitter.split_compound(compounds_splitter.english_words, "doorin", '', results)
    expected = ['do or in', 'door in']
    results = test_support.support.prepare_result(results).split(',')
    assert sorted(expected) == sorted(results)