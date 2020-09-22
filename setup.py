import sys
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

package_dir = {"": "src"}


is_bdist = any(arg.startswith("bdist") for arg in sys.argv)

if is_bdist:
    import lib3to6
    package_dir = lib3to6.fix(package_dir)


setuptools.setup(
    name="processmanager",
    version="0.1.1",
    author="Brandon M. Pace",
    author_email="brandonmpace@gmail.com",
    description="A multiprocessing process manager for Python programs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="multiprocessing multicore process offload manager",
    license="GNU Lesser General Public License v3 or later",
    install_requires=[
        'logcontrol>=0.2.1; python_version >= "3.6"',
        'futures; python_version == "2.7"',
        'typing; python_version < "3.5"',
    ],
    platforms=["any"],
    python_requires=">=2.7",
    project_urls={
        "Code and Issues": "https://github.com/brandonmpace/processmanager",
        "Documentation": "https://processmanager.readthedocs.io"
    },
    packages=setuptools.find_packages("src"),
    package_dir=package_dir,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2"
        "Programming Language :: Python :: 3"
    ]
)
