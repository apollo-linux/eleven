from gi.repository import Adw, Gtk

from gettext import gettext as _

@Gtk.Template(resource_path='/dev/getapollo/Eleven/experimental.ui')
class ElevenExperimentalPage(Adw.Bin):
    __gtype_name__ = 'ElevenExperimentalPage'

    service = None

    status_page = Gtk.Template.Child()
    proceed_button = Gtk.Template.Child()

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        # Translators: os_name is the name of the operating system being installed
        self.status_page.set_description(
            _("This build of {os_name} is experimental software and may not be safe to use in production. You should only continue if you know what you're doing.").format(
                os_name=self.service.config.os_name
            )
        )