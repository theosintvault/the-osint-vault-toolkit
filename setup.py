from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="theosintvault",
    version="0.2.0",
    description="CLI OSINT engine for verifiable intelligence gathering across email, username, and search signals",
    long_description=README,
    long_description_content_type="text/markdown",
    author="theosintvault",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "theosintvault=cli.main:main",
        ],
    },
    keywords=[
        "osint",
        "investigation",
        "recon",
        "intelligence",
        "cli",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Environment :: Console",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    project_urls={
        "Source": "https://github.com/theosintvault/the-osint-vault-toolkit",
        "Issues": "https://github.com/theosintvault/the-osint-vault-toolkit/issues",
    },
)
