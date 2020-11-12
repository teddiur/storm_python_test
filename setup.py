from setuptools import setup

setup(
    name='storm_python_tes',
    version='1.0',
    tests_require=['pytest'],
    scripts=['src/app.py'],
    packages=find_packages(),
    scripts=['bin/hello.py'],
    entry_points={'scrapy': ['settings = myproject.settings']},
)
