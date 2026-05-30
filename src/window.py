from gi.repository import Adw
from gi.repository import Gtk

from .welcome import ElevenWelcomePage

from gettext import gettext as _

@Gtk.Template(resource_path='/dev/getapollo/Eleven/window.ui')
class ElevenWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ElevenWindow'

    welcome_view = Gtk.Template.Child()

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        self.welcome_page = ElevenWelcomePage(self.service)

        self.welcome_view.set_child(self.welcome_page)

        self.welcome_page.try_btn.connect("clicked", self.try_os)
    
    def try_os(self, _button):
        self.close()