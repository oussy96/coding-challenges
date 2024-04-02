from setuptools import setup

setup(
    name='cat-tool',
    version='0.1',
    packages=['src'],
    entry_points={
        'console_scripts': [
            'cccat = src.cccat:cc_cat',
        ],
    },
)
