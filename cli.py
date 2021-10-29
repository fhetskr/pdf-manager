import argparse
import filetype
from file_types import *

def main():
        parser = argparse.ArgumentParser(description 
                = 'Handle data in fillable PDFs.')
        # Note, the help action is handled automatically by what we given in the add_argument(s).
        # Add the remaining commands.
        parser.add_argument('--convert', '-c', action='extend', nargs=3,
                help="""Convert the file given to the specified filetype.
                Output the converted file with the given name.""", 
                metavar=('oldfile', 'filetype', 'newfile'))
        parser.add_argument('--append', '-a', action='extend', nargs=3,
                help="Combine the two pdfs and output them into the new pdf.",
                metavar=('fileone', 'filetwo', 'newfile'))
        parser.add_argument('--split', '-s', action='extend', nargs=3,
                help="""Split the specified PDF as the given page.
                Output the converted file with the given name.""",
                metavar=('oldfile', 'page', 'newfile'))
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
            handle_debug()
            did_something = True
        if(args.convert != None):
            # Tell the user what's happening.
            print(("Converting document {oldfile} to type " +
                "{filetype} and writing the result to {newfile}")
                .format(oldfile=args.convert[0], filetype=args.convert[1], 
                    newfile=args.convert[2]))
            handle_convert(args.convert[0], args.convert[1], args.convert[2])
            did_something = True
        if(args.append != None):
            handle_append(args.append[0], args.append[1], args.append[2])
            did_something = True
        if(args.split != None):
            handle_split(args.split[0], args.split[1], args.split[2])
            did_something = True
        if(args.email != None):
            handle_email(args.split[0], args.split[1])
            did_something = True

        if(not did_something):
            parser.print_help()


def handle_debug():
        print(args)

def handle_convert(old_file, new_filetype, new_file):
    # If we can convert to what the user is requesting,
    if(new_filetype in file_dict):
        # Attempt to guess the FileType of the old file. 
        # If it has no extension AND the library can't do it, 
        # the user will provide an override.
        old_filetype = get_extension(old_file)

        if(old_filetype == None):
            raise Exception("Cannot deduce the type of the first argument.")

        if(not old_filetype in file_dict):
            raise Exception("The file type isn't operable.")

        old_file_inst = file_dict[old_filetype](old_file)
        new_file_inst = old_file_inst.convert(new_filetype, new_file)
        new_file_inst.write()
    else:
        raise Exception("The filetype {new_filetype} isn't allowed!".format(new_filetype=new_filetype))

def handle_append(fileone, filetwo, newfile):
    ext_one = get_extension(fileone)
    ext_two = get_extension(filetwo)
    if(ext_one == ext_two and ext_one == "pdf"):
        new_file_inst = append(ext_one, ext_two, newfile)
        new_file_inst.write()
    else:
        raise Exception("You can only merge PDF files!")

def handle_split(fileone, pageno, newfile):
    ext_one = get_extension(fileone)
    ext_two = get_extension(filetwo)
    if(ext_one == ext_two and ext_one == "pdf"):
        new_file_inst = append(ext_one, ext_two, newfile)
        new_file_inst.write()
    else:
        raise Exception("You can only split PDF files!")


def handle_email(fileone, email):
    result = send(fileone, email)
    if(result == False):
        raise Exception("E-mailing failed.")

def get_extension(filepath):
    # Decompose the path into sections and get the last section.
    names = filepath.split("/")
    split = names[len(names) - 1].split(".")
    ext = "" 
    
    # Append all the .'s together. For example, x.py.bak will have the extension py.bak.
    ext = ".".join(split[1:len(split)])

    if(ext != ""):
        return ext

    # If the filetype wasn't specified as an extension, guess it.
    guessed_filetype = filetype.guess_extension(filepath)
    if(guessed_filetype != None):
        return guessed_filetype

    return None



if __name__ == '__main__':
    main()