---
title: Install
tags:
  - install
---

# Install
You may download this plugin from Pypi:

```embed
url:    https://pypi.org/project/mkdocs-link-embeds-plugin/
name:   Pypi: Download Mkdocs Link Embeds
desc:   The Link Embeds plugin for mkdocs displays links with a more modern appearance. Links will automatically be populated with an image, description, and title for the target website; or you can override the values to specify your own. 
```

<br />

Open your terminal / command prompt and execute:

```
pip install mkdocs-link-embeds-plugin
```

<br />

If for some reason you need to manually install the dependency, then also execute the command:

```
pip install beautifulsoup4
```

<br />

After installation is complete, grab the [link-embeds.css](https://github.com/Aetherinox/mkdocs-link-embeds/blob/main/mkdocs_link_embeds_plugin/resources/link-embeds.css) file available in this repo, and place it in the mkdocs folder where you currently keep your other css overrides.

<br />

Open `mkdocs.yml` and add the following line to define where your CSS file is stored:

```yml
extra_css:
  - path/to/link-embeds.css
```

<br />

Finally, inside `mkdocs.yml`; define the plugin and change whatever values you wish by adding:

```yml
plugins:
  - link-embeds:
      enabled: true
      default_name: "Untitled Link"
      default_desc: "No description found"
      default_image: "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/98179e23-ce03-4101-a858-56db0cd0e8f0"
```

<br />

For an explanation of the settings above, read further down.

<br />
<br />

# Configuration
The following settings are available for this plugin.

| Property | Description |
| --- | --- |
| `enabled` | Specifies if the plugin should be enabled or not. Useful for local environments |
| `default_name` | If the name of the specified website cannot be automatically pulled through the metadata, this will be the fallback name that will appear if you do not define your own custom name |
| `default_desc` | If the description of the specified website cannot be automatically pulled through the metadata, this will be the fallback description that will appear if you do not define your own |
| `default_image` | When specifying a URL to link, this plugin will first attempt to automatically locate an imagine / logo on the website and use that as the cover image. If one cannot be located; this will be the fallback image that will be displayed to the left of each embedded link. |

