# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['HororSnake.py'],
             pathex=['C:/Users/Freeman.Autobot/Desktop/PythonExamples/HororSnake5'],
             binaries=[],
             datas=[('python_icon.ico','.'),('sounds/.','sounds')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='SnakeHoror',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='python_icon.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          version='version.rc')
