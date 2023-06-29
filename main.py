import os, glob, matplotlib, sys
from matplotlib.font_manager import FontManager
if 'all_users' in sys.argv:
    folder_name = '/usr/share/fonts' 
else:
    folder_name = os.path.join(matplotlib.get_data_path(), 'fonts/ttf')

ttf_files = glob.glob('*.ttf')
if not ttf_files:
    raise ValueError('本目录下没有ttf文件')
ttf = ttf_files[0]
os.system(f'mv { ttf } { folder_name } && fc-cache -f -v>/etc/null')
# fc-list 命令可以查看系统字体文件夹中安装的所有字体
cache = matplotlib.get_cachedir()
os.system(f'rm -rf { cache }')

# 找到刚安装的字体的名字（不是文件名）
font_manager = FontManager()
for font in font_manager.ttflist:
    if ttf in font.fname:
        print(font.name)
