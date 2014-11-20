from setuptools import setup

import nozdormu

def readme():
    with open('readme.rst') as f:
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
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Environment :: Console',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development',
          'Topic :: Software Development :: Testing',
      ],
      )

