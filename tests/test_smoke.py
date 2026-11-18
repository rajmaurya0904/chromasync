"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import chromasync


def test_version_is_set() -> None:
    assert chromasync.__version__
