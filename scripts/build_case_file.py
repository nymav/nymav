import os,random,math
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','case');os.makedirs(D,exist_ok=True)
MAN='#E6D3A8';PAP='#F3EAD3';PAP2='#EFE3C6';INK='#2A241C';INK2='#5A5043';RED='#B0281F';TAB='#D8C08C';BLK='#1B1814';CORK='#7A5534'
TW='"Courier New",Courier,"Nimbus Mono PS",monospace';SER='Georgia,"Times New Roman",serif'
CSS=f'''<style>
.tw{{font-family:{TW}}}.se{{font-family:{SER}}}
.red{{transform-box:fill-box;transform-origin:right;animation:red .55s cubic-bezier(.6,0,.3,1) both}}@keyframes red{{from{{transform:scaleX(1)}}to{{transform:scaleX(0)}}}}
.stamp{{transform-box:fill-box;transform-origin:center;animation:st .35s cubic-bezier(.2,1.6,.4,1) both}}@keyframes st{{0%{{opacity:0;transform:scale(2.2) rotate(var(--r))}}100%{{opacity:.9;transform:scale(1) rotate(var(--r))}}}}
.ink{{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:ink 1.6s ease-out both}}@keyframes ink{{to{{stroke-dashoffset:0}}}}
.drop{{animation:dr .6s cubic-bezier(.2,.9,.3,1.2) both}}@keyframes dr{{from{{opacity:0;transform:translateY(-14px)}}to{{opacity:1;transform:none}}}}
.type{{animation:ty .01s steps(1) both}}@keyframes ty{{from{{opacity:0}}to{{opacity:1}}}}
.blink{{animation:bl 1s steps(2) infinite}}@keyframes bl{{50%{{opacity:0}}}}
.sway{{transform-box:fill-box;transform-origin:top center;animation:sw 4s ease-in-out infinite}}@keyframes sw{{50%{{transform:rotate(1.5deg)}}}}
</style>'''
def defs():
    return f'''<defs><filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .27  0 0 0 0 .15  0 0 0 .09 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
<filter id="rough"><feTurbulence baseFrequency=".05" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="2.2"/></filter>
<filter id="sh" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity=".35"/></filter></defs>'''
def save(n,w,h,body):open(f'{D}/{n}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{defs()}{CSS}{body}</svg>')
def paper(x,y,w,h,fill=PAP,rx=3,shadow=True):
    sh='filter="url(#sh)"' if shadow else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {sh}/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" filter="url(#grain)"/>'
def redline(x,y,text,size,d,col=INK,weight='normal',fam='tw',maxw=None):
    w=maxw or len(text)*size*.6+6
    return f'<text x="{x}" y="{y}" class="{fam}" font-size="{size}" font-weight="{weight}" fill="{col}">{text}</text><rect class="red" style="animation-delay:{d:.2f}s" x="{x-3}" y="{y-size*.82:.1f}" width="{w:.0f}" height="{size*1.05:.1f}" fill="{BLK}"/>'
def stamp(cx,cy,text,d,rot=-8,size=22,col=RED):
    w=len(text)*size*.66+30;h=size+22
    return f'<g class="stamp" style="--r:{rot}deg;animation-delay:{d:.2f}s" filter="url(#rough)"><rect x="{cx-w/2:.0f}" y="{cy-h/2:.0f}" width="{w:.0f}" height="{h}" rx="5" fill="none" stroke="{col}" stroke-width="3.5"/><rect x="{cx-w/2+5:.0f}" y="{cy-h/2+5:.0f}" width="{w-10:.0f}" height="{h-10}" rx="3" fill="none" stroke="{col}" stroke-width="1.2"/><text x="{cx}" y="{cy+size*.36:.0f}" text-anchor="middle" class="tw" font-size="{size}" font-weight="700" letter-spacing="3" fill="{col}">{text}</text></g>'
def clip(x,y):
    return f'<path d="M{x} {y+40} V{y+6} a8 8 0 0 1 16 0 V{y+46} a12 12 0 0 1 -24 0 V{y+14}" fill="none" stroke="#8C8C8C" stroke-width="3" stroke-linecap="round"/>'
# ---------------- HERO
W,H=1200,490
b=[   f'<path d="M30 60 q0 -24 24 -24 h230 q14 0 22 12 l18 24 h846 q20 0 20 20 v360 q0 20 -20 20 H50 q-20 0 -20 -20z" fill="{MAN}" filter="url(#sh)"/>',
   f'<path d="M30 60 q0 -24 24 -24 h230 q14 0 22 12 l18 24 h846 q20 0 20 20 v360 q0 20 -20 20 H50 q-20 0 -20 -20z" fill="{MAN}" filter="url(#grain)"/>',
   f'<text x="58" y="62" class="tw" font-size="14" font-weight="700" letter-spacing="2" fill="{INK2}">CASE FILE № NY-0426</text>',
   paper(70,96,700,340),clip(96,78),
   f'<text x="100" y="138" class="tw" font-size="13" letter-spacing="3" fill="{INK2}">SUBJECT PROFILE · APPLIED AI</text>',
   f'<line x1="100" y1="150" x2="740" y2="150" stroke="{INK2}" stroke-width="1"/>']
rows=[('NAME','Nikhil Yarra',30,'bold'),('ROLE','Applied AI Engineer · Founder, Teyrin',17,'normal'),('SPECIALTY','retrieval you can inspect',17,'normal'),('','agents you can verify',17,'normal'),('METHOD','every claim traced to a source',17,'normal'),('BASED','New York City',17,'normal')]
y=196;d=.5
for k,v,s,wt in rows:
    if k:b.append(f'<text x="100" y="{y}" class="tw" font-size="12" letter-spacing="2" fill="{INK2}">{k}</text>')
    b.append(redline(210,y,v,s,d,weight=wt));d+=.35;y+=(46 if s>20 else 36)
b.append(f'<text x="100" y="420" class="tw" font-size="12" fill="{INK2}">FILED BY: github.com/nymav<tspan class="blink"> ▌</tspan></text>')
# fingerprint
fx,fy=960,230
fp=[]
for i in range(11):
    rx,ry=12+i*8,18+i*9.5
    l=2*math.pi*max(rx,ry)*.8
    gap=random.Random(i).uniform(.1,.3)
    fp.append(f'<ellipse class="ink" style="--l:{l:.0f};animation-delay:{.4+i*.08:.2f}s" cx="{fx}" cy="{fy}" rx="{rx}" ry="{ry}" fill="none" stroke="{INK}" stroke-opacity=".75" stroke-width="2.4" stroke-dasharray="{l*(1-gap):.0f} {l*gap:.0f}" transform="rotate({-6+i*2} {fx} {fy})"/>')
b.append(paper(830,96,260,300,PAP2))
b.append(f'<clipPath id="fpc"><rect x="846" y="112" width="228" height="244"/></clipPath><g clip-path="url(#fpc)">{"".join(fp).replace("stroke-dasharray=","data-x=")}</g>')
b.append(f'<text x="960" y="380" text-anchor="middle" class="tw" font-size="12" letter-spacing="3" fill="{INK2}">PRINT ON FILE</text>')
b.append(stamp(960,250,'VERIFIED',3.0,-12,30))
save('hero',W,H,''.join(b))
# ---------------- SECTION TABS
for key,ex,label in [('t-systems','EXHIBIT 01','SYSTEMS'),('t-research','EXHIBIT 02','PUBLISHED EVIDENCE'),('t-built','EXHIBIT 03','ADDITIONAL ITEMS'),('t-board','EXHIBIT 04','THE TRAIL'),('t-kit','EXHIBIT 05','FIELD KIT')]:
    w=len(label)*14+180
    save(key,1200,64,f'<path d="M4 58 v-36 q0 -10 10 -10 h{w-30} q10 0 16 10 l14 36 z" fill="{TAB}"/><path d="M4 58 v-36 q0 -10 10 -10 h{w-30} q10 0 16 10 l14 36 z" fill="{TAB}" filter="url(#grain)"/>'
         f'<text x="22" y="43" class="tw" font-size="13" font-weight="700" letter-spacing="2" fill="{RED}">{ex}</text><text x="140" y="43" class="tw" font-size="17" font-weight="700" letter-spacing="3" fill="{INK}">{label}</text><rect x="0" y="58" width="1200" height="3" fill="{TAB}"/>')
print('hero ok')
# ---------------- EXHIBIT CARDS (systems)
def exhibit(name,letter,title,lines,fig,stamptext,d0=.3):
    W,H=380,400
    b=[paper(10,12,W-20,H-30),f'<rect x="10" y="12" width="{W-20}" height="34" fill="{RED}" fill-opacity=".1"/>',
       f'<text x="26" y="35" class="tw" font-size="13" font-weight="700" letter-spacing="3" fill="{RED}">EXHIBIT {letter}</text><text x="{W-26}" y="35" text-anchor="end" class="tw" font-size="11" fill="{INK2}">github ↗</text>',
       f'<text x="26" y="84" class="se" font-size="28" font-weight="700" fill="{INK}">{title}</text>']
    y=112
    for i,l in enumerate(lines):b.append(redline(26,y,l,13,d0+.3*i,col=INK2));y+=21
    b.append(fig)
    b.append(stamp(W-110,H-56,stamptext,d0+2.2,-7,15))
    save(name,W,H,''.join(b))
def bars():
    out=[];data=[('bm25 §2.1',.55,0),('dense §4.3',.88,1),('hybrid §4.3',.97,1),('dense §1.0',.35,0)]
    for i,(n,v,hit) in enumerate(data):
        y=200+i*30
        out.append(f'<text x="26" y="{y+11}" class="tw" font-size="11" fill="{INK2}">{n}</text><line x1="130" y1="{y+6}" x2="330" y2="{y+6}" stroke="{INK2}" stroke-opacity=".25" stroke-width="10" stroke-linecap="round"/>')
        L=200*v;out.append(f'<line class="ink" style="--l:{L:.0f};animation-delay:{1.2+i*.2:.1f}s" x1="130" y1="{y+6}" x2="{130+L:.0f}" y2="{y+6}" stroke="{RED if hit else INK}" stroke-width="10" stroke-linecap="round"/>')
    out.append(f'<ellipse class="ink" style="--l:340;animation-delay:2.2s" cx="230" cy="245" rx="120" ry="34" fill="none" stroke="{RED}" stroke-width="2" filter="url(#rough)"/>')
    return ''.join(out)
def diff():
    out=[];rows=[('  detect(rev_a, rev_b)',INK2,''),('- "compares two files"',RED,'-'),('+ "compares Git revisions"',INK,'+'),('  README: "compares files"',RED,'!')]
    for i,(t,c,m) in enumerate(rows):
        y=210+i*28
        if m=='!':out.append(f'<path class="ink" style="--l:420;animation-delay:{1.8}s" d="M22 {y+8} q150 10 320 -2" fill="none" stroke="{RED}" stroke-width="2.5" filter="url(#rough)"/>')
        out.append(f'<text class="type" style="animation-delay:{1.0+i*.3:.1f}s" x="26" y="{y}" font-family={TW!r} font-size="13" fill="{c}" xml:space="preserve">{t}</text>')
    out.append(f'<text class="type" style="animation-delay:2.4s" x="250" y="320" font-family={TW!r} font-size="11" fill="{RED}" font-style="italic">← drift!</text>')
    return ''.join(out).replace("font-family='","font-family='")
def compare():
    out=[];vals=[(.8,.84),(.72,.78),(.9,.58),(.66,.7),(.76,.8)]
    for i,(a,c) in enumerate(vals):
        x=40+i*60;base=330
        out.append(f'<rect x="{x}" y="{base-110*a:.0f}" width="18" height="{110*a:.0f}" fill="none" stroke="{INK2}" stroke-width="1.5" stroke-dasharray="3 3"/>')
        col=RED if c<a else INK
        out.append(f'<rect class="drop" style="animation-delay:{1+i*.2:.1f}s" x="{x+22}" y="{base-110*c:.0f}" width="18" height="{110*c:.0f}" fill="{col}" fill-opacity=".85"/>')
    out.append(f'<ellipse class="ink" style="--l:300;animation-delay:2.2s" cx="{40+2*60+20}" cy="{330-60}" rx="34" ry="78" fill="none" stroke="{RED}" stroke-width="2.2" filter="url(#rough)"/>')
    out.append(f'<text x="40" y="350" font-family={TW!r} font-size="10" fill="{INK2}">dashed = pinned baseline</text>')
    return ''.join(out)
exhibit('ex-docatlas','A','DocAtlas',['hybrid retrieval over docs','sources shown, answers cited'],bars(),'PROVIDER TESTED' if False else 'SOURCED')
exhibit('ex-docmend','B','DocMend',['finds docs that lag the code','each finding linked to evidence'],diff(),'DRIFT FOUND')
exhibit('ex-modelguard','C','ModelGuard',['candidate vs pinned baseline','regressions flagged per case'],compare(),'REGRESSION')
# ---------------- PAPERS
def evidence(name,venue,lines,doi,d=.3):
    W,H=590,250
    b=[f'<g class="sway">{paper(16,24,W-36,H-44)}',clip(40,8)]
    b.append(f'<text x="70" y="62" class="tw" font-size="12" font-weight="700" letter-spacing="3" fill="{RED}">EVIDENCE · {venue}</text>')
    y=100
    for i,l in enumerate(lines):b.append(f'<text x="40" y="{y}" class="se" font-size="21" font-weight="700" fill="{INK}">{l}</text>');y+=28
    b.append(f'<line x1="40" y1="{H-54}" x2="{W-40}" y2="{H-54}" stroke="{INK2}" stroke-opacity=".4"/>')
    b.append(f'<text x="40" y="{H-32}" class="tw" font-size="13" fill="{INK2}">doi:{doi}  ↗</text>')
    b.append(stamp(W-110,H-78,'PUBLISHED',d+1.2,6,16))
    b.append('</g>')
    save(name,W,H,''.join(b))
evidence('ev-toi','SSRN',['Tool-Observation Integrity in AI Agents:','A Critical Survey of Validation,','Provenance and Execution Assurance'],'10.2139/ssrn.7545819')
evidence('ev-sim','ZENODO',['Simulator Update Frequency Sensitivity','in Driving Scenario Search'],'10.5281/zenodo.23817382')
# ---------------- ADDITIONAL ITEMS (evidence tags)
def tag(name,no,title,line):
    W,H=380,150
    b=[f'<g class="sway"><path d="M40 24 H360 q10 0 10 10 V126 q0 10 -10 10 H40 L14 80 Z" fill="{PAP}" filter="url(#sh)"/><path d="M40 24 H360 q10 0 10 10 V126 q0 10 -10 10 H40 L14 80 Z" fill="{PAP}" filter="url(#grain)"/>',
       f'<circle cx="42" cy="80" r="7" fill="none" stroke="{INK2}" stroke-width="2"/><path d="M35 80 Q 10 40 2 10" fill="none" stroke="{RED}" stroke-width="2"/>',
       f'<text x="66" y="56" class="tw" font-size="11" letter-spacing="2" fill="{RED}">ITEM {no}</text><text x="66" y="90" class="se" font-size="24" font-weight="700" fill="{INK}">{title}</text>',
       f'<text x="66" y="116" class="tw" font-size="12" fill="{INK2}">{line}</text><text x="350" y="56" text-anchor="end" class="tw" font-size="11" fill="{INK2}">↗</text></g>']
    save(name,W,H,''.join(b))
tag('it-glasspdf','03-A','GlassPDF','local PDF tools · OCR')
tag('it-mailayer','03-B','Mailayer','read-only Gmail analysis')
tag('it-drax','03-C','DRAX TBS','textbook RAG · local models')
# ---------------- DETECTIVE BOARD
W,H=1200,430
b=[f'<rect x="0" y="0" width="{W}" height="{H}" rx="10" fill="{CORK}"/><rect width="{W}" height="{H}" rx="10" fill="{CORK}" filter="url(#grain)"/>',
   f'<rect x="4" y="4" width="{W-8}" height="{H-8}" rx="8" fill="none" stroke="#4E341E" stroke-width="8"/>']
notes=[(60,60,'2022','Data Eng. Intern','Phoenix Global',-3),(250,210,'2022–23','Data Analyst','SYMNN · telecom, GIS',2),(440,50,'2025','Data Analyst','Tubman · RAG data',-2),(630,215,'2025–26','Co-Founder','Xodus · tech vetting',3),(820,55,'2026','AI Engineer','Warren and Carter',-2),(1000,200,'NOW','Founder','Teyrin',2)]
pins=[(x+80,y+14) for x,y,*_ in notes]
path='M'+' L'.join(f'{px} {py}' for px,py in pins)
L=sum(math.dist(pins[i],pins[i+1]) for i in range(5))
b.append(f'<path class="ink" style="--l:{L:.0f};animation-delay:{2.6}s;animation-duration:2.2s" d="{path}" fill="none" stroke="{RED}" stroke-width="2.6"/>')
for i,(x,y,yr,role,org,r) in enumerate(notes):
    fill='#F6E27A' if yr=='NOW' else PAP
    b.append(f'<g class="drop" style="animation-delay:{.2+i*.35:.2f}s"><g transform="rotate({r} {x+80} {y+70})">{paper(x,y,160,128,fill,2)}'
             f'<text x="{x+12}" y="{y+40}" class="tw" font-size="12" font-weight="700" fill="{RED}">{yr}</text><text x="{x+12}" y="{y+70}" class="se" font-size="16" font-weight="700" fill="{INK}">{role}</text><text x="{x+12}" y="{y+94}" class="tw" font-size="11" fill="{INK2}">{org}</text></g>'
             f'<circle cx="{x+80}" cy="{y+14}" r="8" fill="{RED}"/><circle cx="{x+77}" cy="{y+11}" r="3" fill="#F2A79F"/></g>')
b.append(f'<g class="drop" style="animation-delay:2.4s"><g transform="rotate(-2 140 380)">{paper(40,350,420,52,PAP2,2)}<text x="56" y="382" class="tw" font-size="13" fill="{INK}">EDU: M.S. Data Science, NJIT · B.Tech CSE, GITAM</text></g></g>')
b.append(f'<text x="1170" y="400" text-anchor="end" class="tw" font-size="13" font-weight="700" fill="#F3EAD3" opacity=".8">data → retrieval → agents</text>')
save('board',W,H,''.join(b))
# ---------------- FIELD KIT
W,H=1200,330
b=[paper(10,14,W-20,H-34,PAP)]
b.append(f'<text x="34" y="52" class="tw" font-size="12" letter-spacing="3" fill="{INK2}">INVENTORY · TOOLS ON PERSON</text>')
x=34
for i,s in enumerate(['Python','SQL','FastAPI','SQLite','Docker','GitHub Actions','React']):
    w=len(s)*9.6+34
    b.append(f'<g class="drop" style="animation-delay:{.2+i*.12:.2f}s"><rect x="{x}" y="70" width="{w:.0f}" height="36" rx="4" fill="none" stroke="{INK}" stroke-width="1.6" stroke-dasharray="5 3"/><text x="{x+17}" y="94" class="tw" font-size="15" font-weight="700" fill="{INK}">{s}</text></g>');x+=w+12
b.append(f'<text x="34" y="150" class="tw" font-size="12" letter-spacing="3" fill="{INK2}">COMMENDATIONS</text>')
for i,(n,l) in enumerate([('2','papers published'),('14','projects built'),('53','certifications'),('1','company founded')]):
    cx=170+i*280
    b.append(f'<g class="stamp" style="--r:{[-6,4,-3,7][i]}deg;animation-delay:{1.4+i*.35:.2f}s" filter="url(#rough)"><circle cx="{cx}" cy="208" r="52" fill="none" stroke="{RED}" stroke-width="3.5"/><circle cx="{cx}" cy="208" r="44" fill="none" stroke="{RED}" stroke-width="1.2"/>'
             f'<text x="{cx}" y="216" text-anchor="middle" class="se" font-size="34" font-weight="700" fill="{RED}">{n}</text></g>'
             f'<text x="{cx}" y="290" text-anchor="middle" class="tw" font-size="14" font-weight="700" fill="{INK}">{l}</text>')
save('kit',W,H,''.join(b))
print('all ok')
