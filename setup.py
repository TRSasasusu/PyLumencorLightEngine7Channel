# coding: utf-8

from setuptools import setup


def _requires_from_file(filename):
    return _read_from_file(filename).splitlines()

def _read_from_file(filename):
    return open(filename).read()

setup(
    name='lle7ch',
    version='1.0',
    description='Controls SOLA light engine.',
    long_description=_read_from_file('README.md'),
    long_description_content_type="text/markdown",
    url='https://github.com/TRSasasusu/PyLumencorLightEngine7Channel',
    author='kaito kishi',
    author_email='trsasasusu@gmail.com',
    license='GPLv3',
    keywords='biology, life sciences, light, LED, SOLA light engine, Lumencor',
    packages=[
        "lle7ch",
    ],
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    entry_points = {
        'console_scripts': ['lleplan=lle7ch.lleplan:main'],
    },
)
