notesdotpy
==========

A simple command line note taking script written in Python. This is meant to facilitate "brain dumps" rather than organizing, rearranging, etc.  However, the resulting file is a plain text file so you can re-organize to your hearts content.

Simply writes strings entered on the command line to a file (as specified in notes.cfg).

- New notes are appended at the end of the file
- Notes are formatted as markdown style list items (or equivalently YAML sequence items) so it's easy to import them into your other plain text based workflow.
- An [ISO 8601](http://www.w3.org/TR/NOTE-datetime) timestamp is appended to the end of each note (in square brackets).

This script was derived from a Python script found on the [Rosetta Code website](http://rosettacode.org/wiki/Take_notes_on_the_command_line#Python).

## Installation
- put `notes.py` on your `PATH` and make executable (`chmod +x notes.py`)
- Copy `notes.cfg` to `$HOME/.notes.cfg`
- Edit `.notes.cfg` to set the `notedir` and `notefile` parameters to specify the directory and filename of your notes files

### Optional:
- setup an alias in your `.bash_profile`, e.g. `alias note="notes.py"`

## Usage
- `notes.py` -- prints the contents of the notes file
- `notes.py "I wonder how fast an unladen swallow can fly?"` --  adds note to note file

