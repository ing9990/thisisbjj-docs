#!/usr/bin/env python3
"""가이드 문서 검사 — 피로를 주는 기호와 쪼개짐을 막는다. 위반이 있으면 1 로 끝난다.
사용: python3 scripts/lint_docs.py [파일...]  (인자가 없으면 SUMMARY.md 의 모든 페이지)"""
import os, re, sys

BANNED = {"「": "버튼·메뉴 이름은 **굵게**", "」": "버튼·메뉴 이름은 **굵게**", "→": "화살표 대신 문장이나 링크",
          "—": "줄표 대신 문장을 나눠요", "①": "번호 목록", "②": "번호 목록", "③": "번호 목록", "④": "번호 목록",
          "⑤": "번호 목록", "⑥": "번호 목록", "⋯": "점 세 개 대신 실제 메뉴 이름", "※": "안내 박스 하나로",
          "○": "실제 값이나 N", "·": "가운뎃점 나열 대신 문장이나 목록"}
MAX_CHARS, MAX_H2, MAX_HINTS = 1200, 4, 1
LONG_OK = {"help/faq.md", "help/updates.md"}   # 질문·소식이 쌓이는 페이지는 글자 수만 예외


def body_text(src: str) -> str:
    src = re.sub(r"^---\n.*?\n---\n", "", src, flags=re.S)                   # 앞머리
    src = re.sub(r"<figure>.*?</figure>|<table.*?</table>", "", src, flags=re.S)
    src = re.sub(r"\{%.*?%\}", "", src)
    src = re.sub(r"!\[[^\]]*\]\([^)]*\)|\]\([^)]*\)", "]", src)
    return src


def lint(path: str) -> list[str]:
    src = open(path, encoding="utf-8").read()
    text = body_text(src)
    title = re.search(r"^# (.+)$", src, re.M)
    lines = [l for l in text.splitlines() if not l.startswith("# ")]      # 페이지 제목(# )은 사이드바 이름이라 검사 밖
    body = "\n".join(lines)
    plain = re.sub(r"\*\*[^*]+\*\*", "", body)   # **굵게** 쓴 실제 버튼·메뉴 이름(예: 등·하원) 안의 가운뎃점은 허용
    out = []
    for ch, how in BANNED.items():
        n = (plain if ch == "·" else body).count(ch)
        if n:
            out.append(f"'{ch}' {n}개 — {how}")
    chars = len(re.sub(r"\s", "", body))
    if chars > MAX_CHARS and path not in LONG_OK:
        out.append(f"글자 {chars}자 (최대 {MAX_CHARS}) — 말 안 해도 아는 문장을 빼거나 페이지를 나눠요")
    h2 = len(re.findall(r"^## ", body, re.M))
    if h2 > MAX_H2 and path not in LONG_OK:
        out.append(f"소제목 {h2}개 (최대 {MAX_H2})")
    hints = src.count("{% hint")
    if hints > MAX_HINTS:
        out.append(f"안내 박스 {hints}개 (최대 {MAX_HINTS})")
    return out


def pages() -> list[str]:
    summary = open("SUMMARY.md", encoding="utf-8").read()
    return [p for p in re.findall(r"\]\(([^)]+\.md)\)", summary) if os.path.exists(p)]


if __name__ == "__main__":
    targets = [a for a in sys.argv[1:] if a.endswith(".md") and a != "SUMMARY.md"] or pages()
    bad = 0
    for p in targets:
        problems = lint(p)
        if problems:
            bad += 1
            print(p)
            for m in problems:
                print("   ", m)
    print(f"\n{len(targets)}쪽 중 {bad}쪽 위반" if bad else f"{len(targets)}쪽 통과")
    sys.exit(1 if bad else 0)
