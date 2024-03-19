---
title: How to use Link Embeds
tags:
  - usage
---

# Usage
This section explains how to use the Link Embeds plugin and the different options that are available to customize. A list of the available properties have been outlined below, as well as a description of what each one does and how to use them.

<br />
<br />

## Properties
You have numerous properties you can set for each embedded link:

| Property | Description |
| --- | --- |
| `url` | Path to the website you want to link to |
| `name` | Name to display at the top of the embedded link block |
| `desc` | A description to show below the name for the codeblock |
| `image` | An image that will display on the left side of the embedded codeblock. Name and description will show on the right of the image |
| `favicon` | Favicon / small image that will display to the left side of the website address |
| `favicon_size` | Size of the favicon to display next to the website link |

<br />

### URL
The `url` property is the only **required** property that you must set when embedding a website. Simply specify the `url` property, followed by a colon `:`, and then the URL to the website you wish to mebed.

````ini
```embed
url:   https://squidfunk.github.io/mkdocs-material/
```
````

<br />

### Name
The `name` property displays the website title at the top of your embedded website codeblock. If you do not specify a name when adding a new embedded link, the title for the website will be automatically collected by the plugin.

````ini
```embed
url:    https://squidfunk.github.io/mkdocs-material/
name:   Mkdocs Material Theme
```
````

```embed
url:    https://squidfunk.github.io/mkdocs-material/
name:   Mkdocs Material Theme
```

<br />

### Description
The `desc` property displays below the website name. It is a short description that describes the website. By not specifying the `desc` property; the plugin will automatically scan the website and pull the description provided by the website developer.

````ini
```embed
url:    https://squidfunk.github.io/mkdocs-material/
desc:   A custom theme for Mkdocs that makes things look cool.
```
````

```embed
url:    https://squidfunk.github.io/mkdocs-material/
desc:   A custom theme for Mkdocs that makes things look cool.
```


<br />

### Image
The `image` property allows you to display an image to the left of each embedded website. You can either provide the `url` and let the plugin automatically fetch an image to use, or you can force your own image to be used.

<br />

The example below will automatically fetch an image to use from the website you specified:

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
```
````

<br />

To manually use your own image, provide the `image` property.

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
image:    https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjFUDe-vdiprKpCsiLoRmfCdUq0WS5tqUR9fyEzJjQ0g&s
```
````

<br />

On top of being able to specify an image to use; you can also disable images completely by using `false` as the property value:

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
image:    false
```
````

<br />

If you decide to not use an image, you will see the following:

```embed
url:      https://squidfunk.github.io/mkdocs-material/
image:    false
```

<br />
<br />

### Favicon
A favicon is a small, 16x16 pixel icon used on web browsers to represent a website or a web page. Short for “favorite icon,”' favicons are commonly displayed on tabs at the top of a web browser, but they're also found on your browser's bookmark bar, history and in search results, alongside the page url.

<br />

The example below will automatically fetch the favicon to use from the website you specified:

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
```
````

<br />

To manually use your own favicon, provide the `favicon` property.

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
favicon:  https://plmlab.math.cnrs.fr/uploads/-/system/project/avatar/1364/mkdocs_logo.png
```
````

With the code provided above, we grabbed a random image and set it as the favicon, which will show the following:

```embed
url:      https://squidfunk.github.io/mkdocs-material/
favicon:  https://plmlab.math.cnrs.fr/uploads/-/system/project/avatar/1364/mkdocs_logo.png
```

<br />

If you wish to hide the favicon completely, instead of using a website URL, set the property to `false`.

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
favicon:  false
```
````

<br />

If you decide to not use an image, you will see the following:

```embed
url:      https://squidfunk.github.io/mkdocs-material/
favicon:  false
```

<br />

You'll notice that the small icon to the left of the website URL has disappeared.

Additionally, you can force your favicon to use a certain size. This is useful for images that may not appear properly at smaller sizes, or if the icon is hard to see due to similar colors. To change the favicon size, use the `favicon_size` property:

````ini
```embed
url:          https://squidfunk.github.io/mkdocs-material/
favicon:      https://plmlab.math.cnrs.fr/uploads/-/system/project/avatar/1364/mkdocs_logo.png
favicon_size: 26
```
````

```embed
url:          https://squidfunk.github.io/mkdocs-material/
favicon:      https://plmlab.math.cnrs.fr/uploads/-/system/project/avatar/1364/mkdocs_logo.png
favicon_size: 26
```

<br />

The above code will set the size of your favicon to `26 x 26` pixels for width and height. Ensure that you do not set this value too high, otherwise it will look too big for the embedded codeblock compared to the size of the other elements.

<br />
<br />

## Formatting
!!! warning annotate "Formatting Your Codeblock"

    When adding an embedded codeblock, make sure there is at least one blank line BEFORE the codeblock, and one blank line after. This ensures that guides like this can actually display the code instead of having an embedded URL render.

When formatting your embedded link codeblock; you can structure it however you desire. It is not sensitive to how many spaces you use, or if you wrap your links or property values in quotation marks. Anything is acceptable.

Any of the following examples are acceptable and work:

````ini
```embed
url:         "https://yourdomain.com"
url:https://yourdomain.com
```
````

<br />

The only aspect that is required is the name of the property, a colon, and then the value:

```ini
property: value
```

<br />
<br />

## Auto-Generated Metadata
If you create an embedded link block and only specify the `url` property; the plugin will scan the website and automatically fetch information such as:

- The name for the website from the website tag `og:title`
- A description for the website from the website tag `og:description`
- An image / logo that the plugin can display, comes from the html tag `og:image`
- A specified favicon, usually defined by the tag `icon` or `shortcut icon`

<br />

If you decide to manually provide any one of the properties listed above; that custom value will have priority over the automatically fetched information. If you specify `name` along with the `url`; then your custom name will appear in the embedded link block instead of the automatically fetched name. However, the `desc` and `image` will still use the automatically fetched data.