from setuptools import setup

setup(
    name="bscscan-python",
    version="0.0.1",
    description="A minimal, yet complete, python API for bscscan.io.",
    url="https://github.com/chipper85/etherscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=[
        "bscscan",
        "bscscan.configs",
        "bscscan.enums",
        "bscscan.modules",
        "bscscan.utils",
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
