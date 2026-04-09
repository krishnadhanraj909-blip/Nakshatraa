from setuptools import setup, find_packages

setup(
    name='Nakshatraa',  # Replace with your package name
    version='0.1',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A brief description of your package',  # Replace with your package description
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change as needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)