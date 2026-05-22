
from gi.repository import Adw
from gi.repository import Gtk

from .welcome import ElevenWelcomePage

@Gtk.Template(resource_path='/dev/getapollo/Eleven/window.ui')
class ElevenWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ElevenWindow'

    welcome_view = Gtk.Template.Child()
    welcome_page = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
