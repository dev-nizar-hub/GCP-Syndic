import os
import re

search_dirs = ["c:/xampp/htdocs/GCP Syndic Website v2/public", "c:/xampp/htdocs/GCP Syndic Website v2/scratch", "c:/xampp/htdocs/GCP Syndic Website v2/src"]
terms = ["paris", "france", "français", "francais", "île de france", "ile de france", "ile-de-france", "+33"]

results = []

for d in search_dirs:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith(('.html', '.css', '.js', '.py', '.tsx', '.ts')):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as file:
                        for i, line in enumerate(file):
                            lower_line = line.lower()
                            for term in terms:
                                if term in lower_line:
                                    results.append(f"{path}:{i+1}: {line.strip()[:150]}")
                                    break # Only report the line once even if it has multiple terms
                except Exception as e:
                    pass

with open("c:/xampp/htdocs/GCP Syndic Website v2/scratch/scan_results.txt", "w", encoding='utf-8') as out:
    for r in results:
        out.write(r + "\n")

print(f"Found {len(results)} occurrences. Results written to scratch/scan_results.txt")
