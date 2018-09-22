# coding: utf-8

from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='lle7ch',
    version='0.2',
    description='Controls SOLA light engine.',
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
)
