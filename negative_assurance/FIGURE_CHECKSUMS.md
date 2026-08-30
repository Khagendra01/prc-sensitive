# Original exploratory figure checksums

The four original PNGs were generated in the ChatGPT execution environment.
The GitHub connector used for this handoff only supports UTF-8 file writes, so
their binary bytes could not be pushed directly without a corruption risk.

The underlying CSVs are committed, and `regenerate_figures.py` recreates all
four figures. The hashes below identify the original PNG binaries produced
during the exploratory runs.

| Figure | Original size | SHA-256 |
|---|---:|---|
| `p0a/p0a_negative_probability_by_quirk.png` | 108331 bytes | `d289333427f0972cf4a2bbb2519799bb4a6171bdf3666827ffea51f76eddecac` |
| `p0b_pando/p0b_whitebox_uplift_by_condition.png` | 81619 bytes | `1b8b426de09e31437a169d3fbe36770a2c6f35cb655d57562c77f9e765205812` |
| `p0c_ood/p0c_predicted_vs_observed_failure.png` | 93373 bytes | `2cdbee3c266426203d4bb0081ca2e5343a956ddcd7464b1fa23163af204acadd` |
| `p1a_prospective/selective_assurance.png` | 67394 bytes | `50f374e614cec8ce8a33f0594d0528d2431578a149e8add4081f644b84d79288` |

## Local step

```bash
python negative_assurance/regenerate_figures.py
git add negative_assurance/*/*.png
git commit -m "Regenerate negative-assurance figures"
git push origin negative-assurance-side-research
```

The regenerated PNG byte hashes may differ across matplotlib versions even
when the plotted data are identical, because PNG metadata/rendering can vary.
The CSVs are the authoritative numerical artifacts.
