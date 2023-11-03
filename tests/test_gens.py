import pytest

from py_ds.gens.examples import parse_email


def test_should_parse_email():
    generator = parse_email()
    assert next(generator) == ('', '')
    assert generator.send("jack.frost@acme.com") == ('jack.frost', 'acme.com')
    with pytest.raises(StopIteration):
        generator.send("")
