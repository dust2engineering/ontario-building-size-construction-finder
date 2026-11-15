#!/usr/bin/env python3
"""Ontario building size & construction article finder (OBC 2024, Subsection 3.2.2).
Usage:
  python3 building_size_finder.py --group D
  python3 building_size_finder.py --group D --storeys 2 --streets 2
Area tables are reproduced only for articles verified in full; others report 'refer to article'.
"""
import argparse, json, os
DATA = json.load(open(os.path.join(os.path.dirname(__file__), "building-size-articles.json")))
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", required=True, help="e.g. A-2, C, D, E, F-3 (retirement home: 'C (retirement home)')")
    ap.add_argument("--storeys", type=int, default=None)
    ap.add_argument("--streets", type=int, choices=[1, 2, 3], default=None)
    a = ap.parse_args()
    hits = [x for x in DATA["articles"] if x["group"] == a.group]
    if not hits:
        print("No indexed articles for group", a.group, "- groups indexed:", sorted(set(x["group"] for x in DATA["articles"])))
        return
    for x in hits:
        print(f"{x['article']} | Group {x['group']} | max storeys: {x['max_storeys']} | construction: {x['construction']} | sprinklers (per title): {x['sprinkler_per_article_title']}")
        t = x["max_building_area_m2_by_storeys_and_streets"]
        if t == "NL":
            print("   Max building area: not limited by this article.")
        elif t is None:
            print("   Max building area: refer to article (table not reproduced in this tool).")
        elif a.storeys and a.streets:
            row = t.get(str(a.storeys))
            print(f"   Max building area at {a.storeys} storeys facing {a.streets} street(s): {row[a.streets - 1] if row else 'beyond article limit'} m2" if row else "   Storeys beyond this article.")
        else:
            for s, row in t.items():
                print(f"   {s} storey(s): 1 St {row[0]} / 2 St {row[1]} / 3 St {row[2]} (m2)")
        if x["note"]:
            print("   Note:", x["note"])
if __name__ == "__main__":
    main()
