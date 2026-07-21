#!/usr/bin/env python3
"""Extract text AND hyperlink targets from a .docx ELN export (stdlib only, no pip).

Usage:  python tools/read_eln.py path/to/entry.docx

Prints each hyperlink as   '<display text>'  ->  <target url>
so you can see when a link's text and destination disagree — which you cannot
tell from the rendered document. Then prints the plain text of the entry.
"""
import sys, zipfile, xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"

def main(path):
    with zipfile.ZipFile(path) as z:
        rels = ET.fromstring(z.read("word/_rels/document.xml.rels"))
        target = {r.get("Id"): r.get("Target") for r in rels.findall(f"{REL}Relationship")}
        doc = ET.fromstring(z.read("word/document.xml"))

    print("=== HYPERLINKS (display text -> target) ===")
    found = False
    for h in doc.iter(f"{W}hyperlink"):
        rid = h.get(f"{R}id")
        text = "".join(t.text or "" for t in h.iter(f"{W}t"))
        print(f"  '{text}'  ->  {target.get(rid, '(no target)')}")
        found = True
    if not found:
        print("  (none)")

    print("\n=== TEXT ===")
    for p in doc.iter(f"{W}p"):
        line = "".join(t.text or "" for t in p.iter(f"{W}t"))
        if line.strip():
            print(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python tools/read_eln.py path/to/entry.docx")
    main(sys.argv[1])
