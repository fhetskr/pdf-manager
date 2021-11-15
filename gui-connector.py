import handlers
import file_types
import gi

# Require version 3.0 of GTK.
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

builder = None

# Load the GTK Window.
def load_window():
    # Taken from the Python-GTK3-Tutorial: 
    # https://python-gtk-3-tutorial.readthedocs.io/en/latest/builder.html
    global builder

    builder = Gtk.Builder()
    builder.add_from_file("gui-file.glade")

    window = builder.get_object("topwindow")
    window.set_title("PDF Manager")

    # Add all relevant handlers.
    window.connect("destroy", Gtk.main_quit)
    builder.get_object("convert-button").connect("clicked", handle_convert_button)
    builder.get_object("append-button").connect("clicked", handle_append_button)
    builder.get_object("split-button").connect("clicked", handle_split_button)
    builder.get_object("email-button").connect("clicked", handle_email_button)
    
    window.show_all()

    # Show the window and start the main GUI loop.
    window.show_all()
    Gtk.main()

def handle_convert_button(button):
    old_file = builder.get_object("convert-old-file-chooser").get_filename()
    new_type = builder.get_object("convert-filetype-combobox").get_active_text()
    new_path = builder.get_object("convert-path-entry").get_text()
    handlers.handle_convert(old_file, new_type, new_path)

def handle_append_button(button):
    file_one = builder.get_object("file-one-append").get_filename()
    file_two = builder.get_object("file-two-append").get_filename()
    new_path = builder.get_object("new-append-name").get_text()
    handlers.handle_append(new_path, file_one, file_two)

def handle_split_button(button):
    file_to_split = builder.get_object("split-file-chooser").get_filename()
    raw_page_numbers = builder.get_object("split-page-number-entry").get_text()
    page_numbers = None
    if(raw_page_numbers != None):
        page_numbers = raw_page_numbers.split(',')
    handlers.handle_split(file_to_split, *page_numbers)

def handle_email_button(button):
    file_to_email = builder.get_object("email-file-chooser").get_filename()
    email = builder.get_object("email-entry")
    handlers.handle_email(file_to_email, email)

if __name__ == '__main__':
    load_window()
