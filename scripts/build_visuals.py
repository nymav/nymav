"""Draw the profile's original AI-research game scene. No remote stats/services.

Requires Pillow. Fonts are local system fonts, not redistributed. A static PNG
and a slow ambient GIF share the same scene; README honors reduced-motion mode.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
W, H = 1280, 480
COLORS = dict(bg='#0b1220', ink='#ecede4', muted='#a4b4c6', edge='#32445c',
              cyan='#81c7ca', amber='#edb66e', orange='#d67d50')

def font(size, mono=False):
    options = (['/System/Library/Fonts/Menlo.ttc', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'] if mono else
               ['/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'])
    for path in options:
        if Path(path).is_file(): return ImageFont.truetype(path, size)
    return ImageFont.load_default(size=size)

def tracked(d, xy, text, face, fill, spacing=2):
    x, y = xy
    for char in text:
        d.text((x, y), char, font=face, fill=fill)
        x += d.textlength(char, font=face) + spacing

def scene(frame=0):
    """Original 280x210 sprite composition: a quiet AI engineering workstation."""
    im = Image.new('RGB', (280, 210), COLORS['bg']); d = ImageDraw.Draw(im)
    def box(x,y,w,h,c): d.rectangle((x,y,x+w-1,y+h-1),fill=c)
    # Room cutaway, low wall and a shallow raised floor.
    d.polygon([(8,48),(246,48),(272,73),(272,187),(248,204),(8,204)],fill='#142035')
    box(8,48,238,121,'#17253b');box(8,48,238,2,'#34475c')
    d.polygon([(8,169),(246,169),(272,187),(32,187)],fill='#293449')
    d.polygon([(32,187),(272,187),(248,204),(8,204),(8,185)],fill='#1b283b')
    for x in range(23,253,26): d.line((x,171,x+21,185),fill='#344258')
    d.line((10,201,247,201),fill='#415168')
    # Tall window: a game-world night sky, one moon, silhouetted ridges.
    box(24,59,100,72,'#3d5167');box(27,62,94,66,'#0a172c')
    for x,y in [(36,72),(61,81),(105,70),(93,93),(49,96),(76,68)]:
        box(x,y,1,1,'#8faabf')
    d.ellipse((88,73,102,87),fill='#d6d5b4');d.ellipse((92,71,104,83),fill='#0a172c')
    d.polygon([(27,117),(44,104),(60,112),(80,99),(102,116),(120,107),(120,127),(27,127)],fill='#283c54')
    d.polygon([(27,123),(48,115),(63,120),(93,110),(120,120),(120,127),(27,127)],fill='#354c62')
    box(73,62,2,66,'#40536a');box(27,101,94,2,'#40536a')
    # Evidence archive: carefully different books, no fake progress/XP counters.
    box(144,63,72,34,'#0c1829');box(143,97,75,3,'#506074')
    for x,h,c in [(148,22,'#697e91'),(155,26,'#bd9163'),(163,18,'#4c797d'),(170,25,'#b0afa0'),(178,21,'#816c67'),(186,24,'#4e7d87'),(194,19,'#a5835c'),(202,26,'#6d8292')]:
        box(x,96-h,5,h,c);box(x+1,98-h,3,1,'#cfbea0')
    # Three pinned paper sources next to the window.
    for x,y,c in [(135,108,'#a3a897'),(148,114,'#ceb48b'),(161,107,'#91a7a8')]:
        box(x,y,10,14,c);box(x+2,y+4,6,1,'#5b6d74');box(x+2,y+7,5,1,'#5b6d74')
    # Monitor plinth, paired displays: source retrieval and evidence/trace checks.
    box(37,145,185,8,'#ac8157');box(38,153,181,3,'#634e3f')
    box(43,156,5,28,'#4a4f55');box(211,156,5,28,'#4a4f55')
    for x,width in [(53,48),(108,55)]:
        box(x,111,width,32,'#080f1a');box(x+2,113,width-4,26,'#173645')
        box(x+width//2-2,143,4,3,'#71818a');box(x+width//2-9,146,18,1,'#bbc2b6')
    # Source passages in the left screen.
    for y,w in [(117,21),(122,32),(127,26),(132,29)]:box(58,y,w,1,'#709c9d')
    box(57,120,2,8,'#edb66e')
    # A bounded trace on the right screen with a review checkpoint.
    points=[(115,126),(126,118),(140,125),(153,117)]
    d.line(points,fill='#5f8e94')
    for i,(x,y) in enumerate(points):box(x-1,y-1,3,3,'#d9b777' if i==2 else '#9dc3be')
    box(115,134,28,1,'#709c9d')
    # Local machine, vent slots and a single slow status LED.
    box(227,132,14,37,'#101a2a');box(229,134,10,2,'#40556a')
    for y in [140,144,148]:box(230,y,7,1,'#3b4e61')
    box(230,157,2,2,'#b8b88a' if frame < 12 else '#778c80')
    # Keyboard, mouse, notes and a mug.
    d.polygon([(71,150),(104,150),(109,154),(75,154)],fill='#737d80')
    for x in range(76,104,4):box(x,151,2,1,'#b2b6ab')
    box(115,150,4,3,'#a1aaa7');box(176,149,14,5,'#c9bca1')
    d.line((179,150,185,152),fill='#7e8c85');box(199,141,7,7,'#e0c8a0');box(206,143,2,3,'#b9a080')
    # Lamp: warm, localized illumination rather than flashing neon.
    d.line([(196,145),(196,119),(186,109)],fill='#8e9b9e',width=2)
    d.polygon([(178,108),(186,103),(193,110),(181,114)],fill='#c89c63')
    box(181,112,10,1,'#f2d2a0')
    # Researcher at the bench, drawn from behind.
    box(124,145,21,26,'#263e50');box(119,152,5,12,'#35536a');box(145,151,7,11,'#35536a')
    box(120,151,7,4,'#c59a7c');box(147,150,6,4,'#c59a7c')
    box(126,131,16,16,'#c59a7c');box(123,129,19,9,'#26303b');box(126,126,14,5,'#26303b')
    box(130,145,8,4,'#8a7468');box(127,170,5,13,'#182335');box(140,170,5,13,'#182335')
    box(125,181,9,3,'#8b8f91');box(141,181,9,3,'#8b8f91')
    # Chair with a deliberate visible back; foreground plant.
    box(123,157,25,16,'#4e6575');box(126,160,19,2,'#627f8d')
    box(134,173,3,13,'#788087');box(125,185,21,2,'#788087')
    box(23,163,13,14,'#9c7859');box(25,177,9,2,'#5a514c')
    d.line((29,164,29,142),fill='#4b8175',width=2)
    for xy in [(20,146,29,151),(29,140,38,146),(19,155,29,160),(29,151,39,157)]:d.ellipse(xy,fill='#6c9683')
    # A tiny, slow cursor. No rapid flashes or motion behind the text.
    if frame < 12:box(146,134,3,1,'#d9c696')
    # A quiet warm light reflection pulses once across a full loop.
    c=int(76+7*math.sin(frame*2*math.pi/24))
    box(182,154,15,1,(c+35,c+6,c-16))
    return im

def banner(frame):
    im=Image.new('RGB',(W,H),COLORS['bg']);d=ImageDraw.Draw(im)
    # Subtle pixel grid plus a thin structural frame, never a badge wall.
    for x in range(0,W,32):d.line((x,0,x,H),fill='#0e1829')
    for y in range(0,H,32):d.line((0,y,W,y),fill='#0e1829')
    d.line((40,40,1240,40),fill='#344459');d.line((40,440,1240,440),fill='#344459')
    d.rectangle((40,40,44,72),fill=COLORS['amber'])
    tracked(d,(72,74),'NYMAV',font(16,True),COLORS['amber'],3)
    d.text((68,112),'NIKHIL YARRA',font=font(86),fill=COLORS['ink'])
    d.text((72,220),'Applied AI engineering',font=font(29,True),fill=COLORS['ink'])
    d.text((72,279),'Agents · Retrieval · Evaluation',font=font(20,True),fill=COLORS['muted'])
    d.text((72,371),'DocAtlas / DocMend / ModelGuard',font=font(17,True),fill=COLORS['cyan'])
    sprite=scene(frame).resize((560,420),Image.Resampling.NEAREST)
    im.paste(sprite,(660,20))
    return im

if __name__ == '__main__':
    still=banner(0);still.save(OUT/'ai-research-lab.png',optimize=True)
    palette=still.quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    frames=[banner(i).quantize(palette=palette,dither=Image.Dither.NONE) for i in range(24)]
    frames[0].save(OUT/'ai-research-lab.gif',save_all=True,append_images=frames[1:],duration=180,loop=0,optimize=True,disposal=1)
    for path in sorted(OUT.iterdir()):print(path.name,path.stat().st_size)
