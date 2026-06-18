from gi.repository import Adw, Gtk

from gettext import gettext as _

@Gtk.Template(resource_path='/dev/getapollo/Eleven/disks.ui')
class ElevenDisksPage(Adw.Bin):
    __gtype_name__ = 'ElevenDisksPage'

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service