
from setuptools import setup

# requires = ["requests>=2.14.2"]

setup(
    name='UltimatePkg',
    version='0.1',
    description='Ultimate packages',
    # url='https://github.com/whatever/whatever',
    author='crea',
    author_email='masataka0504@gmail.com',
    license='MIT',
    keywords='utilities',
    
    packages=['UltimatePkg'], # もちろん、pip3 install -e . でPCグローバルにライブラリ化したら、ここで書いたパッケージも同時にグローバルに入る
    install_requires=['termcolor'],
    
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)