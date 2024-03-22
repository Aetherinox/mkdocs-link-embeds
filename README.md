<p align="center"></p>
<h1 align="center"><b>Link Embeds Plugin: mkdocs</b></h1>

<div align="center">

![Version](https://img.shields.io/github/v/tag/Aetherinox/mkdocs-link-embeds?logo=GitHub&label=version&color=ba5225) ![Downloads](https://img.shields.io/github/downloads/Aetherinox/mkdocs-link-embeds/total) ![Repo Size](https://img.shields.io/github/repo-size/Aetherinox/mkdocs-link-embeds?label=size&color=59702a) ![Last Commit)](https://img.shields.io/github/last-commit/Aetherinox/mkdocs-link-embeds?color=b43bcc) ![PyPI - Version](https://img.shields.io/pypi/v/mkdocs-link-embeds-plugin)

</div>

<br />

---

<br />

# About
Requires [mkdocs](https://www.mkdocs.org/) to function.

This plugin allows you to display embedded links in a more elegant and modern way with the use of markdown codeblocks. You may either specify a URL and let the plugin auto-fill in details such as the site description and title, or you can override the auto-generated values and add your own.

<br />

<p align="center"><img style="width: 85%;text-align: center;border: 1px solid #353535;" src="https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/afc068d8-fd8e-448e-ab1c-b026cd5076d2"></p>

<br />

<p align="center"><img style="width: 85%;text-align: center;border: 1px solid #353535;" src="https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/a30aff26-8cba-4a90-ab60-75105c5189d6"></p>

<br />

---

<br />

# Documentation
If you wish to view the complete docuemtnation for this plugin, including installation and usage; visit https://aetherinox.github.io/mkdocs-link-embeds/

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

<br />

---

<br />

## Other
This plugin was originally based on ` mkdocs-link-preview-plugin`. However, that plugin stopped being updated, and the style needed to be modernized. As well as giving more control for customization.
The plugin has been completely re-written with a large number of added features.