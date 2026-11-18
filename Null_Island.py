install folium 
import folium
import os

# ==========================================================
# CREATE MAP
# ==========================================================

m = folium.Map(
    location=[0, 0],
    zoom_start=7,
    control_scale=True,
    tiles=None
)

# ==========================================================
# ESRI TREASURE CHART BASEMAP
# ==========================================================

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Treasure Chart"
).add_to(m)

# ==========================================================
# TREASURE SEARCH AREA
# ==========================================================

folium.Circle(
    location=[0, 0],
    radius=300000,
    color="#8B0000",
    weight=6,
    dash_array="12",
    fill=True,
    fill_color="#FFD700",
    fill_opacity=0.18,
    tooltip="Treasure Search Area"
).add_to(m)

# ==========================================================
# TREASURE SEARCH AREA LABEL
# ==========================================================

folium.Marker(
    [0, 0],

    icon=folium.DivIcon(
        html="""
        <div

        onmouseover="
        document.getElementById('info-board').innerHTML=
        '<b>🟡 TREASURE SEARCH AREA</b><hr>The area believed to contain the legendary treasure hidden beneath Null Island.';
        "

        style="
            width:220px;
            height:220px;
        ">

        </div>
        """
    )

).add_to(m)

# ==========================================================
# TREASURE ROUTE
# ==========================================================

folium.PolyLine(
    [
        [0.8, -2.5],
        [0.65, -1.8],
        [0.4, -0.8],
        [0, 0]
    ],
    color="#8B4513",
    weight=4,
    dash_array="10,10",
    tooltip="Treasure Route"
).add_to(m)

# ==========================================================
# X MARKS THE SPOT
# ==========================================================

folium.Marker(
    location=[0, 0],

    icon=folium.DivIcon(
        html="""
        <div

        onmouseover="
        document.getElementById('info-board').innerHTML=
        '<b>❌ NULL ISLAND</b><hr>The Isle of Null lies at 0°N, 0°E.<br><br>Countless lost GIS datasets have washed ashore here after their coordinates were forgotten.<br><br>The treasure lies beneath the X... or does it?';
        "

        onmouseout="
        document.getElementById('info-board').innerHTML=
        '<b>🟡 TREASURE SEARCH AREA</b><hr>The area believed to contain the legendary treasure hidden beneath Null Island.';
        "

        style="
            width:90px;
            height:90px;

            cursor:pointer;

            filter:
                drop-shadow(2px 2px 3px rgba(0,0,0,0.30));

            transform:
                translate(-50%,-50%)
                rotate(-11deg);

            animation:pulse 2.5s infinite;
        "

        >

        <svg width="90" height="90">

            <!-- Main Brush Strokes -->

            <path
                d="M10 22 L28 30 L48 55 L80 74"
                stroke="#c1121f"
                stroke-width="13"
                stroke-linecap="round"
                fill="none"
            />

            <path
                d="M82 18 L64 34 L40 55 L14 76"
                stroke="#c1121f"
                stroke-width="16"
                stroke-linecap="round"
                fill="none"
            />

            <!-- Paint Highlights -->

            <path
                d="M14 22 L30 32 L46 54 L76 70"
                stroke="#ff4444"
                stroke-width="5"
                stroke-linecap="round"
                fill="none"
                opacity="0.7"
            />

            <path
                d="M78 20 L60 35 L38 54 L18 72"
                stroke="#ff4444"
                stroke-width="6"
                stroke-linecap="round"
                fill="none"
                opacity="0.7"
            />

            <!-- Paint Splatters -->

            <circle cx="18" cy="18" r="2" fill="#b22222"/>
            <circle cx="71" cy="16" r="1.8" fill="#b22222"/>
            <circle cx="23" cy="72" r="2.3" fill="#b22222"/>
            <circle cx="74" cy="68" r="1.4" fill="#b22222"/>

        </svg>

        </div>
        """
    )

).add_to(m)

# ==========================================================
# PIRATE SHIP
# ==========================================================

folium.Marker(
    [0.7, -2],

    icon=folium.DivIcon(
        html="""
        <img

        src="pirate_ship.png"

        onmouseover="
        document.getElementById('info-board').innerHTML=
        '<b>⛵ THE BLACK GEOCODER</b><hr>A notorious pirate vessel sailing the Gulf of Guinea in search of the lost treasure of Null Island.';
        "

        onmouseout="
        document.getElementById('info-board').innerHTML=
        '<b>📜 Captain\\'s Information Board</b><hr>Hover over a feature...';
        "

        style="
            width:170px;

            opacity:0.9;

            filter:
                sepia(40%)
                contrast(110%);

            transform:
                translate(-50%,-50%)
                rotate(-12deg);

            cursor:pointer;
        ">

        """
    )

).add_to(m)

# ==========================================================
# KRAKEN
# ==========================================================

folium.Marker(
    [2, -5],

    icon=folium.DivIcon(
        html="""
        <img

        src="kraken.png"

        onmouseover="
        document.getElementById('info-board').innerHTML=
        '<b>🐙 KRAKEN TERRITORY</b><hr>Ancient sailors warned of a great beast inhabiting these waters.<br><br>Many GIS datasets were never seen again.';
        "

        onmouseout="
        document.getElementById('info-board').innerHTML=
        '<b>📜 Captain\\'s Information Board</b><hr>Hover over a feature...';
        "

        style="
            width:180px;

            opacity:0.8;

            filter:
                sepia(60%)
                contrast(115%);

            transform:
                translate(-50%,-50%)
                rotate(-12deg);

            cursor:pointer;
        ">
        """
    )

).add_to(m)

# ==========================================================
# MAP BORDER
# ==========================================================

border_html = """
<div style="
position:fixed;
top:8px;
left:8px;
right:8px;
bottom:8px;

border:10px solid rgba(139,90,43,0.35);

pointer-events:none;

z-index:998;
">
</div>
"""

m.get_root().html.add_child(
    folium.Element(border_html)
)

# ==========================================================
# MARINER'S WARNING 
# ==========================================================

warning_html = """
<div style="
position:fixed;

bottom:180px;
left:80px;

width:260px;

background:#e8d0a9;

padding:12px;

border:3px solid #8b5a2b;

border-radius:4px;

font-family:'Palatino Linotype', 'Book Antiqua', serif;
font-style:italic;
font-size:16px;

color:#4b2e05;

transform:rotate(-8deg);

box-shadow:4px 4px 8px rgba(0,0,0,.25);

pointer-events:none;

z-index:999;
">

⚠️ MARINER'S WARNING

<hr>

Reports tell of a great beast
lurking southwest of Null Island.

Many GIS datasets are said to have been
dragged beneath the waves here.

Proceed at your own peril.

</div>
"""

m.get_root().html.add_child(
    folium.Element(warning_html)
)

# ==========================================================
# TITLE
# ==========================================================

title_html = """
<div style="
position:fixed;
top:15px;
left:50%;
transform:translateX(-50%) rotate(-2deg);
z-index:9999;

background:#e8d0a9;

padding:18px 40px;

border:5px solid #8b5a2b;
border-radius:10px;

font-family:'Trebuchet MS', cursive;
font-size:32px;
font-weight:bold;

color:#4b2e05;

box-shadow:5px 5px 15px rgba(0,0,0,0.4);
">

☠️ THE LOST TREASURE OF NULL ISLAND ☠️

</div>
"""

m.get_root().html.add_child(folium.Element(title_html))

# ==========================================================
# SUBTITLE
# ==========================================================

subtitle_html = """
<div style="
position:fixed;
top:130px;
left:50%;
transform:translateX(-50%) rotate(1deg);

z-index:9998;

background:#f6ead1;

padding:10px 18px;

border:2px solid #8b5a2b;
border-radius:4px;

font-family:Georgia, serif;

box-shadow:3px 3px 8px rgba(0,0,0,.2);
">

X MARKS THE SPOT • 0°N • 0°E

</div>
"""

m.get_root().html.add_child(folium.Element(subtitle_html))


# ==========================================================
# COMPASS ROSE IMAGE
# ==========================================================

compass_html = """
<div style="
position:fixed;
top:15px;
right:20px;

z-index:9999;

pointer-events:none;

transform:rotate(-5deg);
">

<img src="compass_rose_transparent.png"
     style="
     width:170px;

     filter:
         drop-shadow(8px 8px 12px rgba(0,0,0,0.45));

     opacity:0.95;
     ">

</div>
"""

m.get_root().html.add_child(
    folium.Element(compass_html)
)

# ==========================================================
# INFORMATION BOARD
# ==========================================================

info_html = """
<div id="info-board" style="
position:fixed;

top:20px;
left:20px;

width:260px;

background:#f6ead1;

padding:12px;

border:4px solid #8b5a2b;
border-radius:8px;

font-family:Georgia, serif;

font-size:16px;
font-weight:bold;

color:#4b2e05;

text-align:center;

box-shadow:4px 4px 10px rgba(0,0,0,.3);

z-index:9999;
">

📜 Captain's Information Board

<hr>

Hover over a feature...

</div>
"""

m.get_root().html.add_child(
    folium.Element(info_html)
)

# ==========================================================
# CAPTAIN'S KEY
# ==========================================================

legend_html = """
<div style="
position:fixed;
bottom:25px;
right:25px;

width:320px;

background:#f6ead1;

padding:15px;

border:4px solid #8b5a2b;
border-radius:10px;

font-family:Georgia, serif;

box-shadow:5px 5px 12px rgba(0,0,0,.3);

z-index:9999;

transform:rotate(-2deg);
">

<b style="
font-size:18px;
color:#4b2e05;
">
📜 Captain's Key
</b>

<hr style="
border:1px dashed #8b5a2b;
">

<div style="
line-height:1.8;
color:#4b2e05;
">

<span style="
display:inline-block;
vertical-align:middle;
margin-right:6px;
">

<svg width="18" height="18">

    <path
        d="M3 4 L16 16"
        stroke="#6b4423"
        stroke-width="3"
        stroke-linecap="round"
        fill="none"
    />

    <path
        d="M16 4 L4 16"
        stroke="#6b4423"
        stroke-width="3"
        stroke-linecap="round"
        fill="none"
    />

</svg>

</span>

Null Island Treasure

<br>

<span style="
font-size:14px;
filter:grayscale(100%);
">
⛵
</span>
&nbsp; The Black Geocoder

<br>

<span style="
font-size:14px;
filter:grayscale(100%);
">
🐙
</span>
&nbsp; Kraken Territory

<br>

<div style="
display:flex;
align-items:center;
margin-top:6px;
">

<div style="
width:22px;
height:22px;
border:3px dashed #4A2C17;
border-radius:50%;
margin-right:8px;
box-sizing:border-box;
">
</div>

Treasure Search Area

</div>

<div style="
display:flex;
align-items:center;
margin-top:8px;
">

<span style="
display:inline-block;
width:25px;
border-top:3px dashed #A66A3F;
margin-right:8px;
">
</span>

Treasure Route

</div>

</div>

<br>

<div style="
font-style:italic;
font-size:16px;
color:#6b4c24;
">

Beware ye traveller...

Many a misplaced coordinate
has met its fate in these waters.

</div>

</div>
"""

m.get_root().html.add_child(
    folium.Element(legend_html)
)

# ==========================================================
# PARCHMENT EFFECT & ANIMATION
# ==========================================================

style_block = """
<style>

.leaflet-container{
    filter:
        sepia(65%)
        saturate(80%)
        contrast(90%)
        brightness(110%);
}

@keyframes drift1{
    0%{transform:translateX(-30px);}
    50%{transform:translateX(30px);}
    100%{transform:translateX(-30px);}
}

@keyframes drift2{
    0%{transform:translateX(30px);}
    50%{transform:translateX(-30px);}
    100%{transform:translateX(30px);}
}

@keyframes bob{
    0%{transform:translateY(0);}
    50%{transform:translateY(-8px);}
    100%{transform:translateY(0);}
}

@keyframes pulse{
    0%{transform:translate(-50%,-50%) scale(1);}
    50%{transform:translate(-50%,-50%) scale(1.12);}
    100%{transform:translate(-50%,-50%) scale(1);}
}

</style>
"""

m.get_root().header.add_child(
    folium.Element(style_block)
)
# ==========================================================
# CUSTOM STYLING
# ==========================================================

style_block = """
<style>

.leaflet-control-scale {
    margin-bottom: 30px !important;

    margin-left: 30px !important;

    background: #f6ead1 !important;

    border: 2px solid #8b5a2b !important;

    border-radius: 4px !important;

    padding: 3px !important;

    box-shadow: 3px 3px 6px rgba(0,0,0,.25);

    transform: rotate(-1deg);
}

.leaflet-control-scale-line {

    font-family: Georgia, serif !important;

    color: #4b2e05 !important;

    border-color: #8b5a2b !important;

    background: rgba(246,234,209,0.85) !important;
}

</style>
"""

m.get_root().header.add_child(
    folium.Element(style_block)
)

# ==========================================================
# PIRATE SCALE LABEL
# ==========================================================

pirate_scale_label = """
<div style="
position:fixed;

bottom:90px;
left:30px;

background:#f6ead1;

padding:6px 10px;

border:2px solid #8b5a2b;

font-family:Georgia, serif;

font-size:13px;

color:#4b2e05;

z-index:9999;

transform:rotate(-2deg);

box-shadow:3px 3px 6px rgba(0,0,0,.2);
">

⚓ Sailor's Scale

<br>

<span style="
font-size:11px;
font-style:italic;
">
10 Nautical Miles = 1 Mermaid Pod
</span>

</div>
"""

m.get_root().html.add_child(
    folium.Element(pirate_scale_label)
)

# ==========================================================
# LAYER CONTROL
# ==========================================================

folium.LayerControl().add_to(m)

# ==========================================================
# SAVE MAP
# ==========================================================

output_file = os.path.join(
    os.path.expanduser("~"),
    "Downloads",
    "Pirate_Null_Island_Map.html"
)

m.save(output_file)

# ==========================================================
# OPEN MAP
# ==========================================================

print("Creating map...")
print(output_file)

os.startfile(output_file)

print("🏴‍☠️ Treasure map opened!")