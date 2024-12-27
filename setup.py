from setuptools import setup, find_packages

setup(
    name="proyecto-kraken",  # Cambia esto por un nombre único
    version="0.1.0",
    description="Un proyecto para calcular entradas de compra y venta usando las Bandas de Bollinger y la API de Kraken.",
    author="Pedro Montt Pacheco",
    author_email="pmonttpache@alumni.unav.es",
    url="https://github.com/tu_usuario/tu_repositorio",  # Opcional: tu repo de GitHub
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "krakenex==2.2.2",
        "matplotlib==3.10.0",
        "pandas==2.2.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
