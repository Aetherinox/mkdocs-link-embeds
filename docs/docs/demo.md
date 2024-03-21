---
title: Demo
---

# Auto-fetch Metadata
The following example simply specifies the URL for the target website. The name, description, favicon, and image are auto-generated.

```embed
url:        https://squidfunk.github.io/mkdocs-material/
```

````ini
```embed
url: https://squidfunk.github.io/mkdocs-material/
```
````

<br />

# Custom Values
This example uses the same link as the one above, however, each value is manually defined:

```embed
url:            https://squidfunk.github.io/mkdocs-material/
image:          https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjFUDe-vdiprKpCsiLoRmfCdUq0WS5tqUR9fyEzJjQ0g&s
name:           Github: Download Mkdocs
desc:           MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
favicon:        https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/6433449b-2988-4da3-9d43-ff4c992a9fcf
favicon_size:   25
```

```` ini
```embed
url:             https://squidfunk.github.io/mkdocs-material/
image:           https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjFUDe-vdiprKpCsiLoRmfCdUq0WS5tqUR9fyEzJjQ0g&s
name:            Github: Download Mkdocs
desc:            MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
favicon:         https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/6433449b-2988-4da3-9d43-ff4c992a9fcf
favicon_size:    25
```
````

<br />

# Minimal
The following example displays a website, however, removes the image and favicon completely.

```embed
url:            https://squidfunk.github.io/mkdocs-material/
name:           Github: Download Mkdocs
desc:           MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
image:          false
favicon:        false
```

````ini
```embed
url:            https://squidfunk.github.io/mkdocs-material/
name:           Github: Download Mkdocs
desc:           MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
image:          false
favicon:        false
```
````

<br />

# Accent Color
The following presents an embedded link with a custom accent color border

```embed
url:        https://github.com/Aetherinox/mkdocs-link-embeds
accent:     f01348e0
```

````ini
```embed
url:        https://github.com/Aetherinox/mkdocs-link-embeds
accent:     f01348e0
```
````

<br />

# Unresolvable URL
The following is an example of a bad URL being rendered.

```embed
url: https://githubahubahuba.com/badurl/
```

````ini
```embed
url: https://githubahubahuba.com/badurl/
```
````