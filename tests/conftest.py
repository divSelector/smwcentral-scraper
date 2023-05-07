import pytest
from pathlib import Path

@pytest.fixture
def mock_ra_config_dir(tmp_path: Path) -> Path:
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    cfg = config_dir / "retroarch.cfg"
    cfg.touch()
    return config_dir

@pytest.fixture
def mock_not_clean_rom_dir(tmp_path: Path) -> Path:
    clean_rom_dir = tmp_path / "clean"
    clean_rom_dir.mkdir()
    sfc = clean_rom_dir / 'clean.sfc'
    sfc.touch()
    return clean_rom_dir

@pytest.fixture
def mock_empty_dir(tmp_path: Path) -> Path:
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    return empty_dir


