import setuptools

with open("README.md", "r") as file:
	long_description = file.read()

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
	python_requires='>=3.7'
)

