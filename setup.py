from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

def read_file(filename):
    path = os.path.join(here, filename)
    return open(path, encoding="utf-8").read() if os.path.exists(path) else ""

README = read_file("README.rst")
NEWS = read_file("NEWS.txt")

version = "0.5.0"

install_requires = [
    "urllib3>=1.7.1",
    "dnspython>=1.13.0",
]

extras_require = {
    "test": [
        "pytest",
        "pytest-mock",
        "pyOpenSSL>=0.14",
    ]
}

setup(
    name="python-etcd",
    version=version,
    description="A python client for etcd",
    long_description=README + "\n\n" + NEWS,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Database :: Front-Ends",
    ],
    keywords="etcd raft distributed log api client",
    author="Jose Plana",
    author_email="jplana@gmail.com",
    url="http://github.com/jplana/python-etcd",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,

    # Modern testing: no nose, no test_suite
    extras_require=extras_require,
)