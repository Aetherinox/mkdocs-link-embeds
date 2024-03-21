import os
from setuptools import setup, find_packages

with open( "README.md", "r", encoding='UTF-8' ) as fh:
    long_description = fh.read( )

with open( "VERSION", "r", encoding='UTF-8' ) as version_file:
    version_num = version_file.read( ).strip( )

setup(
    name='mkdocs-link-embeds-plugin',
    version=version_num,
    description='Mkdocs plugin which shows embedded links in a more elegant manner.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='mkdocs',
    url='https://github.com/Aetherinox/mkdocs-link-embeds',
    author='Aetherinox',
    author_email='aetherinox@proton.me',
    dependency_links=open("requirements.txt").read().split("\n"),
    license='MIT',
    project_urls={
        "Documentation": "https://aetherinox.github.io/mkdocs-link-embeds",
        "Bug Tracker": "https://github.com/Aetherinox/mkdocs-link-embeds/issues",
        "Source Code": "https://github.com/Aetherinox/mkdocs-link-embeds",
    },
    python_requires='>=2.7',
    install_requires=[
        'requests',
        'mkdocs>=1.2.0',
        'beautifulsoup4>=4.11.0'
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
        'mkdocs.plugins': ['link-embeds = mkdocs_link_embeds_plugin.plugin:LinkEmbedsPlugin']
    }
)
