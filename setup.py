from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='EcommercePlatformDetector',
    packages=['ecommerce_platform_detector'],
    version='0.001',
    license='MIT',
    description='Ecommerce Platform Detector is a Python package that detects the ecommerce platform used by a site.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matt Clarke',
    author_email='matt@practicaldatascience.co.uk',
    url='https://github.com/practical-data-science/EcommercePlatformDetector',
    download_url='https://github.com/practical-data-science/EcommercePlatformDetector/archive/master.zip',
    keywords=['python', 'requests', 'pandas', 'ecommerce', 'platform', 'scraping'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['pandas', 'requests']
)
