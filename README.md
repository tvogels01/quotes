# Quotes for `fortune`

## Installation

```shell
brew install fortune
```

### Use

```shell
fortune quotes
```

And if you have `cowsay` installed:
```shell
fortune quotes | cowsay
```

```text
 _________________________________________
/ Excellence does not require perfection. \
|                                         |
\ -- Henry James                          /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Adding a quote

`QUOTES.md` is the source of truth. `quotes` and `quotes.dat` are generated — never edit them by hand.

1. Add a blockquote to the appropriate themed section of `QUOTES.md`. (Attribution is the last line, prefixed with a dash):

   ```markdown
   > Do the best you can until you know better. Then when you know better, do better.
   >
   > — Maya Angelou
   ```

2. Regenerate the database (runs `scripts/generate_quotes.py`, then `strfile`):

   ```shell
   make
   ```

3. Commit all three files: `QUOTES.md`, `quotes`, `quotes.dat`.

Use `make clean` to remove the generated files.
