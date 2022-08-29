import random
prompt = '''
photorealistic,
dramatic,
dramatic color,
liquid,
Psychedelic,
anime,
render,
detailed,
super detailed,
hyper detailed,
colorful,
atmosphere,
cinematic,
assasins creed art style,
weta digital,
weta FX,
unreal engine,
by wlop,
by ilya kuvshinov,
by ismail inceoglu,
by cory loftis,
by akihiko yoshida,
by james gilleard,
by atey ghailan,
by makoto shinkai,
by goro fujita,
by peter mohrbacher,
by greg rutkowski,
by artgerm,
by alphonse mucha,
by peter mohrbacher, 
by hajime sorayama, 
by wayne barlowe, 
by boris vallejo, 
by aaron horkey, 
by gaston bussiere, 
by craig mullins,
by agnes lawrence pelton,
by albert bierstadt,
by andy warhol,
by annibale carracci,
by anthony van dyck,
by asaf hanuka,
by ben enwonwu,
by caspar david friedrich,
by charlie bowater,
by david mann,
by edward munch,
by frank frazetta,
by frida kahlo,
by hassan mossoudy,
by hayao miyazaki,
by hazem taham,
by H.R. Giger,
by ismail inceoglu,
by Jeff koons,
by john Constable,
by John Kenn mortense,
by jose tapiro Y baro,
by karol bak,
by Katsushika hokusai,
by Kim Tschng Yeul,
by Ko Young Hoon,
by Lee Man Fong,
by Lemma Guya,
by Lisa Frank,
by Ralph Steadman,
by Richard dadd,
by Tony Diterlizzi
by Victto Ngai,
by Wanda Gag,
by Zeng Fanzhi,
art by peter mohrbacher, 
art by ilya kuvshinov,
art by hajime sorayama, 
art by wayne barlowe, 
art by boris vallejo, 
art by aaron horkey, 
art by gaston bussiere, 
art by craig mullins,
art by wlop,
art by ismail inceoglu,
art by cory loftis,
art by akihiko yoshida,
art by james gilleard,
art by atey ghailan,
art by makoto shinkai,
art by goro fujita,
art by peter mohrbacher,
art by greg rutkowski,
art by artgerm,
art by alphonse mucha,
art by agnes lawrence pelton,
art by albert bierstadt,
art by andy warhol,
art by annibale carracci,
art by anthony van dyck,
art by asaf hanuka,
art by ben enwonwu,
art by caspar david friedrich,
art by charlie bowater,
art by david mann,
art by edward munch,
art by frank frazetta,
art by frida kahlo,
art by hassan mossoudy,
art by hayao miyazaki,
art by hazem taham,
art by H.R. Giger,
art by ismail inceoglu,
art by Jeff koons,
art by john Constable,
art by John Kenn mortense,
art by jose tapiro Y baro,
art by karol bak,
art by Katsushika hokusai,
art by Kim Tschng Yeul,
art by Ko Young Hoon,
art by Lee Man Fong,
art by Lemma Guya,
art by Lisa Frank,
art by Ralph Steadman,
art by Richard dadd,
art by Tony Diterlizzi
art by Victto Ngai,
art by Wanda Gag,
art by Zeng Fanzhi,
Chromatic aberration,
rgb dsplacement,
wavy,
whirl,
morph,
spiraling,
twisted rays,
starburst,
emboss,
blobby,
blobs,
erode,
dilate,
tornadic,
RTX,
FXAA,
TXAA,
SSAO,
shaders,
post processing,
GLSL shaders,
OpenGL shaders,
SFX,
CGI,
SFX,
cel shading,
glitch art,
glitchy,
Space art,
abstract art,
space,
galaxy,
smoke, 
dark fantasy,
fantasy,
intricate,
ivy, 
flowers,
epic,
stylized,
sketch,
bold sketch,
character design,
ice gate,
central composition,
baroque, art nouveau,
epic sky, 
cinematic light,
hanging vines,
post-apocalypse,
magical,
volumetric fog,
black background,
shadow,
soft shadow,
concept art,
design concept art,
cyberpunk art,
steampunk blueprint,
volumetric,
volumetric lighting,
goddess of illusion,
stunning, 
breathtaking, 
mirrors, 
glass, 
magic circle,
unreal engine,
unreal engine 5,
octane render,
vray render,
arnold render,
houdini,
terragen,
soft painting,
clear focus,
vfx,
8k,
4k,
16k,
cosy atmosphere, 
ambient blue lights, 
candles, 
fireplace,
32k,
RGB,
CMYK,
VGA,
EGA,
CGA,
HSL,
HCL,
sRGB,
YCbCr,
YPbPr,
scRGB,
Coloroid,
pantone,
8-bit,
12-bit,
pixelart,
#pixelart,
16-bit,
AR,
VR,
point,
dot,
line,
curve,
triangle,
hexagon,
opctagon,
nonagon,
decagon,
heart,
cube,
hypercube,
klein bottle,
monogon, 
digon,
edge,
vertex,
surface,
convex,
interior,
concave,
cyclic,
tangential,
quasi,
quasi regular,
isotaxal,
essence,
divine,
ineffable,
strong,
powerful,
weak,
thin,
massive,
thick,
Huge,
large,
big,
micro,
nano,
flexible,
neoteric,
paradox,
feng shui,
array,
OCD,
Decimal,
Octal,
nonary,
senary,
binary,
megapixel,
realistic,
super realistic,
hyper realistic,
ufotable art style,
ghibli art style,
mappa art style,
global illumination,
pixiv,
artstation,
trending on pixiv,
tranding on artstation,
ray tracing,
god rays,
drawing,
illustration,
doodle,
dot art,
line art,
stipple,
hand-drawn,
crosshatch,
storybook illustration,
graphic novel,
cartographic,
pencil,
graphite,
colored pencil,
charcoal art,
ink,
ballpoint pen,
gel pen,
fountain pen,
calligraphy,
marker art,
dry-erase marker,
wet-erase marker,
pastels and chalk,
paint,
still-life,
canvas,
fine art,
color field painting,
hard edge painting,
scroll painting,
hydro-dipping,
hydrodipped,
easter egg,
street art,
rock art,
artwork,
chinise painting,
watercolor,
acrylic paint,
oil paint,
wet paint,
splatter paint,
glass paint,
coffee paint,
text,
typeface,
says,
says hello,
letters,
words,
lexemes,
written words,
print,
modern art,
digital art,
logo,
postage stamp,
bussiness card,
collage,
photocollage,
magazine,
newspaper,
blueprint,
comic book,
barcode,
poster,
origami,
mosaic,
frame,
decal,
banner,
carving,
etching,
modeling,
glaze,
overglaze,
inglaze,
light,
light art,
light painting,
lightpainting,
resin,
smoke art,
tattoo,
maze,
toy,
public art,
diorama,
hedge trimming,
shoe,
negative space,
scrapbooking,
mixed media,
flottage,
soviet art,
glitter,
scenes,
bokeh,
color grading,
dashcam-footage,
filmic,
film grain,
glamor shot,
golden hour,
time-lapse,
film types,
night vision,
dslr,
35mm,
tri-X 400 TX,
instax,
lomo,
kodak ektar,
macro,
macro view,
telephoto,
microscopic,
electron microscope,
super-resolution microscopy,
wide angel,
panorama,
360 panorama,
360 angle,
fisheye lens,
side-view,
fisheye lens effect,
first person,
third person,
zoom,
isometric,
blur,
blurry,
lens distortion,
exposure,
white balance,
gamma,
contrast,
lens flare,
vignette,
split toning,
warm color palette,
cool color palette,
spectral color,
inverted colors,
chroma,
saturated,
neon,
electric colors,
tonal colors,
complimentary colors,
dark,
dark mode,
polychromatic colors,
light blue,
light blue background,
agfacolor,
2D,
3D,
4D,
5D,
overdimensional,
underdimensional,
hyperdimensional,
subdimensional,
omnidimensional,
extradimensional,
multiverse,
rossdraws global illumination,
anime key visual,
action shot,
young girl,
fanbox,
moody lighting,
lord of the rings,
sharp contrast,
light nover,
light nover cover,
Korean light novel,
Japenese light novel,
Korean light novel cover,
Japenese light novel cover,
game,
visual novel,
full body,
full hd,
dream word,
landscape,
beautiful landscape,
realistic landscape,
photorealistic landscape,
photorealistic dramatic,
photorealistic dramatic anime,
photorealistic dramatic anime boy,
photorealistic dramatic anime girl,
photorealistic dramatic liquid anime girl,
photorealistic dramatic liquid anime boy,
horror,
creepy,
scary,
detailed face,
detailed body,
horror art,
scary art,
creepe art,
funny art,
scary art,
ugly art,
block cities,
Funky pop, 
wearing in punk outfit,
Flat Design Vector Illustrations,
Vector Illustrations,
Flat Design,
RPG Item Icons,
Item Icons,
3D Anime Avatar,
round cute face,
horizon zero dawn,
pubg,
minecraft,
player unknown battleground,
call of duty,
battle field,
world war,
world war 2,
world war 3,
counter strike,
Everlasting summer,
Fate/Stay night,
hdr,
fanart,
artworks,
other dimention,
digital painting,
smooth,
radiant light,
spotlight,
frontlight,
rimlight,
backlight,
strobe,
mud, 
scandinavian mythology,
bright,
crepuscular rays,
rays of shimmering light,
sunlight,
incandescent,
plasma,
tesla coil,
electric arc,
flare,
infrared,
UV,
LED,
AMOLED,
OLED,
Moody lighting,
cinematic lighting,
studio lighting,
soft lighting,
hard lighting,
volumetric lighting,
volumetric,
split lighting,
beautiful lighting,
halogen,
gold,
silver,
rose,
ethereal,
diamond,
biomechanical,
microbes,
Anime Avatar, 
Animal T-Shirt Design,
T-Shirt Design,
Nature Landscape Backgrounds - Winter,
Nature Landscape Backgrounds,
Comic Book Characters,
Birthday Card Mockups,
Card Mockups,
Sci-Fi,
Sci-Fi Zoom Backgrounds,
Animal Crossing Characters,
Anime / Manga,
Retro Psychedelic Posters,
Techno Marble,
Synth,
Synthwave art,
Your Name anime art style,
Nature Sunsets,
Sunsets,
Synthwave,
'''.splitlines()
vocab = len(prompt)
generated = []
num_word = 13
while len(sorted(set(generated), key=lambda d: generated.index(d))) < num_word:
	rand = random.randint(0, vocab)
	generated.append(prompt[rand])
print(' '.join(sorted(set(generated), key=lambda d: generated.index(d))))