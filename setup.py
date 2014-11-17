from setuptools import setup

import nozdormu

def readme():
    with open('readme.md') as f:
        return f.read()

setup(name='nozdormu',
      version=nozdormu.VERSION,
      description='Python benchmarking for humans and dragons',
      long_description=readme(),
      url='https://github.com/sulami/nozdormu',
      author='Robin Schroer',
      author_email='sulami@peerwire.org',
      license='MIT',
      packages=['nozdormu'],
      zip_safe=False,
      )

