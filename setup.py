from setuptools import setup, find_packages

setup(
    name='AutomationChallenge',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=open('requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            'test_Search = AutomationChallenge.src.testCases.test_Search:unittest.main',
        ],
    },
)
