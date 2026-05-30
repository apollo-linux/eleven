from gi.repository import Adw, Gtk

from gettext import gettext as _

@Gtk.Template(resource_path='/dev/getapollo/Eleven/welcome.ui')
class ElevenWelcomePage(Adw.Bin):
    __gtype_name__ = 'ElevenWelcomePage'

    status_page = Gtk.Template.Child()

    install_btn = Gtk.Template.Child()
    try_btn = Gtk.Template.Child()

    service = None

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        # Translators: os_name is the name of the operating system being installed
        self.status_page.set_title(
            _("Welcome to {os_name}").format(
                os_name=self.service.config.os_name
            )
        )

        # Translators: os_name is the name of the operating system being installed
        self.status_page.set_description(
            _("You can try {os_name} out in the live environment. When you're ready to install, you can use this program to install {os_name} to this device").format(
                os_name=self.service.config.os_name
            )
        )
        
        # Translators: os_name is the name of the operating system being installed
        self.install_btn.set_label(
            _("Install {os_name}").format(
                os_name=self.service.config.os_name
            )
        )