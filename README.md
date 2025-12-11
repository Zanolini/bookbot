# BookBot 📚

BookBot is a text analysis tool that reads books and generates statistics about their content. This is my first [Boot.dev](https://www.boot.dev) project!

## Features

- **Word Count** - Counts the total number of words in a book
- **Character Frequency** - Analyzes and counts every alphabetic character
- **Sorted Output** - Displays character counts sorted from most to least common

## Usage

```bash
python main.py <path-to-book>
```

### Example

```bash
python main.py books/frankenstein.txt
```

### Sample Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
Analyzing book found at books/frankenstein.txt...
----------- Character Count ----------
Analyzing book found at books/frankenstein.txt...
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
...
```

## Project Structure

```
bookbot/
├── main.py          # Entry point - handles CLI arguments
├── stats.py         # Text analysis functions
├── books/           # Directory containing book files
│   ├── frankenstein.txt
│   └── mobydick.txt
└── README.md
```

## How It Works

1. Pass a path to a `.txt` book file as a command-line argument
2. BookBot reads the file with UTF-8 encoding
3. It counts all words by splitting on whitespace
4. It counts all alphabetic characters (case-insensitive)
5. Results are displayed sorted by frequency