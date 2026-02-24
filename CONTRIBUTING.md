---
# 🤝 Contributing to TyreWearWiz

First off — thank you for considering contributing to **TyreWearWiz** 🏎️

This project is built for learning, experimentation, and pushing the boundaries of **Formula 1 tyre degradation and race strategy analysis** using real telemetry data powered by **FastF1**.

Whether you're improving visualizations, adding new race analyses, optimizing performance, or fixing bugs — your contribution is valuable.

---

## 📌 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Ways You Can Contribute](#ways-you-can-contribute)
3. [Project Philosophy](#project-philosophy)
4. [Development Setup](#development-setup)
5. [Project Structure Guidelines](#project-structure-guidelines)
6. [Notebook Contribution Standards](#notebook-contribution-standards)
7. [Commit Message Guidelines](#commit-message-guidelines)
8. [Pull Request Process](#pull-request-process)
9. [Reporting Issues](#reporting-issues)

---

## 🧭 Code of Conduct

Be respectful.
Be constructive.
Be data-driven.

We welcome:

* Students
* Motorsport analysts
* Python developers
* Data visualization enthusiasts
* F1 fans

Toxicity, gatekeeping, or dismissive behavior will not be tolerated.

---

## 🚀 Ways You Can Contribute

You can contribute in multiple ways:

### 🛞 1. Add New Race Analyses

* Add new driver degradation studies
* Add new race strategy visualizations
* Add multi-driver compound comparisons

### 📊 2. Improve Visualizations

* Improve matplotlib styling
* Make plots more F1-broadcast inspired
* Improve clarity and labeling

### 🧠 3. Performance Improvements

* Optimize data loading
* Improve caching logic
* Reduce redundant telemetry processing

### 🐞 4. Bug Fixes

* Fix broken notebooks
* Resolve version conflicts
* Improve error handling

### 📘 5. Documentation Improvements

* Improve explanations
* Add inline comments
* Enhance README clarity

---

## 🎯 Project Philosophy

TyreWearWiz follows three core principles:

1. **Clarity over complexity**
2. **Insight over aesthetics**
3. **Real F1 strategy focus over generic plotting**

Every notebook should answer at least one meaningful question about:

* Tyre degradation
* Strategy timing
* Driver management

If a plot looks cool but teaches nothing — it doesn’t belong.

---

## 🛠 Development Setup

Follow the same setup defined in the README.

### 1️⃣ Fork the Repository

Click **Fork** on GitHub.

### 2️⃣ Clone Your Fork

```bash
git clone https://github.com/<your-username>/TyreWearWiz.git
cd TyreWearWiz
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure Guidelines

When adding new notebooks, follow this strict structure:

```
TyreWearWiz/
│
├── Drivers/
│   └── DRIVER_CODE/
│       └── track-year.ipynb
│
├── Multi-drivers/
│   └── Track_Name/
│       └── year.ipynb
│
├── Race-strategy/
│   └── Track_Name/
│       └── year.ipynb
```

### ✅ Naming Rules

* Driver folders → 3-letter FIA codes (e.g., VER, HAM, LEC)
* Track folders → lowercase with underscores (e.g., silverstone, monza)
* Notebook format → `race-year.ipynb`

Consistency is mandatory.

---

## 📓 Notebook Contribution Standards

Each notebook must:

### ✔ Include Clear Sections

* Session loading
* Data cleaning
* Analysis logic
* Visualization
* Conclusion / Insight summary

### ✔ Use Clean Plot Formatting

* Proper axis labels
* Units included
* Legends formatted clearly
* No overlapping labels

### ✔ Include Insight Commentary

At the end of each notebook, include:

```markdown
### Key Insight
- Bullet point summary of findings
- What this tells us about tyre strategy
```

No raw plot dumps without explanation.

---

## 🧾 Commit Message Guidelines

Use structured commit messages:

```
feat: added 2024 monza race strategy visualization
fix: corrected lap filtering bug in VER 2023 analysis
docs: improved README clarity
refactor: optimized telemetry loading logic
```

Avoid vague commits like:

```
update
changes
fix stuff
```

---

## 🔄 Pull Request Process

1. Create a new branch

   ```bash
   git checkout -b feature/monza-2024-strategy
   ```

2. Make your changes

3. Commit properly

4. Push to your fork

5. Open a Pull Request

### PR Must Include:

* Clear description of what was added
* Screenshot of generated visualization
* Explanation of insight gained
* Confirmation that notebook runs without errors

Pull requests without explanation may be rejected.

---

## 🐛 Reporting Issues

If you find a bug:

Open an issue and include:

* Python version
* FastF1 version
* Notebook path
* Full error traceback
* Screenshot (if relevant)

Clear bug reports get fixed faster.

---

## 📈 Feature Request Guidelines

When suggesting a feature:

Explain:

* What problem it solves
* Why it improves tyre strategy understanding
* How it could be implemented

Low-effort feature requests may be declined.

---

## 🏁 Contribution Vision

TyreWearWiz aims to evolve into:

* A complete tyre degradation case study library
* A race strategy educational resource
* A reference for F1 telemetry-based analysis

If you contribute — you're helping build a motorsport analytics knowledge base.

---

## 🙌 Final Note

In Formula 1:

> Marginal gains win championships.

In TyreWearWiz:

> Small improvements create powerful insights.

Thank you for contributing 🏎️
