---
title: Properties
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
| `accent` | An accent color which borders the embedded link box |

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
<!-- md:flag experimental -->

A favicon is a small, 16x16 pixel icon used on web browsers to represent a website or a web page. Short for “favorite icon,”' favicons are commonly displayed on tabs at the top of a web browser, but they're also found on your browser's bookmark bar, history and in search results, alongside the page url.

<br />

!!! warning annotate "Favicon Performance Impact"

    Numerous libraries were tested for scraping websites for favicons, which presented a series of issues and slow performance. This plugin presents a custom method for scaping websites for favicons, which does improve performance, however, if your documentation contains a lot of links; building the documentation may take a bit of time. 

    If you provide an override favicon path; the plugin will not waste the resources trying to find the website favicon which improves performance. If you disable favicons all-together via your `mkdocs.yml`, or for a certain links; it will also improve performance.

    This only affects building your mkdocs, not using the website as a visitor.

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

### Accent
<!-- md:version stable-0.1.7 -->
<!-- md:default `FFFFFF1A` -->

The `accent` property allows you to change the outline color which surrounds the embedded link box. It accepts `hex` values with an opacity

<br />

```embed
url:      https://squidfunk.github.io/mkdocs-material/
accent:   D84689FF
```

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
accent:   D84689FF
```
````

<br />

```embed
url:      https://squidfunk.github.io/mkdocs-material/
accent:   4C59BFE0
```

````ini
```embed
url:      https://squidfunk.github.io/mkdocs-material/
accent:   4C59BFE0
```
````

<br />

#### Using Hex

To create custom colors, you can use combinations of the hexadecimal numbers, which represent specific colors. For a hex color, there are six digits of hexadecimal values. Each pair of two digits represents **red**, **green**, and **blue**. The pattern looks like `#RRGGBB` (where red is R, green is G, and blue is B).

<br />

Colors are represented by a combination of red, green, and blue values. The lowest value (00) will be the darkest version of the color (closest to black), and the highest value (FF) will be the lightest version of the color (closest to white).

<br />

Each single value can be any of the following:

| Type | Characters |
| --- | --- |
| Numerical | 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 |
| Alphabetic | A, B, C, D, E, F |

<br />

The following is a list of common colors to show how your color values should appear:

| Color | Hex |
| --- | --- |
| Black | `000000` |
| White | `FFFFFF` |
| Silver | `C0C0C0` |
| Gray | `808080` |
| Red | `FF0000` |
| Yellow | `FFFF00` |
| Green | `008000` |
| Blue | `0000FF` |

<br />

#### Using Hex Opacity

When it comes to hex colors with opacity / transparency, you will add an additional two values to the hex color, meaning in total, you will have 8 values with the structure `RRGGBBAA`. `00` being completely opaque / transparent, and `FF` being solid. A list of the values for opacity and their percentages have been listed below. _(click the box to show)_
<br />

??? info "Hex Opacity / Transparency Values"

    ``` { .annotate }
      100% — FF
      99% — FC
      98% — FA
      97% — F7
      96% — F5
      95% — F2
      94% — F0
      93% — ED
      92% — EB
      91% — E8
      90% — E6
      89% — E3
      88% — E0
      87% — DE
      86% — DB
      85% — D9
      84% — D6
      83% — D4
      82% — D1
      81% — CF
      80% — CC
      79% — C9
      78% — C7
      77% — C4
      76% — C2
      75% — BF
      74% — BD
      73% — BA
      72% — B8
      71% — B5
      70% — B3
      69% — B0
      68% — AD
      67% — AB
      66% — A8
      65% — A6
      64% — A3
      63% — A1
      62% — 9E
      61% — 9C
      60% — 99
      59% — 96
      58% — 94
      57% — 91
      56% — 8F
      55% — 8C
      54% — 8A
      53% — 87
      52% — 85
      51% — 82
      50% — 80
      49% — 7D
      48% — 7A
      47% — 78
      46% — 75
      45% — 73
      44% — 70
      43% — 6E
      42% — 6B
      41% — 69
      40% — 66
      39% — 63
      38% — 61
      37% — 5E
      36% — 5C
      35% — 59
      34% — 57
      33% — 54
      32% — 52
      31% — 4F
      30% — 4D
      29% — 4A
      28% — 47
      27% — 45
      26% — 42
      25% — 40
      24% — 3D
      23% — 3B
      22% — 38
      21% — 36
      20% — 33
      19% — 30
      18% — 2E
      17% — 2B
      16% — 29
      15% — 26
      14% — 24
      13% — 21
      12% — 1F
      11% — 1C
      10% — 1A
      9% — 17
      8% — 14
      7% — 12
      6% — 0F
      5% — 0D
      4% — 0A
      3% — 08
      2% — 05
      1% — 03
      0% — 00
    ```

<br />

#### Colorpicker
If you would like a visual color picker, utilize the tool below:

```embed
url:    https://www.webfx.com/web-design/color-picker/
name:   Online Color Picker
image:  https://play-lh.googleusercontent.com/DoTrq2XuQOteT32rxsxOgiw2vwjU5nZJP8FFB_0D4VrXfb17c_LEUoW0Rj3my4mAbg
```

<br />

For a color picker with Hex + Opacity, visit:

```embed
url:    https://rgbcolorpicker.com/0-1
name:   Online Color Picker with Opacity
image:  https://is4-ssl.mzstatic.com/image/thumb/Purple124/v4/46/71/a9/4671a9a2-bfdd-ffda-5a8b-5b88f7520c7f/AppIcon-1x_U007emarketing-0-7-0-85-220.png/256x256bb.jpg
```

<br />
<br />