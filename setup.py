from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="osintvault",
    version="0.1.11",
    description="OSINT pivot engine CLI for rapid investigative workflows",
    long_description=README,
    long_description_content_type="text/markdown",
    author="theosintvault",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "osintvault=cli.main:main",
        ],
    },
)
