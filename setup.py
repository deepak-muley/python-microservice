from setuptools import setup, find_packages

setup(
    name="python-microservice",
    version="0.1.0",
    description="",
    long_description="",
    url="https://github.com/deepak-muley/python-microservice",
    author="Deepak Muley",
    author_email="deepak.muley@gmail.com",
    license="",
    classifiers=[
        "Programming Language :: Python",
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['requests'],
    package_data={},
    data_files=None,
    entry_points={
        'console_scripts': [
            'microservice=microservice:main',
        ],
    }
)
