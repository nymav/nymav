"""Draw the profile's original AI-research game scene. No remote stats/services.

Requires Pillow. Fonts are local system fonts, not redistributed. A static PNG
and a slow ambient GIF share the same scene; README honors reduced-motion mode.
"""
import math
from html import escape
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
    tracked(d,(72,74),'AI ENGINEERING',font(15,True),COLORS['amber'],2)
    d.text((68,113),'AGENTS &',font=font(80),fill=COLORS['ink'])
    d.text((68,200),'EVIDENCE',font=font(80),fill=COLORS['ink'])
    d.text((72,325),'Retrieval · Validation · Evaluation',font=font(17,True),fill=COLORS['muted'])
    d.text((72,382),'Research + open-source tools',font=font(16,True),fill=COLORS['cyan'])
    sprite=scene(frame).resize((560,420),Image.Resampling.NEAREST)
    im.paste(sprite,(660,20))
    return im

def project_panel(name, category, accent, kind):
    """A game-interface chapter panel. All capability text remains native Markdown."""
    parts=[]
    def rect(x,y,w,h,color):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')
    def line(coords,color,width=2):parts.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    parts.append('<svg xmlns="http://www.w3.org/2000/svg" width="920" height="172" viewBox="0 0 920 172" role="img">')
    parts.append(f'<title>{escape(name)} — {escape(category)}</title>')
    parts.append('<path d="M0 0H900L920 20V172H20L0 152Z" fill="#101b2c"/>')
    parts.append('<path d="M1 1H899L919 21V171H21L1 151Z" fill="none" stroke="#34475c"/>')
    for x in range(24,920,24):rect(x,0,1,172,'#162236')
    for y in range(24,172,24):rect(0,y,920,1,'#162236')
    rect(0,36,4,62,accent)
    # Original pixel icons: source archive, document change, paired evaluation.
    if kind=='sources':
        rect(42,46,34,48,'#455e72');rect(50,40,34,48,accent);rect(58,34,34,48,'#d7d6bd')
        for y,w in [(46,22),(54,17),(62,20)]:rect(64,y,w,3,'#47616e')
        rect(62,70,16,3,accent)
    elif kind=='changes':
        rect(48,38,34,50,'#d7d6bd');rect(58,47,16,3,'#455e72');rect(58,56,12,3,'#455e72')
        rect(56,65,20,3,accent);rect(77,75,20,3,accent);rect(85,67,3,19,accent)
    else:
        rect(43,41,20,45,'#405b72');rect(70,41,20,45,'#d7d6bd')
        for y,w in [(49,11),(58,8),(67,10)]:rect(47,y,w,3,accent)
        for y,w in [(49,11),(58,11),(67,7)]:rect(74,y,w,3,'#456274')
        line('51,97 63,109 86,86',accent,3)
    parts.append(f'<text x="126" y="76" fill="#ecede4" font-size="40" font-weight="600" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">{escape(name)}</text>')
    parts.append(f'<text x="128" y="112" fill="{accent}" font-size="18" letter-spacing="1" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">{escape(category.upper())}</text>')
    # A small illustrative trace, not a measured score or claimed model result.
    rect(610,38,260,96,'#0b1422')
    if kind=='sources':
        for y,w in [(49,55),(66,74),(83,62),(100,48)]:rect(623,y,w,3,'#4c697a')
        rect(620,78,81,15,'#28474f');rect(623,83,62,3,accent)
        line('704,85 729,85 729,62 757,62',accent)
        rect(759,49,90,27,'#243e4c');rect(768,58,67,3,'#b7c9c2');rect(768,65,48,3,'#6e979d')
    elif kind=='changes':
        for x in [626,768]:
            rect(x,49,66,66,'#213248')
            for y,w in [(60,44),(71,37),(94,40)]:rect(x+10,y,w,3,'#627e8c')
        rect(636,81,36,4,'#997667');rect(778,81,43,4,accent)
        line('697,82 726,82 726,57 762,57',accent)
        rect(721,77,10,10,accent)
    else:
        for y in [61,104]:
            line(f'627,{y} 653,{y} 664,{y-9} 687,{y-9} 698,{y+7} 723,{y+7} 740,{y} 775,{y} 790,{y-8} 840,{y-8}', '#6e969b' if y==61 else accent)
        rect(761,44,2,75,'#4d6276');rect(756,75,12,12,accent)
    rect(42,146,836,1,'#2d4055')
    parts.append('</svg>')
    (OUT/(name.lower()+'.svg')).write_text(''.join(parts)+'\n')

def section_panel(filename, title):
    safe=escape(title)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="88" viewBox="0 0 920 88" role="img">
<title>{safe}</title><path d="M0 0H902L920 18V88H0Z" fill="#142136"/>
<path d="M0 87H920M1 0H901L919 18" fill="none" stroke="#3c5269"/>
<path d="M28 25H36V33H28ZM40 33H48V41H40ZM28 41H36V49H28Z" fill="#edb66e"/>
<text x="72" y="56" fill="#ecede4" font-size="36" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">{safe}</text>
<path d="M804 28H842V56H804ZM816 22H854V50H846M816 56V62H854V54" fill="none" stroke="#658a94" stroke-width="2"/>
</svg>'''
    (OUT/filename).write_text(svg+'\n')

if __name__ == '__main__':
    still=banner(0);still.save(OUT/'ai-workspace.png',optimize=True)
    palette=still.quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    frames=[banner(i).quantize(palette=palette,dither=Image.Dither.NONE) for i in range(24)]
    frames[0].save(OUT/'ai-workspace.gif',save_all=True,append_images=frames[1:],duration=180,loop=0,optimize=True,disposal=1)
    project_panel('DocAtlas','Retrieval & grounding',COLORS['cyan'],'sources')
    project_panel('DocMend','Documentation integrity',COLORS['amber'],'changes')
    project_panel('ModelGuard','Regression evaluation','#b4baa5','evaluation')
    section_panel('research-section.svg','Research outputs')
    section_panel('software-section.svg','More software')
    section_panel('background-section.svg','Tools & background')
    for path in sorted(OUT.iterdir()):print(path.name,path.stat().st_size)
