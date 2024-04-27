import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ ="0.0.0"

REPO_NAME = "Text_summary"
AUTHOR = "KARAN BAIS"
SRC_REPO = "Text_summary"
AUTHOR_EMAIL = "karanbais2701@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Text summerizer made using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)