# -*- mode: python ; coding: utf-8 -*-

added_files = [
    ( 'graphics/runner_icon.jpeg', 'img'),
    ( 'graphics/ground.png', 'img' ),
    ( 'graphics/Sky.png', 'img' ),
    ( 'graphics/Fly/Fly1.png', 'img' ),
    ( 'graphics/Fly/Fly2.png', 'img' ),
    ( 'graphics/snail/snail1.png', 'img' ),
    ( 'graphics/snail/snail2.png', 'img' ),
    ( 'graphics/Player/jump.png', 'img' ),
    ( 'graphics/Player/player_stand.png', 'img' ),
    ( 'graphics/Player/player_walk_1.png', 'img' ),
    ( 'graphics/Player/player_walk_2.png', 'img' ),
    ( 'font/Pixeltype.ttf', 'font'),
    ( 'audio/jump.mp3', 'sfx'),
    ( 'audio/music.wav', 'sfx')
]


a = Analysis(
    ['pygameTutorial.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pygameTutorial',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
