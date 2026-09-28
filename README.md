# PLP Python Week 3 Assignment

## Description of Files
- **grade_reporter.py**: Analyzes a list of student scores, assigns letter grades (A, B, C, F), counts passes/fails, and calculates the average score.
- **bug_hunt.py**: Demonstrates debugging by fixing syntax, logic, and type errors in a Python loop program.

## Reflection
The off-by-one logic error (`count < 5`) in Part B was the hardest bug to find because Python executed the script without raising any warnings or error messages. I knew something was wrong because the expected mathematical output was 15, but the program printed 10 instead. This highlights the importance of testing code against known expected outcomes rather than relying solely on error messages.