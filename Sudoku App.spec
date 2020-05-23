# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['App.py'],
             pathex=['F:\\Projects\\python\\game\\sudoku backtracking visualizer'],
             binaries=[],
             datas=[('D:\\Program\\envs\\tensorflow\\lib\\site-packages\\eel\\eel.js', 'eel'), ('www', 'www')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['win32com', 'numpy', 'cryptography'],
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
          name='Sudoku App',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
