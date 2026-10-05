from gi.repository import Adw, Gtk


@Gtk.Template(resource_path="/dev/getapollo/Eleven/experimental.ui")
class ElevenExperimentalPage(Adw.Bin):
    __gtype_name__ = "ElevenExperimentalPage"

    service = None

    status_page = Gtk.Template.Child()
    proceed_button = Gtk.Template.Child()

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        # Translators: os_name is the name of the operating system being installed
        self.status_page.set_description(
            str(self.status_page.get_description()).format(
                os_name=self.service.config.os_name
            )
        )
