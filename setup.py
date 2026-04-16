from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="osintvault",
    version="0.1.13",
    description="Command-line OSINT pivot engine for email, domain, IP, and username intelligence gathering",
    long_description=README,
    long_description_content_type="text/markdown",
    author="theosintvault",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "osintvault=cli.main:main",
        ],
    },
    keywords=[
        "osint",
        "recon",
        "investigation",
        "intelligence",
        "pivoting",
        "cli",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    project_urls={
        "Source": "https://github.com/theosintvault/the-osint-vault-toolkit",
    },
)
