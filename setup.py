# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
setup(
  name='access',
  version='0.0.11',
  long_description=__doc__,
  author='Rikard Erlandsson',
  author_email='rikard.erlandson@scilifelab.se',
  license='MIT',
  url='http://github.com/Clinical-Genomics/clinical',
  packages=find_packages(),
  include_package_data=True,
  zip_safe=False,
)
