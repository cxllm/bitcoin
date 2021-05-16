from setuptools import setup

with open("README.md", "r") as rd:
    long_description = rd.read()
setup(
    name="bitcoin-cli",
    version="1.0.1-1",
    description="Bitcoin command line tool that tells you current prices",
    url="https://github.com/cxllm/bitcoin",
    author="Callum",
    author_email="me@cxllm.xyz",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    keywords=["bitcoin", "btc", "crypto", "cryptocurrency"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests>=2.25.1"],
    scripts=["bin/bitcoin"],
)
