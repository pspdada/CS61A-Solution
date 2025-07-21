<div align="center">

# CS61A-Solution

CS 61A: Structure and Interpretation of Computer Programs
</div>

This repo collects my solutions to the labs, homework, and projects of the [UC Berkeley CS61A, Summer 2024](https://cs61a.org/) course.

## Relevant resources

### CS61a

- [CS 61A: Structure and Interpretation of Computer Programs](https://cs61a.org/)

### Introduction Pages

- [Composing Programs](https://www.composingprograms.com/)
  - [中文翻译](https://composingprograms.netlify.app/)

## Using `Ok`

Test the homework assignments, labs, and projects with `ok`.

```bash
cd /path/to/dir
python3 ok --local -q [functionName] -v
```

- `--local`: disable network activity to avoid authentication for users without enrolled.
- `-q`: run tests for a specific question
- `-v`: show all tests up to failing line (if any)

To get an assignment score.

```bash
python3 ok --local --score
```

Visit [cs61a.org](https://cs61a.org/articles/using-ok) for more information.
