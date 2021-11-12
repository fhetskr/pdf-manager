import gi
# Require version 3.0 of GTK.
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

# Load the GTK Window.
def load_window():
    builder = Gtk.Builder()
    builder.add_from_file("gui-file.glade")
    window = builder.get_object("topwindow")
    window.show_all()
    print(builder.get_objects())
    # Start the main GUI loop.
    Gtk.main()

if __name__ == '__main__':
    load_window()
    time.sleep(60)
