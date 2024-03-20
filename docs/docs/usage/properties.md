---
title: How to use Link Embeds
tags:
  - usage
---

# Properties
This section explains the various properties that can be used when creating an embedded link within your mkdocs. A list of the available properties have been outlined below, as well as a description of what each one does and how to use them.

<br />

## Overview
You have numerous properties you can set for each embedded link:

| Property | Description |
| --- | --- |
| `url` | Path to the website you want to link to |
| `name` | Name to display at the top of the embedded link block |
| `desc` | A description to show below the name for the codeblock |
| `image` | An image that will display on the left side of the embedded codeblock. Name and description will show on the right of the image |
| `favicon` | Favicon / small image that will display to the left side of the website address |
| `favicon_size` | Size of the favicon to display next to the website link |
| `target` | Specifies how a link will open, either in the same window, or a new window |

<br />

### URL
<!-- md:version stable-0.1.0 -->
<!-- md:flag required -->

The `url` property is the only **required** property that you must set when embedding a website. Simply specify the `url` property, followed by a colon `:`, and then the URL to the website you wish to mebed.

````ini
```embed
url:   https://squidfunk.github.io/mkdocs-material/
```
````

<br />

### Name
<!-- md:version stable-0.1.0 -->
<!-- md:default `Untitled` -->

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
<!-- md:version stable-0.1.0 -->
<!-- md:default `No description` -->

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
<!-- md:version stable-0.1.1 -->
<!-- md:default `https://github.com/Aetherinox/mkdocs-link-embeds/assets/118329232/98179e23-ce03-4101-a858-56db0cd0e8f0` -->

The `image` property allows you to display an image to the left of each embedded website. You can either provide the `url` and let the plugin automatically fetch an image to use, or you can force your own image to be used.

<br />

The example below will automatically fetch an image to use from the website you specified:

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
```
````

<br />

#### Custom
<!-- md:version stable-0.1.1 -->

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

#### Hide
<!-- md:default `false` -->

If you decide to not use an image, you will see the following:

```embed
url:      https://squidfunk.github.io/mkdocs-material/
image:    false
```

<br />
<br />

### Favicon
<!-- md:version stable-0.1.3 -->
<!-- md:default `false` -->

A favicon is a small, 16x16 pixel icon used on web browsers to represent a website or a web page. Short for “favorite icon,”' favicons are commonly displayed on tabs at the top of a web browser, but they're also found on your browser's bookmark bar, history and in search results, alongside the page url.

<br />

The example below will automatically fetch the favicon to use from the website you specified:

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
```
````

<br />

#### Custom
<!-- md:version stable-0.1.3 -->

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

#### Hide
<!-- md:version stable-0.1.3 -->
<!-- md:default `false` -->

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

<br />

#### Size
<!-- md:version stable-0.1.5 -->
<!-- md:default 25 -->

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

### Target
<!-- md:version stable-0.1.6 -->
<!-- md:default `true` -->

The `target` property allows you to define how a link will open when it is pressed. There are two options available:

1. Open link in the **same window** they're using to browse your documenation
2. Open link in **new window**, allowing them to also stay on your documentation site

<br />

You can define `target` in the following manner:

=== ":octicons-file-code-16: `New Window`"

    ````ini
    ```embed
    url:          https://squidfunk.github.io/mkdocs-material/
    target:       blank
    ```
    ````

=== ":octicons-file-code-16: `Same Window`"

    ````ini
    ```embed
    url:          https://squidfunk.github.io/mkdocs-material/
    target:       self
    ```
    ````

<br />

A few keywords have been added so that you can have an easier time remembering what the values are. You may enter any of the following words:

| Target | Acceptable Words |
| --- | --- |
| New Window | `_blank`, `blank`, `new`, `window`, `open` |
| Same Window | `_self`, `self`, `same`, `current` |

<br />

If no target is specified; all links will open in a **new window**.

<br />
<br />