import sys
import json
import os
from pathlib import Path

try:
    from textual.app import App, ComposeResult
    from textual.widgets import Header, Footer, ListView, ListItem, Label, Static, Button
    from textual.containers import Container, Horizontal, Vertical, VerticalScroll
    from textual.screen import Screen
    from textual.binding import Binding
    from textual import on, work
    from rich.text import Text
except ImportError:
    print("Error: Required package 'textual' is not installed.")
    print()
    print("Please install dependencies with:")
    print("  pip install -r requirements.txt")
    print()
    print("Or install textual directly:")
    print("  pip install textual")
    sys.exit(1)

from lib.system_interface import SystemInterface
from lib.systems.fallout import FalloutSystem
from lib.utils import sanitize_filename

# Register available systems
SYSTEMS: list[SystemInterface] = [
    FalloutSystem()
]

class CharacterListItem(ListItem):
    """A list item representing a character."""

    def __init__(self, character_data, system_handler, validation_results):
        super().__init__()
        self.character_data = character_data
        self.system_handler = system_handler
        self.validation_results = validation_results

        self.char_name = character_data['name']
        self.char_class = character_data['class']

        errors = len(validation_results.get('errors', []))
        warnings = len(validation_results.get('warnings', []))

        # Determine status icon/class (using ASCII for terminal compatibility)
        if errors > 0:
            self.status_icon = "[X]"
            self.status_class = "status-error"
        elif warnings > 0:
            self.status_icon = "[!]"
            self.status_class = "status-warning"
        else:
            self.status_icon = "[ok]"
            self.status_class = "status-ok"

    def compose(self) -> ComposeResult:
        yield Label(f"{self.status_icon}  {self.char_name}", classes=self.status_class)
        yield Label(f"      {self.char_class}", classes="subtitle")

class ErrorListItem(ListItem):
    """A list item representing a file that failed to load."""

    def __init__(self, filename, error_msg):
        super().__init__()
        self.filename = filename
        self.error_msg = str(error_msg)

    def compose(self) -> ComposeResult:
        yield Label(f"[X]  {self.filename}", classes="status-error")
        yield Label(f"      Load Error", classes="subtitle")


class CharacterDetails(Static):
    """Displays details and validation report for the selected character."""

    def __init__(self):
        super().__init__()
        self.current_character = None
        self.current_handler = None

    def show_character(self, character, handler, validation):
        self.current_character = character
        self.current_handler = handler

        info = handler.get_character_info(character)
        errors = validation.get('errors', [])
        warnings = validation.get('warnings', [])

        # Get theme colors from app
        theme = self.app.current_theme
        success_color = str(theme.success)
        warning_color = str(theme.warning)
        error_color = str(theme.error)
        primary_color = str(theme.primary)

        content = Text()
        content.append(f"{info['name']}\n", style=f"bold underline {primary_color}")
        content.append(f"{info['class']} | {info['system']}\n\n", style="italic")

        content.append("Validation Status:\n", style="bold")

        if not errors and not warnings:
            content.append("[ok] All checks passed!\n\n", style=success_color)

        if errors:
            content.append(f"[X] {len(errors)} Critical Issues:\n", style=f"bold {error_color}")
            for i, err in enumerate(errors, 1):
                content.append(f"  {i}. {err}\n", style=error_color)
            content.append("\n")

        if warnings:
            content.append(f"[!] {len(warnings)} Warnings/Suggestions:\n", style=f"bold {warning_color}")
            for i, warn in enumerate(warnings, 1):
                content.append(f"  {i}. {warn}\n", style=warning_color)
            content.append("\n")

        self.update(content)

    def show_error(self, filename, error):
        # Get theme colors from app
        theme = self.app.current_theme
        error_color = str(theme.error)

        content = Text()
        content.append(f"File: {filename}\n", style=f"bold underline {error_color}")
        content.append("Critical Load Error\n\n", style=f"bold {error_color}")
        content.append(f"Could not load character data:\n{error}\n", style=error_color)
        content.append("\nThis file may be corrupted, or it might not be a valid Character export.", style="italic")
        self.update(content)

    def clear(self):
        self.current_character = None
        self.current_handler = None
        self.update("Select a character to see details.")


class CharacterManagerApp(App):
    """A TUI to manage RPG characters."""

    CSS = """
    Screen {
        layout: horizontal;
    }

    #sidebar {
        width: 30%;
        height: 100%;
        dock: left;
        border-right: solid $primary;
        background: $surface;
    }

    #main_content {
        width: 70%;
        height: 100%;
        padding: 1 2;
    }

    CharacterListItem {
        height: auto;
        padding: 1;
        border-bottom: solid $secondary;
    }

    CharacterListItem:hover {
        background: $boost;
    }

    .subtitle {
        color: $text-muted;
        text-style: italic;
    }

    .status-ok {
        color: $success;
    }

    .status-warning {
        color: $warning;
    }

    .status-error {
        color: $error;
    }

    CharacterDetails {
        height: 80%;
        overflow-y: auto;
        border: solid $secondary;
        padding: 1;
    }

    #actions {
        height: 20%;
        border-top: solid $primary;
        align: center middle;
        layout: grid;
        grid-size: 3;
        grid-gutter: 1;
        padding: 1;
    }

    Button {
        width: 100%;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("m", "generate_markdown", "Markdown"),
        ("h", "generate_html", "HTML"),
        ("a", "generate_html_appendix", "HTML+Appendix"),
        ("r", "refresh_list", "Refresh"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Vertical(id="sidebar"),
            Vertical(
                CharacterDetails(),
                Container(
                    Button("Markdown (M)", id="btn_md", variant="primary"),
                    Button("HTML (H)", id="btn_html", variant="primary"),
                    Button("HTML + Appx (A)", id="btn_html_appx", variant="primary"),
                    id="actions"
                ),
                id="main_content"
            )
        )
        yield Footer()

    def on_mount(self) -> None:
        self.refresh_character_list()

    def refresh_character_list(self):
        sidebar = self.query_one("#sidebar", Vertical)
        # Clear existing items
        sidebar.remove_children()

        export_dir = Path("fvtt_export")
        if not export_dir.exists():
            sidebar.mount(Label("Directory 'fvtt_export' not found!"))
            return

        files = list(export_dir.glob("*.json"))
        if not files:
            sidebar.mount(Label("No JSON files found."))
            return

        loaded_any = False
        items_to_add = []
        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Detect system
                handler = None
                for system in SYSTEMS:
                    if system.can_handle(file_path, data):
                        handler = system
                        break

                if handler:
                    try:
                        char = handler.load_character(file_path)
                        validation = handler.validate(char)
                        info = handler.get_character_info(char)

                        item = CharacterListItem(info, handler, validation)
                        # Attach the full objects to the item for retrieval
                        item.character_obj = char
                        items_to_add.append(item)
                        loaded_any = True
                    except Exception as e:
                        # Character matched system but failed to load (e.g. missing keys)
                        items_to_add.append(ErrorListItem(file_path.name, e))
                        loaded_any = True
                else:
                    # No system matched - consider it an unknown/invalid file
                    items_to_add.append(ErrorListItem(file_path.name, "Unknown format or unsupported system"))
                    loaded_any = True

            except Exception as e:
                # File read error or JSON parse error
                items_to_add.append(ErrorListItem(file_path.name, f"JSON Error: {e}"))
                loaded_any = True

        if loaded_any:
            list_view = ListView(*items_to_add, id="char_list")
            sidebar.mount(list_view)
            list_view.focus()
        else:
            sidebar.mount(Label("No JSON files found."))

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Update details when a character is highlighted (cursor moved)."""
        if event.item is None:
            return
        item = event.item
        details = self.query_one(CharacterDetails)

        if isinstance(item, CharacterListItem):
            details.show_character(item.character_obj, item.system_handler, item.validation_results)
        elif isinstance(item, ErrorListItem):
            details.show_error(item.filename, item.error_msg)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle Enter key on a character (same as highlight for now)."""
        if event.item is None:
            return
        item = event.item
        details = self.query_one(CharacterDetails)

        if isinstance(item, CharacterListItem):
            details.show_character(item.character_obj, item.system_handler, item.validation_results)
        elif isinstance(item, ErrorListItem):
            details.show_error(item.filename, item.error_msg)

    @on(Button.Pressed)
    def handle_buttons(self, event: Button.Pressed):
        if event.button.id == "btn_md":
            self.action_generate_markdown()
        elif event.button.id == "btn_html":
            self.action_generate_html()
        elif event.button.id == "btn_html_appx":
            self.action_generate_html_appendix()

    def get_current_selection(self):
        try:
            list_view = self.query_one("#char_list", ListView)
            if list_view.index is not None:
                item = list_view.children[list_view.index]
                return item
        except:
            pass
        return None

    def generate_sheet(self, format_type, **options):
        item = self.get_current_selection()
        if not item:
            self.notify("No character selected!", severity="warning")
            return

        try:
            handler = item.system_handler
            char = item.character_obj

            content = handler.generate_sheet(char, format_type, options)

            output_dir = Path("character_sheets")
            output_dir.mkdir(exist_ok=True)

            # Generate filename
            safe_name = sanitize_filename(char.name)
            ext = 'html' if format_type == 'html' else 'md'
            output_file = output_dir / f"{safe_name}.{ext}"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            self.notify(f"Saved: {output_file}", severity="information")

        except Exception as e:
            self.notify(f"Error: {e}", severity="error")

    def action_generate_markdown(self):
        self.generate_sheet("markdown")

    def action_generate_html(self):
        self.generate_sheet("html")

    def action_generate_html_appendix(self):
        self.generate_sheet("html", appendix=True)

    def action_refresh_list(self):
        self.refresh_character_list()
        self.query_one(CharacterDetails).clear()

if __name__ == "__main__":
    app = CharacterManagerApp()
    app.run()
