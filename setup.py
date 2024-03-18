import os

from setuptools import setup, find_packages

VERSION_NUMBER = '0.1.0'


def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-link-embeds-plugin',
    version=VERSION_NUMBER,
    description='Mkdocs plugin which shows embedded links in a more elegant manner.',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    keywords='mkdocs',
    url='https://github.com/Aetherinox/mkdocs-link-embeds',
    author='Aetherinox',
    author_email='aetherinox@proton.me',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    package_data={'': ['resources/template.html']},
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
            'link-embeds = mkdocs_link_embeds_plugin.plugin:LinkEmbedsPlugin'
        ]
    }
)
