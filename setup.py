from setuptools import find_packages, setup

setup(
    name='analyzer',
    description='Text analysis using NLTK',
    author='Clovis Mugaruka',
    email_address='clovis.mugaruka@gmail.com'
    version='1.0.0',
    packages=find_ipackages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
