from gi.repository import Adw, Gtk

@Gtk.Template(resource_path='/dev/getapollo/Eleven/welcome.ui')
class ElevenWelcomePage(Adw.Bin):
    __gtype_name__ = 'ElevenWelcomePage'

    status_page = Gtk.Template.Child()
    install_btn = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)