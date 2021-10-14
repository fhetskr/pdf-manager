import argparse
from file_types import *

def main():
        parser = argparse.ArgumentParser(description 
                = 'Handle data in fillable PDFs.')
        # Note, the help action is handled automatically by what we given in the add_argument(s).
        # Add the remaining commands.
        parser.add_argument('--convert', '-c', action='append', nargs=3, 
                help="""Convert the file given to the specified filetype.
                Output the converted file with the given name.""", 
                metavar=('oldfile', 'newfile', 'newfiletype'))
        parser.add_argument('--append', '-a', action='append', nargs=3,
                help="Combine the two pdfs and output them into the new pdf.",
                metavar=('fileone', 'filetwo', 'newfile'))
        parser.add_argument('--split', '-s', action='append', nargs=3,
                help="""Split the specified PDF as the given page.
                Output the converted file with the given name."""
                metavar=('oldfile', 'page', 'newfile'))
        parser.add_argument('--email', '-e', action='append', nargs=2,
                help="Email the given file to the specified email address."
                metavar=('file', 'email'))
        parser.add_argument('--debug', '-d', action='store_true',
                help="Run the given command in debug mode.")

        # Parse the arguments.
        args = parser.parse_args()
        print("Below is a short debug for the CLI Parser (are the arguments right?\n")
        print(args)

        # TODO: Based on the arguments supplied, execute the proper code.


if __name__ == '__main__':
    main()
