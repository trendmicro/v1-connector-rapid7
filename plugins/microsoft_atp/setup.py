# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="microsoft_atp-rapid7-plugin",
      version="5.2.0",
      description="The Windows Defender Advanced Threat Protection plugin allows Rapid7 InsightConnect users to quickly take remediation actions across their organization. This plugin can isolate machines, run virus scans, and quarantine files",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_microsoft_atp']
      )
