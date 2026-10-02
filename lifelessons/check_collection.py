#!/usr/bin/env python3
"""Audit the whole Life Lessons collection after running check_storyboard.py.

Checks character presence, matching steps, repeated magic sentences, metadata,
exact duplicate stories, and near-duplicate prose. Similarity is an editorial
signal, not proof that two stories teach the same skill.
"""
import argparse
import itertools
from pathlib import Path
import re

from check_storyboard import section, words


def shingles(prose, size=5):
    # Exclude numbered teaching lists and shared breathing/catchphrase scaffolding.
    lines = [line for line in prose.splitlines()
             if not re.match(r"^\d+\. ", line)
             and not any(term in line for term in (
                 "Rosie's Steps", "Smell the rose", "Blow out the candle",
                 "One step at a time", "練習", "加油"))]
    tokens = words(" ".join(lines))
    return {tuple(tokens[i:i + size]) for i in range(len(tokens) - size + 1)}


def audit(folder):
    files = sorted(folder.glob("*.md"))
    failures, records, sets = [], [], {}
    magic_owners, places, previous_coaches = {}, {}, set()
    for path in files:
        md = path.read_text(encoding="utf-8")
        story = section(md, r"## The Story\n")
        blessing = section(md, r"## 🌙 Goodnight Blessing\n")
        board = md.split("## 🎬 Video Storyboard", 1)[-1]
        recap = section(md, r"## 🌹 Rosie's Steps \(Recap\)\n")
        number = int(path.name.split("-", 1)[0])
        for name in ("Cat the penguin", "Tori"):
            if name not in story:
                failures.append(f"{path.name}: {name} missing from story")
        stills = re.findall(r"\*\*Still:\*\* `([^`]+)`", board)
        for token, minimum in (("CAT", 2), ("TORI", 1)):
            count = sum(bool(re.search(rf"\b{token}\b", still)) for still in stills)
            if count < minimum:
                failures.append(f"{path.name}: {token} appears in {count} stills")
        taught = re.findall(r"^\d+\. (.+)$", story, re.M)
        repeated = re.findall(r"^\d+\. (.+)$", recap, re.M)
        if not 4 <= len(repeated) <= 6 or taught != repeated * 2:
            failures.append(f"{path.name}: teaching, practice, and recap steps differ")
        if number >= 17:
            for step in repeated:
                if len(words(step)) > 14:
                    failures.append(f"{path.name}: step exceeds 14 words")
        match = re.search(r'\*\*Magic sentence:\*\* "(.+?)"', md)
        if not match:
            failures.append(f"{path.name}: magic sentence header missing")
        else:
            magic = words(match[1])
            key = tuple(magic)
            if key in magic_owners:
                failures.append(f"{path.name}: repeats the magic sentence from {magic_owners[key]}")
            magic_owners[key] = path.name
            spoken = words(story)
            occurrences = sum(spoken[i:i + len(magic)] == magic
                              for i in range(len(spoken) - len(magic) + 1))
            if occurrences < 3:
                failures.append(f"{path.name}: magic sentence repeated only {occurrences} times")
        if number >= 17:
            coaches_match = re.search(r"\*\*Coaches:\*\* (.+)", md)
            coaches = set(coaches_match[1].split(" + ")) if coaches_match else set()
            if len(coaches) not in (2, 3):
                failures.append(f"{path.name}: expected two or three coaches")
            if coaches & previous_coaches:
                failures.append(f"{path.name}: coach repeated from previous new story")
            previous_coaches = coaches
            setting = re.search(r"\*\*Setting:\*\* (.+?) \(practice\), then (.+?) \(real outing\)", md)
            if not setting:
                failures.append(f"{path.name}: practice and real places are not declared")
            else:
                for kind, place in zip(("practice", "real"), setting.groups()):
                    key = (kind, place)
                    if key in places:
                        failures.append(f"{path.name}: repeats {kind} place from {places[key]}")
                    places[key] = path.name
        cast = set(re.findall(r"^- `([A-Z]+)` →", board, re.M))
        for still in stills:
            for token in set(re.findall(r"\b[A-Z]{3,}\b", still)) - cast:
                failures.append(f"{path.name}: undeclared still character {token}")
        narrated = len(words(story)) + len(words(blessing))
        declared = re.search(r"\*\*Narrated words:\*\* (\d+)", board)
        if declared and int(declared[1]) != narrated:
            failures.append(f"{path.name}: narrated word metadata {declared[1]} != {narrated}")
        sets[path.name] = shingles(story)
        records.append((path, number, story))
    pairs = []
    for (p, _, prose), (q, _, other) in itertools.combinations(records, 2):
        if words(prose) == words(other):
            failures.append(f"duplicate stories: {p.name} / {q.name}")
        a, b = sets[p.name], sets[q.name]
        score = len(a & b) / max(1, len(a | b))
        pairs.append((score, p.name, q.name))
        if score >= 0.35:
            failures.append(f"near-duplicate prose ({score:.1%}): {p.name} / {q.name}")
    numbers = [number for _, number, _ in records]
    if numbers != list(range(1, len(records) + 1)):
        failures.append("story numbering has gaps or duplicate numbers")
    print(f"Audited {len(records)} stories and {len(pairs)} story pairs.")
    print("Closest prose pairs after excluding shared teaching scaffolding:")
    for score, p, q in sorted(pairs, reverse=True)[:8]:
        print(f"  {score:.1%}: {p} / {q}")
    for failure in failures:
        print("FAIL:", failure)
    if not failures:
        print("PASS: Cat, Tori, steps, magic sentences, cast, metadata, duplication, new places, and coach rotation.")
    return not failures


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent / "stories")
    raise SystemExit(0 if audit(parser.parse_args().folder) else 1)
