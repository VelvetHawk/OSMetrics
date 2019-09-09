import setuptools

with open("README.md", "r") as readme_file:
	long_description = readme_file.read()

# Code sourced from:
# https://stackoverflow.com/questions/1706198/python-how-to-ignore-comment-lines-when-reading-in-a-file
# This is to avoid have to keep both requirements.txt AND install_requires in sync
with open('requirements.txt') as requirements_file:
	requirements = requirements_file.read().splitlines()
	for requirement in requirements:
		if requirement.startswith("#"):
			requirements.remove(requirement)

setuptools.setup(
	name="OS Metrics",
	version="0.1",
	author="Artem Semenov",
	packages=setuptools.find_packages(),
	description="Package to collect OS metrics",
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent"
	],
	python_requires='>=3.7',
	install_requires=[
		# Hello
		"",
		# Hi
		""
	]
)

