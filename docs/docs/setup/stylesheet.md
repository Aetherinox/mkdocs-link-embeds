---
title: Install
tags:
  - install
---

## Create New Stylesheet
After you have followed the instructions on the previous page [install](../../setup/install), you now need to install the stylesheet properties which will allow the plugin to appear properly in your install of mkdocs.

Copy the code in the below codeblock and create a new file within your mkdocs folder where you currently place your other custom css files; which is usually `/docs/stylesheets/`. 

You can name the file whatever, but for documentation purposes; we will create `/docs/stylesheets/link-embeds.css`. 

The stylesheet code is also available on the repo located [here](https://github.com/Aetherinox/mkdocs-link-embeds/blob/main/mkdocs_link_embeds_plugin/resources/link-embeds.css).

<br />

``` title="link-embeds.css"
--8<-- "https://raw.githubusercontent.com/Aetherinox/mkdocs-link-embeds/main/mkdocs_link_embeds_plugin/resources/link-embeds.css"
```

<br />

## Modify mkdocs.yml
After you have created the css file, you now need to open your `mkdocs.yml` config file and tell mkdocs where to find your new CSS file using the `extra_css` property:

``` yaml
extra_css:
  - stylesheets/link-embeds.css
```

<br />

If you are going to be editing the stylesheet and want to make sure you don't get stuck with a cached version that doesn't change for long periods; append a version number to the end of the css file path:

``` yaml
extra_css:
  - stylesheets/link-embeds.css?v1.0
```

<br />

If you make changes to this plugin's `link-embeds.css` file and want to see the changes immediately; change `v1.0` to a higher number and then refresh your page.

<br />

---

<br />