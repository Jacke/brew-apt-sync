# Universal Packages (UniPack)

## Stack

- Python (TUI)
- Scripts
- YAML for package sync

## Flow

```bash

┌───────────────────┐    ┌─────────────────────┐
│                   │    │                     │
│    Brew bundle    │    │dpkg --get-selections│
│                   │    │                     │
└───┬───────────┬───┘    └───┬───────────┬─────┘
    ├───────────┤            ├───────────┤
    │ Brewfile  │◄───┐ ┌────►│selections │
    └▲──────────┘    │ │     └───────────┘
     │               │ │            ▲
     │               │ │            │
     │             ┌─┴─┴──┐         │
     │             │ YAML │         │
     │             └──────┘         │
     │                              │
     │                              │
     │                              │
     └──────────────────────────────┘
```

## Libs

[GitHub - Textualize/textual: Textual is a TUI (Text User Interface) framework for Python inspired by modern web development.](https://github.com/Textualize/textual)

[GitHub - Textualize/rich: Rich is a Python library for rich text and beautiful formatting in the terminal.](https://github.com/Textualize/rich)

[Example Programs - Urwid 2.1.2](http://urwid.org/examples/index.html)

[GitHub - pallets/click: Python composable command line interface toolkit](https://github.com/pallets/click)
