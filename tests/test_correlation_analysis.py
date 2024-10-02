import pandas as pd
from correlation_insight.utils import (
    test_normality,
    test_linearity,
    choisir_correlation_auto
)
from correlation_insight.correlation_analysis import analyser_correlation
import pytest

@pytest.fixture
def df_linear():
    """Fixture pour un DataFrame avec une relation linéaire."""
    data = {
        'var1': [1, 2, 3, 4, 5],
        'var2': [2, 4, 6, 8, 10]  # Relation parfaitement linéaire
    }
    return pd.DataFrame(data)

def test_test_linearity(df_linear):
    """Test de la fonction test_linearity."""
    # Test de la linéarité entre var1 et var2
    result = test_linearity(df_linear, 'var1', 'var2')
    print(f"Durbin-Watson stat: {result}")
    assert result == True  # Les deux variables sont linéairement reliées

def test_normality(df_linear):
    """Test de la fonction test_normality."""
    result = test_normality(df_linear, 'var1')
    assert result == True  # var1 devrait être normalement distribué

def test_test_non_linearity(df_linear):
    """Test de la fonction test_non_linearity."""
    result = test_non_linearity(df_linear, 'var1', 'var2')
    assert result == False  # Il ne devrait pas y avoir de non-linéarité ici

# Ajoutez d'autres tests si nécessaire
