from sentences import get_determiner, get_noun, get_verb
import pytest

def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 6 times.
    for _ in range(6):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(6):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test the singular nouns.
    singular_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 6 times.
    for _ in range(6):
        word = get_noun(1)

        # Verify that the word returned from get_noun is
        # one of the words in the singular_nouns list.
        assert word in singular_nouns

    # Test the plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    for _ in range(6):
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    # Test the past verbs.
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 6 times.
    for _ in range(6):
        word = get_verb(1, 'past')

        # Verify that the word returned from get_verb is
        # one of the words in the past_verbs list.
        assert word in past_verbs
    
    # Test the singular present verbs.
    singular_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    # This loop will repeat the statements inside it 6 times.
    for _ in range(6):
        word = get_verb(1, 'present')

        # Verify that the word returned from get_verb is
        # one of the words in the singular_present_verbs list.
        assert word in singular_present_verbs

    # Test the plural present verbs.
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    # This loop will repeat the statements inside it 6 times.
    for _ in range(6):
        word = get_verb(2, 'present')

        # Verify that the word returned from get_verb is
        # one of the words in the plural_present_verbs list.
        assert word in plural_present_verbs

    # Test the future verbs.
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(6):
        word = get_verb(1, 'future')

        # Verify that the word returned from get_verb
        # is one of the words in the future_verbs list.
        assert word in future_verbs

        

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])