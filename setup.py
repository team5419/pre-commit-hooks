from setuptools import find_packages
from setuptools import setup


setup(
    name='team5419_hooks',
    description='team5419 specific kotlin precommit hooks',
    url='https://github.com/team5419/pre-commit-hooks',
    version='0.3.15',

    packages=find_packages(),
    extras_require={':python_version<"3.5"': ['typing']},
    entry_points={
        'console_scripts': [
            'detekt_wrapper = team5419_hooks.detekt_wrapper:main'
        ],
    },
)
