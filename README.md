# Fermat's Last Theorem Near Miss Finder

## Project Description
This program searches for "near misses" of Fermat's Last Theorem, which states that there are no positive integers x, y, and z such that x^n + y^n = z^n for n > 2. The program systematically searches for combinations where x^n + y^n is close to z^n for some integer z.

## Background
Pierre Fermat's Last Theorem sparked 400 years of mathematical exploration after he claimed to have a proof but never provided it. The theorem states that there are no natural numbers x, y, and z such that x^n + y^n = z^n, where n is a natural number greater than 2. Andrew Wiles finally published a proof in 1995.

This program doesn't attempt to disprove the theorem (which is now proven), but rather looks for cases where the equation is "almost" true - what we call "near misses."

## Features
- Interactive input for parameters n (power) and k (range limit)
- Systematic search through all combinations within the range
- Real-time display of new "best" near misses as they're found
- Progress tracking during execution
- Detailed final results with both absolute and relative miss values

## Requirements
- Python 3.6 or higher

## Installation
1. Clone this repository:
```
git clone https://github.com/yourusername/fermats_near_misses.git
cd fermats_near_misses
```

2. No additional dependencies are required as the program only uses Python standard libraries.

## Usage
### Running the Python Script
```
python fermats_near_miss.py
```

### Running the Executable
The executable file is located in the `dist` folder. You can run it in two ways:

1. Navigate to the `dist` folder and double-click on `fermats_near_miss.exe`

2. Or run it from the command line:
```
.\dist\fermats_near_miss.exe
```

## How It Works
1. The program prompts for two parameters:
   - n: The power to use (2 < n < 12)
   - k: The upper limit for x and y values (k > 10)

2. For each x,y combination (where 10 ≤ x,y ≤ k), the program:
   - Calculates x^n + y^n
   - Finds integers z and z+1 that "bracket" this value
   - Calculates the "miss" as the smallest of [(x^n + y^n) - z^n] or [(z+1)^n - (x^n + y^n)]
   - Calculates the relative miss by dividing by (x^n + y^n)
   - Tracks and displays the smallest relative miss found

3. The program displays the final best near miss when the search completes.

## Example Output
```
New best result found!
  x = 27, y = 84, z = 85
  27^3 + 84^3 < 85^3
  Absolute miss: 4
  Relative miss: 0.0000006092%
  Progress: 8100/8100 combinations checked (100.00%)

==================================================
SEARCH COMPLETE
==================================================
Best near miss found:
  x = 27, y = 84, z = 85
  27^3 + 84^3 ≈ 85^3
  27^3 + 84^3 = 636056
  85^3 = 614125
  Absolute miss: 4
  Relative miss: 0.0000006092%

Total time: 0.15 seconds
Total combinations checked: 8100
```

## Authors
- Mario Opoku Adusei

## Course Information
SU25-CPSC-60500-001 Assignment 1

## Date
June 14, 2025
