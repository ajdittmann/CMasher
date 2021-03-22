# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = 'diverging'

# RGB-values of this colormap
cm_data = [[0.57869284, 0.94700453, 0.95383509],
           [0.57330096, 0.94244813, 0.95218584],
           [0.56790414, 0.93790619, 0.95055025],
           [0.56250183, 0.93337844, 0.94892950],
           [0.55709400, 0.92886470, 0.94732325],
           [0.55168026, 0.92436472, 0.94573223],
           [0.54626041, 0.91987829, 0.94415663],
           [0.54083428, 0.91540519, 0.94259649],
           [0.53540142, 0.91094515, 0.94105277],
           [0.52996183, 0.90649797, 0.93952504],
           [0.52451517, 0.90206341, 0.93801392],
           [0.51906115, 0.89764122, 0.93651980],
           [0.51359971, 0.89323118, 0.93504255],
           [0.50813051, 0.88883304, 0.93358271],
           [0.50265329, 0.88444654, 0.93214066],
           [0.49716797, 0.88007146, 0.93071625],
           [0.49167433, 0.87570754, 0.92930975],
           [0.48617195, 0.87135452, 0.92792190],
           [0.48066080, 0.86701216, 0.92655247],
           [0.47514069, 0.86268020, 0.92520162],
           [0.46961139, 0.85835838, 0.92386959],
           [0.46407266, 0.85404645, 0.92255672],
           [0.45852424, 0.84974413, 0.92126329],
           [0.45296603, 0.84545117, 0.91998924],
           [0.44739784, 0.84116729, 0.91873474],
           [0.44181946, 0.83689223, 0.91749997],
           [0.43623070, 0.83262572, 0.91628509],
           [0.43063137, 0.82836747, 0.91509023],
           [0.42502129, 0.82411721, 0.91391555],
           [0.41940026, 0.81987466, 0.91276117],
           [0.41376812, 0.81563953, 0.91162721],
           [0.40812469, 0.81141153, 0.91051377],
           [0.40246980, 0.80719037, 0.90942095],
           [0.39680330, 0.80297576, 0.90834883],
           [0.39112505, 0.79876739, 0.90729746],
           [0.38543488, 0.79456497, 0.90626692],
           [0.37973269, 0.79036819, 0.90525724],
           [0.37401834, 0.78617674, 0.90426845],
           [0.36829174, 0.78199032, 0.90330056],
           [0.36255279, 0.77780859, 0.90235356],
           [0.35680142, 0.77363124, 0.90142744],
           [0.35103745, 0.76945793, 0.90052248],
           [0.34526089, 0.76528834, 0.89963852],
           [0.33947179, 0.76112213, 0.89877532],
           [0.33367017, 0.75695898, 0.89793279],
           [0.32785588, 0.75279849, 0.89711137],
           [0.32202912, 0.74864036, 0.89631060],
           [0.31619008, 0.74448422, 0.89553017],
           [0.31033866, 0.74032967, 0.89477063],
           [0.30447528, 0.73617639, 0.89403125],
           [0.29860011, 0.73202399, 0.89331209],
           [0.29271343, 0.72787206, 0.89261309],
           [0.28681572, 0.72372025, 0.89193378],
           [0.28090735, 0.71956814, 0.89127427],
           [0.27498896, 0.71541533, 0.89063408],
           [0.26906124, 0.71126143, 0.89001292],
           [0.26312486, 0.70710597, 0.88941086],
           [0.25718092, 0.70294859, 0.88882703],
           [0.25123043, 0.69878883, 0.88826140],
           [0.24527462, 0.69462621, 0.88771373],
           [0.23931508, 0.69046034, 0.88718322],
           [0.23335351, 0.68629075, 0.88666946],
           [0.22739188, 0.68211696, 0.88617198],
           [0.22143248, 0.67793848, 0.88569042],
           [0.21547800, 0.67375483, 0.88522406],
           [0.20953152, 0.66956553, 0.88477214],
           [0.20359659, 0.66537008, 0.88433394],
           [0.19767730, 0.66116797, 0.88390868],
           [0.19177835, 0.65695868, 0.88349548],
           [0.18590517, 0.65274164, 0.88309369],
           [0.18006401, 0.64851634, 0.88270206],
           [0.17426203, 0.64428224, 0.88231942],
           [0.16850747, 0.64003882, 0.88194450],
           [0.16280986, 0.63578543, 0.88157637],
           [0.15718007, 0.63152155, 0.88121346],
           [0.15163047, 0.62724665, 0.88085394],
           [0.14617558, 0.62296002, 0.88049685],
           [0.14083138, 0.61866121, 0.88013964],
           [0.13561664, 0.61434953, 0.87978090],
           [0.13055227, 0.61002443, 0.87941833],
           [0.12566179, 0.60568534, 0.87904945],
           [0.12097171, 0.60133167, 0.87867186],
           [0.11651156, 0.59696278, 0.87828307],
           [0.11231340, 0.59257814, 0.87787994],
           [0.10841196, 0.58817719, 0.87745920],
           [0.10484430, 0.58375940, 0.87701740],
           [0.10164914, 0.57932420, 0.87655087],
           [0.09886510, 0.57487117, 0.87605525],
           [0.09652994, 0.57039990, 0.87552588],
           [0.09468006, 0.56590987, 0.87495827],
           [0.09334588, 0.56140087, 0.87434666],
           [0.09255347, 0.55687251, 0.87368561],
           [0.09231938, 0.55232472, 0.87296842],
           [0.09265244, 0.54775739, 0.87218838],
           [0.09355187, 0.54317052, 0.87133816],
           [0.09500670, 0.53856430, 0.87040963],
           [0.09699741, 0.53393908, 0.86939415],
           [0.09949602, 0.52929541, 0.86828228],
           [0.10246810, 0.52463411, 0.86706387],
           [0.10587541, 0.51995613, 0.86572833],
           [0.10967576, 0.51526281, 0.86426419],
           [0.11382580, 0.51055574, 0.86265950],
           [0.11828050, 0.50583694, 0.86090155],
           [0.12299581, 0.50110877, 0.85897736],
           [0.12792818, 0.49637399, 0.85687361],
           [0.13303495, 0.49163581, 0.85457687],
           [0.13827461, 0.48689788, 0.85207389],
           [0.14360717, 0.48216423, 0.84935190],
           [0.14899424, 0.47743927, 0.84639902],
           [0.15439799, 0.47272781, 0.84320453],
           [0.15978344, 0.46803477, 0.83975943],
           [0.16511635, 0.46336535, 0.83605671],
           [0.17036521, 0.45872465, 0.83209177],
           [0.17550082, 0.45411767, 0.82786267],
           [0.18049667, 0.44954915, 0.82337025],
           [0.18532943, 0.44502339, 0.81861819],
           [0.18997899, 0.44054421, 0.81361291],
           [0.19442908, 0.43611475, 0.80836325],
           [0.19866639, 0.43173758, 0.80288030],
           [0.20268189, 0.42741446, 0.79717672],
           [0.20646873, 0.42314661, 0.79126674],
           [0.21002416, 0.41893452, 0.78516513],
           [0.21334744, 0.41477813, 0.77888727],
           [0.21644007, 0.41067692, 0.77244864],
           [0.21930549, 0.40662992, 0.76586449],
           [0.22194871, 0.40263581, 0.75914954],
           [0.22437598, 0.39869301, 0.75231781],
           [0.22659392, 0.39479978, 0.74538284],
           [0.22861020, 0.39095420, 0.73835702],
           [0.23043243, 0.38715428, 0.73125216],
           [0.23206893, 0.38339797, 0.72407881],
           [0.23352752, 0.37968323, 0.71684701],
           [0.23481608, 0.37600805, 0.70956590],
           [0.23594240, 0.37237043, 0.70224378],
           [0.23691411, 0.36876841, 0.69488810],
           [0.23773864, 0.36520013, 0.68750558],
           [0.23842228, 0.36166379, 0.68010314],
           [0.23897259, 0.35815764, 0.67268550],
           [0.23939501, 0.35468004, 0.66525875],
           [0.23969623, 0.35122941, 0.65782678],
           [0.23988177, 0.34780424, 0.65039394],
           [0.23995694, 0.34440312, 0.64296415],
           [0.23992678, 0.34102470, 0.63554088],
           [0.23979609, 0.33766769, 0.62812723],
           [0.23956944, 0.33433088, 0.62072594],
           [0.23925118, 0.33101313, 0.61333943],
           [0.23884542, 0.32771334, 0.60596984],
           [0.23835581, 0.32443050, 0.59861944],
           [0.23778580, 0.32116362, 0.59129023],
           [0.23713919, 0.31791178, 0.58398324],
           [0.23641859, 0.31467410, 0.57670083],
           [0.23562751, 0.31144977, 0.56944356],
           [0.23476863, 0.30823799, 0.56221282],
           [0.23384436, 0.30503801, 0.55501014],
           [0.23285756, 0.30184913, 0.54783592],
           [0.23181055, 0.29867067, 0.54069108],
           [0.23070554, 0.29550198, 0.53357645],
           [0.22954464, 0.29234247, 0.52649273],
           [0.22832987, 0.28919153, 0.51944051],
           [0.22706312, 0.28604862, 0.51242029],
           [0.22574622, 0.28291320, 0.50543250],
           [0.22438088, 0.27978477, 0.49847747],
           [0.22296875, 0.27666284, 0.49155548],
           [0.22151140, 0.27354694, 0.48466672],
           [0.22001024, 0.27043662, 0.47781146],
           [0.21846644, 0.26733144, 0.47099036],
           [0.21688162, 0.26423100, 0.46420287],
           [0.21525699, 0.26113489, 0.45744915],
           [0.21359342, 0.25804272, 0.45072991],
           [0.21189245, 0.25495414, 0.44404423],
           [0.21015473, 0.25186874, 0.43739306],
           [0.20838166, 0.24878622, 0.43077545],
           [0.20657379, 0.24570619, 0.42419227],
           [0.20473243, 0.24262836, 0.41764250],
           [0.20285807, 0.23955237, 0.41112692],
           [0.20095176, 0.23647793, 0.40464482],
           [0.19901430, 0.23340473, 0.39819596],
           [0.19704615, 0.23033243, 0.39178094],
           [0.19504823, 0.22726077, 0.38539893],
           [0.19302121, 0.22418944, 0.37904975],
           [0.19096568, 0.22111817, 0.37273324],
           [0.18888207, 0.21804663, 0.36644962],
           [0.18677107, 0.21497457, 0.36019827],
           [0.18463321, 0.21190170, 0.35397893],
           [0.18246898, 0.20882775, 0.34779136],
           [0.18027883, 0.20575244, 0.34163532],
           [0.17806319, 0.20267549, 0.33551054],
           [0.17582247, 0.19959662, 0.32941673],
           [0.17355705, 0.19651555, 0.32335359],
           [0.17126727, 0.19343202, 0.31732082],
           [0.16895348, 0.19034573, 0.31131809],
           [0.16661598, 0.18725641, 0.30534506],
           [0.16425505, 0.18416377, 0.29940139],
           [0.16187095, 0.18106754, 0.29348671],
           [0.15946392, 0.17796741, 0.28760066],
           [0.15703418, 0.17486310, 0.28174285],
           [0.15458188, 0.17175430, 0.27591300],
           [0.15210713, 0.16864071, 0.27011088],
           [0.14961017, 0.16552201, 0.26433584],
           [0.14709112, 0.16239789, 0.25858744],
           [0.14455007, 0.15926804, 0.25286525],
           [0.14198701, 0.15613210, 0.24716916],
           [0.13940203, 0.15298974, 0.24149861],
           [0.13679522, 0.14984061, 0.23585293],
           [0.13416654, 0.14668436, 0.23023175],
           [0.13151588, 0.14352057, 0.22463501],
           [0.12884334, 0.14034890, 0.21906169],
           [0.12614878, 0.13716893, 0.21351147],
           [0.12343203, 0.13398023, 0.20798415],
           [0.12069311, 0.13078240, 0.20247868],
           [0.11793173, 0.12757495, 0.19699505],
           [0.11514778, 0.12435745, 0.19153238],
           [0.11234104, 0.12112938, 0.18609015],
           [0.10951121, 0.11789024, 0.18066797],
           [0.10665810, 0.11463950, 0.17526489],
           [0.10378128, 0.11137658, 0.16988075],
           [0.10088052, 0.10810090, 0.16451437],
           [0.09795529, 0.10481182, 0.15916562],
           [0.09500529, 0.10150871, 0.15383328],
           [0.09202991, 0.09819083, 0.14851704],
           [0.08902871, 0.09485748, 0.14321584],
           [0.08600106, 0.09150787, 0.13792899],
           [0.08294630, 0.08814114, 0.13265572],
           [0.07986379, 0.08475645, 0.12739482],
           [0.07675264, 0.08135279, 0.12214593],
           [0.07361211, 0.07792919, 0.11690747],
           [0.07044121, 0.07448455, 0.11167864],
           [0.06723890, 0.07101767, 0.10645840],
           [0.06400410, 0.06752732, 0.10124526],
           [0.06073553, 0.06401210, 0.09603817],
           [0.05743181, 0.06047052, 0.09083573],
           [0.05409148, 0.05690097, 0.08563621],
           [0.05071284, 0.05330166, 0.08043811],
           [0.04729398, 0.04967062, 0.07523980],
           [0.04383290, 0.04600573, 0.07003905],
           [0.04032533, 0.04230459, 0.06483370],
           [0.03681198, 0.03855880, 0.05962158],
           [0.03343838, 0.03492349, 0.05439990],
           [0.03020655, 0.03145663, 0.04916556],
           [0.02711859, 0.02815891, 0.04391515],
           [0.02417669, 0.02503115, 0.03863829],
           [0.02138315, 0.02207428, 0.03360127],
           [0.01874050, 0.01928945, 0.02894484],
           [0.01625140, 0.01667799, 0.02466102],
           [0.01391875, 0.01424146, 0.02074208],
           [0.01174570, 0.01198170, 0.01718058],
           [0.00973575, 0.00990088, 0.01396944],
           [0.00789285, 0.00800160, 0.01110189],
           [0.00622148, 0.00628698, 0.00857157],
           [0.00472684, 0.00476083, 0.00637274],
           [0.00341513, 0.00342790, 0.00450037],
           [0.00229394, 0.00229426, 0.00295046],
           [0.00137302, 0.00136800, 0.00172056],
           [0.00066576, 0.00066063, 0.00081098],
           [0.00019292, 0.00019060, 0.00022793],
           [0.00000000, 0.00000000, 0.00000000],
           [0.00025040, 0.00017502, 0.00016171],
           [0.00089250, 0.00059932, 0.00054846],
           [0.00189565, 0.00122701, 0.00111293],
           [0.00325248, 0.00203616, 0.00183195],
           [0.00496152, 0.00301225, 0.00268996],
           [0.00702387, 0.00414441, 0.00367535],
           [0.00944207, 0.00542401, 0.00477886],
           [0.01221955, 0.00684390, 0.00599285],
           [0.01536031, 0.00839795, 0.00731084],
           [0.01886877, 0.01008083, 0.00872721],
           [0.02274967, 0.01188778, 0.01023700],
           [0.02700798, 0.01381454, 0.01183582],
           [0.03164888, 0.01585720, 0.01351971],
           [0.03667771, 0.01801217, 0.01528506],
           [0.04205331, 0.02027615, 0.01712860],
           [0.04743448, 0.02264601, 0.01904731],
           [0.05278280, 0.02511884, 0.02103842],
           [0.05810212, 0.02769188, 0.02309935],
           [0.06339578, 0.03036252, 0.02522770],
           [0.06866672, 0.03312824, 0.02742124],
           [0.07391755, 0.03598666, 0.02967787],
           [0.07915058, 0.03893547, 0.03199563],
           [0.08436788, 0.04193076, 0.03437269],
           [0.08957133, 0.04487310, 0.03680730],
           [0.09476262, 0.04777329, 0.03929785],
           [0.09994327, 0.05063312, 0.04180586],
           [0.10511470, 0.05345424, 0.04426624],
           [0.11027818, 0.05623812, 0.04669049],
           [0.11543497, 0.05898610, 0.04908014],
           [0.12058623, 0.06169939, 0.05143664],
           [0.12573283, 0.06437919, 0.05376147],
           [0.13087571, 0.06702659, 0.05605592],
           [0.13601574, 0.06964256, 0.05832121],
           [0.14115372, 0.07222801, 0.06055848],
           [0.14629062, 0.07478363, 0.06276864],
           [0.15142706, 0.07731028, 0.06495279],
           [0.15656359, 0.07980873, 0.06711196],
           [0.16170085, 0.08227966, 0.06924706],
           [0.16683960, 0.08472357, 0.07135883],
           [0.17198044, 0.08714103, 0.07344805],
           [0.17712369, 0.08953271, 0.07551570],
           [0.18226984, 0.09189912, 0.07756253],
           [0.18741984, 0.09424042, 0.07958888],
           [0.19257368, 0.09655736, 0.08159583],
           [0.19773177, 0.09885035, 0.08358407],
           [0.20289508, 0.10111941, 0.08555379],
           [0.20806344, 0.10336526, 0.08750608],
           [0.21323743, 0.10558811, 0.08944138],
           [0.21841762, 0.10778812, 0.09136011],
           [0.22360393, 0.10996587, 0.09326320],
           [0.22879730, 0.11212120, 0.09515070],
           [0.23399749, 0.11425475, 0.09702362],
           [0.23920524, 0.11636644, 0.09888215],
           [0.24442056, 0.11845670, 0.10072704],
           [0.24964399, 0.12052553, 0.10255859],
           [0.25487559, 0.12257327, 0.10437748],
           [0.26011591, 0.12459987, 0.10618400],
           [0.26536485, 0.12660577, 0.10797891],
           [0.27062320, 0.12859067, 0.10976227],
           [0.27589064, 0.13055515, 0.11153501],
           [0.28116790, 0.13249892, 0.11329723],
           [0.28645496, 0.13442228, 0.11504958],
           [0.29175191, 0.13632542, 0.11679264],
           [0.29705953, 0.13820797, 0.11852645],
           [0.30237754, 0.14007037, 0.12025185],
           [0.30770619, 0.14191267, 0.12196930],
           [0.31304596, 0.14373465, 0.12367902],
           [0.31839698, 0.14553642, 0.12538157],
           [0.32375929, 0.14731812, 0.12707753],
           [0.32913312, 0.14907971, 0.12876734],
           [0.33451869, 0.15082119, 0.13045146],
           [0.33991640, 0.15254233, 0.13213020],
           [0.34532626, 0.15424328, 0.13380421],
           [0.35074842, 0.15592402, 0.13547398],
           [0.35618306, 0.15758449, 0.13714001],
           [0.36163037, 0.15922465, 0.13880282],
           [0.36709053, 0.16084442, 0.14046291],
           [0.37256368, 0.16244373, 0.14212082],
           [0.37805000, 0.16402251, 0.14377710],
           [0.38354964, 0.16558067, 0.14543231],
           [0.38906272, 0.16711815, 0.14708703],
           [0.39458938, 0.16863485, 0.14874187],
           [0.40012983, 0.17013060, 0.15039738],
           [0.40568435, 0.17160517, 0.15205410],
           [0.41125283, 0.17305863, 0.15371282],
           [0.41683537, 0.17449090, 0.15537425],
           [0.42243210, 0.17590183, 0.15703906],
           [0.42804355, 0.17729090, 0.15870770],
           [0.43366930, 0.17865845, 0.16038126],
           [0.43930967, 0.18000413, 0.16206038],
           [0.44496489, 0.18132764, 0.16374576],
           [0.45063472, 0.18262915, 0.16543847],
           [0.45631970, 0.18390803, 0.16713910],
           [0.46201950, 0.18516452, 0.16884881],
           [0.46773436, 0.18639826, 0.17056845],
           [0.47346448, 0.18760891, 0.17229894],
           [0.47920962, 0.18879660, 0.17404153],
           [0.48496988, 0.18996107, 0.17579727],
           [0.49074562, 0.19110178, 0.17756713],
           [0.49653658, 0.19221882, 0.17935252],
           [0.50234275, 0.19331200, 0.18115474],
           [0.50816415, 0.19438111, 0.18297514],
           [0.51400073, 0.19542596, 0.18481519],
           [0.51985242, 0.19644640, 0.18667645],
           [0.52571914, 0.19744228, 0.18856057],
           [0.53160107, 0.19841308, 0.19046915],
           [0.53749771, 0.19935910, 0.19240426],
           [0.54340877, 0.20028035, 0.19436797],
           [0.54933468, 0.20117600, 0.19636211],
           [0.55527440, 0.20204691, 0.19838936],
           [0.56122832, 0.20289223, 0.20045191],
           [0.56719565, 0.20371253, 0.20255260],
           [0.57317599, 0.20450784, 0.20469433],
           [0.57916892, 0.20527822, 0.20688019],
           [0.58517386, 0.20602391, 0.20911357],
           [0.59119008, 0.20674530, 0.21139818],
           [0.59721668, 0.20744301, 0.21373809],
           [0.60325256, 0.20811785, 0.21613772],
           [0.60929703, 0.20877009, 0.21860179],
           [0.61534817, 0.20940159, 0.22113570],
           [0.62140456, 0.21001357, 0.22374524],
           [0.62746447, 0.21060762, 0.22643678],
           [0.63352553, 0.21118613, 0.22921738],
           [0.63958513, 0.21175191, 0.23209485],
           [0.64563982, 0.21230887, 0.23507773],
           [0.65168622, 0.21286089, 0.23817550],
           [0.65771956, 0.21341377, 0.24139850],
           [0.66373458, 0.21397413, 0.24475810],
           [0.66972486, 0.21455034, 0.24826659],
           [0.67568308, 0.21515214, 0.25193732],
           [0.68160009, 0.21579224, 0.25578419],
           [0.68746554, 0.21648527, 0.25982171],
           [0.69326730, 0.21724893, 0.26406422],
           [0.69899173, 0.21810359, 0.26852538],
           [0.70462353, 0.21907270, 0.27321678],
           [0.71014648, 0.22018170, 0.27814698],
           [0.71554399, 0.22145733, 0.28331983],
           [0.72080022, 0.22292581, 0.28873331],
           [0.72590133, 0.22461074, 0.29437873],
           [0.73083669, 0.22653107, 0.30024056],
           [0.73559980, 0.22869924, 0.30629757],
           [0.74018868, 0.23112025, 0.31252449],
           [0.74460563, 0.23379177, 0.31889417],
           [0.74885652, 0.23670514, 0.32537978],
           [0.75294975, 0.23984693, 0.33195617],
           [0.75689531, 0.24320059, 0.33860116],
           [0.76070380, 0.24674807, 0.34529597],
           [0.76438593, 0.25047094, 0.35202454],
           [0.76795189, 0.25435133, 0.35877448],
           [0.77141115, 0.25837247, 0.36553575],
           [0.77477256, 0.26251881, 0.37229998],
           [0.77804379, 0.26677651, 0.37906169],
           [0.78123206, 0.27113290, 0.38581549],
           [0.78434357, 0.27557695, 0.39255809],
           [0.78738394, 0.28009877, 0.39928656],
           [0.79035818, 0.28468967, 0.40599881],
           [0.79327055, 0.28934218, 0.41269364],
           [0.79612522, 0.29404938, 0.41936940],
           [0.79892565, 0.29880546, 0.42602547],
           [0.80167495, 0.30360528, 0.43266135],
           [0.80437600, 0.30844427, 0.43927664],
           [0.80703138, 0.31331841, 0.44587105],
           [0.80964362, 0.31822399, 0.45244410],
           [0.81221449, 0.32315820, 0.45899641],
           [0.81474632, 0.32811795, 0.46552728],
           [0.81724057, 0.33310108, 0.47203740],
           [0.81969904, 0.33810529, 0.47852656],
           [0.82212337, 0.34312856, 0.48499471],
           [0.82451481, 0.34816932, 0.49144226],
           [0.82687469, 0.35322603, 0.49786935],
           [0.82920424, 0.35829737, 0.50427616],
           [0.83150475, 0.36338199, 0.51066266],
           [0.83377726, 0.36847888, 0.51702911],
           [0.83602265, 0.37358719, 0.52337592],
           [0.83824196, 0.37870600, 0.52970315],
           [0.84043630, 0.38383440, 0.53601074],
           [0.84260624, 0.38897198, 0.54229933],
           [0.84475296, 0.39411782, 0.54856862],
           [0.84687704, 0.39927156, 0.55481910],
           [0.84897918, 0.40443278, 0.56105104],
           [0.85106052, 0.40960072, 0.56726414],
           [0.85312150, 0.41477522, 0.57345893],
           [0.85516280, 0.41995592, 0.57963557],
           [0.85718516, 0.42514246, 0.58579419],
           [0.85918925, 0.43033456, 0.59193494],
           [0.86117573, 0.43553193, 0.59805796],
           [0.86314524, 0.44073436, 0.60416341],
           [0.86509839, 0.44594163, 0.61025145],
           [0.86703576, 0.45115357, 0.61632226],
           [0.86895794, 0.45637003, 0.62237602],
           [0.87086547, 0.46159088, 0.62841291],
           [0.87275892, 0.46681601, 0.63443311],
           [0.87463920, 0.47204504, 0.64043642],
           [0.87650647, 0.47727814, 0.64642338],
           [0.87836125, 0.48251527, 0.65239419],
           [0.88020442, 0.48775608, 0.65834869],
           [0.88203632, 0.49300068, 0.66428723],
           [0.88385731, 0.49824908, 0.67021010],
           [0.88566842, 0.50350091, 0.67611704],
           [0.88746952, 0.50875657, 0.68200879],
           [0.88926189, 0.51401550, 0.68788483],
           [0.89104529, 0.51927818, 0.69374601],
           [0.89282093, 0.52454412, 0.69959190],
           [0.89458878, 0.52981366, 0.70542311],
           [0.89634962, 0.53508661, 0.71123963],
           [0.89810404, 0.54036289, 0.71704153],
           [0.89985224, 0.54564269, 0.72282926],
           [0.90159503, 0.55092583, 0.72860276],
           [0.90333293, 0.55621228, 0.73436222],
           [0.90506623, 0.56150220, 0.74010799],
           [0.90679545, 0.56679555, 0.74584023],
           [0.90852137, 0.57209219, 0.75155895],
           [0.91024440, 0.57739217, 0.75726444],
           [0.91196493, 0.58269559, 0.76295698],
           [0.91368350, 0.58800243, 0.76863675],
           [0.91540062, 0.59331269, 0.77430396],
           [0.91711684, 0.59862638, 0.77995883],
           [0.91883267, 0.60394350, 0.78560155],
           [0.92054867, 0.60926404, 0.79123233],
           [0.92226538, 0.61458800, 0.79685141],
           [0.92398322, 0.61991544, 0.80245907],
           [0.92570273, 0.62524639, 0.80805555],
           [0.92742442, 0.63058086, 0.81364111],
           [0.92914880, 0.63591886, 0.81921600],
           [0.93087638, 0.64126043, 0.82478051],
           [0.93260773, 0.64660556, 0.83033488],
           [0.93434340, 0.65195425, 0.83587937],
           [0.93608384, 0.65730657, 0.84141433],
           [0.93782955, 0.66266254, 0.84694004],
           [0.93958104, 0.66802220, 0.85245683],
           [0.94133881, 0.67338558, 0.85796503],
           [0.94310336, 0.67875272, 0.86346495],
           [0.94487519, 0.68412366, 0.86895696],
           [0.94665494, 0.68949837, 0.87444133],
           [0.94844316, 0.69487684, 0.87991840],
           [0.95024017, 0.70025923, 0.88538863],
           [0.95204644, 0.70564557, 0.89085241],
           [0.95386245, 0.71103593, 0.89631013],
           [0.95568907, 0.71643015, 0.90176204],
           [0.95752647, 0.72182844, 0.90720868],
           [0.95937505, 0.72723088, 0.91265052],
           [0.96123539, 0.73263749, 0.91808795],
           [0.96310823, 0.73804818, 0.92352130],
           [0.96499363, 0.74346320, 0.92895121],
           [0.96689210, 0.74888260, 0.93437814],
           [0.96880452, 0.75430622, 0.93980239],
           [0.97073082, 0.75973439, 0.94522466],
           [0.97267159, 0.76516710, 0.95064542],
           [0.97462750, 0.77060429, 0.95606508],
           [0.97659851, 0.77604628, 0.96148437],
           [0.97858550, 0.78149292, 0.96690364],
           [0.98058853, 0.78694445, 0.97232360],
           [0.98260802, 0.79240093, 0.97774480],
           [0.98464455, 0.79786238, 0.98316775],
           [0.98669804, 0.80332910, 0.98859321]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.redshift', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
