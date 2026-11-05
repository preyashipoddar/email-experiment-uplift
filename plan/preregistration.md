# Pre-registration

*To be written and committed before any outcome is summarized by arm.*

## Hypotheses
H1: The Mens e-mail changes spend per customer compared with no e-mail.
H2: The Womens e-mail changes spend per customer compared with no e-mail.
Both are tested two-sided, because an e-mail can lower spend as well as raise it (annoyance,
unsubscribes, customers waiting for a sale), and a one-sided test could not detect that.
Null for each: no difference in mean spend per customer between the e-mail arm and no e-mail.

## Primary metric
Spend per customer (`spend`) over the two weeks after the send, averaged over every customer in
the arm, including the ones who spent $0.
I chose spend over conversion because it is the only outcome that can be weighed against the cost
of sending an email, and conversion says whether someone bought but not how much.

## Secondary and diagnostic metrics
Secondary: conversion (`conversion`). Diagnostic: site visit (`visit`). Visits are far more common
than purchases, so the test can detect much smaller changes in them, and they show whether the
email reached people at all.
Secondary and diagnostic metrics are reported with confidence intervals and no multiple-testing
correction, as supporting evidence only. The decision rests on the primary metric alone.

## Comparisons and multiple-testing correction
Two primary comparisons: Mens vs No E-Mail, and Womens vs No E-Mail. The Holm correction is
applied across these two at a family-wise α of 0.05, so the stricter of the two is tested at 0.025.
Mens vs Womens is exploratory. I will report the difference and its confidence interval, but it
is not a pre-registered test and is not part of the Holm family. Making it a third comparison
would raise the MDE on the main question in order to answer a secondary one.

## Statistical tests
Primary: Welch's t-test on spend per customer for each comparison, two-sided, because it does not
assume the arms have equal variance and e-mail arms may vary more.
Robustness check: a bootstrap confidence interval for each difference in means, resampling
customers within each arm, 10,000 resamples, fixed random seed.
If the two disagree, Welch's t-test is the result of record and both are reported.

## Heavy-tail handling (chosen blind)
With arms hidden, 99.1% of customers spent $0, so a 99th-percentile cap would equal $0 and remove
every purchase.
Among the 578 buyers, spend runs from $29.99 to $499, and several buyers sit at exactly $499
(observed during the blinded check; not recorded in notebook 01-checks), which suggests the
file is already top-coded.
Decision: no additional cap. I will analyze raw spend and check the result with a bootstrap
confidence interval.
I made this choice before looking at any outcome by arm, because a cap picked after seeing
results could be chosen, consciously or not, to make one email look better.

## Pre-specified segments
Only these segments are analyzed as pre-registered. Anything else is labelled exploratory.
- `newbie`: new customer in the past 12 months vs returning
- `channel`: Phone / Web / Multichannel
- `mens` and `womens`: whether the customer had bought from that category before
- `history_segment`, collapsed into three groups: under $100 (band 1, 22,970 customers),
  $100 to $350 (bands 2 to 3, 26,543), and $350 and over (bands 4 to 7, 14,487). Chosen from
  covariate counts alone to give the most even group sizes.

Each segment is tested with an e-mail by segment interaction term in a regression, not with
separate t-tests per group. Segment results are secondary: each group is smaller than a full
arm, so its MDE is larger (about 2.1 times the full-sample MDE for the smallest history group),
and a null within a segment is not evidence of no effect there.

## Variance reduction (CUPED)
Covariate: `history` (dollars spent in the year before the send). It was measured before the
e-mail, so the e-mail cannot have affected it.
θ = cov(spend, history) / var(history), estimated pooled across all arms.
Adjusted spend = spend − θ × (history − mean history).
The plain (unadjusted) estimate is the result of record, because the MDE above was computed for
it. The CUPED estimate is reported alongside it, with the variance reduction and how much the
confidence intervals narrowed. If `history` predicts two-week spend weakly, I will report the
small gain as it is.

## Minimum detectable effect (blinded)
Computed from pooled data with arms hidden: two-sided α = 0.025 (the strictest Holm step, 0.05
split over 2 comparisons), power = 0.80, n = 21,306 per arm (the smallest arm).
Spend: MDE = $0.45 per customer, about 43% of mean spend ($1.05).
Conversion: MDE = 0.28 percentage points, about 31% of the pooled rate (0.90%).
A non-significant result will not show that an email has no effect. It will mean the test could
not tell the effect apart from zero, and I will report the confidence interval to show which
effect sizes the data rule out.

## Decision rule
- If an e-mail's Holm-adjusted p-value is below 0.05 and its effect is positive, that e-mail works.
  If both work, I recommend the one with the larger estimated effect and note that the difference
  between them is exploratory.
- If an e-mail's Holm-adjusted p-value is below 0.05 and its effect is negative, I recommend not
  sending it.
- If neither is significant, I will not conclude that the e-mails do not work. I will report the
  confidence intervals, state which effect sizes they rule out, and recommend a follow-up test.
- Who to send to (everyone, a pre-registered segment, or the top share of customers by predicted
  uplift) is decided later, on a held-out half of the data, by comparing those policies across a
  range of contact costs and margins and reporting the break-even contact cost. No contact cost is
  assumed.
