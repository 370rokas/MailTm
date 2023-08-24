import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MailTm",
    version="0.0.81",
    author="MainSilent, 370rokas",
    description="Fork of MailTM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['mail', 'email', 'temporary mail', 'temporary email', 'mailtm'],
    url="https://github.com/370rokas/MailTm",
    project_urls={
        "Bug Tracker": "https://github.com/370rokas/MailTm/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['requests']
)
