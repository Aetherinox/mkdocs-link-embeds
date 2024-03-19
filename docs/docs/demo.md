---
title: Demo
---

# Auto-fetch Metadata
The following example simply specifies the URL to the target website. The name, description, and image are auto-generated.

```embed
url:        https://github.com/mkdocs/mkdocs/releases
```

````
```embed
url:    https://github.com/mkdocs/mkdocs/releases
```
````

<br />

# Custom Values
This example uses the same link as the one above, however, each value is manually defined:

```embed
url:    https://github.com/mkdocs/mkdocs/releases
image:  https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjFUDe-vdiprKpCsiLoRmfCdUq0WS5tqUR9fyEzJjQ0g&s
name:   Github: Download Mkdocs
desc:   MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
```

````
```embed
url:    https://github.com/mkdocs/mkdocs/releases
image:  https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjFUDe-vdiprKpCsiLoRmfCdUq0WS5tqUR9fyEzJjQ0g&s
name:   Github: Download Mkdocs
desc:   MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
```
````

<br />

# Unresolvable URL
The following is an example of a bad URL being rendered.

```embed
url:    https://githubahubahuba.com/mkdocs/mkdocs/releases
```

````
```embed
url:    https://githubahubahuba.com/mkdocs/mkdocs/releases
```
````