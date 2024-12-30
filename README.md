# EVT-GARCH Project

## Tail Behavior and Extreme Value Analysis of GARCH(1,1) Models

**Author**: Hugo Belzil  
**Course**: MATH 598 - Extreme Value Analysis  
**Instructor**: Prof. Johanna Nešlehová  
**Date**: December 2024

---

## Overview

This repository contains the code and analysis for the project "Tail Behavior and Extreme Value Analysis of GARCH(1,1) Models," conducted as part of the MATH 598 course at McGill University. The project investigates the tail behavior and extreme value properties of GARCH(1,1) models, with a particular focus on financial data.

The study involves:

1. Theoretical analysis of GARCH(1,1) models' tail behavior using Breiman's Lemma and results on regular variation.
2. Tail-index computation for GARCH models with different innovation distributions (Gaussian, Student's t, and Generalized Hyperbolic).
3. Application of these results to the Dow Jones daily log-return dataset.
4. Comparison with the Block Maxima method for extreme value analysis using different sizes for blocks.

---

## Features

- **Tail Behavior Analysis**: Investigates how GARCH models capture heavy-tailed behavior.
- **Tail-Index Computation**: Numerical computation of the tail index for various innovation distributions.
- **Application to Financial Data**: Analyzes daily log-returns of the Dow Jones index.
- **Comparison with EVT Techniques**: Evaluates the Block Maxima method for GARCH model extremes.

---

## Repository Structure

- `Numerical_computations_python/`: Contains the Python code for the tail-index computations. The code was originally created on jupyter notebook (google colab, link available in the commented code)
- `data_analysis_R/`: Includes the plain R code for fitting the GARCH models and block-maxima method. Also includes the `.Rmd` for both implementations.
- `plots_python/`: Plots generated during the analysis (coded in Python, google colab link available in the comments)
- `evt_garch_finalproject.pdf`: Final project report (PDF), detailing the analysis and results.
- `README.md`: Project overview and instructions (this file).

---

## Key Findings

1. **Tail-Index Estimations**:  
   - Gaussian innovations: Tail index \( &kappa; = 5.67 \)  
   - Student’s t-distributed innovations: Tail index \( &kappa; = 4.85 \)  
   - Generalized Hyperbolic innovations: Tail index \( &kappa; = 4.46 \)  

2. **Best-Fit Model**:  
   The GARCH(1,1) model with Generalized Hyperbolic innovations seems to provide the most accurate fit for the Dow Jones data.

3. **Block Maxima Method Limitations**:  
   Found to be less suitable for financial data due to time-dependence and clustering in extremes.

---

## Results

Detailed results, including the numerical outputs and visualizations, are available in the `Numerical_computations_python/` and `data_analysis_R/` directories. The final report, `evt_garch_finalproject.pdf`, provides an in-depth explanation of the methods and findings. If you notice any typo or mistake of any kind, please let me know hugo [dot] belzil [at] mail.mcgill.ca!.

---

## Acknowledgments

This project was completed under the supervision of Prof. Johanna Nešlehová for MATH 598 at McGill University, whom I thank immensely for her help and support. We also acknowledge the contributions of Mikosch & Stǎricǎ (2000) and Embrechts, McNeil, & Frey (2005) for foundational theoretical results.

---
