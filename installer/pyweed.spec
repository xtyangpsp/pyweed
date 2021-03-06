# -*- mode: python -*-

block_cipher = None

#
ONE_FILE = True

a = Analysis(['../pyweed/pyweed_launcher.py'],
             pathex=['/workspace/test/pyweed/installer'],
             binaries=[],
             datas=[],
             hiddenimports=['ipykernel.datapub'],
             hookspath=['hooks'],
             runtime_hooks=['rthooks/qtconsole.py', 'rthooks/obspy.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# Standard args for directory-based build
exe_args = [pyz, a.scripts]
exe_kwargs = dict(
    exclude_binaries=True,
    name='PyWEED',
    debug=True,
    strip=False,
    upx=True,
    console=True
)
# Overrides for single-file build
if ONE_FILE:
    exe_args += [
        a.binaries,
        a.zipfiles,
        a.datas,
    ]
    exe_kwargs['exclude_binaries'] = False

exe = EXE(*exe_args, **exe_kwargs)

if ONE_FILE:
    # The Mac .app bundle only works in single-file mode
    app = BUNDLE(exe,
                 name='PyWEED.app',
                 icon='icon.icns',
                 bundle_identifier='edu.iris.PyWEED')
else:
    # Bundle the dependencies along with the executable
    coll = COLLECT(exe,
                   a.binaries,
                   a.zipfiles,
                   a.datas,
                   strip=False,
                   upx=True,
                   name='pyweed')

