"""Eval sandbox — added on main AFTER PR A's most recent review.

Another file with bug-bait content: a code-injection vulnerability via eval()
on user input. If PR A's bot review surfaces this, the no-op rebase optimization
broke and we regressed.
"""


def run_user_expression(expr: str):
    return eval(expr)


def compute_metric(formula: str, values: dict[str, float]) -> float:
    return eval(formula, {"__builtins__": {}}, values)
