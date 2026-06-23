# Turtle Project Reference

This folder is a reusable reference for Python Turtle projects that combine
movement, comments, score display, boundaries, and moving triangle enemies. It
is designed as a template students can copy from while organizing their own
projects.

## What This Covers

- Basic Turtle movement: `forward()`, `left()`, `right()`, `goto()`, `penup()`,
  and `pendown()`.
- Clean code sections: imports, functions, variables and attributes, one-time
  setup, and continuous game logic.
- A separate score turtle that writes in the corner and clears old text before
  writing updated score text.
- A square border drawn by a border turtle.
- Boundary checks that calculate the next x/y position before moving or
  stamping.
- Collision checks that use `global score` when updating the score inside a
  function.
- Moving triangle enemies that turn around when they hit a boundary.

## Files

- `starter/main.py` gives a structured starting point with TODO sections.
- `solution/main.py` gives a complete reference implementation.

## Sound Note

This template uses visual feedback only. CodeHS allows uploaded files in
programs, including common audio formats such as MP3, OGG, and WAV. The CodeHS
Python Turtle command reference does not list a portable built-in Turtle sound
command, so the reference code stays visual-only. For Turtle projects, use
visual feedback such as score changes, color changes, stamps, or written
messages. If a project needs reliable sound, test sound in the exact CodeHS
environment first or move that version into a game-focused environment such as
Pygame.

Official references:

- CodeHS file uploads: https://help.codehs.com/en/articles/2372009-uploading-a-file-to-your-program
- CodeHS Python Turtle commands: https://codehs.com/documentation/new/python-turtle

## Suggested Extension

After the starter version works, add more triangle enemies:

1. Create another triangle turtle.
2. Store it in the `enemies` list.
3. Give it its own `dx` and `dy` values.
4. Confirm that it bounces from all four border sides.
5. Confirm that the score changes only when the player and triangle collide.
