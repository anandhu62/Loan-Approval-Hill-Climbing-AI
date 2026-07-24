# Loan-Approval-Hill-Climbing-AI
# Loan Approval using Hill Climbing Optimization

An interpretable rule-based loan approval system developed using the Hill Climbing heuristic search algorithm. The project generates optimized decision rules for loan approval using the UCI Bank Marketing Dataset while emphasizing transparency and interpretability over black-box machine learning models.

---

## Project Overview

This project applies the Hill Climbing optimization algorithm to discover effective rule-based patterns for loan approval prediction. Candidate rules are evaluated using Precision, Coverage, and Lift to improve decision quality while maintaining interpretability.

Unlike traditional machine learning models, the generated rules can be easily understood and analyzed by financial institutions.

---

## Features

- Rule-based loan approval prediction
- Hill Climbing optimization
- Lift-based evaluation function
- Automatic rule generation
- Interpretable decision rules
- Uses the UCI Bank Marketing Dataset

---

## Technologies Used

- Python
- Pandas
- Random Module

---

## Dataset

**Dataset:** Bank Marketing Dataset

Source:
https://archive.ics.uci.edu/ml/datasets/bank+marketing

Dataset file required:

```
bank-full.csv
```

---

## Project Structure

```
Loan-Approval-Hill-Climbing-AI
│
├── loan_approval_hill_climbing.py
├── bank-full.csv
├── README.md
├── requirements.txt
└── report/
```

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python loan_approval_hill_climbing.py
```

---

## Sample Output

```
Generated Rule

IF balance > 2500 AND age > 45
THEN Approve Loan

Evaluation Score:
1.842
```

*(The generated rule may vary because the algorithm uses random initialization.)*

---

## Future Enhancements

- Interactive web interface
- Rule visualization
- Comparison with additional heuristic search algorithms
- Export generated rules as reports
- Performance dashboard

---

## Author

Anandakrishnan T M

MCA Student

Amrita Vishwa Vidyapeetham
