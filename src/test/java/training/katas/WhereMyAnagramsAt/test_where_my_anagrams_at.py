from src.main.java.training.katas.WhereMyAnagramsAt.where_my_anagrams_at import anagrams
from typing import List
import pytest


test_data = [
    ('abba', ['aabb', 'abcd', 'bbaa', 'dada'], ['aabb', 'bbaa']),
    ('racer', ['crazer', 'carer', 'racar',
               'caers', 'racer'], ['carer', 'racer']),
    ('laser', ['lazing', 'lazy',  'lacer'], [])
]


@ pytest.mark.parametrize("word,words,expected_result", test_data)
def test_where_my_anagrams_at(word: str, words: List[str], expected_result: List[str]):
    assert expected_result == anagrams(word, words)


'''
Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
'''
