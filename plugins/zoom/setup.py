# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="zoom-rapid7-plugin",
      version="4.1.10",
      description="[Zoom](https://zoom.us) is a cloud platform for video and audio conferencing, chat, and webinars. The Zoom plugin allows you to add and remove users as part of of workflow, while also providing the ability to trigger workflows on new user sign-in and sign-out activity events. This plugin uses the [Zoom API](https://marketplace.zoom.us/docs/api-reference/introduction) and requires a Pro, Business, or Enterprise plan",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_zoom']
      )
