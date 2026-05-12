# Python Technical Test — Rush Assignments

## Overview

This repository contains solutions to all five rush assignments. Each assignment implements a `rush(x, y)` function that renders a rectangle of width `x` and height `y` using character-based graphics in the terminal.

## Structure

```
rush-1-1/rush.py    — Corners: o, Edges: - and |
rush-1-2/rush.py    — Corners: / and \, Edges: *
rush-1-3/rush.py    — Top corners: A, Bottom corners: C, Edges: B
rush-1-4/rush.py    — Left corners: A, Right corners: C, Edges: B
rush-1-5/rush.py    — Diagonal corners: A and C, Edges: B
```

## Usage

Each `rush.py` exports a `rush(x, y)` function. To test manually:

```bash
cd rush-1-1
python3 -c "from rush import rush; rush(5, 3)"
```

## Error Handling

All assignments print `Invalid size` to stderr and return when `x <= 0` or `y <= 0`.
