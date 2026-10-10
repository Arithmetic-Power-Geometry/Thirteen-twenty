# Reference-by-reference literature prose and citation mapping

Date: 2026-10-10. Source of truth: `references/lonely_runner.bib` (31 records). Each entry below has a paper-ready paraphrase, an appropriate experiment mapping, a citation key, and a bibliography record derived from the repository. The prose is deliberately cautious: a title/abstract does not justify attributing unverified theorem details. Suggested experiment ranges are topical cross-references, **not a claim that every report already contains a citation to that source**. Citations should be inserted only where the paper actually discusses the corresponding result.

## Reusable introduction prose

The lonely runner problem originated in Diophantine approximation and was reformulated geometrically as a view-obstruction question. It asks whether, for any set of distinct constant runner speeds, each runner has a time at which all others are at least the reciprocal of the total number of runners away around the unit circle. Foundational contributions by Wills and Cusick, subsequent small-runner results, and later geometric, analytic, and computational approaches provide the context for this question. Modern research addresses bounded-runner cases, loneliness spectra, tight configurations, finite-checking reductions, and shifted variants, but these developments must not be conflated with an unrestricted proof. \cite{Wills1967Original,Cusick1973ViewObstruction,PerarnauSerra2025Survey,MalikiosisSantosSchymura2025}

## Annotated entries

### 1. PerarnauSerra2016

**Source:** Perarnau, Guillem and Serra, Oriol}, title = {Correlation Among Runners and Some Results on the Lonely Runner Conjecture (2016}, volume = {23). *Correlation Among Runners and Some Results on the Lonely Runner Conjecture}, journal = {The Electronic Journal of Combinatorics*. DOI: https://doi.org/10.37236/5123}, url = {https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i1p50

**Role:** Pairwise correlations and overlap inequalities.

**Paper-ready prose:** Perarnau and Serra study correlations between runner positions and derive bounds relevant to simultaneous separation. This is the appropriate prior-work citation for the overlap, spanning-tree and Bonferroni-based certificates; in particular, the spanning-tree method in Experiment 49 must not be presented as a new inequality. \\cite{PerarnauSerra2016}

**Relevant experiment themes:** 41–42, 49–52.

**BibTeX citation:** `\\cite{PerarnauSerra2016}`.

### 2. Tao2018

**Source:** Tao, Terence}, title = {Some remarks on the lonely runner conjecture (2018}, volume = {13). *Some remarks on the lonely runner conjecture}, journal = {Contributions to Discrete Mathematics*. DOI: https://doi.org/10.55016/ojs/cdm.v13i2.62728}, url = {https://cdm.ucalgary.ca/article/view/62728

**Role:** General lower bounds and analytic techniques.

**Paper-ready prose:** Tao develops bounds and observations concerning the lonely runner problem. Cite this work when discussing analytic lower bounds, the difficulty of the sharp threshold, and the distinction between partial bounds and the full conjecture. \\cite{Tao2018}

**Relevant experiment themes:** 25–36, 51.

**BibTeX citation:** `\\cite{Tao2018}`.

### 3. GiriKravitz2025

**Source:** Giri, Vikram and Kravitz, Noah}, title = {The structure of {Lonely Runner (2026}, doi = {10.1017/S0305004125101497). *The structure of {Lonely Runner} spectra*. DOI: https://doi.org/10.1017/S0305004125101497}, eprint = {2304.01462

**Role:** Maximum-loneliness spectra and structural restrictions.

**Paper-ready prose:** Giri and Kravitz investigate the possible values of maximum loneliness and structural aspects of these spectra. The paper provides background for critical-value and rational-rank experiments; do not infer that it settles the conjecture. \\cite{GiriKravitz2025}

**Relevant experiment themes:** 43–47, 53–55.

**BibTeX citation:** `\\cite{GiriKravitz2025}`.

### 4. BeckEverett2026

**Source:** Beck, Matthias and Everett, Samuel}, title = {Lonely Runner Relations (2026}, eprint = {2609.06259). *Lonely Runner Relations}, year = {2026*. https://arxiv.org/abs/2609.06259}, note = {Preprint; publication status not verified

**Role:** Short integer relations and rigidity.

**Paper-ready prose:** Beck and Everett analyze integer relations among speed configurations. The connection to Experiment 45 is direct: its exclusion test invokes a published short-relation theorem and should be identified as a corollary rather than a new unconditional proof. \\cite{BeckEverett2026}

**Relevant experiment themes:** 45, 51, 56–58.

**BibTeX citation:** `\\cite{BeckEverett2026}`.

### 5. Jensen2026

**Source:** Jensen, Alathea}, title = {Mixed thresholds in the Lonely Runner Conjecture (2026}, eprint = {2605.27941). *Mixed thresholds in the Lonely Runner Conjecture}, year = {2026*. https://arxiv.org/abs/2605.27941}, note = {Preprint; publication status not verified

**Role:** Mixed-threshold variants.

**Paper-ready prose:** Jensen studies a mixed-threshold form of the runner problem. Cite this work when comparing uniform separation thresholds with runner-dependent constraints, not as proof of the standard conjecture. \\cite{Jensen2026}

**Relevant experiment themes:** 25–35 (threshold context).

**BibTeX citation:** `\\cite{Jensen2026}`.

### 6. Allikvere2026

**Source:** Allikvere, Jaan}, title = {Fourteen and fifteen lonely runners (2026}, eprint = {2609.02604). *Fourteen and fifteen lonely runners}, year = {2026*. https://arxiv.org/abs/2609.02604}, note = {Version 2; reports proofs for fourteen and fifteen total runners, not sixteen

**Role:** Computer-assisted higher-runner results.

**Paper-ready prose:** Allikvere reports computer-assisted results for fourteen and fifteen runners. The result should be described using the paper's own runner-count convention and should not be extrapolated to all dimensions. \\cite{Allikvere2026}

**Relevant experiment themes:** Research status; 36–58.

**BibTeX citation:** `\\cite{Allikvere2026}`.

### 7. Zhang2026

**Source:** Zhang, Yuhan}, title = {Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound (2026}, eprint = {2608.13599). *Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound}, year = {2026*. https://arxiv.org/abs/2608.13599}, note = {Version 2 title; preprint

**Role:** Tight configurations and modified instances.

**Paper-ready prose:** Zhang studies tight instances, including modifications and infinite-family behavior. Cite this for equality cases and classification questions; computational observations about tightness must be distinguished from established general classifications. \\cite{Zhang2026}

**Relevant experiment themes:** 46–47, 53–55.

**BibTeX citation:** `\\cite{Zhang2026}`.

### 8. Rosenfeld2025

**Source:** Rosenfeld, Matthieu}, title = {The lonely runner conjecture holds for eight runners (2025}, eprint = {2509.14111). *The lonely runner conjecture holds for eight runners}, year = {2025*. https://arxiv.org/abs/2509.14111}, note = {Initial preprint title and author verified; inspect version history and any later publication before submission

**Role:** Eight-runner case.

**Paper-ready prose:** Rosenfeld's preprint addresses the eight-runner case. Cite it only for the specific bounded-runner result reported in the preprint, noting that publication status may change. \\cite{Rosenfeld2025}

**Relevant experiment themes:** Research status.

**BibTeX citation:** `\\cite{Rosenfeld2025}`.

### 9. SungkawichaiTrakulthongchai2026

**Source:** Sungkawichai, Touch and Trakulthongchai, Tanupat}, title = {Eleven, twelve, and thirteen lonely runners (2026}, eprint = {2604.23906). *Eleven, twelve, and thirteen lonely runners}, year = {2026*. https://arxiv.org/abs/2604.23906}, note = {Computer-assisted preprint, initially submitted 26 April 2026

**Role:** Eleven through thirteen runners.

**Paper-ready prose:** Sungkawichai and Trakulthongchai report computer-assisted results for eleven, twelve and thirteen runners. Cite as bounded-runner progress, not as an unrestricted theorem. \\cite{SungkawichaiTrakulthongchai2026}

**Relevant experiment themes:** Research status.

**BibTeX citation:** `\\cite{SungkawichaiTrakulthongchai2026}`.

### 10. PerarnauSerra2025Survey

**Source:** Perarnau, Guillem and Serra, Oriol}, title = {The lonely runner conjecture turns 60 (2025}, volume = {58). *The lonely runner conjecture turns 60}, journal = {Computer Science Review*. DOI: https://doi.org/10.1016/j.cosrev.2025.100798}, url = {https://doi.org/10.1016/j.cosrev.2025.100798

**Role:** Survey and historical synthesis.

**Paper-ready prose:** Perarnau and Serra survey the conjecture's history, equivalent formulations, partial results, and connections to discrete geometry and approximation. This is the preferred broad contextual citation for the introduction and research-gap section. \\cite{PerarnauSerra2025Survey}

**Relevant experiment themes:** 11–58, introduction.

**BibTeX citation:** `\\cite{PerarnauSerra2025Survey}`.

### 11. Trakulthongchai2026NineTen

**Source:** Trakulthongchai, Tanupat}, title = {Nine and Ten Lonely Runners (2026}, volume = {33). *Nine and Ten Lonely Runners}, journal = {The Electronic Journal of Combinatorics*. DOI: https://doi.org/10.37236/14972}, url = {https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i2p46

**Role:** Nine- and ten-runner cases.

**Paper-ready prose:** Trakulthongchai treats the nine- and ten-runner cases. Cite when documenting the progression of verified finite-runner results; avoid conflating runners with the number of relative speeds. \\cite{Trakulthongchai2026NineTen}

**Relevant experiment themes:** Research status.

**BibTeX citation:** `\\cite{Trakulthongchai2026NineTen}`.

### 12. Rosenfeld2025Nine

**Source:** Rosenfeld, Matthieu}, title = {The lonely runner conjecture holds for nine runners (2025}, eprint = {2512.01912). *The lonely runner conjecture holds for nine runners}, year = {2025*. https://arxiv.org/abs/2512.01912}, note = {Preprint; journal publication status not verified

**Role:** Independent nine-runner preprint.

**Paper-ready prose:** Rosenfeld studies the nine-runner case in a separate preprint. Cite as a distinct source only when comparing proof methods or chronology, rather than duplicating a single progress claim. \\cite{Rosenfeld2025Nine}

**Relevant experiment themes:** Research status.

**BibTeX citation:** `\\cite{Rosenfeld2025Nine}`.

### 13. BarajasSerra2008

**Source:** Barajas, Javier and Serra, Oriol}, title = {The Lonely Runner with Seven Runners (2008}, volume = {15). *The Lonely Runner with Seven Runners}, journal = {The Electronic Journal of Combinatorics*. DOI: https://doi.org/10.37236/772}, url = {https://www.combinatorics.org/ojs/index.php/eljc/article/view/v15i1r48

**Role:** Classical seven-runner theorem.

**Paper-ready prose:** Barajas and Serra prove the seven-runner case of the classical conjecture. This is a foundational bounded-dimension result and should appear in historical context. \\cite{BarajasSerra2008}

**Relevant experiment themes:** Introduction; dimension-specific context.

**BibTeX citation:** `\\cite{BarajasSerra2008}`.

### 14. MalikiosisSantosSchymura2025

**Source:** Malikiosis, Romanos Diogenes and Santos, Francisco and Schymura, Matthias}, title = {Linearly exponential checking is enough for the lonely runner conjecture and some of its variants (2025}, volume = {13). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants}, journal = {Forum of Mathematics, Sigma*. DOI: https://doi.org/10.1017/fms.2025.10107}, eprint = {2411.06903

**Role:** Finite-checking reductions and zonotopes.

**Paper-ready prose:** Malikiosis, Santos and Schymura establish finite-checking reductions and study shifted variants via geometric formulations. Cite when describing exact decision methods; their theorem does not make an arbitrary finite experimental search an all-dimensional proof. \\cite{MalikiosisSantosSchymura2025}

**Relevant experiment themes:** 37, 43, 46–47, 54–56.

**BibTeX citation:** `\\cite{MalikiosisSantosSchymura2025}`.

### 15. Bedert2025Riesz

**Source:** Bedert, Benjamin}, title = {Riesz products and the {Lonely Runner Conjecture (2025}, eprint = {2511.16636). *Riesz products and the {Lonely Runner Conjecture}: A wider gap of loneliness*. https://arxiv.org/abs/2511.16636}, note = {arXiv v1, submitted 20 November 2025

**Role:** Riesz-product analytic bounds.

**Paper-ready prose:** Bedert uses Riesz-product methods to investigate improved loneliness bounds. Cite when discussing harmonic-analytic strategies, especially alongside the Fourier baseline; the preprint is not a proof of the full conjecture. \\cite{Bedert2025Riesz}

**Relevant experiment themes:** 36.

**BibTeX citation:** `\\cite{Bedert2025Riesz}`.

### 16. BlancoCriadoSantos2026

**Source:** Blanco, M{\'o}nica and Criado, Francisco and Santos, Francisco (2026}, eprint = {2603.24784). *Coloopless zonotopes and counterexamples to the {Shifted Lonely Runner Conjecture}*. https://arxiv.org/abs/2603.24784v2}, note = {arXiv v2, revised 27 April 2026; shifted conjecture is distinct from ordinary LRC

**Role:** Shifted conjecture counterexamples.

**Paper-ready prose:** Blanco, Criado and Santos investigate zonotopes and counterexamples to a shifted lonely-runner formulation. Cite this to separate shifted from ordinary LRC; shifted counterexamples are not classical counterexamples. \\cite{BlancoCriadoSantos2026}

**Relevant experiment themes:** 40–42, 58.

**BibTeX citation:** `\\cite{BlancoCriadoSantos2026}`.

### 17. Cordella2026

**Source:** Cordella, Francesco}, title = {Odd denominators in the {Lonely Runner (2026}, eprint = {2609.03444). *Odd denominators in the {Lonely Runner} spectrum for six speeds*. https://arxiv.org/abs/2609.03444v2}, note = {arXiv v2, revised 8 September 2026

**Role:** Spectrum denominators.

**Paper-ready prose:** Cordella studies odd denominators in the loneliness spectrum for six speeds. Cite for arithmetic restrictions on candidate maximum-loneliness values and comparison with exact rational optimizers. \\cite{Cordella2026}

**Relevant experiment themes:** 46–47, 53–55.

**BibTeX citation:** `\\cite{Cordella2026}`.

### 18. BohmanHolzmanKleitman2001

**Source:** Bohman, Tom and Holzman, Ron and Kleitman, Dan}, title = {Six Lonely Runners (2001}, volume = {8). *Six Lonely Runners}, journal = {The Electronic Journal of Combinatorics*. DOI: https://doi.org/10.37236/1602}, url = {https://www.combinatorics.org/ojs/index.php/eljc/article/view/v8i2r3

**Role:** Six-runner case and foundational methods.

**Paper-ready prose:** Bohman, Holzman and Kleitman establish a classical small-runner result and develop relevant structural ideas. Cite in the progression of dimension-specific results and in the reduction to integer-speed formulations where the paper is directly used. \\cite{BohmanHolzmanKleitman2001}

**Relevant experiment themes:** 11–24; introduction.

**BibTeX citation:** `\\cite{BohmanHolzmanKleitman2001}`.

### 19. BeckSchymura2024

**Source:** Beck, Matthias and Schymura, Matthias}, title = {Deep Lattice Points in Zonotopes, Lonely Runners, and Lonely Rabbits (2024}, volume = {2024). *Deep Lattice Points in Zonotopes, Lonely Runners, and Lonely Rabbits}, journal = {International Mathematics Research Notices*. DOI: https://doi.org/10.1093/imrn/rnad232}, eprint = {2301.12182

**Role:** Zonotope geometry and lonely runners.

**Paper-ready prose:** Beck and Schymura connect the problem with lattice points and zonotopes. Cite when moving from modular witnesses to discrete geometry; distinguish their geometric reductions from a complete solution. \\cite{BeckSchymura2024}

**Relevant experiment themes:** 37–45.

**BibTeX citation:** `\\cite{BeckSchymura2024}`.

### 20. BieniaGoddynGvozdjakSeboTarsi1998

**Source:** Bienia, Wojciech and Goddyn, Luis and Gvozdjak, Pavol and Seb{\H{o} (1998}, volume = {72). *Flows, View Obstructions, and the Lonely Runner}, journal = {Journal of Combinatorial Theory, Series B*. DOI: https://doi.org/10.1006/jctb.1997.1770}, url = {https://doi.org/10.1006/jctb.1997.1770

**Role:** Flows and view obstructions.

**Paper-ready prose:** Bienia and coauthors connect lonely runners to flow and view-obstruction formulations. Cite for historical equivalences and structural viewpoints, not as a source for later numerical experiments. \\cite{BieniaGoddynGvozdjakSeboTarsi1998}

**Relevant experiment themes:** 11–24, 39–40.

**BibTeX citation:** `\\cite{BieniaGoddynGvozdjakSeboTarsi1998}`.

### 21. Poliakova2026Shifted

**Source:** Poliakova, Daria}, title = {More (shifted) runners, less loneliness (2026}, eprint = {2609.23952). *More (shifted) runners, less loneliness}, year = {2026*. https://arxiv.org/abs/2609.23952v1}, note = {Preprint, version 1, submitted 20 September 2026; shifted problem only

**Role:** Shifted runner variants.

**Paper-ready prose:** Poliakova studies a shifted variant of runner separation. The shifted setting differs from the classical common-start formulation, so claims must remain explicitly scoped. \\cite{Poliakova2026Shifted}

**Relevant experiment themes:** 40–42.

**BibTeX citation:** `\\cite{Poliakova2026Shifted}`.

### 22. Rifford2021LonelyTime

**Source:** Rifford, Ludovic}, title = {On the time for a runner to get lonely (2021}, eprint = {2111.13688). *On the time for a runner to get lonely}, year = {2021*. https://arxiv.org/abs/2111.13688}, note = {arXiv preprint; first submitted 25 November 2021

**Role:** Time-to-loneliness questions.

**Paper-ready prose:** Rifford studies the timing of runner separation. Cite for witness-time and time-bound questions, which are logically different from proving existence at the sharp threshold. \\cite{Rifford2021LonelyTime}

**Relevant experiment themes:** 37–43.

**BibTeX citation:** `\\cite{Rifford2021LonelyTime}`.

### 23. Czerwinski2012Random

**Source:** Czerwi{\'n}ski, Sebastian (2012}, volume = {119). *Random runners are very lonely}, journal = {Journal of Combinatorial Theory, Series A*. DOI: https://doi.org/10.1016/j.jcta.2012.02.002}, eprint = {1102.4464

**Role:** Probabilistic runner configurations.

**Paper-ready prose:** Czerwiński analyzes random speed configurations. Cite for typical-case or probabilistic behavior, never as a worst-case guarantee for all speed sets. \\cite{Czerwinski2012Random}

**Relevant experiment themes:** 24, 29–35.

**BibTeX citation:** `\\cite{Czerwinski2012Random}`.

### 24. FanSun2026Amending

**Source:** Fan, Ho Tin and Sun, Alec}, title = {Amending the Lonely Runner Spectrum Conjecture (2026}, volume = {33). *Amending the Lonely Runner Spectrum Conjecture}, journal = {The Electronic Journal of Combinatorics*. DOI: https://doi.org/10.37236/13840}, url = {https://doi.org/10.37236/13840

**Role:** Loneliness spectrum and critical-time characterization.

**Paper-ready prose:** Fan and Sun amend a proposed description of the loneliness spectrum and develop critical-time information. Cite before presenting finite critical-time maximization or endpoint tests, to distinguish computational implementations from earlier mathematics. \\cite{FanSun2026Amending}

**Relevant experiment themes:** 43, 46–47, 54–55.

**BibTeX citation:** `\\cite{FanSun2026Amending}`.

### 25. AlcantaraCriadoSantos2026Zonotopes

**Source:** Alc{\'a}ntara, David and Criado, Francisco and Santos, Francisco (2026}, doi = {10.1080/10586458.2026.2651085). *Covering Radii of 3-Zonotopes and the Shifted Lonely Runner Conjecture}, journal = {Experimental Mathematics*. DOI: https://doi.org/10.1080/10586458.2026.2651085}, url = {https://doi.org/10.1080/10586458.2026.2651085

**Role:** Three-zonotope covering radii and shifted LRC.

**Paper-ready prose:** Alcántara, Criado and Santos analyze covering radii of three-dimensional zonotopes in relation to shifted LRC. The shifted problem must be explicitly distinguished from the original conjecture. \\cite{AlcantaraCriadoSantos2026Zonotopes}

**Relevant experiment themes:** 55.

**BibTeX citation:** `\\cite{AlcantaraCriadoSantos2026Zonotopes}`.

### 26. BeckHostenSchymura2016Polyhedra

**Source:** Beck, Matthias and Hosten, Serkan and Schymura, Matthias}, title={Lonely Runner Polyhedra (2016}, eprint={1606.01783). *Lonely Runner Polyhedra}, year={2016*. https://arxiv.org/abs/1606.01783}, note={Preprint metadata verified; check for subsequent journal version before submission

**Role:** Polyhedral viewpoint.

**Paper-ready prose:** Beck, Hosten and Schymura study lonely-runner polyhedra. Cite for polyhedral formulations and modular families; the paper is not evidence that a prime-shift lifting lemma is new. \\cite{BeckHostenSchymura2016Polyhedra}

**Relevant experiment themes:** 37–45, 57.

**BibTeX citation:** `\\cite{BeckHostenSchymura2016Polyhedra}`.

### 27. Wills1967Original

**Source:** Wills, J{\"o}rg M. (1967}, volume = {71). *Zwei S{\"a}tze {\"u*. DOI: https://doi.org/10.1007/BF01298332}, url = {https://doi.org/10.1007/BF01298332

**Role:** Historical origin.

**Paper-ready prose:** Wills's work on inhomogeneous Diophantine approximation is a foundational historical source. Cite in the first statement of the conjecture's origin, alongside Cusick's view-obstruction formulation. \\cite{Wills1967Original}

**Relevant experiment themes:** Introduction; 11–24.

**BibTeX citation:** `\\cite{Wills1967Original}`.

### 28. CusickPomerance1984

**Source:** Cusick, Thomas W. and Pomerance, Carl}, title = {View-obstruction problems, {III (1984}, volume = {19). *View-obstruction problems, {III}*. DOI: https://doi.org/10.1016/0022-314X(84)90097-0}, url = {https://doi.org/10.1016/0022-314X(84)90097-0

**Role:** Classical view-obstruction bounds.

**Paper-ready prose:** Cusick and Pomerance study view-obstruction problems and contribute to the early development of the conjecture. Cite in the history of established small-dimension cases and geometric reformulations. \\cite{CusickPomerance1984}

**Relevant experiment themes:** Introduction; 11–24.

**BibTeX citation:** `\\cite{CusickPomerance1984}`.

### 29. Kravitz2021Barely

**Source:** Kravitz, Noah}, title = {Barely lonely runners and very lonely runners: a refined approach to the {Lonely Runner Problem (2021}, volume = {1). *Barely lonely runners and very lonely runners: a refined approach to the {Lonely Runner Problem}*. DOI: https://doi.org/10.5070/C61055383}, url = {https://doi.org/10.5070/C61055383

**Role:** Refined loneliness-spectrum conjecture.

**Paper-ready prose:** Kravitz formulates a stronger conjectural structure for maximum loneliness and proves selected cases. This is particularly relevant when discussing tightness, discrete spectrum values, and gaps above the standard threshold; do not claim the refined conjecture is proved generally. \\cite{Kravitz2021Barely}

**Relevant experiment themes:** 46–47, 53–55.

**BibTeX citation:** `\\cite{Kravitz2021Barely}`.

### 30. Cusick1973ViewObstruction

**Source:** Cusick, Thomas W.}, title = {View-obstruction problems (1973}, volume = {9). *View-obstruction problems}, journal = {Aequationes Mathematicae*. DOI: https://doi.org/10.1007/BF01832623}, url = {https://doi.org/10.1007/BF01832623

**Role:** View-obstruction formulation.

**Paper-ready prose:** Cusick's work introduces a geometric view-obstruction formulation connected to the lonely runner problem. Cite for the historical equivalence and geometric motivation. \\cite{Cusick1973ViewObstruction}

**Relevant experiment themes:** Introduction; 11–24.

**BibTeX citation:** `\\cite{Cusick1973ViewObstruction}`.

### 31. GoddynWong2006Tight

**Source:** Goddyn, Luis and Wong, Erick B.}, title = {Tight instances of the lonely runner (2006}, volume = {6). *Tight instances of the lonely runner}, journal = {Integers*. https://www.sfu.ca/~goddyn/Papers/063tight_lonely_runner.pdf}, note = {14 pages; journal article archived by the authors and at Zenodo record 8275490

**Role:** Tight instances and equality.

**Paper-ready prose:** Goddyn and Wong study configurations attaining the conjectured threshold exactly. Cite before asserting new tight families or interpreting zero-measure safety as a novel structural phenomenon. \\cite{GoddynWong2006Tight}

**Relevant experiment themes:** 46–47, 53–55.

**BibTeX citation:** `\\cite{GoddynWong2006Tight}`.

## Bibliography integrity and citation controls

- Every one of the 31 bibliography keys is covered exactly once by a prose annotation. The BibTeX database itself remains the canonical source of author, year, DOI and venue fields.
- Distinguish *n* moving relative speeds from *n+1* total runners when reporting dimensional results.
- The classical conjecture, shifted conjecture, and strengthened spectrum conjectures are different claims.
- Do not describe established union-bound, Bonferroni, spanning-tree, modular, or finite-critical-time methods as newly discovered.
- The current archive includes Experiment 58, although `experiments/INDEX.md` has lagged behind; never use that index alone to infer experiment coverage.
- **Submission gate:** verify individual theorem-to-source claims against the primary full texts, check each BibTeX entry with the publisher or arXiv, and run a citation-key audit after drafting the paper.
