from setuptools import find_packages, setup

setup(name='notewell',
      version='0.1.0',
      description='Notewell ai stuff',
      author='Notewell contributors',
      packages=find_packages(),
      url="https://github.com/false-positive/notewell.git",
      install_requires=[
          'spacy==2.2.4',
          'Questgen @ git+https://github.com/CodenameSource/Questgen.ai.git',
          'pke @ git+https://github.com/boudinfl/pke.git@f651015f9c931cf245a753f4457bb49f0befa5fd',
          'overrides==3.1.0',
      ],
      )
