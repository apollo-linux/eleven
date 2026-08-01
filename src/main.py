
import sys
import gi

from gettext import gettext as _

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import ElevenWindow

from .service import ElevenInstallerService

class ElevenApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='dev.getapollo.Eleven',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
                         resource_base_path='/dev/getapollo/Eleven')
        self.create_action('quit', lambda *_: self.quit(), ['<control>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)
        self.service = ElevenInstallerService()

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = ElevenWindow(application=self, service=self.service)
        
        if not self.service.config.exists:
            # Catch out systems where the configuration is not filled in to ensure that Eleven doesn't mistakenly run in this situation
            no_config_dialog = Adw.AlertDialog.new(
                heading = _(
                    "Installer not configured"
                ),
                body = _(
                    "The configuration file for the installer is not present. If you are an end user, please report this error to your OS vendor. [Error 11]"
                )
            )
            no_config_dialog.set_prefer_wide_layout(True)
            no_config_dialog.add_response("close", _("Close"))
            no_config_dialog.connect("response", self.close_no_config_warning)
            no_config_dialog.present(None)
        elif not self.service.config.valid:
            # Catch out systems where the configuration is missing settings to ensure that Eleven doesn't mistakenly run in this situation
            no_config_dialog = Adw.AlertDialog.new(
                heading = _(
                    "Installer missing settings"
                ),
                body = _(
                    "The installer configuration is missing settings. If you are an end user, please report this error to your OS vendor. [Error 12]"
                )
            )
            no_config_dialog.set_prefer_wide_layout(True)
            no_config_dialog.add_response("close", _("Close"))
            no_config_dialog.connect("response", self.close_broken_config_warning)
            no_config_dialog.present(None)
        else:
            win.present()

    def on_about_action(self, *args):
        """Callback for the app.about action."""
        about = Adw.AboutDialog(application_name='Eleven',
                                application_icon='dev.getapollo.Eleven',
                                developer_name='Izzy',
                                version='0.1.0',
                                # Translators: Replace "translator-credits" with your name/username, and optionally an email or URL.
                                translator_credits = _('translator-credits'),
                                developers=['Izzy'],
                                copyright='© 2026 Izzy')
        about.present(self.props.active_window)

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

    def close_no_config_warning(dialog, response, *args):
        quit(11)

    def close_broken_config_warning(dialog, response, *args):
        quit(12)

def main(version):
    """The application's entry point."""
    app = ElevenApplication()
    return app.run(sys.argv)
