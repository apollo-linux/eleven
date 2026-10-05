import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, GObject, Gio, Gtk


@Gtk.Template(resource_path="/dev/getapollo/Eleven/installation.ui")
class ElevenInstallationPage(Adw.Bin):
    __gtype_name__ = "ElevenInstallationPage"
    # __gsignals__ = {
    #     "proceed-disks-page": (GObject.SignalFlags.RUN_FIRST, None, (str,)),
    # }
    status_page: Adw.StatusPage = Gtk.Template.Child()

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        # FIXME: utilize `LOGO` variable on `/etc/os-release` as the base

        self.status_page.set_title(
            str(self.status_page.get_title()).format(
                os_name=self.service.config.os_name
            )
        )
