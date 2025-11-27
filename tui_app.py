from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Label, Static, Button
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.binding import Binding
from textual import on, work
from rich.text import Text
from pathlib import Path
import json
import os

from lib.system_interface import SystemInterface
from lib.systems.fallout import FalloutSystem

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

        # Determine status icon/color
        if errors > 0:
            self.status_icon = "❌"
            self.status_color = "red"
        elif warnings > 0:
            self.status_icon = "⚠️ "
            self.status_color = "yellow"
        else:
            self.status_icon = "✅"
            self.status_color = "green"

    def compose(self) -> ComposeResult:
        yield Label(f"{self.status_icon}  {self.char_name}")
        yield Label(f"    {self.char_class}", classes="subtitle")


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

        content = Text()
        content.append(f"{info['name']}\n", style="bold underline cyan")
        content.append(f"{info['class']} | {info['system']}\n\n", style="italic")

        content.append("Validation Status:\n", style="bold")

        if not errors and not warnings:
            content.append("✅  All checks passed!\n\n", style="green")

        if errors:
            content.append(f"❌  {len(errors)} Critical Issues:\n", style="bold red")
            for i, err in enumerate(errors, 1):
                content.append(f"  {i}. {err}\n", style="red")
            content.append("\n")

        if warnings:
            content.append(f"⚠️   {len(warnings)} Warnings/Suggestions:\n", style="bold yellow")
            for i, warn in enumerate(warnings, 1):
                content.append(f"  {i}. {warn}\n", style="yellow")
            content.append("\n")

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
        # Clear existing items (brute force removal)
        for child in sidebar.children:
            child.remove()

        list_view = ListView(id="char_list")

        export_dir = Path("fvtt_export")
        if not export_dir.exists():
            sidebar.mount(Label("Directory 'fvtt_export' not found!"))
            return

        files = list(export_dir.glob("*.json"))
        if not files:
            sidebar.mount(Label("No JSON files found."))
            return

        loaded_any = False
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
                        list_view.append(item)
                        loaded_any = True
                    except Exception as e:
                        # self.notify(f"Error loading {file_path.name}: {e}", severity="error")
                        pass

            except Exception as e:
                pass

        if loaded_any:
            sidebar.mount(list_view)
            list_view.focus()
        else:
            sidebar.mount(Label("No valid characters found."))

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        item = event.item
        if isinstance(item, CharacterListItem):
            details = self.query_one(CharacterDetails)
            details.show_character(item.character_obj, item.system_handler, item.validation_results)

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
            safe_name = "".join(c for c in char.name if c.isalnum() or c in (' ', '_')).rstrip().replace(' ', '_').lower()
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
