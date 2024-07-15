<div align="center">
<h6>Mkdocs Plugin</h6>
<h1>♾️ Link Embeds ♾️</h1>

<br />

<p>Display embedded links in a more elegant and modern way with the use of markdown codeblocks. Supports automatically fetching website data, or allows for you to override various values.</p>

<br />

<img src="https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/a30aff26-8cba-4a90-ab60-75105c5189d6" width="630">

<br />
<br />

</div>

<div align="center">

<!-- prettier-ignore-start -->
[![Version][github-version-img]][github-version-uri] [![Version][pypi-version-img]][pypi-version-uri]  [![Build Status][github-build-pypi-img]][github-build-pypi-uri] [![Downloads][github-downloads-img]][github-downloads-uri] [![Size][github-size-img]][github-size-img] [![Last Commit][github-commit-img]][github-commit-img]
<!-- prettier-ignore-end -->

</div>

<br />

---

<br />

- [About](#about)
- [Documentation](#documentation)
- [Install](#install)
  - [Usage](#usage)

<br />

---

<br />

# About
This plugin requires [mkdocs](https://www.mkdocs.org/) to function.

This plugin allows you to display embedded links in a more elegant and modern way with the use of markdown codeblocks. You may either specify a URL and let the plugin auto-fill in details such as the site description and title, or you can override the auto-generated values and add your own.

<br />

<p align="center"><img style="width: 85%;text-align: center;border: 1px solid #353535;" src="https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/afc068d8-fd8e-448e-ab1c-b026cd5076d2"></p>

<br />

<p align="center"><img style="width: 85%;text-align: center;border: 1px solid #353535;" src="https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/a30aff26-8cba-4a90-ab60-75105c5189d6"></p>

<br />

---

<br />

# Documentation
If you wish to view the complete documentation for this plugin, including installation and usage; visit https://aetherinox.github.io/mkdocs-link-embeds/

<br />

---

<br />

# Install

Install the package for this plugin by running the command:

```text
pip install mkdocs-link-embeds-plugin
```

<br />

Once you [install](#install) the package above, open your `mkdocs.yml` and add a few new lines:

<br />

```yaml
plugins:
  - link-embeds:
      enabled: true
      name_default: "Untitled Link"
      desc_default: "No description found"
      image_default: "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/c0298d98-0910-4235-a88f-0c3e2f704ba7"
      image_disabled: false
      favicon_default: "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/b37da9c6-6f17-4c3f-9c94-c346a6f31bfa"
      favicon_disabled: false
      favicon_size: 25
      target: "blank"
      accent: "FFFFFF1A"
      verbose: false

extra_css:
  - path/to/link-embeds.css
```

<br />

Ensure you download the contents of `mkdocs_link_embeds_plugin/resources/link-embeds.css` and place the file in your mkdocs directory. It must be placed in the path you specified under `extra_css` in the mkdocs.yml config above.

<br />

---

<br />

## Usage
Once you have installed this plugin, you may now create a new page in your mkdocs project and insert a new codeblock with the following syntax:

<br />

````markdown
```embed
url:            https://github.com/mkdocs/mkdocs/releases
name:           Github: Download Mkdocs
desc:           MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
image:          https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/98179e23-ce03-4101-a858-56db0cd0e8f0
favicon:        https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/13a151b1-d7f9-4e27-909b-a26986ab0954
favicon_size:   25
target:         new
accent:         4C59BFE0
```
````

<br />

This plugin accepts numerous properties:
- `url`: The URL to the link.
- `name`: Name / Title to show at the top of each embed.
- `desc`: A description of what the site is for.
- `image`: Image to display on the left side of each embedded website.
- `favicon`: Favicon to display at the bottom, next to the link.
- `favicon_size`: Favicon size.
- `target`: Determines whether link opens in new window or same window.
- `accent`: Specify accent color for embedded link surrounding border

<br />

The only **required** value is `url`.

<br />

If you provide only the `url`, and leave the others out; the plugin will attempt to check if your URL is valid, and then auto-fetch the metadata for that website. It will be used to populate the fields you did not provide.

<br />

If you do provide values such as `desc`, `name`, or `image`; those user inputs will take priority over the automatically fetched values.

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<br />
<br />

<!-- prettier-ignore-start -->

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
  [github-commit-uri]: https://github.com/Aetherinox/mkdocs-link-embeds/commits/main/
<!-- prettier-ignore-end -->
