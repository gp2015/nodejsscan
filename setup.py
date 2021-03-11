from setuptools import setup, find_packages

setup(
    name="nodejsscan",
    description='Static security code scanner (SAST) for Node.js applications',
    version="4.4",
    author="Ajin Abraham",
    author_email="ajin25@gmail.com",
    license='GPL v3',
    packages=find_packages(include=[
        "core",
        "core.*",
    ]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': [
            "nodejsscan = core.cli:main",
        ]
    },

    # Include additional files into the package
    include_package_data=True,
    # Details
    # url="http://pypi.python.org/pypi/nodejsscan/",

    long_description='open("README.md").read()',
    long_description_content_type='text/markdown',

    # Dependent packages (distributions)
    install_requires=[
        "njsscan==0.2.3",
        "gunicorn==20.0.4",
        "flask==1.1.2",
        "jinja2==2.11.3",
        "psycopg2-binary==2.8.6",
        "Flask-SQLAlchemy==2.4.4",
        "Flask-Migrate==2.7.0",
        "Flask-Script==2.0.6",
        "GitPython==3.1.14"
    ],
)

