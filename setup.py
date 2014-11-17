from setuptools import setup

def readme():
    with open('readme.md') as f:
        return f.read()

setup(name='nozdormu',
      version='0.1',
      description='Python benchmarking for humans and dragons',
      lon_description=readme(),
      url='https://github.com/sulami/nozdormu',
      author='Robin Schroer',
      author_email='sulami@peerwire.org',
      license='MIT',
      packages=['nozdormu'],
      install_requires=[
          'python>=3.2'
      ],
      zip_safe=False,
      )

