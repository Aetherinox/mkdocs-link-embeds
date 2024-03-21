---
title: How to use Link Embeds
tags:
  - usage
---

# Formatting Rules
This section explains a few important notes to take into consideration when creating embedded links within your mkdocs.

<br />

## Syntax
When formatting your embedded link codeblock; you can structure it however you desire. It is not sensitive to how many spaces you use, or if you wrap your links or property values in quotation marks. Anything is acceptable.

The following examples show how properties within your embedded note can be structured:

````ini
```embed
url:https://yourdomain.com
url: 'https://yourdomain.com'
url:    "https://yourdomain.com"
```
````

<br />

The only aspect that is required is the name of the property, a colon, and then the value:

```ini
property: value
```

<br />

## Line Breaks
When adding an embedded codeblock, make sure there is at least **one blank line** _BEFORE_ the codeblock, and one _after_. This ensures that guides like this can actually display the raw code for the embedded block instead of having the code transform into a rendered embedded link.

```` ini hl_lines="1 5"
< --- BLANK LINE HERE --- >
```embed
url   : yourdomain.com
```
< --- BLANK LINE HERE --- >
````


<br />
<br />


## Metadata Priority
If you create an embedded link codeblock and only specify the `url` property; the plugin will scan the website and automatically fetch information such as:

- The name for the website from the website's html tag `og:title`
- A description for the website from the website's html tag `og:description`
- An image / logo that the plugin can display from website's html tag `og:image`
- A specified favicon, usually defined by the website's html tag `icon` or `shortcut icon`

<br />

If you decide to manually override any one of the properties listed above; that custom value will have priority over the automatically fetched value. 

Take the following as an example:

````ini
```embed
url:        https://squidfunk.github.io/mkdocs-material/
name:       My Title
```
````

```embed
url:        https://squidfunk.github.io/mkdocs-material/
name:       My Title
```

<br />

In the example above, only `url` and `name` were specified. By specifying a custom `name`, `desc`, `image`, or `favicon`; you are overriding whatever the plugin was able to automatically fetch from the website; and your custom specified value will be used instead of the automatically fetched `name`.

However, since only the `name` was specified, the other properties will still use the automatically fetched information captured from the specified website.

<br />
<br />

## Accent Colors
When specifying an accent color for your embedded links, you may specify a hex color with or without the pound symbol `#` Both examples are acceptable:

<br />

=== ":octicons-paintbrush-16: `Example 1`"
    ```
    accent:  d9204ce0
    ```

=== ":octicons-paintbrush-16: `Example 2`"
    ```
    accent:  #d9204ce0
    ```