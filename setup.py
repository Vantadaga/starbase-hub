from setuptools import setup

setup(
    name="starbase-hub",
    version="0.2.0",
    packages=["app"],
    entry_points={
        "console_scripts": [
            "closures = app.__main__:main"
        ]
    },
)
