from setuptools import setup

setup(name='MSVNPackages',
      version='0.2',
      description='Random functions from courses at DTU',
      packages=['MSVNPackages'],
      author_email='Magnusvinjebo@hotmail.com',
      zip_safe=False,
      install_requires=[
          'numpy',
          'matplotlib'
      ],)
