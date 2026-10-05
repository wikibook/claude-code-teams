import json
import subprocess

def run_case(case):
    diff = open(case["input"], encoding="utf-8").read()
    prompt = "다음 diff를 검토하고 위반 여부를 보고해줘.\n\n" + diff
    out = subprocess.run(
        ["claude", "--agent", case["target"], "-p", prompt,
         "--output-format", "json"],
        capture_output=True, encoding="utf-8")
    result = json.loads(out.stdout)["result"]
    flagged = "[중요]" in result
    hit = all(k in result for k in case["expect"])
    return {"id": case["id"],
            "pass": flagged == case["must_flag"] and hit,
            "flagged": flagged}

cases = json.load(open("evals/cases.json", encoding="utf-8"))
results = [run_case(c) for c in cases]
passed = sum(r["pass"] for r in results)
print(f"{passed}/{len(results)} 통과")
for r in results:
    if not r["pass"]:
        print(f"  실패: {r['id']} (위반 보고 {'있음' if r['flagged'] else '없음'})")
