from gi.repository import Adw
from gi.repository import Gtk

from .welcome import ElevenWelcomePage
from .disks import ElevenDisksPage
from .experimental import ElevenExperimentalPage

from gettext import gettext as _

@Gtk.Template(resource_path='/dev/getapollo/Eleven/window.ui')
class ElevenWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ElevenWindow'

    welcome_view = Gtk.Template.Child()
    disks_view = Gtk.Template.Child()
    stack = Gtk.Template.Child()

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        self.welcome_page = ElevenWelcomePage(self.service)
        self.disks_page = ElevenDisksPage(self.service)

        self.welcome_view.set_child(self.welcome_page)
        self.disks_view.set_child(self.disks_page)

        if service.config.experimental:
            self.experimental_view = Adw.NavigationPage()
            self.experimental_view.set_title(_("Experimental Software"))
            self.experimental_page = ElevenExperimentalPage(self.service)
            self.experimental_view.set_child(self.experimental_page)

            self.experimental_page.proceed_button.connect("clicked", self.acknowledge_experimental_warning)

            self.stack.replace(
                [
                    self.experimental_view,
                ]
            )

            self.stack.pop_to_page(self.experimental_view)

        self.welcome_page.try_btn.connect("clicked", self.try_os)
        self.welcome_page.install_btn.connect("clicked", self.show_disks_view)
    
    def try_os(self, _button):
        self.close()

    def acknowledge_experimental_warning(self, _button):
        self.stack.push(self.welcome_view)

    def show_disks_view(self, _button):
        self.stack.push(self.disks_view)