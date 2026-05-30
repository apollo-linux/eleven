from gi.repository import Adw
from gi.repository import Gtk

from .welcome import ElevenWelcomePage

from gettext import gettext as _

@Gtk.Template(resource_path='/dev/getapollo/Eleven/window.ui')
class ElevenWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ElevenWindow'

    welcome_view = Gtk.Template.Child()
    welcome_page = Gtk.Template.Child()

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        # Translators: os_name is the name of the operating system being installed
        self.welcome_title = _("Welcome to {os_name}").format(
            os_name=self.service.os_name
        )
        
        # Translators: os_name is the name of the operating system being installed
        self.welcome_message = _(
            "You can try {os_name} out in the live environment. When you're ready to install, you can use this program to install {os_name} to this device"
        ).format(
            os_name=self.service.os_name
        )

        self.welcome_page.status_page.set_title(self.welcome_title)
        self.welcome_page.status_page.set_description(self.welcome_message)
        
        # Translators: os_name is the name of the operating system being installed
        self.welcome_page.install_btn.set_label(
            _("Install {os_name}").format(
                os_name=self.service.os_name
            )
        )

        self.welcome_view.set_title(self.welcome_title)
