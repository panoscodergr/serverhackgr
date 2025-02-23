from setuptools import setup, find_packages

setup(
    name="serverhack",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="serverhack",
    author_email="serverhackgr@gmail.com",
    description="Μια βιβλιοθήκη για HTTP server και requests",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/panoscodergr/serverhack",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",  # Χρησιμοποίησε το πεδίο license για την άδεια
    python_requires='>=3.6',
)
