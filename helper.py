"""Reproducible synthetic credit data for the classification notebook."""

import numpy as np
import pandas as pd


def generate_credit_data(n=1200, random_state=42):
    """Return bureau score, debt/income (%) and a binary default indicator.

    Scores follow a stylized 300–850 scale; debt/income is monthly debt
    payments divided by gross monthly income, expressed as a percentage.
    Features are available at application; default is observed over the next
    12 months. These are teaching data, not an operational credit model.
    Bernoulli sampling produces overlapping classes even at identical risk.
    """
    rng = np.random.default_rng(random_state)
    bureau_score = np.clip(rng.normal(660, 85, n), 300, 850).round().astype(int)
    debt_income = np.clip(rng.normal(32, 13, n), 5, 65).round(1)
    linear_predictor = -1.1 - 0.018 * (bureau_score - 650) + 0.075 * (debt_income - 30)
    probability = 1 / (1 + np.exp(-linear_predictor))
    return pd.DataFrame({
        'bureau_score': bureau_score,
        'debt_income': debt_income,
        'default': rng.binomial(1, probability),
    })


if __name__ == '__main__':
    from pathlib import Path

    output = Path(__file__).resolve().parent / 'data' / 'credit_synthetic.csv'
    generate_credit_data().to_csv(output, index=False)
