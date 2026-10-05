import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, GObject, Gio, Gtk


@Gtk.Template(resource_path="/dev/getapollo/Eleven/disks.ui")
class ElevenDisksPage(Adw.Bin):
    __gtype_name__ = "ElevenDisksPage"
    __gsignals__ = {
        "proceed-disks-page": (GObject.SignalFlags.RUN_FIRST, None, (str,)),
    }

    disks_list: Gtk.ListBox = Gtk.Template.Child()
    tpm_unlock: Adw.SwitchRow = Gtk.Template.Child()
    disk_encryption: Adw.SwitchRow = Gtk.Template.Child()
    install_button: Gtk.Button = Gtk.Template.Child()
    alert_idk: Adw.AlertDialog = Gtk.Template.Child()

    selected_drive = None
    tpm_unlock_enable = False
    disk_encryption_enable = False

    def _on_dialog_click(self, object: Adw.AlertDialog, drive):
        print(object)

    def _select_drive(self, object: Gtk.CheckButton, drive):
        if object.get_active():
            self.selected_drive = drive
            self.install_button.set_sensitive(True)
            print(self.selected_drive)
            self.alert_idk.set_body(
                str(self.alert_idk.get_body()).format(
                    disk_name=self.selected_drive.model
                )
            )
        else:
            self.selected_drive = None
            self.install_button.set_sensitive(False)

    @Gtk.Template.Callback()
    def on_toggle_tpm_unlock(self, idk, idk2):
        if self.disk_encryption.get_active():
            self.tpm_unlock_enable = not self.tpm_unlock.get_active()

    @Gtk.Template.Callback()
    def on_toggle_disk_encryption(self, idk, idk2):
        self.disk_encryption_enable = self.disk_encryption.get_active()
        if not self.disk_encryption_enable:
            self.tpm_unlock.set_active(self.disk_encryption_enable)
        self.tpm_unlock.set_sensitive(self.disk_encryption_enable)

    def _handle_installation_confirmation(
        self, dialog: Adw.AlertDialog, task: Gio.Task
    ):
        response = dialog.choose_finish(task)
        if response == "continue":
            self.emit("proceed-disks-page", "")

    @Gtk.Template.Callback()
    def on_install_button_clicked(self, element: Gtk.Button):
        self.alert_idk.choose(
            self, callback=self._handle_installation_confirmation
        )

    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        self.alert_idk.set_heading(
            str(self.alert_idk.get_heading()).format(
                os_name=self.service.config.os_name
            )
        )

        drives_model = self.service.disks.get_drives()
        select_drive_check = Gtk.CheckButton()

        for list_item in drives_model:
            select_button = Gtk.CheckButton(
                group=select_drive_check, active=False
            )
            select_button.connect(
                "toggled",
                lambda _self: self._select_drive(_self, list_item),
            )
            action_row = Adw.ActionRow(
                title=list_item.model,
                subtitle=f"{list_item.size} - {list_item.id}",
            )

            action_row.add_suffix(select_button)
            row_img = Gtk.Image(
                icon_name="drive-harddisk-solidstate-symbolic",
                pixel_size=24,
                css_classes=["icon-round-background"],
            )

            action_row.add_prefix(row_img)

            action_row.connect(
                "activated",
                lambda _self: self._select_drive(_self, list_item),
            )

            self.disks_list.append(action_row)
