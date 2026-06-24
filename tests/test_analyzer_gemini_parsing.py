from __future__ import annotations

from src.kaven import analyzer


def test_parse_analysis_response_handles_markdown_fenced_json() -> None:
    text = '''```json
    [
      {
        "event": "호르무즈 해협 긴장 고조",
        "severity": 4,
        "category": "energy",
        "affected_assets": ["WTI", "KOSPI"],
        "signal": "hedge",
        "confidence": 0.8,
        "reasoning": "유조선 항로 불안이 커졌습니다.",
        "source_url": null,
        "source_title": "Reuters",
        "event_time": null,
        "region": "hormuz"
      }
    ]
    ```'''

    events = analyzer._parse_analysis_response(text)

    assert len(events) == 1
    assert events[0]["event"] == "호르무즈 해협 긴장 고조"


def test_parse_analysis_response_salvages_complete_objects_from_truncated_array() -> None:
    text = '''```json
    [
      {
        "event": "호르무즈 해협 긴장 고조",
        "severity": 4,
        "category": "energy",
        "affected_assets": ["WTI", "KOSPI"],
        "signal": "hedge",
        "confidence": 0.8,
        "reasoning": "유조선 항로 불안이 커졌습니다.",
        "source_url": null,
        "source_title": "Reuters",
        "event_time": null,
        "region": "hormuz"
      },
      {
        "event": "대만 해협 군사훈련 확대",
        "severity": 4,
        "category": "semiconductor",
        "affected_assets": ["삼성전자", "SK하이닉스"],
        "signal": "watch",
        "confidence": 0.72,
        "reasoning": "반도체 공급망 긴장이 커질 수 있습니다.",
        "source_url": null,
        "source_title": "AP",
        "event_time": null,
        "region": "taiwan"
      },
      {
        "event": "잘리다'''

    events = analyzer._parse_analysis_response(text)

    assert len(events) == 2
    assert events[0]["event"] == "호르무즈 해협 긴장 고조"
    assert events[1]["event"] == "대만 해협 군사훈련 확대"
