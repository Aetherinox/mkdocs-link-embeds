---
tags:
  - changelog
---

# Changelog

![Version](https://img.shields.io/github/v/tag/Aetherinox/mkdocs-link-embeds?logo=GitHub&label=version&color=ba5225) ![Downloads](https://img.shields.io/github/downloads/Aetherinox/mkdocs-link-embeds/total) ![Repo Size](https://img.shields.io/github/repo-size/Aetherinox/mkdocs-link-embeds?label=size&color=59702a) ![Last Commit)](https://img.shields.io/github/last-commit/Aetherinox/mkdocs-link-embeds?color=b43bcc) ![PyPI - Version](https://img.shields.io/pypi/v/mkdocs-link-embeds-plugin)

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
<br />