# Kaven Runtime (src/kaven)

**KAVEN = Korean AI-based Vigilance for Event Navigation**

이 문서는 `src/kaven` 런타임 모듈 전용 설명입니다.

## 엔트리포인트

- `kaven.py` : 수집 → 분석 → dedup → 발송 오케스트레이션
- `collectors/` : AIS/ADS-B/뉴스/소셜 수집기
- `analyzer.py` : 이벤트 분석
- `signal_generator.py` : 알림 발송

## 실행

```bash
python src/kaven/kaven.py --once
python src/kaven/kaven.py --watch --interval 5
```

## 로그

- 실행 로그: `src/kaven/logs/maven_YYYYMMDD.jsonl`
- dedup 캐시: `src/kaven/logs/sent_cache.json`

## 주의

- `.env`는 `src/kaven/.env`에서 로드되며, 빈 값(`KEY=`)은 기존 환경변수도 unset합니다.
- 로컬 LLM 사용 시 `OPENAI_BASE_URL`, `OPENAI_MODEL`, `OPENAI_API_KEY`(선택)를 설정하면 OpenAI 호환 API로 분석할 수 있습니다.
- 기본값은 안전 모드입니다: `KAVEN_ENABLE_OUTBOUND=1`을 주기 전까지 텔레그램 발송이 비활성화됩니다.
- `KAVEN_ENABLE_CONVEX_UPLOAD=1`을 주기 전까지 Convex 업로드는 비활성화됩니다.
- 테스트 및 웹앱 실행 방법은 루트 `README.md`를 참고하세요.
