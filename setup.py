from setuptools import setup, find_packages
import os

version = '0.10'

setup(name='collective.twitterportlet',
      version=version,
      description="A Twitter portlet for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Sharkbyte Studios',
      author_email='support@sharkbyte.co.uk',
      url='http://sharkbyte.co.uk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'python-twitter',
          'simplejson'
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
