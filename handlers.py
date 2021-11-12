from file_types import *

def handle_debug(args):
        print(args)

def handle_convert(old_file, new_filetype, new_file):
    # If we can convert to what the user is requesting,
    if(new_filetype in file_dict):
        # Attempt to guess the FileType of the old file. 
        # If it has no extension AND the library can't do it, 
        # the user will provide an override.
        old_filetype = get_extension(old_file)

        if(old_filetype == None):
            raise file_types.FileError("Cannot deduce the type of the first argument.")

        if(not old_filetype in file_dict):
            raise file_types.FileError("The file type isn't operable.")
        
        old_file_inst = file_dict[old_filetype](old_file)
        new_file_inst = old_file_inst.convert(new_filetype, new_file)
        new_file_inst.write()
    else:
        raise FileError("The filetype {new_filetype} isn't allowed!".format(new_filetype=new_filetype))

def handle_append(fileone, filetwo, newfile):
    ext_one = get_extension(fileone)
    ext_two = get_extension(filetwo)
    if(ext_one == ext_two and ext_one == "pdf"):
        new_file_inst = append(ext_one, ext_two, newfile)
        new_file_inst.write()
    else:
        raise FileTypes.FileError("You can only merge PDF files!")

def handle_split(fileone, pageno, newfile):
    ext_one = get_extension(fileone)
    ext_two = get_extension(filetwo)
    if(ext_one == ext_two and ext_one == "pdf"):
        new_file_inst = append(ext_one, ext_two, newfile)
        new_file_inst.write()
    else:
        raise FileTypes.FileError("You can only split PDF files!")


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

    # Otherwise, we have no idea. Let the system know.
    return None

