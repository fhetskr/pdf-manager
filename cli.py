import argparse
import filetype
import merge_break as mb
from file_types import *
import handlers

def main():
        parser = argparse.ArgumentParser(description 
                = 'Handle data in fillable PDFs.')
        # Note, the help action is handled automatically by what we given in the add_argument(s).
        # Add the remaining commands.
        parser.add_argument('--convert', '-c', action='extend', nargs=3,
                help="""Convert the file given to the specified filetype.
                Output the converted file with the given name.""", 
                metavar=('oldfile', 'filetype', 'newfile'))
        parser.add_argument('--append', '-a', action='extend', nargs='+',
                help="Combine pdfs and output them into one new pdf.",
                metavar=('newpath', 'files'))
        parser.add_argument('--split', '-s', action='extend', nargs='+',
                help="""Split the specified PDF as the given page.
                Output the converted file with the given name.""",
                metavar=('oldfile', 'pages'))
        parser.add_argument('--email', '-e', action='extend', nargs=2,
                help="Email the given file to the specified email address.",
                metavar=('file', 'email'))
        parser.add_argument('--debug', '-d', action='store_true',
                help="Run the given command in debug mode.")

        # Parse the arguments.
        args = parser.parse_args()


        # Based on the arguments supplied, execute the proper code.
        # If we end up doing nothing, we're going to display the help page.
        did_something = False

        if(args.debug):
            # Print out helpful debugging information.
            print("Below is a short debug" +
                "(are the arguments right?)")
            handlers.handle_debug(args)
            handle_debug(args)
            did_something = True
        if(args.convert != None):
            # Tell the user what's happening.
            print(("Converting document {oldfile} to type " +
                "{filetype} and writing the result to {newfile}")
                .format(oldfile=args.convert[0], filetype=args.convert[1], 
                    newfile=args.convert[2]))
            handlers.handle_convert(args.convert[0], args.convert[1], args.convert[2])
            did_something = True
        if(args.append != None):
            handlers.handle_append(args.append[0], *(args.append[1:]))
            did_something = True
        if(args.split != None):
            handlers.handle_split(args.split[0], *(args.split[1:]))
            did_something = True
        if(args.email != None):
            handlers.handle_email(args.split[0], args.split[1])
            did_something = True

        if(not did_something):
            parser.print_help()

if __name__ == '__main__':
    main()
