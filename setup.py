import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ ="0.0.0"

REPO_NAME = "Text_summary"
AUTHOR = "KARAN BAIS"
SRC_REPO = "Text_summary"
AUTHOR_EMAIL = "karanbais2701@gmail.com"

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
# return all the list of requirments

    requirements = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [r.replace('\n','')for r in requirments]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

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
    install_requires=get_requirements('requirements.txt'),
)