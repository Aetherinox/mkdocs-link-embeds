---
title: Install
tags:
  - install
---

# Install
The following explains how to install the Link Embeds plugin.


<br />

## Pip

You may download this plugin from Pypi:

```embed
url:      https://pypi.org/project/mkdocs-link-embeds-plugin/
name:     Pypi: Download Mkdocs Link Embeds
desc:     The Link Embeds plugin for mkdocs displays links with a more modern appearance. Links will automatically be populated with an image, description, and title for the target website; or you can override the values to specify your own. 
favicon:  https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/25a032c6-515f-4cc8-a278-d9bc6b13dbe5
```

<br />

Open your terminal / command prompt and execute:

```
pip install mkdocs-link-embeds-plugin
```

<br />

!!! note annotate "Plugin Dependencies: Version v0.1.2"

    The package has been modified to automatically install any dependencies that this plugin requires. You should not have to manually install `beautifulsoup4`. If you end up having to install it, reach out and create a Github issue.

If for some reason you need to manually install the dependency; execute the following:

```shell
pip install beautifulsoup4
```

<br />

## Install CSS
After installation is complete, grab the [link-embeds.css](https://github.com/Aetherinox/mkdocs-link-embeds/blob/main/mkdocs_link_embeds_plugin/resources/link-embeds.css) file available in this repo, and place it in the mkdocs folder where you currently keep your other css overrides.

<br />

Open `mkdocs.yml` and add the following line to define where your CSS file is stored:

``` yaml
extra_css:
  - path/to/link-embeds.css
```

<br />

Finally, inside `mkdocs.yml`; define the plugin and change whatever values you wish by adding:

``` yaml
plugins:
  - link-embeds:
      enabled: true
      favicon_disabled: false
      favicon_size: 25
      favicon_default: "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/b37da9c6-6f17-4c3f-9c94-c346a6f31bfa"
      name_default: "Untitled Link"
      desc_default: "No description found"
      image_disabled: false
      image_default: "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/c0298d98-0910-4235-a88f-0c3e2f704ba7"
```

<br />

For an explanation of the settings above, read further down.

<br />
<br />

## Configuration
The following settings are available for this plugin.

| Property | Description |
| --- | --- |
| `enabled` | Specifies if the plugin should be enabled or not. Useful for local environments |
| `name_default` | If the name of the specified website cannot be automatically pulled through the metadata, this will be the fallback name that will appear if you do not define your own custom name |
| `desc_default` | If the description of the specified website cannot be automatically pulled through the metadata, this will be the fallback description that will appear if you do not define your own |
| `image_default` | When specifying a URL to link, this plugin will first attempt to automatically locate an imagine / logo on the website and use that as the cover image. If one cannot be located; this will be the fallback image that will be displayed to the left of each embedded link. |
| `image_disabled` | Disables images for every embedded block |
| `favicon_default` | Sets the default favicon to use when the plugin cannot automatically find one |
| `favicon_size` | Global size to set the favicon for all embedded links |
| `favicon_disabled` | Disables favicon for every embedded block |
