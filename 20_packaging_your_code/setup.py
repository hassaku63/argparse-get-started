from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='argparse_tutorial',
    version='0.0.1',
    install_requires=[
        'python-backlog',
        'PyYAML'
    ],
    description='argparseを使ったCLIのサンプル',
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    author='hassaku63',
    author_email='takuyahashimoto1988@gmail.com',
    license='CC0',
    classifiers=[
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Natural Language :: Japanese',
    ],
    keywords='nulab backlog argparse',
    url='https://github.com/hassaku63/argparse-get-started',
    entry_points={
        # https://packaging.python.org/guides/distributing-packages-using-setuptools/#entry-points
        # https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation
        'console_scripts': [
            'backlog_list_wiki = example_cli.cli:main'
        ]
    },
    packages=find_packages(exclude=['tests*']),
)