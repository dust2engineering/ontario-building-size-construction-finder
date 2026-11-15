# Ontario Building Size & Construction Article Finder (OBC 3.2.2)

Subsection 3.2.2 of the Ontario Building Code is a wall of more than 70 articles — one for every combination of occupancy, height, construction type and sprinkler status. This finder indexes the verified articles by major occupancy group and, where the maximum-area table could be read completely and cross-checked, returns the permitted building area by storeys and streets faced.

**Live web tool:** https://dust2engineering.github.io/ontario-building-size-construction-finder/web/

## How it works

- Filter by major occupancy group to see every candidate 3.2.2 article with its storey limit, construction type and title-level sprinkler status.
- Streets faced follows 3.2.2.10: 1 street by default, 2 streets at ≥ 50% of the perimeter within 15 m of a street, 3 streets at ≥ 75%.
- Where an article's area table is reproduced, enter storeys and streets for the maximum building area (NL = not limited).
- Articles whose tables could not be read completely in public sources are still listed — marked 'refer to article' — so the index is complete even where the numbers are not reproduced. No values are guessed.

## Data in this repository

- `building-size-articles.json` — the article index as machine-readable JSON (article, group, storeys, construction, sprinkler status, area tables where verified, notes).
- Article identities and titles verified against the O. Reg. 163/24 index (CodeIndex) and OBC 2024 text (BuildCodes.ca); reproduced area tables cross-checked between two public sources. Article 3.2.2.25's table is deliberately excluded: public sources conflict on one cell (600 vs 1600 m²).

## Command line

```bash
python3 building_size_finder.py --group D --storeys 2 --streets 2
```

## Worked examples

- [example-office-article.txt](examples/example-office-article.txt)
- [example-retail-nl.txt](examples/example-retail-nl.txt)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Building general. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
