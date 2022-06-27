import setuptools

VERSION = "5.2.1"

with open("README.md", "r") as f:
	long_description = f.read()
	
setuptools.setup(
	name="ghicon",
	packages=setuptools.find_packages(),
	version=VERSION,
	license="MIT",
	description="GitHubesque identicon generator.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="Ali Azam",
	author_email="azam.vw@gmail.com",
	url="https://github.com/agzg/ghicon",
	download_url=f"https://github.com/agzg/ghicon/archive/refs/tags/{VERSION}.tar.gz",
	keywords=["identicon", "generator", "github", "pillow", "icon"],
	install_requires=["Pillow>=9.0.1"],
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10"
	],
)
