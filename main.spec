# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['C:\storyboard\decrease_data'],
    binaries=[],
    datas=[ ('c_rows_columns.py', '.'), 
   			 ('computation.py', '.'), 
    			('initialization.py', '.'), 
  			  ('input_file.py', '.'), 
   			 ('output_result.py', '.'), 
   			 ('gui.py', '.'), 
    			('meassage.py', '.'),],

    hiddenimports=['pandas', 'numpy','tkinter','Enum'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
splash = Splash(
    'ndslogo.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='main',
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
    icon=['sheep.ico'],
)
