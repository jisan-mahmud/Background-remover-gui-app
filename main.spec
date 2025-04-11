# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/processor.py', '.'),
        ('src/ui.py', '.'),
        ('src/assets/*', 'assets')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DeepErase',
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
    icon=['public/images/icon.ico'],
    version_info={
        'version': '1.0',
        'company_name': 'SyntexError',
        'file_description': 'DeepErase Application',
        'legal_copyright': 'Copyright © 2025',
    },
)
