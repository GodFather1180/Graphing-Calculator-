# Graphing Calculator

A TI-83-style graphing calculator built in Python, with a custom GUI and a hand-rolled rendering layer instead of a charting library.

## Features

- **Math mode** — standard arithmetic (`+ - * / ^`), parentheses, and trig functions (`sin`, `cos`, `tan`)
- **Graph mode** — plots `f(X)` against a drawn coordinate grid
- On-screen expression builder with `del` (backspace) and `CLEAR`
- Calculator-style button layout: digits, operators, trig functions, and directional keys for graph panning

## Built with

- **Python 3**
- **PySimpleGUI** — window and button layout
- **turtle** — used as a drawing surface (embedded on a `PySimpleGUI` canvas) for the grid, plotted functions, and on-screen expression/result text

## Running

```bash
pip install PySimpleGUI
python3 main.py
```
