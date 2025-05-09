from setuptools import setup, find_packages

setup(
    name="bargal",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "requests>=2.25.0",
        "pandas>=2.2.0"
    ],
    entry_points={
        "console_scripts": [
            "bargal-imgdown=bargal.commands.download_image:main",
            "bargal-datasetdown=bargal.commands.download_dataset:main",
        ],
    },
    author="ludanortmun",
    description="A tool for barred galaxy detection and analysis",
    python_requires=">=3.7"
)