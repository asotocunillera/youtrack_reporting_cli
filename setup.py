from setuptools import find_packages, setup

install_requires = [
    "certifi==2024.2.2",
    "charset-normalizer==3.3.2",
    "idna==3.7",
    "python-dotenv==1.0.1",
    "requests==2.31.0",
    "urllib3==2.2.1",
]


setup(
    name="youtrack_app",
    version="1.0.0",
    author="Álvaro Soto",
    author_email="asotocunillera@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
)
