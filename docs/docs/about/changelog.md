---
title: "Changelog"
tags:
  - changelog
---

# Changelog

<p align="center" markdown="1">

[![Version-Github][github-version-img]][github-version-uri]
[![Version-Pypi][pypi-version-img]][pypi-version-uri]
[![Build Status][github-build-pypi-img]][github-build-pypi-uri]
[![Downloads][github-downloads-img]][github-downloads-uri]
[![Size][github-size-img]][github-size-img]
[![Last Commit][github-commit-img]][github-commit-img]

</p>

### <!-- md:version stable- --> 0.2.0 <small>Aug 07, 2024</small> { id="0.2.0" }

- `feat`: add verbose printing and plugin setting
- `perf`: disable fetchurl if user inputs custom values
- `perf`: use .join in favor of += for concat
- `fix`: title, name site metadata not converted to string
- `ci`: update github workflows
- `style`: changed the overall code structure to combine statements, make things more streamline.
- `docs`: new dark theme

<br />

### <!-- md:version stable- --> 0.1.10 <small>Mar 22, 2024</small> { id="0.1.10" }

- `feat`: integrated developer logging which ties into verbose mode

<br />

### <!-- md:version stable- --> 0.1.9 <small>March 22, 2024</small> { id="0.1.9" }

- `feat`: add `verbose` config
    - outputs various detailed logs related to certain processes

<br />

### <!-- md:version stable- --> 0.1.8 <small>March 21, 2024</small> { id="0.1.8" }

- `feat`: add `accent` property
- `feat`: advanced favicon fetching
- `dep`: added package `request` to dependencies
- `change`: ability to give custom names, descriptions, and images for invalid links
- `change`: add backup metadata sources for all properties, e.g: `og:description` and `description`
- `change`: added user agent to keep certain sites from blocking crawling
- `fix`: certain websites returning nil values for missing metadata

<br />

### <!-- md:version stable- --> 0.1.7 <small>March 21, 2024</small> { id="0.1.7" }

- `refactor`: removal of fallback template
    - plugin now uses one template to control all links
- `refactor`: updated and cleaned css file to remove excess properties
- `change`: updated regex rule
    - now ignores spaces between property and value
- `change`: `BeautifulSoup` now handles all links through the same methods, both valid and invalid
- `change`: `fetchurl` module now utilized to grab link metadata
- `change`: added css properties to define additional properties for users using different mkdocs themes

<br />

### <!-- md:version stable- --> 0.1.6 <small>March 19, 2024</small> { id="0.1.6" }

- `feat`: added `target` property for embed code blocks
- `change`: updated fallback.html template to match that of the view.html template

<br />

### <!-- md:version stable- --> 0.1.5 <small>March 19, 2024</small> { id="0.1.5" }

- `feat`: added `favicon_size` property for embed code blocks
- `fix`: bug which made codeblock css conflict with normal codeblocks and syntax highlighting

<br />

### <!-- md:version stable- --> 0.1.3 <small>March 19, 2024</small> { id="0.1.3" }

- `feat`: added `favicon` property for embed code blocks
- `feat`: added `favicon_disabled` config option
- `feat`: added `favicon_default` config option
- `feat`: added `image_default` config option
- `feat`: added `false` value which can be used for `image` and `favicon` properties
- `change`: renamed all default value configs
    - `default_name` ⮞ `name_default`
    - `default_desc` ⮞ `desc_default`
    - `default_image` ⮞ `image_default`
- `change`: plugin now uses new structure

<br />

### <!-- md:version stable- --> 0.1.2 <small>March 19, 2024</small> { id="0.1.2" }

- `change`: updated plugin structure to utilize `pyproject.toml` and install dependencies
- `fix`: make regex rule more strict in regards to `embed` keyword.
    - before update, embedded link would display if you added any letters after `embed`, such as `embedasdasdasd`

<br />

### <!-- md:version stable- --> 0.1.1 <small>March 18, 2024</small> { id="0.1.1" }

- `fix`: changed matching rules so that raw-code embedded codeblocks will not render
- `fix`: z-index on embedded link cover with mkdocs Material theme header
- `style`: modified how embedded links appear and now utilize mkdocs css variables
- `style`: changed default cover image for unresolved links

<br />

### <!-- md:version stable- --> 0.1.0 <small>March 18, 2024</small> { id="0.1.0" }

- First public release

<br />

### <!-- md:version stable- --> 0.0.6 <small>March 15, 2024</small> { id="0.0.6" }

- Initial private release

<br />

---

<br />

<!-- BADGE > GENERAL -->
  [general-npmjs-uri]: https://npmjs.com
  [general-nodejs-uri]: https://nodejs.org
  [general-npmtrends-uri]: http://npmtrends.com/mkdocs-link-embeds

<!-- BADGE > VERSION > GITHUB -->
  [github-version-img]: https://img.shields.io/github/v/tag/Aetherinox/mkdocs-link-embeds?logo=GitHub&label=Version&color=ba5225
  [github-version-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/releases

<!-- BADGE > VERSION > NPMJS -->
  [npm-version-img]: https://img.shields.io/npm/v/mkdocs-link-embeds?logo=npm&label=Version&color=ba5225
  [npm-version-uri]: https://npmjs.com/package/mkdocs-link-embeds

<!-- BADGE > VERSION > PYPI -->
  [pypi-version-img]: https://img.shields.io/pypi/v/mkdocs-link-embeds-plugin
  [pypi-version-uri]: https://pypi.org/project/mkdocs-link-embeds-plugin/

<!-- BADGE > LICENSE > MIT -->
  [license-mit-img]: https://img.shields.io/badge/MIT-FFF?logo=creativecommons&logoColor=FFFFFF&label=License&color=9d29a0
  [license-mit-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/blob/main/LICENSE

<!-- BADGE > GITHUB > DOWNLOAD COUNT -->
  [github-downloads-img]: https://img.shields.io/github/downloads/Aetherinox/mkdocs-link-embeds/total?logo=github&logoColor=FFFFFF&label=Downloads&color=376892
  [github-downloads-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/releases

<!-- BADGE > NPMJS > DOWNLOAD COUNT -->
  [npmjs-downloads-img]: https://img.shields.io/npm/dw/%40aetherinox%2Fmkdocs-link-embeds?logo=npm&&label=Downloads&color=376892
  [npmjs-downloads-uri]: https://npmjs.com/package/mkdocs-link-embeds

<!-- BADGE > GITHUB > DOWNLOAD SIZE -->
  [github-size-img]: https://img.shields.io/github/repo-size/Aetherinox/mkdocs-link-embeds?logo=github&label=Size&color=59702a
  [github-size-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/releases

<!-- BADGE > NPMJS > DOWNLOAD SIZE -->
  [npmjs-size-img]: https://img.shields.io/npm/unpacked-size/mkdocs-link-embeds/latest?logo=npm&label=Size&color=59702a
  [npmjs-size-uri]: https://npmjs.com/package/mkdocs-link-embeds

<!-- BADGE > CODECOV > COVERAGE -->
  [codecov-coverage-img]: https://img.shields.io/codecov/c/github/Aetherinox/mkdocs-link-embeds?token=MPAVASGIOG&logo=codecov&logoColor=FFFFFF&label=Coverage&color=354b9e
  [codecov-coverage-uri]: https://codecov.io/github/Aetherinox/mkdocs-link-embeds

<!-- BADGE > ALL CONTRIBUTORS -->
  [contribs-all-img]: https://img.shields.io/github/all-contributors/Aetherinox/mkdocs-link-embeds?logo=contributorcovenant&color=de1f6f&label=contributors
  [contribs-all-uri]: https://github.com/all-contributors/all-contributors

<!-- BADGE > GITHUB > BUILD > NPM -->
  [github-build-img]: https://img.shields.io/github/actions/workflow/status/Aetherinox/mkdocs-link-embeds/npm-release.yml?logo=github&logoColor=FFFFFF&label=Build&color=%23278b30
  [github-build-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/actions/workflows/npm-release.yml

<!-- BADGE > GITHUB > BUILD > Pypi -->
  [github-build-pypi-img]: https://img.shields.io/github/actions/workflow/status/Aetherinox/mkdocs-link-embeds/release-pypi.yml?logo=github&logoColor=FFFFFF&label=Build&color=%23278b30
  [github-build-pypi-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/actions/workflows/release-pypi.yml

<!-- BADGE > GITHUB > TESTS -->
  [github-tests-img]: https://img.shields.io/github/actions/workflow/status/Aetherinox/mkdocs-link-embeds/npm-tests.yml?logo=github&label=Tests&color=2c6488
  [github-tests-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/actions/workflows/tests.yml

<!-- BADGE > GITHUB > COMMIT -->
  [github-commit-img]: https://img.shields.io/github/last-commit/Aetherinox/mkdocs-link-embeds?logo=conventionalcommits&logoColor=FFFFFF&label=Last%20Commit&color=313131