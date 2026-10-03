
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk, Gio
from gettext import gettext as _

@Gtk.Template(resource_path='/dev/getapollo/Eleven/disks.ui')
class ElevenDisksPage(Adw.Bin):
    __gtype_name__ = 'ElevenDisksPage'

    disks_list = Gtk.Template.Child()
    selected_drive = ""


    def select_drive(self, drive):
        self.selected_drive = drive
        print(self.selected_drive)
    
    def __init__(self, service, **kwargs):
        super().__init__(**kwargs)

        self.service = service

        model = self.service.disks.get_drives()

        # model = Gtk.StringList(strings=["Default Item 1", "Default Item 2", "Default Item 3"])
        select_button_main = Gtk.CheckButton()

        for list_item in model:
            select_button = Gtk.CheckButton(group=select_button_main, active=False)
            action_row =Adw.ActionRow(
                    title=list_item.model,
                    subtitle=f"{list_item.size} - {list_item.id}",
                )

            action_row.add_suffix(select_button)
            row_img = Gtk.Image(icon_name='drive-harddisk-solidstate-symbolic', pixel_size=24, css_classes=["icon-round-background"])

            action_row.add_prefix(row_img)

            action_row.connect(
                "activated",
                lambda _self: self.select_drive(list_item),
            )
            self.disks_list.append(
                action_row
            )

