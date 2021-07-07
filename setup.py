from setuptools import setup

with open("README.md", "r",encoding='utf-8') as file:
   long_description = file.read()

setup(
    name='compie',
    version='2.3b0',    
    description='''A Python module made for use with numbers and data''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Whirlpool-Programmer/pycompute',
    author='Whirlpool-Programmer',
    author_email='whirlpool.programmer@outlook.com',
    license='MIT License',
    packages=['compie'],
    classifiers =[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ]
)
'''
BUILD COMMANDS
python setup.py sdist
python setup.py bdist_wheel --universal
python -m twine upload dist/*.*
'''
