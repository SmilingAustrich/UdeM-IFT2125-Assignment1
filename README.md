# 📊 Algorithm Analysis (Asymptotic Notation & Recurrences)

![Course](https://img.shields.io/badge/Course-IFT2125-blue?style=for-the-badge)
![University](https://img.shields.io/badge/University-UdeM-navy?style=for-the-badge)

A comprehensive analysis of algorithmic complexity, focusing on asymptotic proofs, the resolution of linear recurrences, and the application of the Master Theorem.

---

## 🌍 Language / Langue

* [🇬🇧 English Version](#-english-version)
* [🇫🇷 Version Française](#-version-française)

---

## 🇬🇧 English Version

### ✨ Project Overview

This assignment provides a rigorous mathematical framework for analyzing the efficiency of algorithms. It covers the formal verification of asymptotic bounds, methods for solving complex recurrences, and practical complexity analysis of code snippets.

**Key Features Implemented:**

* **Asymptotic Proofs:** Rigorous proof by contradiction for Big O notation, evaluating functions like `⌊n/2⌋` and `n^n log(n!)`.
* **Recurrence Solving:** Step-by-step resolution of linear recurrences using characteristic polynomials, roots with multiplicity, and particular solutions for non-homogeneous parts.
* **Master Theorem Application:** Analysis of various recurrence relations to determine tight complexity bounds (Θ).
* **Algorithm Analysis:** Evaluation of recursive Python functions (e.g., fractal trees) and efficient list-processing techniques like double pointers.

### 🚀 Getting Started

**Topics Covered:**

* Asymptotic Notation (O, Ω, Θ)
* Linear Homogeneous and Non-Homogeneous Recurrences
* Recursive Complexity Analysis
* Double Pointers Technique for O(n) search

### 💻 Analysis Examples

**1. Asymptotic Bounds:**

```prolog
⌊n/2⌋ ∉ O(n)          % Proved by contradiction
n^n log(n!) ∉ O(n^3 log(n))  % log(n!) grows faster than log(n)
```

**2. Master Theorem Applications:**

```prolog
t(n) = t(n/2) + 4n      => Θ(n)         % Case: l < b^k [cite: 410]
t(n) = 2t(n/2) + 2n     => Θ(n log n)   % Case: l = b^k [cite: 410]
t(n) = 4t(n/3) + 2n     => Θ(n^1.26...) % Case: l > b^k [cite: 411]
```

**3. Recursive Code Complexity:**

For a recursive Python function making 3 calls of size `(n−1)`:

```prolog
t(n) = 3t(n−1) + 1
Complexity: Θ(3^n)
```

---

## 🇫🇷 Version Française

### ✨ Vue d'ensemble

Ce travail pratique fournit un cadre mathématique rigoureux pour analyser l'efficacité des algorithmes. Il couvre la vérification formelle des bornes asymptotiques, les méthodes de résolution de récurrences complexes et l'analyse pratique de la complexité de segments de code.

**Fonctionnalités Clés :**

* **Preuves Asymptotiques :** Preuves rigoureuses par contradiction pour la notation Grand O, évaluant spécifiquement des fonctions telles que `⌊n/2⌋` et `n^n log(n!)`.
* **Résolution de Récurrences :** Résolution étape par étape de récurrences linéaires utilisant les polynômes caractéristiques, les racines avec multiplicité et les solutions particulières pour les parties non homogènes.
* **Théorème Maître :** Analyse de diverses relations de récurrence pour déterminer des bornes de complexité précises (Θ).
* **Analyse d'Algorithmes :** Évaluation de fonctions Python récursives (ex: arbres fractals) et techniques efficaces de traitement de listes comme les doubles pointeurs.

### 🚀 Démarrage

**Sujets Abordés :**

* Notation Asymptotique (O, Ω, Θ)
* Récurrences Linéaires Homogènes et Non Homogènes
* Analyse de Complexité Récursive
* Technique des Doubles Pointeurs pour une recherche en O(n)

### 💻 Exemples d'Analyse

**1. Bornes Asymptotiques :**

```prolog
⌊n/2⌋ ∉ O(n)          % Prouvé par contradiction
n^n log(n!) ∉ O(n^3 log(n))  % log(n!) croît plus vite que log(n)
```

**2. Applications du Théorème Maître :**

```prolog
t(n) = t(n/2) + 4n      => Θ(n)         % Cas: l < b^k [cite: 410]
t(n) = 2t(n/2) + 2n     => Θ(n log n)   % Cas: l = b^k [cite: 410]
t(n) = 4t(n/3) + 2n     => Θ(n^1.26...) % Cas: l > b^k [cite: 411]
```

**3. Complexité de Code Récursif :**

Pour une fonction Python récursive effectuant 3 appels de taille `(n−1)`:

```prolog
t(n) = 3t(n−1) + 1
Complexité: Θ(3^n)
```

---

## 👤 Auteur

Tarik Hireche | tarik.hireche@umontreal.ca
Université de Montréal - IFT2125
