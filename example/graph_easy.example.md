---
title: Graph::Easy Example
author: igbanam@
date: 2022-09-09
extensions:
 - graph-easy
---

# Graph::Easy

Now you can add graphs to your text presentations.

This extension supports graphs in Dot notation, and text notation.

For rendering, it supports ASCII (as default) and Box Art.

---

# Dot Notation

More text

```graph_easy
digraph {
  terminal -> lookatme;
  markdown -> lookatme;
  images -> lookatme;
  awesome -> lookatme;
}
```
---

# Text Notation

```graph_easy-boxart
  [ box ] -- uses --> [ arrow ], [ diamond ]
```

