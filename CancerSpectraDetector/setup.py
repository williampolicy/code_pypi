from setuptools import setup, find_packages

setup(
    name='CancerSpectraDetector',
    version='0.1',
    packages=find_packages(),
    author='Xiaowen Kang',
    author_email='kangxiaowen@gmail.com',
    description='A package to detect societal cancers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
