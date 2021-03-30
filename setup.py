from setuptools import setup

with open("README.rst", "r") as fh:
   long_description = fh.read()

setup(
    name='whirlcalc',
    version='0.1.0',    
    description='''python\' eval() function can be limiting.. But WhirlCalc can\' be.''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Whirlpool-Programmer/whirlcalc',
    author='Whirlpool-Programmer',
    author_email='whirlpool.programmer@outlook.com',
    license='MIT License',
    packages=['whirlcalc'],
    classifiers =[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ]
)
