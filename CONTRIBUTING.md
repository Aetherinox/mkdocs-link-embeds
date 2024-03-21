<h1 align="center"><b>Contributing</b></h1>

<div align="center">

![Version](https://img.shields.io/github/v/tag/Aetherinox/mkdocs-link-embeds?logo=GitHub&label=version&color=ba5225) ![Downloads](https://img.shields.io/github/downloads/Aetherinox/mkdocs-link-embeds/total) ![Repo Size](https://img.shields.io/github/repo-size/Aetherinox/mkdocs-link-embeds?label=size&color=59702a) ![Last Commit)](https://img.shields.io/github/last-commit/Aetherinox/mkdocs-link-embeds?color=b43bcc) ![PyPI - Version](https://img.shields.io/pypi/v/mkdocs-link-embeds-plugin)

</div>

<br />

---

<br />

- [Submitting Bugs](#submitting-bugs)
- [Contributing](#contributing)
  - [Pull requests eligible for review](#pull-requests-eligible-for-review)
  - [Conventional Commit Specification](#conventional-commit-specification)
    - [Types](#types)
      - [Example 1:](#example-1)
      - [Example 2:](#example-2)
  - [References](#references)
  - [Vertical alignment](#vertical-alignment)
  - [Spaces Instead Of Tabs](#spaces-instead-of-tabs)
  - [Indentation Style](#indentation-style)
  - [Commenting](#commenting)
  - [Casing](#casing)


---

<br />

## Submitting Bugs

Please ensure that when you submit bugs; you are detailed.

* Explain the issue
* Describe how the function should operate, and what you are experiencing instead.
* Provide possible options for a resolution or insight

<br />

---

<br />

## Contributing

The source is here for everyone to collectively share and colaborate on. If you think you have a possible solution to a problem; don't be afraid to get your hands dirty.

Unless you are fixing a known bug, we strongly recommend discussing it with the core team via a GitHub issue before getting started to ensure your work does not conflict with future plans.

All contributions are made via pull requests. To make a pull request, you will need a GitHub account; if you are unclear on this process, see [GitHub's documentation on forking and pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork). Pull requests should be targeted at the master branch. 

<br />

### Pull requests eligible for review

- Follow the repository's code formatting conventions (see below);
- Include tests that prove that the change works as intended and does not add regressions;
- Document the changes in the code and/or the project's documentation;
- Pass the CI pipeline;
- Include a proper git commit message following the [Conventional Commit Specification](https://www.conventionalcommits.org/en/v1.0.0/#specification).

<br />

If all of these items are checked, the pull request is ready to be reviewed and you should change the status to "Ready for review" and request review from a maintainer.

Reviewers will approve the pull request once they are satisfied with the patch.

<br />

### Conventional Commit Specification

When commiting your changes, we require you to follow the Conventional Commit Specification, described below.

**The Conventional Commits** is a specification for the format and content of a commit message. The concept behind Conventional Commits is to provide a rich commit history that can be read and understood by both humans and automated tools. Conventional Commits have the following format:

<br />

```
<type>[(optional <scope>)]: <description>

[optional <body>]

[optional <footer(s)>]
```

#### Types
| Type | Description |
| --- | --- |
| `feat` | Introduces a new feature |
| `fix` | A bug fix for the end user |
| `docs` | A change to the website or Markdown documents |
| `build` | The commit alters the build process. E.g: creating a new build task, updating the release script, editing Makefile. |
| `test` | Adds missing tests, refactoring tests; no production code change. Usually changes the suite of automated tests for the product. |
| `perf` | Improves performance of algorithms or general execution time of the product, but does not fundamentally change an existing feature. |
| `style` | Updates or reformats the style of the source code, but does not otherwise change the product implementation. Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc) |
| `refactor` | A change to production code that leads to no behavior difference, e.g. splitting files, renaming internal variables, improving code style, etc. |
| `change` | Changes the implementation of an existing feature. |
| `chore` | Includes a technical or preventative maintenance task that is necessary for managing the product or the repository, but is not tied to any specific feature. E.g. updating dependencies. These are usually done for maintanence purposes. |
| `ci` | Changes related to Continuous Integration (usually `yml` and other configuration files). |
| `misc` | Anything else that doesn't change production code, yet is not ci, test or chore. |
| `revert` | Revert to a previous commit |
| `remove` | Removes a feature from the product. Typically features are deprecated first for a period of time before being removed. Removing a feature from the product may be considered a breaking change that will require a major version number increment. |
| `deprecate` | Deprecates existing functionality, but does not remove it from the product. |

<br />

##### Example 1:

```
feat(core): allow customization of interface
^───^────^  ^────────────────────────────────^
│   │       │
│   │       └───⫸ (DESC):   Summary in present tense. Use lower case not title case!
│   │
│   └───────────⫸ (SCOPE):  The package(s) that this change affects
│
└───────────────⫸ (TYPE):   See list above
```

<br />

##### Example 2:
```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope: animations|bazel|benchpress|common|compiler|compiler-cli|core|
  │                          elements|forms|http|language-service|localize|platform-browser|
  │                          platform-browser-dynamic|platform-server|router|service-worker|
  │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|ngcc|ve|
  │                          devtools....
  │
  └─⫸ Commit Type: build|ci|doc|docs|feat|fix|perf|refactor|test
                    website|chore|style|type|revert|deprecate
```

<br />

### References
If you are pushing a commit which addresses a submitted issue, reference your issue in the description of your commit. You may also optionally add the major issue to the end of your commit title.

References should be on their own line, following the word `Ref` or `Refs`

```
Title:          fix(core): fix error message displayed for users. [#22]
Description:    The description of your commit

                Ref: #22, #34, #37
```

<br />

### Vertical alignment
Align similar elements vertically, to make typo-generated bugs more obvious

```python
def __init__( self ):
    self.fetchurl           = FetchURL( )
    self.url_pattern        = re.compile( "^((http|https)?://)?(?P<host>[a-zA-Z0-9./?:@\\-_=#]+\\.[a-zA-Z]{2,6})[a-zA-Z0-9.&/?:@\\-_=#가-힇]*$" )
    self.templ_view         = None
```

<br />

### Spaces Instead Of Tabs
When writing your code, set your IDE to utilize **spaces**, with a configured tab size of `4 characters`.

<br />

### Indentation Style
This section is utilized for other languages not exclusive to Python. Typically, we try to stick to `Allman` as the indentation style. This style puts the brace associated with a control statement on the next line, indented to the same level as the control statement. Statements within the braces are indented to the next level.

<br />

This section can however be ignored for Python projects, as python maintains a very strict set of formatting parameters (one of the negatives of Python).

<br />

### Commenting
Use block comments to document a small section of code. These are useful when you have to write several lines of code to perform a single action, such as importing data from a file or updating a database entry. They’re important in helping others understand the purpose and functionality of a given code block.

PEP 8 provides the following rules for writing block comments:

- Indent block comments to the same level as the code that they describe.
- Start each line with a # followed by a single space.
- Separate paragraphs by a line containing a single #.

```python
for num in range( 0, 10 ):
    # Loop over `num` ten times and print out the value of `number`
    # followed by a newline character.
    print( i, "\n" )
```

<br />

### Casing
When writing your code, stick to one of three different styles:

| Style | Example |
| --- | --- |
| Snake Case | `my_variable` |
| Camel Case | `myVariable` |
| Camel Snake Case | `my_Variable` |

<br />

The case style may vary and we're not extremely picky on this, but ensure it is labeled properly and not generic.