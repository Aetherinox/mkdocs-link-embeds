---
title: How to use Link Embeds
tags:
  - usage
---

# Configs
This plugin includes a few `mkdocs.yml` configuration properties that you can define, as described below.

<br />

## Overview
You have numerous properties you can set for each embedded link:

| Config Value | Description |
| --- | --- |
| `enabled` | Specifies if the plugin is enabled or disabled. Useful for local environments |
| `name_default` | Default name to give an embedded link if the plugin cannot automatically find one, and if the user has not provided one. |
| `desc_default` | Default description to give an embedded link if the plugin cannot automatically find one, and if the user has not provided one. |
| `image_default` | Default image to give an embedded link if the plugin cannot automatically find one, and if the user has not provided one. |
| `image_disabled` | All embedded links will hide the left side image by default |
| `favicon_default` | Default favicon to give an embedded link if the plugin cannot automatically find one, and if the user has not provided one. |
| `favicon_disabled` | All embedded links will hide the favicon by default. |
| `favicon_size` | Default size to use on all favicons if the user has not specified a custom size. |
| `target` | Defines how all embedded links will open by default, unless the user specifies a custom property for each link |
| `accent` | Specifies the default border color each embedded link will be outlined with |

<br />

## Modifying Configs
The config options listed above can all be specified within your `mkdocs.yml` file. Add the following to the `plugins` section:

``` yaml
plugins:
  - link-embeds:
      enabled: !ENV CI # (1)!
      name_default: "Untitled Link"
      desc_default: "No description found"
      image_default: "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/c0298d98-0910-4235-a88f-0c3e2f704ba7"
      image_disabled: false
      favicon_default: "https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/13a151b1-d7f9-4e27-909b-a26986ab0954"
      favicon_disabled: false
      favicon_size: 25
      target: "blank" # (2)!
      accent: "FFFFFF1A"
```

1.  Use this setting to enable or disable the plugin. If you only want to use this plugin for better organization and
    always want to enable the plugins that are part of it, use:

    ``` yaml
    plugins:
      - link-embeds:
          enabled: true
    ```

2.  Available options:
      - New Window:`blank`
      - Current Window: `self`