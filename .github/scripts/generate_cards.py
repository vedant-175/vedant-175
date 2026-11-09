"""Generate GitHub stats / top-languages / streak SVG cards using only the
built-in GITHUB_TOKEN (no personal access token needed)."""
import json, os, sys, urllib.request
from datetime import date, timedelta
from html import escape

USER = os.environ.get("GH_USER", "vedant-175")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("OUT_DIR", "assets")
BG, FG, MUTED, ACC = "#0d1117", "#c9d1d9", "#8b949e", "#34d399"
FONT = "font-family='Segoe UI,Helvetica,Arial,sans-serif'"


def api(url, data=None):
    req = urllib.request.Request(url, data=data)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-cards")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch():
    q = """query($u:String!){user(login:$u){
      repositories(ownerAffiliations:OWNER,privacy:PUBLIC){totalCount}
      followers{totalCount}
      pullRequests{totalCount}
      issues{totalCount}
      contributionsCollection{
        totalCommitContributions totalPullRequestContributions totalIssueContributions
        contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}"""
    g = api("https://api.github.com/graphql",
            json.dumps({"query": q, "variables": {"u": USER}}).encode())["data"]["user"]
    repos, page = [], 1
    while True:
        chunk = api(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&page={page}")
        repos += chunk
        if len(chunk) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]
    langs = {}
    for r in own:
        for k, v in api(r["languages_url"]).items():
            langs[k] = langs.get(k, 0) + v
    return g, own, langs


def card(w, h, title, body):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>"
            f"<rect x='.5' y='.5' width='{w-1}' height='{h-1}' rx='12' fill='{BG}' stroke='#30363d'/>"
            f"<text x='24' y='36' {FONT} font-size='18' font-weight='600' fill='{ACC}'>{escape(title)}</text>"
            f"{body}</svg>")


def stats_svg(g, own):
    cc = g["contributionsCollection"]
    stars = sum(r["stargazers_count"] for r in own)
    rows = [("Total stars", stars), ("Commits (last year)", cc["totalCommitContributions"]),
            ("Pull requests", g["pullRequests"]["totalCount"]), ("Issues", g["issues"]["totalCount"]),
            ("Public repos", g["repositories"]["totalCount"]),
            ("Contributions (last year)", cc["contributionCalendar"]["totalContributions"])]
    body = "".join(
        f"<text x='24' y='{70+i*30}' {FONT} font-size='14' fill='{MUTED}'>{escape(k)}</text>"
        f"<text x='330' y='{70+i*30}' {FONT} font-size='14' font-weight='600' fill='{FG}' text-anchor='end'>{v}</text>"
        for i, (k, v) in enumerate(rows))
    return card(360, 70 + len(rows) * 30, f"{USER}'s GitHub Stats", body)


def langs_svg(langs):
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda x: -x[1])[:6]
    body = ""
    for i, (name, n) in enumerate(top):
        pct = n * 100 / total
        y = 62 + i * 30
        body += (f"<text x='24' y='{y+4}' {FONT} font-size='13' fill='{FG}'>{escape(name)}</text>"
                 f"<text x='336' y='{y+4}' {FONT} font-size='13' fill='{MUTED}' text-anchor='end'>{pct:.1f}%</text>"
                 f"<rect x='24' y='{y+10}' width='312' height='6' rx='3' fill='#21262d'/>"
                 f"<rect x='24' y='{y+10}' width='{max(3, 312*pct/100):.0f}' height='6' rx='3' fill='{ACC}'/>")
    return card(360, 70 + len(top) * 30, "Top Languages", body)


def streak_svg(g):
    days = {}
    for w in g["contributionsCollection"]["contributionCalendar"]["weeks"]:
        for d in w["contributionDays"]:
            days[date.fromisoformat(d["date"])] = d["contributionCount"]
    longest = run = 0
    for d in sorted(days):
        run = run + 1 if days[d] > 0 else 0
        longest = max(longest, run)
    last = max(days)
    cur, d = 0, last if days[last] > 0 else last - timedelta(days=1)
    while days.get(d, 0) > 0:
        cur += 1
        d -= timedelta(days=1)
    total = sum(days.values())
    cols = [(total, "Contributions", "last year"), (cur, "Current streak", "days"), (longest, "Longest streak", "days")]
    body = "".join(
        f"<text x='{70+i*110}' y='95' {FONT} font-size='30' font-weight='700' fill='{ACC if i==1 else FG}' text-anchor='middle'>{v}</text>"
        f"<text x='{70+i*110}' y='120' {FONT} font-size='12' fill='{FG}' text-anchor='middle'>{a}</text>"
        f"<text x='{70+i*110}' y='138' {FONT} font-size='11' fill='{MUTED}' text-anchor='middle'>{b}</text>"
        for i, (v, a, b) in enumerate(cols))
    return card(360, 165, "Contribution Streak", body)


def main():
    g, own, langs = fetch()
    os.makedirs(OUT, exist_ok=True)
    for name, svg in (("github-stats.svg", stats_svg(g, own)),
                      ("github-languages.svg", langs_svg(langs)),
                      ("github-streak.svg", streak_svg(g))):
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
