# -*- mode: python ; coding: utf-8 -*-
import os

a = Analysis(
    ['src/main.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('src/processor.py', '.'),
        ('src/ui.py', '.'),
        ('public/images/icon.ico', 'public/images'),
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
    icon= os.path.abspath('public/images/icon.ico'),
    version_info={
        'version': '1.0',
        'company_name': 'SyntexError',
        'file_description': 'DeepErase Application',
        'legal_copyright': 'Copyright © 2025',
    },
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)