import sys
import json
import webbrowser
from pathlib import Path
from typing import Optional

try:
    from textual.app import App, ComposeResult, ScreenStackError
    from textual.widgets import Header, Footer, ListView, ListItem, Label, Static, Button
    from textual.containers import Container, Horizontal, Vertical
    from textual.screen import ModalScreen
    from textual.css.query import NoMatches
    from textual import on
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
from lib.output_path import sheet_path, write_sheet

PROJECT_ROOT = Path(__file__).resolve().parent

# Register available systems
SYSTEMS: list[SystemInterface] = [
    FalloutSystem()
]

class CharacterListItem(ListItem):
    """A list item representing a character."""

    def __init__(self, character_data, system_handler, validation_results, character_obj):
        super().__init__()
        self.character_data = character_data
        self.system_handler = system_handler
        self.validation_results = validation_results
        self.character_obj = character_obj

        self.char_name = character_data['name']
        self.char_class = character_data['class']

        errors = len(validation_results.get('errors', []))
        warnings = len(validation_results.get('warnings', []))

        # Determine status icon/class (using ASCII for terminal compatibility)
        if errors > 0 or warnings > 0:
            self.status_icon = "[!]"
            self.status_class = "status-warning"
        else:
            self.status_icon = "[ok]"
            self.status_class = "status-ok"

    def compose(self) -> ComposeResult:
        yield Label(f"{self.status_icon}  {self.char_name}", classes=self.status_class, markup=False)
        yield Label(f"      {self.char_class}", classes="subtitle", markup=False)

class ErrorListItem(ListItem):
    """A list item representing a file that failed to load."""

    def __init__(self, filename, error_msg):
        super().__init__()
        self.filename = filename
        self.error_msg = str(error_msg)

    def compose(self) -> ComposeResult:
        yield Label(f"[X]  {self.filename}", classes="status-error", markup=False)
        yield Label(f"      Load Error", classes="subtitle")


class ReplaceSheetScreen(ModalScreen[bool]):
    """Ask before replacing a previously exported sheet."""

    BINDINGS = [("escape", "cancel", "Cancel")]

    CSS = """
    ReplaceSheetScreen { align: center middle; }
    #replace_dialog { width: 65; height: auto; padding: 1 2; background: $surface; border: solid $warning; }
    #replace_choices { height: 3; margin-top: 1; }
    #replace_choices Button { width: 1fr; }
    """

    def __init__(self, path: Path):
        super().__init__()
        self.path = path

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label(f"Replace existing sheet?\n{self.path}", markup=False),
            Horizontal(Button("Cancel", id="cancel"), Button("Replace", id="replace"), id="replace_choices"),
            id="replace_dialog",
        )

    @on(Button.Pressed)
    def choose(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "replace")

    def action_cancel(self) -> None:
        self.dismiss(False)


class CharacterDetails(Static):
    """Displays details and validation report for the selected character."""

    def __init__(self):
        super().__init__("Select a character to see details.")
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
        primary_color = str(theme.primary)

        content = Text()
        content.append(f"{info['name']}\n", style=f"bold underline {primary_color}")
        content.append(f"{info['class']} | {info['system']}\n\n", style="italic")
        content.append(f"Source: {character.character_file.name}\n", style="dim")
        stats = character.derived_stats
        content.append(f"Health: {stats['current_health']}/{stats['max_health']}  "
                       f"Defense: {stats['defense']}  Initiative: {stats['initiative']}\n\n")

        content.append("Validation Status:\n", style="bold")

        if not errors and not warnings:
            content.append("[ok] All checks passed!\n\n", style=success_color)

        if errors:
            content.append(f"[!] {len(errors)} Health Warnings (check before printing):\n", style=f"bold {warning_color}")
            for i, err in enumerate(errors, 1):
                content.append(f"  {i}. {err}\n", style=warning_color)
            content.append("\n")

        if warnings:
            content.append(f"[i] {len(warnings)} Completeness Notes:\n", style=f"bold {warning_color}")
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
        content.append("\nCheck the export type and system, then export the actor again if needed.", style="italic")
        self.update(content)

    def clear(self):
        self.current_character = None
        self.current_handler = None
        self.update("Select a character to see details.")


class CharacterManagerApp(App):
    """A TUI to manage RPG characters."""

    TITLE = "RPG Sheets"

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
        height: 1fr;
        overflow-y: auto;
        border: solid $secondary;
        padding: 1;
    }

    #actions {
        height: 6;
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
    #output_status {
        height: auto;
        min-height: 2;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("m", "generate_markdown", "Markdown"),
        ("h", "generate_html", "HTML"),
        ("a", "generate_html_appendix", "HTML+Appendix"),
        ("r", "refresh_list", "Refresh"),
        ("o", "open_sheet", "Open sheet"),
    ]

    def __init__(self):
        super().__init__()
        self.last_output: Optional[Path] = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Vertical(id="sidebar"),
            Vertical(
                CharacterDetails(),
                Static("Exports are saved in character_sheets/", id="output_status", markup=False),
                Container(
                    Button("Markdown (M)", id="btn_md", variant="primary"),
                    Button("HTML (H)", id="btn_html", variant="primary"),
                    Button("HTML + Appx (A)", id="btn_html_appx", variant="primary"),
                    Button("Open last sheet (O)", id="btn_open", disabled=True),
                    id="actions"
                ),
                id="main_content"
            )
        )
        yield Footer()

    async def on_mount(self) -> None:
        await self.refresh_character_list()

    async def refresh_character_list(self):
        sidebar = self.query_one("#sidebar", Vertical)
        selected = self.get_current_selection()
        selected_path = (selected.character_obj.character_file if isinstance(selected, CharacterListItem)
                         else selected.filename if isinstance(selected, ErrorListItem) else None)
        # Clear existing items
        await sidebar.remove_children()

        export_dir = PROJECT_ROOT / "fvtt_export"
        if not export_dir.exists():
            sidebar.mount(Label(f"Import: copy a Foundry actor JSON to {export_dir}, then press R."))
            return

        files = sorted(export_dir.glob("*.json"))
        if not files:
            sidebar.mount(Label(f"No characters yet. Copy a Foundry actor JSON to {export_dir}, then press R."))
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
                        char = handler.load_character(file_path, data=data)
                        validation = handler.validate(char)
                        info = handler.get_character_info(char)

                        item = CharacterListItem(info, handler, validation, char)
                        items_to_add.append(item)
                        loaded_any = True
                    except Exception as e:
                        # Character matched system but failed to load (e.g. missing keys)
                        items_to_add.append(ErrorListItem(file_path.name, e))
                        loaded_any = True
                else:
                    # No system matched - consider it an unknown/invalid file
                    if not isinstance(data, dict):
                        reason = "Expected a Foundry actor JSON object"
                    elif data.get('type') not in ('character', 'robot'):
                        reason = f"Unsupported actor type: {data.get('type', 'missing')}"
                    elif not isinstance(data.get('system'), dict):
                        reason = "Missing or invalid system object"
                    else:
                        stats = data.get('_stats')
                        system_id = stats.get('systemId') if isinstance(stats, dict) else None
                        reason = f"Unsupported or missing Foundry systemId: {system_id} (expected fallout)"
                    items_to_add.append(ErrorListItem(file_path.name, reason))
                    loaded_any = True

            except Exception as e:
                # File read error or JSON parse error
                items_to_add.append(ErrorListItem(file_path.name, f"Cannot read export: {e}"))
                loaded_any = True

        if loaded_any:
            list_view = ListView(*items_to_add, id="char_list")
            await sidebar.mount(list_view)
            for index, entry in enumerate(items_to_add):
                path = (entry.character_obj.character_file if isinstance(entry, CharacterListItem)
                        else entry.filename)
                if path == selected_path:
                    list_view.index = index
                    break
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
        elif event.button.id == "btn_open":
            self.action_open_sheet()

    def get_current_selection(self):
        try:
            list_view = self.query_one("#char_list", ListView)
            if list_view.index is not None:
                item = list_view.children[list_view.index]
                return item
        except (NoMatches, IndexError):
            pass
        return None

    def _save_sheet(self, output_file: Path, content: str, replace: bool = False,
                    has_health_warnings: bool = False) -> None:
        """Save once and keep the resulting location visible."""
        try:
            write_sheet(output_file, content, replace=replace)
            self.last_output = output_file
            hint = "  (O to open)" if output_file.suffix == '.html' else ""
            self.query_one("#output_status", Static).update(f"Saved: {output_file}{hint}")
            self.query_one("#btn_open", Button).disabled = output_file.suffix != '.html'
            self.notify(f"Saved: {output_file.name}", severity="information")
            if has_health_warnings:
                self.notify("Health warnings: check the sheet before printing.", severity="warning")
        except OSError as error:
            self.notify(f"Could not save sheet: {error}", severity="error")

    def generate_sheet(self, format_type, **options):
        try:
            if isinstance(self.screen, ReplaceSheetScreen):
                return
        except ScreenStackError:
            pass  # Unit tests can call this action before the app starts.
        item = self.get_current_selection()
        if not item:
            self.notify("No character selected!", severity="warning")
            return
        if isinstance(item, ErrorListItem):
            self.notify(f"Cannot generate sheet: {item.filename} failed to load", severity="error")
            return
        if not isinstance(item, CharacterListItem):
            self.notify("Select a character before generating a sheet.", severity="warning")
            return
        try:
            handler = item.system_handler
            char = item.character_obj

            content = handler.generate_sheet(char, format_type, options)

            output_dir = PROJECT_ROOT / "character_sheets"
            output_dir.mkdir(exist_ok=True)
            output_file = sheet_path(char, output_dir, format_type, options.get('appendix', False))
            health_warnings = bool(item.validation_results.get('errors'))
            if output_file.exists():
                self.push_screen(
                    ReplaceSheetScreen(output_file),
                    lambda replace: self._save_sheet(output_file, content, replace=True,
                                                     has_health_warnings=health_warnings) if replace else None,
                )
            else:
                self._save_sheet(output_file, content, has_health_warnings=health_warnings)

        except Exception as e:
            self.notify(f"Error: {e}", severity="error")

    def action_generate_markdown(self):
        self.generate_sheet("markdown")

    def action_generate_html(self):
        self.generate_sheet("html")

    def action_generate_html_appendix(self):
        self.generate_sheet("html", appendix=True)

    def action_open_sheet(self):
        if isinstance(self.screen, ReplaceSheetScreen):
            return
        if self.last_output is None or not self.last_output.is_file() or self.last_output.suffix != '.html':
            self.notify("No generated HTML sheet to open.", severity="warning")
            return
        if not webbrowser.open(self.last_output.as_uri()):
            self.notify(f"Could not open browser. File: {self.last_output}", severity="warning")

    async def action_refresh_list(self):
        if isinstance(self.screen, ReplaceSheetScreen):
            return
        self.query_one(CharacterDetails).clear()
        await self.refresh_character_list()

if __name__ == "__main__":
    app = CharacterManagerApp()
    app.run()
