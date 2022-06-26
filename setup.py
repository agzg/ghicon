# from requests import get
import setuptools

REPOSITORY = "https://github.com/agzg/ghicon"
# version = get(REPOSITORY).url.split("/")[-1]

with open("README.md", "r") as f:
	long_description = f.read()
	
setuptools.setup(
	name="ghicon",
	packages=setuptools.find_packages(),
	version="4.2.0",
	license="MIT",
	description="GitHubesque identicon generator.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="Ali Azam",
	author_email="azam.vw@gmail.com",
	url="https://github.com/agzg/ghicon",
	download_url="https://github.com/agzg/ghicon/archive/refs/tags/4.2.0.tar.gz",
	keywords=["identicon", "generator", "github", "pillow", "icon"],
	install_requires=["pillow"],
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python"
	],
)

