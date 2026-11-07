from pathlib import Path
from PIL import Image
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
res = root / "android" / "app" / "src" / "main" / "res"
src = Image.open(root / "assets" / "app-icon-source.png").convert("RGBA")

# Preserve the uploaded artwork; resize it into Android launcher icon densities.
for folder, size in [("mipmap-mdpi",48),("mipmap-hdpi",72),("mipmap-xhdpi",96),("mipmap-xxhdpi",144),("mipmap-xxxhdpi",192)]:
    out = res / folder
    out.mkdir(parents=True, exist_ok=True)
    icon = src.resize((size,size), Image.Resampling.LANCZOS)
    icon.save(out / "ic_launcher.png")
    icon.save(out / "ic_launcher_round.png")
    # Adaptive foreground: keep the supplied rounded-square artwork large while leaving a small safe margin for launcher masks.
    fg = Image.new("RGBA", (size,size), (0,0,0,0))
    artwork = src.resize((int(size*.94),int(size*.94)), Image.Resampling.LANCZOS)
    fg.alpha_composite(artwork, ((size-artwork.width)//2,(size-artwork.height)//2))
    fg.save(out / "ic_launcher_foreground.png")

v26 = res / "mipmap-anydpi-v26"
v26.mkdir(parents=True, exist_ok=True)
(v26 / "ic_launcher.xml").write_text('''<?xml version="1.0" encoding="utf-8"?>\n<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n    <background android:drawable="@color/ic_launcher_background" />\n    <foreground android:drawable="@mipmap/ic_launcher_foreground" />\n</adaptive-icon>\n''')
(v26 / "ic_launcher_round.xml").write_text('''<?xml version="1.0" encoding="utf-8"?>\n<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n    <background android:drawable="@color/ic_launcher_background" />\n    <foreground android:drawable="@mipmap/ic_launcher_foreground" />\n</adaptive-icon>\n''')
values = res / "values"
values.mkdir(parents=True, exist_ok=True)
(values / "ic_launcher_background.xml").write_text('''<?xml version="1.0" encoding="utf-8"?>\n<resources><color name="ic_launcher_background">#000000</color></resources>\n''')

# Keep the launcher label consistent with the project name.
strings = values / "strings.xml"
if strings.exists():
    tree = ET.parse(strings)
    rt = tree.getroot()
    app_name = rt.find("string[@name='app_name']")
    if app_name is None:
        app_name = ET.SubElement(rt, "string", {"name":"app_name"})
    app_name.text = "Graph Studio"
    tree.write(strings, encoding="utf-8", xml_declaration=True)
else:
    strings.write_text('<?xml version="1.0" encoding="utf-8"?>\n<resources><string name="app_name">Graph Studio</string></resources>\n')
