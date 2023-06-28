import os, glob, matplotlib, sys
from matplotlib.font_manager import FontManager
if len(sys.argv) > 1 and sys.argv[1] == 1:
    all_user = True  
else:
    all_user = False
    
if all_user:
    folder_name = '/usr/share/fonts'
else:
    
    font_manager = FontManager()
    folder_name = os.path.dirname(next(iter(font_manager.ttflist)).fname)
    #set(os.path.dirname(i.fname) for i in font_manager.ttflist)
ttf = glob.glob('*.ttf')[0]
os.system(f'mv { ttf } { folder_name } && fc-cache -f -v>/etc/null')
# fc-list
cache = matplotlib.get_cachedir()
os.system(f'rm -rf { cache }')

font_manager = FontManager()
for font in font_manager.ttflist:
    if ttf in font.fname:
        print(font.name)
