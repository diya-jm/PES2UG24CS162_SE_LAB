from spam_scoring import score_message, classify, filter_inbox, inbox_status


def test_spam_words():
    assert score_message("free winner urgent prize", False, 0) == 8


def test_uppercase_words():
    assert score_message("HELLO", False, 0) == 1


def test_normal_and_short_words():
    assert score_message("hello ABC", False, 0) == 0


def test_link_count_more_than_three():
    assert score_message("hello", False, 4) == 4


def test_link_count_between_one_and_three():
    assert score_message("hello", False, 2) == 1


def test_no_links():
    assert score_message("hello", False, 0) == 0


def test_known_sender_negative_score():
    assert score_message("hello", True, 0) == 0


def test_known_sender_positive_score():
    assert score_message("free urgent", True, 0) == 1


def test_classify_spam():
    assert classify(8) == "spam"


def test_classify_suspicious():
    assert classify(4) == "suspicious"


def test_classify_clean():
    assert classify(2) == "clean"


def test_filter_inbox_all_categories():
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


def test_filter_empty_inbox():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0
    }


def test_inbox_status_empty():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"


def test_inbox_status_flooded():
    assert inbox_status({"spam": 6, "suspicious": 2, "clean": 2}) == "flooded"


def test_inbox_status_noisy():
    assert inbox_status({"spam": 3, "suspicious": 4, "clean": 3}) == "noisy"


def test_inbox_status_healthy():
    assert inbox_status({"spam": 1, "suspicious": 2, "clean": 7}) == "healthy"