# __init__.py

from correlation_insight.correlation_analysis import (
    analyser_correlation,
    analyser_correlation_multiple
)
from correlation_insight.utils import (
    test_normality,
    test_linearity,
    test_non_linearity,
    desequilibre_outliers,
    choisir_correlation_auto,
    calculer_correlation,
    visualiser_relation,
    obtenir_significativite
)
