# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='hybrid_analysis-rapid7-plugin',
      version='2.0.1',
      description='Lookup file hashes to determine if they are malicious',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_hybrid_analysis']
      )