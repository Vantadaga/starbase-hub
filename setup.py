from setuptools import setup

setup(
    name="closure_app",
    version="0.1.0",
    packages=["closure_app"],
    entry_points={
        "console_scripts": [
            "closures = closure_app.__main__:main"
        ]
    },
)
