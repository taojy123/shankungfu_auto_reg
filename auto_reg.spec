# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'auto_reg.py'],
             pathex=['E:\\Workspace\\GitHub\\shankungfu_auto_reg'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'Auto_reg.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
