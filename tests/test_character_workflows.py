"""Regression checks for loading, validation, and TUI error handling."""

import unittest
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

from lib.character_data import Character
from lib.fallout_character_validator import CharacterValidator
from lib.fallout_sheet_generator import CharacterSheetGenerator
from lib.systems.fallout import FalloutSystem
from rpg_sheets import CharacterManagerApp, ErrorListItem


class CharacterWorkflowTests(unittest.TestCase):
    def make_character(self, actor_type='character', items=None):
        data = {
            'name': 'Test Actor',
            'type': actor_type,
            'system': {'level': {'value': 1}},
            'items': items if items is not None else [],
        }
        return Character(Path('unused.json'), data=data)

    def test_rejects_non_actor_and_malformed_exports(self):
        for data in ([], {'type': 'item', 'system': {}, 'items': []},
                     {'type': 'character', 'system': [], 'items': []},
                     {'type': 'robot', 'system': {}, 'items': {}}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                Character(Path('unused.json'), data=cast(Any, data))

    def test_system_ignores_items_and_non_object_json(self):
        system = FalloutSystem()
        for data in ([], {'type': 'item', 'name': 'A', 'system': {},
                          '_stats': {'systemId': 'fallout'}},
                     {'type': 'character', 'name': 'A', 'system': {}, '_stats': []}):
            self.assertFalse(system.can_handle(Path('unused.json'), cast(Any, data)))
        self.assertTrue(system.can_handle(Path('unused.json'), {
            'type': 'robot', 'name': 'R', 'system': {},
            '_stats': {'systemId': 'fallout'},
        }))

    def test_stashed_items_reported_and_validation_repeatable(self):
        items = [
            {'name': 'Gun', 'type': 'weapon', 'system': {'stashed': True}},
            {'name': 'Coat', 'type': 'apparel', 'system': {'stashed': True}},
        ]
        validator = CharacterValidator(self.make_character(items=items))
        validator.run_validation(verbose=False)
        self.assertIn('No weapons equipped (1 available)', validator.completeness_issues)
        self.assertIn('No apparel equipped (1 available)', validator.completeness_issues)
        original = (list(validator.health_warnings), list(validator.completeness_issues))
        validator.run_validation(verbose=False)
        self.assertEqual(original, (validator.health_warnings, validator.completeness_issues))

    def test_error_item_cannot_generate_sheet(self):
        app = CharacterManagerApp()
        with patch.object(app, 'get_current_selection', return_value=ErrorListItem('bad.json', 'Invalid JSON')):
            with patch.object(app, 'notify') as notify:
                app.generate_sheet('markdown')
        notify.assert_called_once_with('Cannot generate sheet: bad.json failed to load', severity='error')

    def test_example_export_renders_both_formats(self):
        example = next(Path('fvtt_export').glob('fvtt-Actor-marcel-*.json'))
        generator = CharacterSheetGenerator(Character(example))
        self.assertIn('## Body Status', generator.generate_markdown_sheet())
        self.assertIn('Marcel', generator.generate_html_sheet())


class CharacterManagerUITests(unittest.IsolatedAsyncioTestCase):
    async def test_tui_loads_example_and_refreshes(self):
        app = CharacterManagerApp()
        async with app.run_test() as pilot:
            self.assertIsNotNone(app.get_current_selection())
            await pilot.press('r')
            self.assertIsNotNone(app.get_current_selection())


if __name__ == '__main__':
    unittest.main()
