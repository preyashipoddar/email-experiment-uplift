# Project instructions for Claude

Analysis of the Hillstrom email experiment (64,000 customers; arms: Mens E-Mail, Womens E-Mail,
No E-Mail; outcomes `visit`, `conversion`, `spend` two weeks after the send). Python only.

## How Claude helps here: TUTOR MODE

The owner is building this to learn it and to be able to defend every line in an interview.
- Explain concepts, review her code, give hints, point to the right function or paper.
- **Do not write implementations for her unless she explicitly asks for code on that step.**
  Small snippets to illustrate an idea are fine; full notebook cells are not.
- `plan/preregistration.md` must be written by her. Claude may ask questions that sharpen it,
  never draft it.

## The pre-registration rule — check before every analysis step

**No outcome column (`visit`, `conversion`, `spend`) may be summarized by arm until
`plan/preregistration.md` is filled in and committed.** Check with
`git log --oneline -- plan/preregistration.md`. Before that commit, only these are allowed:
arm counts, covariates, and outcome distributions POOLED with arms hidden (for blinded power).
If asked to do something that would reveal an effect early, say so and stop.

## Order of work

1. Pre-registration (hypotheses; primary metric spend per customer; Holm across the two
   email-vs-control comparisons; Welch t + bootstrap; heavy-tail rule chosen blind; segments
   named in advance; CUPED covariate `history`; decision rule)
2. `notebooks/01-checks` — SRM (chi-square vs 1/3 each), standardized mean differences, blinded MDE
3. `notebooks/02-aa-peeking` — control arm split into fake arms, 20 looks, ~2,000 sims;
   false-positive rate fixed vs peeking vs an O'Brien-Fleming-shaped boundary `c*sqrt(K/k)`
   with `c` calibrated by simulation (look order is simulated; there are no timestamps)
4. `notebooks/03-ab-analysis` — run the plan exactly; report nulls; CUPED variance reduction
5. `notebooks/04-uplift` — T-learner (gradient boosting), 50/50 split stratified by arm, Qini
   on held-out half; no oversampling of the rare class
6. `notebooks/05-decision` — three policies; value = margin x incremental spend - cost x emails;
   report the break-even contact cost across a margin sweep (do not invent an email cost)
7. `plan/followup-test.md`, `memo.md`, README results, `tests/` for `src/abtools.py`

## Honesty rules

- She **analyzed** this experiment; she did not design, run or launch it. Never write otherwise.
- The follow-up test is a **proposed** design.
- Report every pre-registered result, including nulls. Anything not in the plan is "exploratory".
- Raw data quirk to note, not silently fix: `zip_code` spells Suburban as `Surburban`.
