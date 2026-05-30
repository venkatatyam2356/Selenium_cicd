from setuptools import setup, find_packages

setup(
    name="exp_tracker",
    version="0.1.0",
    author="Venkata Ratnam Atyam",
    author_email="x23291788@student.ncirl.ie",
    description="A python library project for managing personal expenses",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/venkat2356/expense_tracker",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "boto3>=1.26.0",  # Include other dependencies if needed
    ],
)
