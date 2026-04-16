from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="osintvault",
    version="0.1.10",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'osintvault=cli.main:main',
        ],
    },
)
