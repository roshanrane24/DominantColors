from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="DominantColors",
    version="0.2.2",
    author="Roshan Rane",
    author_email="roshan.ran3@gmail.com",
    description="A package to extract dominant colors from an image.",
    long_description=long_description,
    url="https://github.com/roshanrane24/DominantColors",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independant"
    ],
    package_dir={"": "."},
    packages=find_packages(where="."),
    install_requires=["opencv-python", "sklearn", "numpy"],
    python_requires=">=3.6"
)
