FORTUNE_SOURCE := QUOTES.md
FORTUNE_TEXT   := quotes
FORTUNE_DAT    := quotes.dat

.PHONY: all clean

all: $(FORTUNE_DAT)

$(FORTUNE_TEXT): $(FORTUNE_SOURCE) scripts/generate_quotes.py
	python3 scripts/generate_quotes.py $(FORTUNE_SOURCE) $(FORTUNE_TEXT)

$(FORTUNE_DAT): $(FORTUNE_TEXT)
	strfile $(FORTUNE_TEXT) $(FORTUNE_DAT)

clean:
	rm -f $(FORTUNE_TEXT) $(FORTUNE_DAT)
