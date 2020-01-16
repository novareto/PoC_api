import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt')
)

setup(
    name='gkmsg',
    version='0.1',
    url='',
    author='',
    author_email='',
    description="",
    long_description=long_description,
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='ZPL',
    install_requires=[
        'horseman',
        'bjoern'
    ],
)
