# lookatme.contrib.graph_easy

Introduce text graphs with the Dot notation

## Installation

If this project has been pushed up to pypi:

```bash
pip install lookatme.contrib.graph_easy
```

## Usage

Add the graph_easy into the extensions array in the slide YAML header:

```markdown
---
title: A title
author: Me
date: 2019-12-04
extensions:
  - graph_easy
---
```

With the extension installed and declared in the YAML header, use it in your
markdown by declaring normal code blocks with the graph-easy extension
language. Examples are below.

~~~markdown
```graph_easy
[ box ] - uses -> [ arrow ], [ diamond ]
```
~~~

This defaults to the ASCII rendering

```
+---------+  uses   +-------+
|   box   | ------> | arrow |
+---------+         +-------+
  |
  | uses
  v
+---------+
| diamond |
+---------+
```

An equivalent notation for the above is

~~~markdown
```graph_easy-ascii
[ box ] - uses -> [ arrow ], [ diamond ]
```
~~~

## Supported Render Formats

### ASCII

`graph_easy-ascii`

…as above

### Box Art

`graph_easy-boxart`

```
┌─────────┐  uses   ┌───────┐
│   box   │ ──────> │ arrow │
└─────────┘         └───────┘
  │
  │ uses
  ∨
┌─────────┐
│ diamond │
└─────────┘
```
