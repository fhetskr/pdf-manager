import file_types
import filetype
import merge_break as mb

def handle_debug(args):
        print(args)

def handle_convert(old_file, new_filetype, new_file):
    if(old_file == None):
        raise file_types.FileError("The file to convert must be input.")

    if(new_filetype == None):
        raise file_types.FileError("The filetype must be something.")

    if(new_file == None):
        raise file_types.FileError("The new file path must be input.")

    # If we can convert to what the user is requesting,
    if(new_filetype in file_types.file_dict):
        # Attempt to guess the FileType of the old file. 
        # If it has no extension AND the library can't do it, 
        # the user will provide an override.
        old_filetype = get_extension(old_file)

        if(old_filetype == None):
            raise file_types.FileError("Cannot deduce the type of the first argument.")

        if(not old_filetype in file_types.file_dict):
            raise file_types.FileError("The file type isn't operable.")
        
        old_file_inst = file_types.file_dict[old_filetype](old_file)
        old_file_inst.read()
        new_file_inst = old_file_inst.convert(new_filetype, new_file)
        new_file_inst.write()
    else:
        raise file_types.FileError("The filetype {new_filetype} isn't allowed!".format(new_filetype=new_filetype))

def handle_append(new_path, *files):
    if(new_path == None):
        raise Exception("The new path must be entered.")

    if(files == None):
        raise Exception("There must be files to split.")

    # ensure all files are pdfs
    if get_extension(new_path) == None or get_extension(new_path).lower() != 'pdf':
        raise Exception("Given path must be to a PDF file!")
    for file in files:
        if get_extension(file) == None or get_extension(file).lower() != 'pdf':
            raise Exception("Only PDF files may be merged!")
    mb.append(new_path, *files)


def handle_split(oldfile, *pages):
    if oldfile == None:
        raise Exception("There must be a file to split.")

    if pages == None:
        raise Exception("There must be pages to split the file by.")

    if get_extension(new_path != None) and get_extension(oldfile).lower() != 'pdf':
        raise Exception("Only PDF files may be split!")
    new_file_names = []
    c = 0
    for i in range(len(pages) + 1):
        c += 1
        new_file_names.append('{}_part_{}.pdf'.format(oldfile[:-4], c))
    mb.split(oldfile, [int(p) for p in pages], *new_file_names)


def handle_email(fileone, email):
    if fileone == None:
        raise Exception("There must be a file to e-mail")

    if email == None:
        raise Exception("There must be an e-mail to send a file to.")

    result = send(fileone, email)
    if(result == False):
        raise Exception("E-mailing failed.")

def get_extension(filepath):
    if(filepath == None):
        return None

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

