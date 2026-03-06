# Random Password Generator (Python)

A command-line password generator built with Python that creates strong random passwords based on user-defined length.

## Project Overview

This project generates secure passwords using Python and validates user input in a loop so multiple passwords can be created in one run.

## Features

- Generates random passwords from letters, numbers, and symbols
- Uses Python's `secrets` module for cryptographically secure randomness
- Validates invalid and non-positive length input
- Supports repeated password generation with a simple `yes/no` flow

## Skills Used

- Python fundamentals: variables, functions, loops, and conditionals
- Exception handling with `try` / `except`
- Input validation and control flow with `continue` and `break`
- String construction using `"".join(...)` and comprehensions
- Secure random generation with the `secrets` standard library
- Basic CLI UX design through clear prompts and messages

## What I Learned

- Why `secrets` is better than `random` for password generation
- How to structure a `while` loop to separate parsing, validation, and output
- How to prevent runtime errors by handling invalid user input safely
- How to write cleaner, more maintainable code by organizing logic clearly

## Example Run

```text
Enter the desired password length: 12
Generated password: G@4m!p2Q#z1A
Do you want to generate another password? (yes/no): no
```

## How To Run

1. Make sure Python 3 is installed.
2. Run:

```bash
python random-password.py
```

## Future Improvements

- Let users choose which character groups to include (letters, numbers, symbols)
- Add a password strength indicator
- Save generated passwords to a file (optional)
- Add unit tests for password length and validation behavior
