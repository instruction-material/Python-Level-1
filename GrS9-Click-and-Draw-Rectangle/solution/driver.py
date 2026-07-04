import argparse
import code
import importlib.util
import pathlib
import sys
import turtle
from types import ModuleType

#################
#   CONSTANTS   #
#################

ARGUMENT_DESCRIPTION = "Load Python turtle files"
FILES_ARGUMENT = "files"
FILES_METAVAR = "FILES"
FULLSCREEN_ATTRIBUTE = "-fullscreen"
FULLSCREEN_ENABLED = True
REPL_BANNER = ""
REPL_PROMPT = "[33m[00m "
SCREEN_SIZE_RATIO = 1.0
WINDOW_TITLE = "Python Turtle on Replit"


#################
#   FUNCTIONS   #
#################

def parse_args() -> argparse.Namespace:
	"""Parse driver file paths from the command line"""
	parser = argparse.ArgumentParser(description=ARGUMENT_DESCRIPTION)
	parser.add_argument(FILES_ARGUMENT, metavar=FILES_METAVAR, type=pathlib.Path, nargs="*")
	return parser.parse_args()


def configure_screen() -> turtle.Screen:
	"""Create and configure the Turtle screen"""
	screen = turtle.Screen()
	canvas = screen.getcanvas()
	tk_window = canvas.winfo_toplevel()
	tk_window.attributes(FULLSCREEN_ATTRIBUTE, FULLSCREEN_ENABLED)

	screen.title(WINDOW_TITLE)
	screen.setup(SCREEN_SIZE_RATIO, SCREEN_SIZE_RATIO)
	return screen


def load_modules(file_paths: list[pathlib.Path]) -> list[ModuleType]:
	"""Load each requested Python file as a module"""
	modules: list[ModuleType] = []

	# Import each provided file so its variables become available in the REPL
	for file_path in file_paths:
		spec = importlib.util.spec_from_file_location(file_path.stem, file_path)

		# Stop with a clear import error if Python cannot build a module spec
		if spec is None or spec.loader is None:
			raise ImportError(f"Unable to load {file_path}")

		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)
		modules.append(module)

	return modules


def build_repl_locals(modules: list[ModuleType]) -> dict[str, object]:
	"""Build the local namespace exposed to the interactive shell"""
	# Use an empty namespace when no lesson module is provided
	if not modules:
		return {}

	main_module = modules[0]
	return {attribute: getattr(main_module, attribute) for attribute in dir(main_module)}


def main() -> None:
	"""Start the Turtle screen and interactive Python shell"""
	args = parse_args()
	screen = configure_screen()

	print(WINDOW_TITLE)
	modules = load_modules(args.files)
	repl_locals = build_repl_locals(modules)

	sys.ps1 = REPL_PROMPT
	code.interact(local=repl_locals, banner=REPL_BANNER)

	screen.mainloop()


if __name__ == "__main__":
	main()
