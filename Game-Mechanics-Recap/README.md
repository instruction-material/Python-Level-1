# Game Mechanics Recap

Canonical source repository: `Python-Level-1`

This project consolidates the legacy `Game-Mechanics-Recap` and `Game-Mechanics-Recap-Template` folders into the common course wrapper layout.

## Structure

- `starter/` contains the starter/template snapshot.
- `solution/` contains the solution/reference snapshot.

## Loop-stop exercises

1. Move a turtle one pixel 100times. Update the counter after every move.
2. Start at (0, 0), face upward, and stop when y is above 50.
3. Start at (0, 0), face left, and stop when y is above 50 or x is below -100.

The second and third examples reset position and heading so earlier drawings
do not determine their starting state. The limits use strict comparisons:
y = 50 and x = -100 are still inside. Test both stopping conditions separately
and check that a rightward position such as x = 101 does not trigger the left limit.

The starter preserves the original exercise prompts. The reference implements
the three walks; its window stays responsive after the loops finish.
Run the bounded source regression without a graphics window:

```sh
python3 -m unittest discover -s Game-Mechanics-Recap -p 'test_*.py'
```
