from setuptools import setup, find_packages

setup(
    name='my_correlation_package',  # Nom de ton package
    version='0.1.0',                # Version initiale
    description='A package to perform automatic correlation analysis',
    author='Ton Nom',
    author_email='ton.email@example.com',
    url='https://github.com/ton-compte/my_correlation_package',  # URL du projet
    packages=find_packages(),  # Recherche automatiquement les sous-packages
    install_requires=[          # Les dépendances nécessaires
        'pandas',
        'numpy',
        'scipy',
        'matplotlib',
        'seaborn',
        'statsmodels',
    ],
    classifiers=[               # Métadonnées (pour PyPI)
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',     # Version minimale de Python
)
