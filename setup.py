from setuptools import find_packages, setup

setup(
        author = 'Louie Tran',
        description = " A package used for inputing, processing, exporting text for a specific research project",
        name = 'TextAnalysis_ProjectHero',
        version = '1.0.0',
        packages = find_packages(include=['TextAnalysis_ProjectHero','TextAnalysis_ProjectHero.*']),
        install_requires=[
                'pandas>=1.0',
                'regex>=2021.0.0',
                'datetime>4.0'
                'num2words==0.5.10',
                'contractions==0.0.52'
        ],
        python_requires='>=2.7, <3.8.0'
)