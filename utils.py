# utils.py

import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import linear_reset
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Test de normalité
def test_normality(df, column):
    stat, p = stats.shapiro(df[column].dropna())
    return p > 0.05

# 2. Test de linéarité : Durbin-Watson
def test_linearity(df, var1, var2):
    X = sm.add_constant(df[var1])
    model = sm.OLS(df[var2], X).fit()
    dw_stat = sm.stats.durbin_watson(model.resid)
    return 1.5 <= dw_stat <= 2.5

# 3. Test de non-linéarité : RESET de Ramsey
def test_non_linearity(df, var1, var2):
    X = sm.add_constant(df[var1])
    model = sm.OLS(df[var2], X).fit()
    ramsey_test = linear_reset(model, power=2)
    return ramsey_test.pvalue < 0.05

# 4. Détection de déséquilibres et valeurs aberrantes
def desequilibre_outliers(var_des):
    if var_des.isnull().all():
        return {"is_balanced": False, "skewness": np.nan, "num_outliers": 0}

    value_counts = var_des.value_counts()
    max_frequency = value_counts.max()
    min_frequency = value_counts.min()
    skewness = stats.skew(var_des.dropna())

    Q1, Q3 = np.percentile(var_des.dropna(), [25, 75])
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = var_des[(var_des < lower_bound) | (var_des > upper_bound)]

    return {
        "is_balanced": (max_frequency / min_frequency) < 10,
        "skewness": skewness,
        "num_outliers": len(outliers)
    }

# 5. Choisir la méthode de corrélation
def choisir_correlation_auto(df, var1, var2, normal_var1, normal_var2):
    if normal_var1 and normal_var2:
        return "pearson" if test_linearity(df, var1, var2) else "spearman"
    if test_non_linearity(df, var1, var2):
        if desequilibre_outliers(df[var1])['is_balanced'] or desequilibre_outliers(df[var2])['is_balanced']:
            return "kendall"
    return "spearman"

# 6. Calculer la corrélation
def calculer_correlation(method, df, var1, var2):
    return df[var1].corr(df[var2], method=method)

# 7. Visualiser la relation
def visualiser_relation(df, var1, var2, mode='manuel'):
    # Le code original de visualisation ici
    pass

# 8. Obtenir la significativité
def obtenir_significativite(p_value):
    if p_value < 0.001: return '***'
    if p_value < 0.01: return '**'
    if p_value < 0.05: return '*'
    return ''
