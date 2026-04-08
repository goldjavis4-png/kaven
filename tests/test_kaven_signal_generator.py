from __future__ import annotations

import importlib


def test_outbound_disabled_by_default(monkeypatch) -> None:
    monkeypatch.delenv("KAVEN_ENABLE_OUTBOUND", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
    mod = importlib.import_module("src.kaven.signal_generator")
    mod = importlib.reload(mod)

    assert mod.ENABLE_OUTBOUND is False
    assert mod.CHAT_ID == ""


def test_outbound_can_be_enabled_explicitly(monkeypatch) -> None:
    monkeypatch.setenv("KAVEN_ENABLE_OUTBOUND", "1")
    monkeypatch.setenv("KAVEN_ENABLE_URGENT_DM", "true")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "12345")
    monkeypatch.setenv("TELEGRAM_USER_DM", "67890")
    mod = importlib.import_module("src.kaven.signal_generator")
    mod = importlib.reload(mod)

    assert mod.ENABLE_OUTBOUND is True
    assert mod.ENABLE_DM is True
    assert mod.CHAT_ID == "12345"
    assert mod.USER_DM == "67890"
