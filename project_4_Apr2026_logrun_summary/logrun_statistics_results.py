# Claude Opus 5 says this script is rubbish because:
'''
Nothing about who you play with predicts whether you time the key. Not their score, not how much damage they do. The only things in this data with real signal are the effort numbers (which dungeons and key levels ate your time) and the composition counts (which are descriptive, not causal).

First, a mini crash course on the jargon
Term	What it means here
r	Correlation. Ranges −1 to +1. 0 = no relationship. ±0.1 = trivial. ±0.3 = moderate. ±0.5+ = strong.
p	Probability of seeing a result this big by pure luck if there were no real effect. Below 0.05 is the usual "worth taking seriously" line.
95% CI	The range of true values compatible with your data. If the range includes 0, you can't rule out "no effect at all."
point-biserial	Just a normal correlation where one variable is yes/no (timed vs. not timed).
partial r|kl	Correlation after mathematically removing the influence of key level. This is the honest number, because higher keys are harder AND attract better players — those two effects cancel each other out and hide real patterns.
Pearson vs. Spearman	Pearson = straight-line relationship. Spearman = rank order only, so it's not wrecked by outliers. When they disagree wildly, you have outlier problems.
pseudo-replication	Counting the same player 10 times as if they were 10 independent people. Inflates confidence falsely. Your script correctly does a "one row per player" version to avoid this.
Section 1 — Does teammate score predict timing the key?
Avg all 5      r=+0.047  p=0.457   CI[-0.08,+0.17]   partial=+0.099 (p=0.116)
Tank           r=+0.044  p=0.419   CI[-0.06,+0.15]   partial=+0.094 (p=0.086)
Healer         r=-0.048  p=0.390   CI[-0.16,+0.06]   partial=-0.006 (p=0.912)
2 non-me DPS   r=+0.043  p=0.464   CI[-0.07,+0.16]   partial=+0.073 (p=0.218)

Finding: no detectable relationship. Every r is within rounding distance of zero, every p is nowhere near 0.05, and every confidence interval straddles zero. In plain terms: knowing a teammate's end-of-season RIO told you essentially nothing about whether that key got timed.

The mean-score comparison makes it concrete:

Timed runs averaged 3980 across the group; untimed averaged 3962. A gap of 18 points on a ~4000-point scale — 0.45%. That's noise.
Healers actually scored 37 points lower in timed runs. Don't read anything into that either; it's the same size as the noise.

The one thing that's almost interesting: the partial correlations (controlling for key level) are all bigger than the raw ones — tank goes from +0.044 to +0.094, p=0.086. That's the confound doing exactly what the caveat predicts: high-score tanks were in higher keys, which are harder to time, which masked whatever small benefit they brought. It's still not significant, but it's the only directional hint in the whole section, and it points at the tank.

Power warning: with n≈250–330 you could only reliably detect r ≈ 0.15+. So this is "no effect found," not "no effect exists." A genuinely small effect (r=0.08) would be invisible to this dataset. You'd need ~1,000+ runs.

Timed rate by key level:

+18: 25%   +19: 26%   +20: 12%   +21: 16%   +22: 27%

This is not the smooth decline you'd expect. +20 was your wall — half the success rate of +18/+19. +21 recovering to 16% and +22 hitting 27% (on only 11 runs, so ±huge) suggests that by the time you were pushing 21s and 22s your group/gear had improved enough to outrun the difficulty increase. The +20 pit is likely a mix of "grinding it out under-geared" and it being where you spent the most raw attempts.

Section 2 — Does a DPS's damage share predict their score?
Run-level Pearson    n=638  r=-0.063  p=0.111  CI[-0.14,+0.01]  partial=-0.050
Run-level Spearman   n=638  r=-0.011
Player-level Pearson n=335  r=-0.001  p=0.989  CI[-0.11,+0.11]
Player-level Spearman n=335 r=+0.031

Finding: flat zero. This is the cleanest null result in the report. r = −0.001 with p = 0.989 is about as close to "literally no relationship" as real data gets.

Two things worth flagging:

Pearson (−0.063) vs Spearman (−0.011) at run level — the gap means outliers were dragging the straight-line version negative. The rank-based number, which ignores them, is basically zero. Trust Spearman here.
Your data has garbage in it. Look at the bottom of the list: Peshounh 0.1%, Uldreht 0.0%, Phoffer 0.0%, Azuwrath 0.0% — those are almost certainly missing/broken log parses, not DPS players who did no damage. And Zyntharen shows rio = 662 across 7 runs, which in a +18-and-up dataset is impossible — that's a wrong character lookup, a name-server mismatch, or an alt. Zyntharen alone is a massive leverage point dragging the Pearson correlation negative (30.1% share = above average, paired with a score 3,300 points below everyone else). Strip those five rows and rerun; I'd bet the run-level Pearson moves from −0.063 to roughly zero, matching Spearman.

Why this null makes sense anyway: DPS share is nearly mechanically constrained. Most players cluster between 25–32%, i.e. "roughly a third of the group's damage, as expected." There just isn't enough spread for score to correlate with. The genuine outliers at the low end (Suplesa 10.4%, Grâvêyârd 7.9%, Menschenfres 12.0%, Zapsadin 11.8%) all have high scores of 4,045–4,256 — these are people who joined a run that died early, or whose logs are partial, not bad players.

Section 3 — Where your time actually went

This is your most useful section, because it's descriptive counting rather than underpowered inference.

By key level (per dungeon, averaged):

        attempts  groups  minutes
+18       8.4      4.8     126.8
+19       8.7      6.2     155.9
+20      15.2      6.8     191.7   ← the wall
+21      10.0      6.6     165.7
+22       2.2      1.6      37.9   ← only partially attempted

+20 cost you ~1.8× the attempts of +18/+19 per dungeon and over 3 hours per dungeon on average. Consistent with the 12% timed rate above. +21 was easier than +20 — again, gear/skill outran difficulty.

By dungeon (+18 to +21):

                       attempts  groups  minutes
Seat of the Triumvirate  15.0     7.8     217.5   ← worst
Nexus-Point Xenas        16.5     7.8     192.9   ← worst
Magisters' Terrace       10.5     7.2     194.7
Algeth'ar Academy        11.0     6.8     174.6
Skyreach                 11.5     7.0     163.0
Maisara Caverns          10.0     5.2     158.9
Windrunner Spire          7.5     4.5     119.6
Pit of Saron              4.5     3.8      96.1   ← cheapest

Nexus-Point and Seat were your tar pits — 3.5× the attempts of Pit of Saron. Note Magisters' Terrace is interesting: only 10.5 attempts but 194.7 minutes — long runs, i.e. you were failing late/on time rather than wiping early. Nexus-Point is the opposite: 16.5 attempts in 192.9 min ≈ 11.7 min/attempt, meaning lots of quick disasters.

(The "UNKNOWN AREA" row with n=1 is a parsing failure — one run your script couldn't identify. Harmless but worth fixing.)

Total vs. attempts-until-upgrade — this is the important comparison:

	Total attempts	Attempts until the upgrade	Wasted
+18	8.4	4.5	46%
+19	8.7	6.0	31%
+20	15.2	3.8	75%
+21	10.0	4.4	56%

Read this carefully, because the note at the bottom is doing heavy lifting. "Attempts-until-upgrade" only counts dungeon/level combos you eventually timed. Combos you never timed contribute nothing there but are fully counted in the total. So the gap isn't purely "wasted effort after success" — it's mostly effort sunk into keys that never got timed at all.

The +20 row is the headline: when a +20 did go, it went in 3.8 attempts / 69 minutes. But the average +20 dungeon cost 15.2 attempts / 192 minutes. Meaning: +20s either clicked almost immediately or never clicked at all. That's a strong argument for a bail-out rule — if you're 5+ attempts deep on a specific dungeon at a given level with no timer even close, the historical odds of it turning around are poor. Reroll the dungeon.

Per-dungeon upgrade cost confirms the dungeon rankings: Magisters' Terrace timed in 2.0 attempts when it timed, Skyreach took 7.5 and Seat 6.2.

Section 4 — Composition prevalence
                                    Trio    Trio + healer/tank pair
Score-upgrade keys (n=35)          57.1%          42.9%
All timed keys     (n=68)          38.2%          26.5%
All logged runs    (n=358)         34.4%          23.2%

Finding: there's a clean upward gradient — 34% → 38% → 57%. The Aug/UDK/DevDH trio was present in a majority of your score-upgrade keys but only about a third of all runs.

But do not read this as "the meta comp wins." Three reasons:

Your script's own caveat is correct — this measures your invite habits, not comp effectiveness. There's no comparison group.
Time is a massive confound. Look at the "missing" list: nearly every early-season run (April 23–30) is missing an Unholy DK. The trio became available to you later in the season — which is exactly when your gear, practice, and key levels were also peaking. Comp availability and player power rose together, so you can't separate them.
n=35 is small. 20/35 vs 123/358 looks suggestive, but you'd want a proper test (chi-square or Fisher's exact), and even then confound #2 invalidates the causal reading.

What would actually answer the question: restrict to a single time window and a single key level, then compare timed-rate with-trio vs without-trio. You have the data to do that; you just haven't sliced it that way.

Bottom line
❌ Teammate score does not predict timing keys in your data (all r < 0.1, all p > 0.08). Underpowered, so treat as "not detected," not "disproven." Tank score is the only faint hint.
❌ DPS damage share does not predict player score at all (r = −0.001). Genuine null, and it makes mechanical sense — everyone clusters at 25–32%.
✅ +20 was your bottleneck, at ~2x the effort and half the success rate of neighbouring levels. +21 and +22 were easier than +20.
✅ Nexus-Point Xenas and Seat of the Triumvirate cost 3x what Pit of Saron did. Route around them where possible.
✅ Keys that went, went fast (3.8 attempts at +20). Keys that didn't, never did. Strongest actionable finding: set an attempt cap and reroll.
⚠️ The meta trio appears in 57% of upgrade keys vs 34% of all runs, but this is confounded by season timing and is descriptive only.
Three fixes before you rerun
Purge the bad rows — Zyntharen (rio=662) and the four 0.0% DPS-share players. They're data errors and Zyntharen is single-handedly bending your Pearson correlation.
The reverse-causality problem is fundamental. End-of-season score is partly caused by timing these very keys. That means Section 1 is somewhat circular by construction. If Raider.IO gives you historical/weekly score snapshots, use score-at-time-of-run instead — that would turn this from an association into something closer to a real predictor test.
Cluster your standard errors by player and by night, or bootstrap at the player level. As your caveat says, all p-values here are optimistic because the same ~20 people recur constantly.
'''

'''
# logstats.py — statistical analysis over logsummary_rio.csv
#
# Usage:
#   from logstats import print_statistics
#   print_statistics("logsummary_rio.csv", player_scores=player_scores)
#
# or standalone:
#   python logstats.py logsummary_rio.csv

import csv
import math
import os
import re
from collections import defaultdict

from logrun import (
    duration_to_seconds,
    amount_to_float,
    get_sort_dt,
    score_to_avg_keylevel,
)

# ---------------------------------------------------------------------------
# Small stats toolbox
# ---------------------------------------------------------------------------

def _mean(xs):
    return sum(xs) / len(xs) if xs else float('nan')


def pearson(x, y):
    n = len(x)
    if n < 3:
        return None
    mx, my = _mean(x), _mean(y)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    if sxx <= 0 or syy <= 0:
        return None
    return sxy / math.sqrt(sxx * syy)


def _ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    out = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            out[order[k]] = avg
        i = j + 1
    return out


def spearman(x, y):
    if len(x) < 3:
        return None
    return pearson(_ranks(x), _ranks(y))


def partial_pearson(x, y, z):
    """corr(x, y) controlling for z."""
    rxy, rxz, ryz = pearson(x, y), pearson(x, z), pearson(y, z)
    if rxy is None or rxz is None or ryz is None:
        return None
    denom = math.sqrt(max(0.0, (1 - rxz ** 2) * (1 - ryz ** 2)))
    if denom == 0:
        return None
    return (rxy - rxz * ryz) / denom


def _phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def fisher_ci(r, n, k_controls=0):
    """Return (p, lo, hi) via Fisher z. k_controls = #covariates partialled out."""
    dof_n = n - k_controls
    if r is None or dof_n < 5 or abs(r) >= 0.999999:
        return None, None, None
    z = math.atanh(r)
    se = 1.0 / math.sqrt(dof_n - 3)
    p = 2.0 * (1.0 - _phi(abs(z) / se))
    return p, math.tanh(z - 1.96 * se), math.tanh(z + 1.96 * se)


def fmt_corr(label, x, y, z=None, width=34):
    """Print one correlation line. If z is given, also print the partial r."""
    n = len(x)
    r = pearson(x, y)
    if r is None:
        print(f"  {label.ljust(width)} n={n:<4} r=   N/A")
        return
    p, lo, hi = fisher_ci(r, n)
    ptxt = f"p={p:.3f}" if p is not None else "p=  N/A"
    citxt = f"[{lo:+.2f},{hi:+.2f}]" if lo is not None else ""
    line = f"  {label.ljust(width)} n={n:<4} r={r:+.3f}  {ptxt}  95%CI {citxt}"
    if z is not None:
        rp = partial_pearson(x, y, z)
        if rp is not None:
            pp, _, _ = fisher_ci(rp, n, k_controls=1)
            line += f"   | partial r|kl={rp:+.3f} (p={pp:.3f})" if pp is not None \
                    else f"   | partial r|kl={rp:+.3f}"
    print(line)


# ---------------------------------------------------------------------------
# Roles / specs
# ---------------------------------------------------------------------------

'''
# Must comment it out like this because otherwise we get a terminal warnings about \ in string
# def _norm(s):
    # return re.sub(r"[\s'\-_]", "", s or "").lower()
'''

TANK_SPECS   = {'blood', 'vengeance', 'guardian', 'brewmaster', 'protection'}
HEALER_SPECS = {'restoration', 'holy', 'discipline', 'mistweaver', 'preservation'}


def resolve_role(spec, _, csv_role=''):
    """Trust the CSV role column (parsed from Tanks:/Healers:/DPS:) if present."""
    cr = (csv_role or '').strip().lower()
    if cr in ('tank', 'healer', 'dps'):
        return cr
    s = (spec or '').strip().lower()
    if s in TANK_SPECS:
        return 'tank'
    if s in HEALER_SPECS:
        return 'healer'
    return 'dps'


def has_spec(rec, spec_prefix, cls_name):
    """Prefix match on spec so 'Devour' matches 'Devourer'."""
    sp, cn = _norm(spec_prefix), _norm(cls_name)
    return any(_norm(p['spec']).startswith(sp) and _norm(p['cls']) == cn
               for p in rec['players'])


# ---------------------------------------------------------------------------
# Record loading
# ---------------------------------------------------------------------------

def _f(v):
    try:
        f = float(v)
        return f if f > 0 else None
    except (TypeError, ValueError):
        return None


def load_records(csv_file, player_scores=None, my_name="Powerpegging",
                 min_key_level=18):
    with open(csv_file, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    rows.sort(key=lambda r: get_sort_dt(r.get('timestamp', '')))

    recs = []
    for row in rows:
        dungeon = row.get('dungeon', '').strip()
        try:
            kl = int(row.get('key_level', '').strip())
        except ValueError:
            continue
        if not dungeon or kl < min_key_level:
            continue

        players = []
        for idx in range(1, 6):
            px = f'player{idx}_'
            name = row.get(px + 'name', '').strip()
            if not name:
                continue
            spec = row.get(px + 'spec', '').strip()
            cls  = row.get(px + 'class', '').strip()
            role = resolve_role(spec, cls, row.get(px + 'role', ''))

            # "25.75m (307.7k)" -> 25 750 000.0    (amount_to_float handles k/m/b)
            dmg = amount_to_float(row.get(px + 'damage_amount', '').split('(')[0])

            score = None
            if player_scores:
                score = _f(player_scores.get(name))
            if score is None:
                score = _f(row.get(px + 'rio_score', ''))   # enriched CSV column

            players.append({'name': name, 'spec': spec, 'cls': cls,
                            'role': role, 'dmg': dmg, 'score': score,
                            'is_me': name == my_name})

        total_dmg = sum(p['dmg'] for p in players)
        for p in players:
            p['dmg_frac'] = (p['dmg'] / total_dmg) if total_dmg > 0 else None

        recs.append({
            'dungeon': dungeon,
            'kl': kl,
            'timed': row.get('completion', '').strip() == '1',
            'upgrade': row.get('IsScoreUpgrade', '').strip() not in ('', '0'),
            'secs': duration_to_seconds(row.get('duration', '')),
            'ts': row.get('timestamp', '').strip(),
            'players': players,
            'group': frozenset(p['name'] for p in players),
        })
    return recs


# ---------------------------------------------------------------------------
# Group counting (same >=3 overlap rule as the milestone summary)
# ---------------------------------------------------------------------------

def count_groups(group_sets):
    reps = []
    for g in group_sets:
        if not any(len(g & e) >= 3 for e in reps):
            reps.append(set(g))
    return len(reps)


# ---------------------------------------------------------------------------
# 1 + 2. Correlations
# ---------------------------------------------------------------------------

def section_correlations(recs, _):
    print("\n" + "=" * 78)
    print("1) KEY SUCCESS  vs  END-OF-SEASON SCORE   (point-biserial)")
    print("=" * 78)

    buckets = {
        'Avg score, all 5 players': ([], [], []),
        'Tank score':               ([], [], []),
        'Healer score':             ([], [], []),
        'Avg score, 2 non-me DPS':  ([], [], []),
    }
    # each bucket = (success[], score[], keylevel[])

    def push(key, succ, score, kl):
        if score is None:
            return
        b = buckets[key]
        b[0].append(succ)
        b[1].append(score)
        b[2].append(kl)

    for r in recs:
        succ = 1.0 if r['timed'] else 0.0
        kl = float(r['kl'])
        ps = r['players']

        all_scores = [p['score'] for p in ps if p['score'] is not None]
        if len(ps) == 5 and len(all_scores) == 5:
            push('Avg score, all 5 players', succ, _mean(all_scores), kl)

        tanks   = [p['score'] for p in ps if p['role'] == 'tank'   and p['score'] is not None]
        healers = [p['score'] for p in ps if p['role'] == 'healer' and p['score'] is not None]
        if len(tanks) == 1:
            push('Tank score', succ, tanks[0], kl)
        if len(healers) == 1:
            push('Healer score', succ, healers[0], kl)

        odps = [p['score'] for p in ps
                if p['role'] == 'dps' and not p['is_me'] and p['score'] is not None]
        if len(odps) >= 2:
            push('Avg score, 2 non-me DPS', succ, _mean(odps), kl)

    for label, (x, y, z) in buckets.items():
        fmt_corr(label, x, y, z)

    print("\n  Mean score of TIMED vs UNTIMED runs (same samples):")
    for label, (x, y, _z) in buckets.items():
        t = [b for a, b in zip(x, y) if a == 1.0]
        u = [b for a, b in zip(x, y) if a == 0.0]
        if t and u:
            print(f"    {label.ljust(28)} timed {(_mean(t)):7.0f} (n={len(t):3d})"
                  f"   untimed {(_mean(u)):7.0f} (n={len(u):3d})"
                  f"   delta {(_mean(t) - _mean(u)):+7.0f}")
        else:
            print(f"    {label.ljust(28)} (need both timed and untimed runs)")

    print("\n  Timed rate by key level (context for the confounding):")
    by_kl = defaultdict(lambda: [0, 0])
    for r in recs:
        by_kl[r['kl']][0] += 1
        by_kl[r['kl']][1] += 1 if r['timed'] else 0
    for kl in sorted(by_kl):
        n, t = by_kl[kl]
        print(f"    +{kl}: {t}/{n} timed ({100.0 * t / n:.0f}%)")

    # ---- 2. DPS% vs score, non-me DPS only ---------------------------------
    print("\n" + "=" * 78)
    print("2) DPS SHARE (% of group damage)  vs  END-OF-SEASON SCORE  (non-me DPS)")
    print("=" * 78)

    fr, sc, kls = [], [], []
    per_player = defaultdict(list)
    for r in recs:
        if len(r['players']) != 5:
            continue
        for p in r['players']:
            if p['role'] != 'dps' or p['is_me']:
                continue
            if p['dmg_frac'] is None or p['score'] is None:
                continue
            fr.append(p['dmg_frac'] * 100.0)
            sc.append(p['score'])
            kls.append(float(r['kl']))
            per_player[p['name']].append((p['dmg_frac'] * 100.0, p['score']))

    fmt_corr('Run-level (Pearson)', fr, sc, kls)
    rs = spearman(fr, sc)
    print(f"  {'Run-level (Spearman)'.ljust(34)} n={len(fr):<4} "
          f"r={rs:+.3f}" if rs is not None else "  Run-level (Spearman): N/A")

    px = [_mean([a for a, _ in v]) for v in per_player.values()]
    py = [_mean([b for _, b in v]) for v in per_player.values()]
    print("\n  Player-level (one point per unique player - avoids pseudo-replication):")
    fmt_corr('Mean DPS share vs score', px, py)
    rsp = spearman(px, py)
    if rsp is not None:
        print(f"  {'Mean DPS share vs score (Spearman)'.ljust(34)} "
              f"n={len(px):<4} r={rsp:+.3f}")

    print("\n  Per-player detail (runs, mean DPS share, score):")
    for name in sorted(per_player, key=lambda k: -_mean([a for a, _ in per_player[k]])):
        v = per_player[name]
        print(f"    {name.ljust(20)} n={len(v):<3} "
              f"share={_mean([a for a, _ in v]):5.1f}%  rio={_mean([b for _, b in v]):6.0f}")


# ---------------------------------------------------------------------------
# 3. Attempts / groups / minutes
# ---------------------------------------------------------------------------

def _aggregate(recs):
    """(dungeon, kl) -> totals over every logged run."""
    agg = defaultdict(lambda: {'attempts': 0, 'secs': 0, 'groups': [], 'timed': 0})
    for r in recs:
        a = agg[(r['dungeon'], r['kl'])]
        a['attempts'] += 1  #type:ignore
        a['secs'] += r['secs']
        a['groups'].append(set(r['group']))  #type:ignore
        a['timed'] += 1 if r['timed'] else 0  #type:ignore
    for a in agg.values():
        a['n_groups'] = count_groups(a['groups'])
        a['mins'] = a['secs'] / 60.0  #type:ignore
    return agg


def _cycles(recs):
    """
    Replicates the milestone counter: attempts / groups / minutes accumulated
    since the previous score upgrade on that (dungeon, key level).
    Only emits a cycle when an upgrade actually happened.
    """
    state = defaultdict(lambda: {'attempts': 0, 'secs': 0, 'groups': []})
    out = []
    for r in recs:                      # recs are chronological
        st = state[(r['dungeon'], r['kl'])]
        st['attempts'] += 1  #type:ignore
        st['secs'] += r['secs']
        st['groups'].append(set(r['group']))  #type:ignore
        if r['upgrade']:
            out.append({'dungeon': r['dungeon'], 'kl': r['kl'],
                        'attempts': st['attempts'],
                        'groups': count_groups(st['groups']),
                        'mins': st['secs'] / 60.0})
            state[(r['dungeon'], r['kl'])] = {'attempts': 0, 'secs': 0, 'groups': []}
    return out


def _table(rows, _, label_fn, header):
    print(f"\n  {header}")
    print(f"    {'':<22}{'n':>4} {'attempts':>10} {'groups':>9} {'minutes':>9}")
    for k in sorted(rows):
        items = rows[k]
        if not items:
            continue
        print(f"    {label_fn(k).ljust(22)}{len(items):>4} "
              f"{_mean([i['attempts'] for i in items]):>10.1f} "
              f"{_mean([i['groups'] for i in items]):>9.1f} "
              f"{_mean([i['mins'] for i in items]):>9.1f}")


def section_effort(recs, kl_range=(18, 22), dungeon_kl_range=(18, 21)):
    print("\n" + "=" * 78)
    print("3) EFFORT PER KEY LEVEL AND PER DUNGEON")
    print("=" * 78)

    agg = _aggregate(recs)
    cyc = _cycles(recs)

    # --- totals (every run counted, whether or not it was ever timed) -------
    by_kl = defaultdict(list)
    for (d, kl), a in agg.items():
        if kl_range[0] <= kl <= kl_range[1]:
            by_kl[kl].append({'attempts': a['attempts'], 'groups': a['n_groups'],
                              'mins': a['mins'], 'dungeon': d})
    _table(by_kl, 'kl', lambda k: f"+{k}",
           "TOTAL effort, averaged across dungeons that have data at that level "
           "(n = #dungeons):")

    by_dg = defaultdict(list)
    for (d, kl), a in agg.items():
        if dungeon_kl_range[0] <= kl <= dungeon_kl_range[1]:
            by_dg[d].append({'attempts': a['attempts'], 'groups': a['n_groups'],
                             'mins': a['mins'], 'kl': kl})
    _table(by_dg, 'dungeon', lambda k: k[:22],
           f"TOTAL effort per dungeon, averaged over key levels "
           f"+{dungeon_kl_range[0]}..+{dungeon_kl_range[1]} (n = #key levels):")

    # --- cycle view (attempts needed to reach an upgrade) -------------------
    c_kl = defaultdict(list)
    for c in cyc:
        if kl_range[0] <= c['kl'] <= kl_range[1]:
            c_kl[c['kl']].append(c)
    _table(c_kl, 'kl', lambda k: f"+{k}",
           "ATTEMPTS-UNTIL-UPGRADE (only key levels that were eventually timed; "
           "n = #upgrades):")

    c_dg = defaultdict(list)
    for c in cyc:
        if dungeon_kl_range[0] <= c['kl'] <= dungeon_kl_range[1]:
            c_dg[c['dungeon']].append(c)
    _table(c_dg, 'dungeon', lambda k: k[:22],
           f"ATTEMPTS-UNTIL-UPGRADE per dungeon, +{dungeon_kl_range[0]}.."
           f"+{dungeon_kl_range[1]} (n = #upgrades):")

    print("\n  NOTE: the two views differ because 'attempts-until-upgrade' is "
          "conditional on\n        an upgrade eventually happening; key levels you "
          "never timed contribute\n        0 rows there but are fully counted in the "
          "TOTAL view.")


# ---------------------------------------------------------------------------
# 4. Composition
# ---------------------------------------------------------------------------

CORE = [('Augmentation', 'Evoker'),
        ('Unholy',       'Death Knight'),
        ('Devourer',       'Demon Hunter')]


def _core_trio(rec):
    return all(has_spec(rec, s, c) for s, c in CORE)


def _support_pair(rec):
    heal = has_spec(rec, 'Mistweaver', 'Monk') or has_spec(rec, 'Restoration', 'Druid')
    tank = has_spec(rec, 'Brewmaster', 'Monk') or has_spec(rec, 'Guardian', 'Druid')
    return heal and tank


def section_comp(recs):
    print("\n" + "=" * 78)
    print("4) COMPOSITION PREVALENCE")
    print("=" * 78)

    def report(label, subset):
        if not subset:
            print(f"\n  {label}: no runs in this subset")
            return
        c1 = [r for r in subset if _core_trio(r)]
        c2 = [r for r in c1 if _support_pair(r)]
        n = len(subset)
        print(f"\n  {label} (n={n})")
        print(f"    Aug Evoker + Unholy DK + Devourer DH               : "
              f"{100.0 * len(c1) / n:5.1f}%  ({len(c1)}/{n})")
        print(f"    ... + (MW Monk | Resto Druid) + (BrM Monk | Guard.): "
              f"{100.0 * len(c2) / n:5.1f}%  ({len(c2)}/{n})")
        missing = [r for r in subset if not _core_trio(r)]
        if missing:
            print("    Runs WITHOUT the core trio:")
            for r in missing:
                miss = [f"{s} {c}" for s, c in CORE if not has_spec(r, s, c)]
                print(f"      {r['ts'][:10]} {r['dungeon']} +{r['kl']}  "
                      f"missing: {', '.join(miss)}")

    report("Score-upgrade keys", [r for r in recs if r['upgrade']])
    report("All timed keys",     [r for r in recs if r['timed']])
    report("All logged runs",    recs)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def print_statistics(csv_file, player_scores=None, my_name="Powerpegging",
                     min_key_level=18):
    if not os.path.isfile(csv_file):
        print(f"No file '{csv_file}' found.")
        return

    recs = load_records(csv_file, player_scores, my_name, min_key_level)
    if not recs:
        print("No runs at or above the minimum key level.")
        return

    n_scored = sum(1 for r in recs
                   if all(p['score'] is not None for p in r['players']))
    print("\n" + "=" * 78)
    print(f"STATISTICAL ANALYSIS  —  {len(recs)} runs at +{min_key_level} or higher, "
          f"{n_scored} with full score data")
    print("=" * 78)

    section_correlations(recs, my_name)
    section_effort(recs)
    section_comp(recs)

    print("\n" + "=" * 78)
    print("CAVEATS")
    print("=" * 78)
    print("""  * Key level confounds success vs score: stronger groups push higher keys,
    which are harder. Always read the 'partial r|kl' column, not the raw r.
  * Scores are END-OF-SEASON (a single snapshot), while the runs span the whole
    season. A player's score at the time of the run was lower. This makes the
    score an outcome as well as a predictor -> reverse causality is likely
    (timing keys raises your score), so treat these as associations only.
  * Runs are not independent: the same handful of players recur, and multiple
    attempts on the same key share a group and a night. p-values are optimistic.
  * 'Success' comes from the completion heuristic in logrun.py, which infers
    completion from duration + final-boss pulls; it is not ground truth.
  * Composition percentages are conditional on your own pug/premade habits, not
    a measure of which comps work.""")


if __name__ == '__main__':
    import sys
    print_statistics(sys.argv[1] if len(sys.argv) > 1 else "logsummary_rio.csv")
'''