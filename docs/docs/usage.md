---
title: How to use Link Embeds
tags:
  - usage
---

# Usage
In order to embed links within your documentation; you must utilize a `codeblock`. To signify a codeblock as an embed portal, you must append `embed` on the same line as your three backticks.

````
```embed
```
````

<br />

To specify a link, simply define `url: yourdomain.com` between your codeblock backticks

````
```embed
url:   https://yourdomain.com
```
````

<br />

!!! warning annotate "Formatting Your Codeblock"

    When adding an embedded codeblock, make sure there is at least one blank line BEFORE the codeblock, and one blank line after. This ensures that guides like this can actually display the code instead of having an embedded URL render.

<br />

When formatting your embedded link codeblock; you can structure it however you desire. It is not sensitive to how many spaces you use, or if you wrap your links and other definitions in quotation marks. Anything is acceptable.

Any of the following examples are acceptable and work:

````
```embed
url:         "https://yourdomain.com"
url:https://yourdomain.com
```
````

<br />
<br />

# Properties
You have numerous properties you can set for each embedded link:

| Property | Description |
| --- | --- |
| `url` | Path to the website you want to link to |
| `name` | Name to display at the top of the embedded link block |
| `desc` | A description to show below the name for the codeblock |
| `image` | An image that will display on the left side of the embedded codeblock. Name and description will show on the right of the image |
| `favicon` | Favicon / small image that will display to the left side of the website address |

<br />

For `image` and `favicon`, you can supply a direct image URL, or you can specify `false` to turn them off completely.

<br />

```
url:        https://github.com/mkdocs/mkdocs/releases
image:      false
favicon:    false
```

<br />

The above example will display an embedded link without an image or favicon (_as shown below_).

<br />

```embed
url:        https://github.com/mkdocs/mkdocs/releases
image:      false
favicon:    false
```

<br />
<br />

# Auto-Generated Metadata
If you create an embedded link block and only specify the `url` property; the plugin will scan the website and automatically fetch information such as:

- The name for the website from the website tag `og:title`
- A description for the website from the website tag `og:description`
- An image / logo that the plugin can display, comes from the html tag `og:image`
- A specified favicon, usually defined by the tag `icon` or `shortcut icon`

<br />

If you decide to manually provide any one of the properties listed above; that custom value will have priority over the automatically fetched information. If you specify `name` along with the `url`; then your custom name will appear in the embedded link block instead of the automatically fetched name. However, the `desc` and `image` will still use the automatically fetched data.