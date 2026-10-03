"""UI workflow checks for safe exports and discoverable results."""

import io
import json
import os
import shutil
import stat
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import cast
from unittest.mock import patch

from textual.widgets import Label

from lib.character_data import Character
from lib.fallout_sheet_generator import CharacterSheetGenerator
from lib.output_path import sheet_path, write_sheet
from rpg_sheets import CharacterManagerApp, CharacterListItem, ErrorListItem, ReplaceSheetScreen


class OutputPathTests(unittest.TestCase):
    def test_format_appendix_and_source_have_distinct_names(self):
        actor = {'name': 'Same Name', 'type': 'character', 'system': {}, 'items': []}
        first = Character(Path('fvtt_export/first.json'), data=actor)
        second = Character(Path('fvtt_export/second.json'), data=actor)
        output = Path('character_sheets')
        self.assertNotEqual(sheet_path(first, output, 'html'), sheet_path(second, output, 'html'))
        self.assertNotEqual(sheet_path(first, output, 'html'), sheet_path(first, output, 'html', True))
        self.assertNotEqual(sheet_path(first, output, 'html'), sheet_path(first, output, 'markdown'))
        self.assertEqual(sheet_path(first, output, 'html'), sheet_path(first, output, 'html'))

    def test_replace_does_not_follow_symlink_and_long_names_fit(self):
        actor = {'name': 'Ä' * 500, 'type': 'character', 'system': {}, 'items': []}
        character = Character(Path('fvtt_export/long.json'), data=actor)
        with tempfile.TemporaryDirectory() as temp:
            output = sheet_path(character, Path(temp), 'html')
            self.assertLessEqual(len(output.name.encode('utf-8')), 255)
            protected = Path(temp) / 'protected'
            protected.write_text('keep', encoding='utf-8')
            output.symlink_to(protected)
            with self.assertRaises(FileExistsError):
                write_sheet(output, 'new')
            write_sheet(output, 'new', replace=True)
            self.assertEqual(protected.read_text(encoding='utf-8'), 'keep')
            self.assertFalse(output.is_symlink())
            self.assertEqual(output.read_text(encoding='utf-8'), 'new')

    def test_same_basename_in_different_directories_has_distinct_names(self):
        actor = {'name': 'Same Name', 'type': 'character', 'system': {}, 'items': []}
        output = Path('character_sheets')
        with tempfile.TemporaryDirectory() as temp:
            first = Character(Path(temp) / 'campaign_a' / 'actor.json', data=actor)
            second = Character(Path(temp) / 'campaign_b' / 'actor.json', data=actor)
            self.assertNotEqual(sheet_path(first, output, 'html'), sheet_path(second, output, 'html'))

    def test_relative_and_absolute_source_have_same_name(self):
        actor = {'name': 'Same Name', 'type': 'character', 'system': {}, 'items': []}
        output = Path('character_sheets')
        relative = Character(Path('fvtt_export/actor.json'), data=actor)
        absolute = Character(Path('fvtt_export/actor.json').resolve(), data=actor)
        self.assertEqual(sheet_path(relative, output, 'html'), sheet_path(absolute, output, 'html'))

    def test_replace_creates_file_with_umask_permissions(self):
        previous = os.umask(0o022)
        try:
            with tempfile.TemporaryDirectory() as temp:
                fresh = Path(temp) / 'fresh.html'
                write_sheet(fresh, 'new', replace=True)
                self.assertEqual(stat.S_IMODE(fresh.stat().st_mode), 0o644)
                private = Path(temp) / 'private.html'
                private.write_text('old', encoding='utf-8')
                private.chmod(0o600)
                write_sheet(private, 'new', replace=True)
                self.assertEqual(stat.S_IMODE(private.stat().st_mode), 0o644)
                self.assertEqual(sorted(entry.name for entry in Path(temp).iterdir()),
                                 ['fresh.html', 'private.html'])
        finally:
            os.umask(previous)

    def test_cli_refuses_replace_without_flag(self):
        from lib import fallout_sheet_generator as generator
        example = next((Path(__file__).resolve().parents[1] / 'fvtt_export').glob('fvtt-Actor-marcel-*.json'))
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'example.html'
            args = ['generator', str(example), '--format', 'html']
            with patch.object(generator, 'sheet_path', return_value=target), patch('sys.argv', args):
                with redirect_stdout(io.StringIO()):
                    generator.main()
                original = target.read_bytes()
                with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as failure:
                    generator.main()
                self.assertEqual(failure.exception.code, 1)
                self.assertEqual(target.read_bytes(), original)
            with patch.object(generator, 'sheet_path', return_value=target), patch('sys.argv', args + ['--replace']):
                with redirect_stdout(io.StringIO()):
                    generator.main()


class RobotSheetTests(unittest.TestCase):
    def render(self, actor_type):
        items = [{'name': 'Leather Coat', 'type': 'apparel', 'system': {}}]
        data = {'name': 'Unit', 'type': actor_type, 'system': {'level': {'value': 1}}, 'items': items}
        return CharacterSheetGenerator(Character(Path('unused.json'), data=data)).generate_html_sheet()

    def test_robot_html_omits_apparel_section(self):
        html = self.render('robot')
        self.assertNotIn('<h2>Apparel</h2>', html)
        self.assertIn('<h2>Robot Armor</h2>', html)

    def test_character_html_keeps_apparel_section(self):
        html = self.render('character')
        self.assertIn('<h2>Apparel</h2>', html)
        self.assertNotIn('<h2>Robot Armor</h2>', html)


class StatusStylingTests(unittest.IsolatedAsyncioTestCase):
    def make_item(self, validation):
        info = {'name': 'Test Actor', 'class': 'Lvl 1 Vault Dweller'}
        return CharacterListItem(info, None, validation, None)

    def test_health_warnings_use_error_icon_and_class(self):
        item = self.make_item({'errors': ['Max health is 0'], 'warnings': ['No perks']})
        self.assertEqual((item.status_icon, item.status_class), ('[X]', 'status-error'))

    def test_informational_issues_keep_warning_icon_and_class(self):
        item = self.make_item({'errors': [], 'warnings': ['No perks']})
        self.assertEqual((item.status_icon, item.status_class), ('[!]', 'status-warning'))

    async def test_health_warning_label_renders_in_error_color(self):
        app = CharacterManagerApp()
        with tempfile.TemporaryDirectory() as temp:
            with patch('rpg_sheets.PROJECT_ROOT', Path(temp)):
                async with app.run_test() as pilot:
                    health = self.make_item({'errors': ['Max health is 0'], 'warnings': []})
                    note = self.make_item({'errors': [], 'warnings': ['No perks']})
                    failed = ErrorListItem('bad.json', 'Invalid JSON')
                    await app.query_one('#sidebar').mount(health, note, failed)
                    await pilot.pause()
                    health_label, note_label, failed_label = (
                        entry.query(Label).first() for entry in (health, note, failed))
                    self.assertTrue(str(health_label.render()).startswith('[X]'))
                    self.assertEqual(health_label.styles.color, failed_label.styles.color)
                    self.assertNotEqual(health_label.styles.color, note_label.styles.color)


class ExportUITests(unittest.IsolatedAsyncioTestCase):
    async def test_save_cancel_replace_open_and_refresh(self):
        app = CharacterManagerApp()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            exports = root / 'fvtt_export'
            exports.mkdir()
            sample = next((Path(__file__).resolve().parents[1] / 'fvtt_export').glob('fvtt-Actor-marcel-*.json'))
            shutil.copyfile(sample, exports / sample.name)
            output = root / 'sheet.html'
            with patch('rpg_sheets.PROJECT_ROOT', root), patch('rpg_sheets.sheet_path', return_value=output), \
                    patch('rpg_sheets.webbrowser.open') as browser:
                async with app.run_test() as pilot:
                    self.assertTrue(app.query_one('#btn_open').disabled)
                    selected = app.get_current_selection()
                    self.assertIsInstance(selected, CharacterListItem)
                    source = cast(CharacterListItem, selected).character_obj.character_file
                    app.action_generate_html()
                    await pilot.pause()
                    self.assertTrue(output.exists())
                    self.assertEqual(app.last_output, output)
                    self.assertFalse(app.query_one('#btn_open').disabled)
                    original = output.read_bytes()
                    app.action_generate_html_appendix()
                    await pilot.pause()
                    self.assertIsInstance(app.screen, ReplaceSheetScreen)
                    await pilot.press('r')
                    self.assertIsInstance(app.screen, ReplaceSheetScreen)
                    await pilot.press('escape')
                    await pilot.pause()
                    self.assertNotIsInstance(app.screen, ReplaceSheetScreen)
                    app.action_generate_html_appendix()
                    await pilot.pause()
                    await pilot.click('#cancel')
                    await pilot.pause()
                    self.assertEqual(output.read_bytes(), original)
                    app.action_generate_html_appendix()
                    await pilot.pause()
                    await pilot.click('#replace')
                    await pilot.pause()
                    self.assertNotIsInstance(app.screen, ReplaceSheetScreen)
                    self.assertIn('Appendix: Skill Descriptions', output.read_text(encoding='utf-8'))
                    await pilot.click('#btn_open')
                    browser.assert_called_once_with(output.as_uri())
                    await pilot.press('r')
                    current = app.get_current_selection()
                    self.assertIsInstance(current, CharacterListItem)
                    self.assertEqual(cast(CharacterListItem, current).character_obj.character_file, source)

    async def test_invalid_actor_has_actionable_reason(self):
        app = CharacterManagerApp()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            exports = root / 'fvtt_export'
            exports.mkdir()
            (exports / 'wrong.json').write_text(json.dumps({'type': 'npc', 'name': 'Nope', 'system': {}}))
            with patch('rpg_sheets.PROJECT_ROOT', root):
                async with app.run_test():
                    item = app.get_current_selection()
                    self.assertIsInstance(item, ErrorListItem)
                    self.assertIn('Unsupported actor type: npc', item.error_msg)


if __name__ == '__main__':
    unittest.main()
