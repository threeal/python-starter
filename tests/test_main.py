import importlib.metadata
import sys

import pytest

from bonacci.__main__ import main


def test_version_uses_package_metadata(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    def package_version(name: str) -> str:
        assert name == "bonacci"
        return "1.2.3"

    monkeypatch.setattr(importlib.metadata, "version", package_version)
    monkeypatch.setattr(sys, "argv", ["bonacci", "--version"])

    with pytest.raises(SystemExit) as result:
        main()

    assert result.value.code == 0
    assert capsys.readouterr().out == "1.2.3\n"
