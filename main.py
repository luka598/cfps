import requests as r
import random

contestType = input("Contest type ('CF'): ") or "CF"
contestName = input("Contest name contains ('Div 2.'): ") or "Div. 2"
problem = input("Problem ('A'): ") or "A"
nProblems = int(input("n problems (50): ") or "50")
outputFile = input("Output file ('problems.txt'): ") or "problems.txt"


res = r.get("https://codeforces.com/api/contest.list").json()["result"]
res = [
    x
    for x in res
    if x["phase"] == "FINISHED"
    and x["type"] == contestType
    and contestName in x["name"]
]
res = res[: max(nProblems, 100)]
assert len(res) >= nProblems, "Not enough problems"
res = random.choices(res, k=nProblems)
with open(outputFile, "w") as f:
    for x in res:
        f.write(f"https://codeforces.com/contest/{x['id']}/problem/{problem}")
        f.write("\n")
