import pandas as pd
import random

# ==========================================================
# Loan Approval using Hill Climbing Optimization
# Author: Anandakrishnan T M
# Dataset: UCI Bank Marketing Dataset
# ==========================================================

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("bank-full.csv", sep=";")

columns = ["age", "balance", "job", "marital", "y"]
data = data[columns].dropna()

# -----------------------------
# Baseline Success Rate
# -----------------------------
baseline = len(data[data["y"] == "yes"]) / len(data)


# -----------------------------
# Apply Rule
# -----------------------------
def apply_rule(data, rule):
    """
    Filters the dataset based on a generated rule.
    """

    subset = data.copy()

    for column, operator, value in rule:

        if operator == ">":
            subset = subset[subset[column] > value]

        elif operator == "<":
            subset = subset[subset[column] < value]

        elif operator == "=":
            subset = subset[subset[column] == value]

    return subset


# -----------------------------
# Rule Evaluation Function
# -----------------------------
def evaluate(rule):
    """
    Evaluates a rule using:
    - Precision
    - Coverage
    - Lift
    """

    subset = apply_rule(data, rule)

    if len(subset) < 50:
        return 0

    success = subset[subset["y"] == "yes"]

    precision = len(success) / len(subset)
    coverage = len(subset) / len(data)
    lift = precision / baseline

    score = (0.7 * lift) + (0.3 * coverage)

    return score


# -----------------------------
# Generate Random Condition
# -----------------------------
def random_condition():

    column = random.choice(["age", "balance", "job", "marital"])

    if column == "job":
        return (
            column,
            "=",
            random.choice(data["job"].unique())
        )

    elif column == "marital":
        return (
            column,
            "=",
            random.choice(data["marital"].unique())
        )

    elif column == "age":
        return (
            column,
            ">",
            random.randint(25, 55)
        )

    else:
        return (
            column,
            ">",
            random.randint(500, 4000)
        )


# -----------------------------
# Remove Duplicate Conditions
# -----------------------------
def clean_rule(rule):

    unique = {}

    for column, operator, value in rule:

        if column not in unique or value > unique[column][2]:
            unique[column] = (
                column,
                operator,
                value
            )

    return list(unique.values())


# -----------------------------
# Hill Climbing Algorithm
# -----------------------------
def hill_climbing():

    current_rule = [
        ("balance", ">", 1500)
    ]

    current_score = evaluate(current_rule)

    for _ in range(200):

        neighbor = current_rule.copy()

        if random.random() > 0.5 and len(neighbor) > 1:

            neighbor.pop(
                random.randint(
                    0,
                    len(neighbor) - 1
                )
            )

        else:

            neighbor.append(
                random_condition()
            )

        if len(neighbor) > 3:
            continue

        neighbor = clean_rule(neighbor)

        score = evaluate(neighbor)

        if score > current_score:

            current_rule = neighbor
            current_score = score

    return current_rule, current_score


# -----------------------------
# Display Rule
# -----------------------------
def format_rule(rule):

    conditions = []

    for column, operator, value in rule:
        conditions.append(
            f"{column} {operator} {value}"
        )

    return "IF " + " AND ".join(conditions) + " THEN Approve Loan"


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":

    rule, score = hill_climbing()

    print("=" * 60)
    print(" Loan Approval using Hill Climbing Optimization ")
    print("=" * 60)

    print("\nGenerated Rule:\n")
    print(format_rule(rule))

    print("\nEvaluation Score:")
    print(round(score, 3))
