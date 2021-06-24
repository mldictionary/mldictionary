import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='mldictionary',
    version='0.1.6',
    description='word\'s dictionary for several language',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PabloEmidio/mldictionary',
    author='Pablo Emidio',
    author_email='p.emidiodev@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.25.1', 'beautifulsoup4>=4.9.3'],
    python_requires='>=3.9',
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
)
