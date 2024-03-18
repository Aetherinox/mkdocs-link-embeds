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

<p align="center"><img style="width: 85%;text-align: center;border: 1px solid #353535;" src="https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/5eab3f3a-b4bc-4c1a-a914-05df344f7ee0"></p>

<br />

<p align="center"><img style="width: 85%;text-align: center;border: 1px solid #353535;" src="https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/252fda99-47c7-40d1-9103-e98b40fce997"></p>

<br />

---

<br />


# Install

```text
pip install beautifulsoup4
pip install mkdocs-link-embeds-plugin
```

<br />

Once you [install](#install) the packages above, open your `mkdocs.yml` and add a few new lines:

<br />

```yaml
plugins:
  - link-embeds:
      enabled: true
      default_name: "Untitled Link"
      default_desc: "No description found"
      default_image: "https://path/to/default/image.png"
  
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
url:    https://github.com/mkdocs/mkdocs/releases
image:  https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjFUDe-vdiprKpCsiLoRmfCdUq0WS5tqUR9fyEzJjQ0g&s
name:   Github: Download Mkdocs
desc:   MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions.
```
````

<br />

This plugin takes 4 values:
- `url`: The URL to the link
- `image`: Image to display on the left side of each embedded website.
- `name`: Name / Title to show at the top of each embed
- `desc`: A description of what the site is for.

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