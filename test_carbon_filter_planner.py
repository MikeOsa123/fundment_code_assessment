import pytest
from carbon_filter_planner import filter_plan

def test_basic_case():
    assert filter_plan("a?bb") == "aabb"
    
def test_multiple_options_case():
    options = ["ababb", "bbabb", "baabb"]
    assert filter_plan("??abb") in options
    
def test_no_question_marks_case():
    assert filter_plan("ababa") == "ababa"
    
def test_all_question_marks_case():
    options = ["aabba", "aabbb", "abaab", "ababb", "babaa", "babbb", "bbaab", "bbaba", "aabaa"]
    assert filter_plan("?????") in options
        
def test_only_one_question_mark_case():
    options = ["aba", "abb"]
    assert filter_plan("?ba") in options
    assert filter_plan("?bb") in options
