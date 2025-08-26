from setuptools import setup, find_packages

setup(
    name="m3_demo_project",
    version="0.1.0",
    description="test Django + M3/ObjectPack project",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    py_modules=["manage"],
    install_requires=[
        "django==2.2.2",
        "m3-django-compat==1.10.2",
        "m3-core==2.2.30",
        "m3-ui==2.2.122",
        "m3-objectpack==2.2.47",
        "pytz",
        "sqlparse",
    ],
    entry_points={
        "console_scripts": [
            "m3-demo = app.cli:main",
        ]
    },
    python_requires=">=3.8,<3.12",
)
