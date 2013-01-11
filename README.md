notesdotpy
==========

A simply command line note taking script written in Python. This is meant to facilitate "brain dumps" rather than organizing, rearranging, etc.  However, the resulting file is a plain text file so you can re-organize to your hearts content.

Simply writes strings entered on the command line to a file (as specified in notes.cfg). Notes are formatted as markdown style list items (or equivalently YAML sequence items) so it's easy to import them into your other plain text based workflow.

This script was derived from a Python script found here: http://rosettacode.org/wiki/Take_notes_on_the_command_line#Python

## Installation
- put `notes.py` on your `PATH` and make executable (`chmod +x notes.py`)
- Copy `notes.cfg` to `$HOME/.notes.cfg`
- Edit `.notes.cfg` to set the `notedir` and `notefile` parameters to specify the directory and filename of your notes files

### Optional:
- setup an alias in your `.bash_profile`, e.g. `alias note="notes.py"`

# Usage

- `notes.py` -- simply prints the contents of the file

- `notes.py "I wonder how fast an unladen swallow can fly?"` --  adds note to file

