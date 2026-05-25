"""Regression tests for the Claude plugin manifest."""

from __future__ import annotations

import json
from pathlib import Path


def test_autoregen_user_config_has_default_false() -> None:
    """Fresh installs need a default so Stop hook substitution works."""
    manifest = json.loads(Path('.claude-plugin/plugin.json').read_text(encoding='utf-8'))

    autoregen = manifest['userConfig']['autoregen']
    assert autoregen['type'] == 'boolean'
    assert autoregen['default'] is False
