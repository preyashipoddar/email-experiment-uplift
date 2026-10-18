# Email experiment: from A/B test to targeting decision

Analysis of a randomized email experiment on 64,000 retail customers (Kevin Hillstrom's
MineThatData E-Mail Analytics challenge, 2008): did each email work, for whom, and who should
be emailed once the cost of contact is counted.

**Status: in progress.** The analysis plan is pre-registered in `plan/preregistration.md` and
committed before any outcome is opened; the commit history is the record.

## Planned work

1. Randomization checks: sample ratio mismatch, covariate balance, blinded power
2. A/A simulation on the control arm: how often repeated peeking declares a false winner, and a
   sequential boundary calibrated by simulation
3. A/B analysis: effects per arm, Holm correction, bootstrap intervals, CUPED
4. Uplift model (T-learner) scored with a Qini curve on held-out data
5. Decision: email everyone vs best segment vs top X% by predicted uplift, with a break-even
   contact cost
6. Design of the follow-up test

## Data

`python scripts/get_data.py` downloads the CSV to `data/raw/` (not committed).
