# correlation_analysis.py

from correlation_insight.utils import (
    test_normality, 
    choisir_correlation_auto, 
    calculer_correlation, 
    visualiser_relation, 
    obtenir_significativite
)
from scipy import stats
import itertools
import pandas as pd

# Fonction principale d'analyse de corrélation
def analyser_correlation(df, var1, var2, mode='auto'):
    normal_var1 = test_normality(df, var1)
    normal_var2 = test_normality(df, var2)

    if mode == 'auto':
        method = choisir_correlation_auto(df, var1, var2, normal_var1, normal_var2)
    else:
        method = visualiser_relation(df, var1, var2)

    correlation_value = calculer_correlation(method, df, var1, var2)
    print(f"Corrélation ({method}) entre {var1} et {var2} : {correlation_value}")
    
    return correlation_value, method

# Fonction pour analyser plusieurs paires de variables
def analyser_correlation_multiple(df, variables, mode='auto'):
    resultats = []
    combinaisons = itertools.combinations(variables, 2)

    for var1, var2 in combinaisons:
        print(f"\nAnalyse de la corrélation entre '{var1}' et '{var2}' :")
        normal_var1 = test_normality(df, var1)
        normal_var2 = test_normality(df, var2)

        if mode == 'auto':
            method = choisir_correlation_auto(df, var1, var2, normal_var1, normal_var2)
        else:
            method = visualiser_relation(df, var1, var2)

        corr, p_value = stats.pearsonr(df[var1], df[var2]) if method == "pearson" else \
                        stats.spearmanr(df[var1], df[var2]) if method == "spearman" else \
                        stats.kendalltau(df[var1], df[var2])

        resultats.append({
            'Variable 1': var1,
            'Variable 2': var2,
            'Valeur de Corrélation': corr,
            'P-value': p_value,
            'Méthode de Corrélation': method,
            'Significativité': obtenir_significativite(p_value)
        })

    return pd.DataFrame(resultats, columns=['Variable 1', 'Variable 2', 'Valeur de Corrélation', 'P-value', 'Méthode de Corrélation', 'Significativité'])
