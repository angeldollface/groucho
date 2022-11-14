# GROUCHO :guitar: :snake:

![GitHub CI](https://github.com/angeldollface/groucho/actions/workflows/python.yml/badge.svg)

***Convert between numbers of different bases. :guitar: :snake:***

## ABOUT :books:

Roughly a year ago, I set myself the challenge of implementing a set of functions that could convert between numbers of different bases. I implemented this in Dart and Javascript.I then decided to re-write this implementation in Python 3. The Dart implementation can be found [here](https://github.com/angeldollface/harpo) and the Javascript implementation [here](https://github.com/angeldollface/zeppo). The bases this library handles are: base 10, base 2, and base 16.

## USAGE :hammer:

### REQUIREMENTS

You should have the following tools installed and available from the command line:

- [Git](https://git-scm.org)
- [Python 3.5+](https://www.python.org/downloads/)
- Pip for Python 3.5+ (Usually comes with Python.)

### INSTALLING *GROUCHO* ON YOUR SYSTEM

To use *Groucho* on your own system with your own projects, run the following command:

```bash
python -m pip install git+https://github.com/angeldollface/groucho
```

### API

- `reverse_array(array)`: Reverses the order of an array and returns the reversed array.
- `letter_index(letter)`: Gets the index of a letter in the alphabet. Returns zero if the letter isn't in the alphabet.
- `get_letter_from_index(index)`: Gets the letter from a supplied index. Returns an empty string if a letter cannot be found.
- `bin_to_dec(binaryNumber)`: Converts a base 2 number as a string to a base 10 number as an integer.
- `dec_to_bin(decimalNumber)`: Converts a base 10 number as an integer to a base 2 number as a string.
- `hex_to_dec(hexNumber)`: Converts a base 16 number as a string to a base 10 number as an integer.
- `is_bin(expr)`: Checks whether the supplied number string is a binary number and returns a boolean based on this.
- `is_int(expr`: A function to check whether a string is an integer. Returns a boolean.

### TEST THE EXAMPLE

To test the included example in the folder `example`, execute the following steps:

- 1.) Clone this repository to your machine:

```bash
git clone https://github.com/angeldollface/groucho
```

- 2.) Change directory into the repository's root:

```bash
cd groucho
```

- 3.) Change directory into the `example` folder:

```bash
cd example
```

- 4.) Install the example's dependencies:

```bash
python -m pip install -r requirements.txt
```

- 5.) Run the example:

```bash
python main.py
```

## CHANGELOG :black_nib:

### Version 1.0.0

- Initial release.
- Upload to GitHub.
- Getting re-acquainted with the Python eco system.

## NOTE :scroll:

- *Groucho :guitar: :snake:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.