# Chromasync

**A zero-config CLI tool that synchronizes color design tokens (Tailwind, CSS variables, Style Dictionary) bidirectionally with Figma variables via API.**

Design token drift happens silently when someone tweaks a hex code in Tailwind or CSS files without updating Figma, or vice versa, resulting in mismatched UIs and endless QA back-and-forth. Chromasync eliminates manual copy-pasting between codebase variables and Figma by automatically pushing and pulling color tokens via API in seconds.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

- **Token Normalization:** Parses input token files (Tailwind JSON, CSS custom properties, or Style Dictionary formats) and converts color representations (HEX, RGB, HSL) into standard sRGB color objects with normalized keys.
- **Figma Variables API Interaction:** Connects to the Figma REST API to fetch variable collections, local variable IDs, and current color values across specified files and modes.
- **Diff Computation:** Compares local code tokens against remote Figma variables by matching variable names and computed hex values to identify additions, modifications, and drift.
- **Bidirectional Syncing:** Emits HTTP update payloads to push local changes to Figma or generates formatted token files to update local codebases.

## Limitations

<!-- Honest and short: what it does NOT do, known gaps. -->

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
