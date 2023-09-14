from rusty_results import Ok, Err


def test_can_create_OK():
    ok = Ok("foobar")
    assert ok.value == "foobar"


def test_can_create_Err():
    err = Err("All is lost")
    assert err.err == "All is lost"


def test_can_match_ok():
    ok = Ok("foobar")
    match ok:
        case Ok(x):
            assert x == "foobar"
        case _:
            assert False, "Match didn't work as expected"


def test_can_match_err():
    err = Err("error")
    match err:
        case Err(error):
            assert error == "error"
        case _:
            assert False, "Match didn't work as expected"


def test_util_methods():
    ok = Ok("foobar")
    err = Err("error")
    assert ok.is_ok()
    assert err.is_err()
    assert not ok.is_err()
    assert not err.is_ok()
    assert ok.tuple() == ("ok", "foobar")
    assert err.tuple() == ("err", "error")
