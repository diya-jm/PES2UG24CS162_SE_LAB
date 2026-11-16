from spam_scoring import score_message, classify, filter_inbox, inbox_status


def test_spam_and_non_spam_words():
    assert score_message("free", False, 0) == 2
    assert score_message("hello", False, 0) == 0


def test_uppercase_word_branches():
    assert score_message("HELLO", False, 0) == 1
    assert score_message("ABC", False, 0) == 0
    assert score_message("hello", False, 0) == 0


def test_link_count_branches():
    assert score_message("hello", False, 4) == 4
    assert score_message("hello", False, 1) == 1
    assert score_message("hello", False, 0) == 0


def test_known_sender_branches():
    assert score_message("hello", True, 0) == 0
    assert score_message("free urgent", True, 0) == 1
    assert score_message("hello", False, 0) == 0


def test_classification_branches():
    assert classify(8) == "spam"
    assert classify(4) == "suspicious"
    assert classify(0) == "clean"


def test_filter_inbox_branches():
    messages = [
        ("free winner urgent prize", False, 0),
        ("free urgent", False, 0),
        ("hello", False, 0)
    ]

    assert filter_inbox(messages) == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1
    }

    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0
    }


def test_inbox_status_branches():
    assert inbox_status({
        "spam": 0, "suspicious": 0, "clean": 0
    }) == "empty"

    assert inbox_status({
        "spam": 6, "suspicious": 2, "clean": 2
    }) == "flooded"

    assert inbox_status({
        "spam": 3, "suspicious": 4, "clean": 3
    }) == "noisy"

    assert inbox_status({
        "spam": 1, "suspicious": 2, "clean": 7
    }) == "healthy"