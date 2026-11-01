# Homology modelling of ABCA1 variants

Built during my Computer Science and Biosciences degree at IIIT-Delhi (2023). It builds 3D models of ABCA1 missense variants (`Y159N.fasta`, `V825I.fasta`) from the cryo-EM structure of human ABCA1 (PDB [5XJY](https://www.rcsb.org/structure/5XJY), chain A), using [MODELLER](https://salilab.org/modeller/).

| Step | Script | Output |
|---|---|---|
| Align target to template | `align2D.py` | `Target-template.ali` / `.pap` |
| Build 5 models, scored by DOPE and GA341 | `build.py` | `*.B9999000*.pdb`, `build.log` |
| Per-residue DOPE energy profile of a built model | `evaluate.py` | `Target.profile`, `Template.profile` |
| Compare target and template energy profiles | `plot_profiles.py` | plot |

Requires MODELLER (free academic licence) and matplotlib. The modelled structures feed the docking in [Virtual-Screening](https://github.com/aryanteng/Virtual-Screening). Archived: kept for reference, not maintained.
