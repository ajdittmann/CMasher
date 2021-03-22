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
cm_type = 'sequential'

# RGB-values of this colormap
cm_data = [[0.00000000, 0.00000000, 0.00000000],
           [0.00023639, 0.00020226, 0.00023557],
           [0.00082902, 0.00069702, 0.00083114],
           [0.00173560, 0.00143561, 0.00174934],
           [0.00294053, 0.00239559, 0.00297761],
           [0.00443582, 0.00356230, 0.00451025],
           [0.00621705, 0.00492506, 0.00634452],
           [0.00828201, 0.00647541, 0.00847949],
           [0.01062993, 0.00820645, 0.01091534],
           [0.01326107, 0.01011229, 0.01365301],
           [0.01617646, 0.01218784, 0.01669392],
           [0.01937778, 0.01442856, 0.02003995],
           [0.02286721, 0.01683039, 0.02369319],
           [0.02664730, 0.01938967, 0.02765585],
           [0.03072102, 0.02210299, 0.03193035],
           [0.03509168, 0.02496719, 0.03651922],
           [0.03976291, 0.02797932, 0.04140199],
           [0.04454302, 0.03113658, 0.04629382],
           [0.04928304, 0.03443630, 0.05114892],
           [0.05399533, 0.03787584, 0.05597073],
           [0.05868339, 0.04142892, 0.06076185],
           [0.06335046, 0.04493712, 0.06552465],
           [0.06799943, 0.04839768, 0.07026120],
           [0.07263296, 0.05181299, 0.07497324],
           [0.07725354, 0.05518513, 0.07966241],
           [0.08186368, 0.05851583, 0.08433036],
           [0.08646508, 0.06180706, 0.08897775],
           [0.09105960, 0.06506041, 0.09360551],
           [0.09564964, 0.06827687, 0.09821511],
           [0.10023626, 0.07145815, 0.10280649],
           [0.10482135, 0.07460521, 0.10738052],
           [0.10940638, 0.07771911, 0.11193756],
           [0.11399271, 0.08080089, 0.11647780],
           [0.11858176, 0.08385138, 0.12100147],
           [0.12317489, 0.08687133, 0.12550870],
           [0.12777301, 0.08986175, 0.12999907],
           [0.13237788, 0.09282291, 0.13447299],
           [0.13699024, 0.09575574, 0.13892976],
           [0.14161115, 0.09866084, 0.14336899],
           [0.14624172, 0.10153875, 0.14779023],
           [0.15088311, 0.10438988, 0.15219298],
           [0.15553630, 0.10721472, 0.15657653],
           [0.16020210, 0.11001384, 0.16093991],
           [0.16488140, 0.11278769, 0.16528219],
           [0.16957505, 0.11553672, 0.16960225],
           [0.17428413, 0.11826118, 0.17389909],
           [0.17900918, 0.12096167, 0.17817118],
           [0.18375084, 0.12363869, 0.18241701],
           [0.18850969, 0.12629275, 0.18663491],
           [0.19328691, 0.12892393, 0.19082348],
           [0.19808239, 0.13153319, 0.19498041],
           [0.20289704, 0.13412077, 0.19910392],
           [0.20773080, 0.13668755, 0.20319159],
           [0.21258461, 0.13923373, 0.20724137],
           [0.21745811, 0.14176038, 0.21125054],
           [0.22235147, 0.14426822, 0.21521654],
           [0.22726471, 0.14675805, 0.21913666],
           [0.23219765, 0.14923080, 0.22300806],
           [0.23714993, 0.15168754, 0.22682780],
           [0.24212099, 0.15412944, 0.23059285],
           [0.24711009, 0.15655782, 0.23430018],
           [0.25211626, 0.15897413, 0.23794673],
           [0.25713854, 0.16137982, 0.24152953],
           [0.26217565, 0.16377652, 0.24504565],
           [0.26722589, 0.16616614, 0.24849232],
           [0.27228784, 0.16855038, 0.25186695],
           [0.27735947, 0.17093135, 0.25516720],
           [0.28243873, 0.17331110, 0.25839104],
           [0.28752369, 0.17569158, 0.26153672],
           [0.29261195, 0.17807503, 0.26460295],
           [0.29770123, 0.18046354, 0.26758881],
           [0.30278922, 0.18285917, 0.27049383],
           [0.30787362, 0.18526395, 0.27331796],
           [0.31295219, 0.18767976, 0.27606159],
           [0.31802278, 0.19010842, 0.27872554],
           [0.32308336, 0.19255157, 0.28131100],
           [0.32813205, 0.19501072, 0.28381950],
           [0.33316713, 0.19748721, 0.28625289],
           [0.33818708, 0.19998221, 0.28861326],
           [0.34319055, 0.20249672, 0.29090290],
           [0.34817638, 0.20503158, 0.29312427],
           [0.35314360, 0.20758749, 0.29527991],
           [0.35809139, 0.21016499, 0.29737244],
           [0.36301911, 0.21276449, 0.29940451],
           [0.36792626, 0.21538631, 0.30137876],
           [0.37281246, 0.21803065, 0.30329778],
           [0.37767746, 0.22069762, 0.30516412],
           [0.38252108, 0.22338728, 0.30698026],
           [0.38734325, 0.22609961, 0.30874858],
           [0.39214396, 0.22883455, 0.31047140],
           [0.39692324, 0.23159201, 0.31215090],
           [0.40168119, 0.23437187, 0.31378920],
           [0.40641790, 0.23717400, 0.31538835],
           [0.41113353, 0.23999824, 0.31695021],
           [0.41582823, 0.24284442, 0.31847660],
           [0.42050218, 0.24571239, 0.31996923],
           [0.42515554, 0.24860199, 0.32142974],
           [0.42978844, 0.25151309, 0.32285977],
           [0.43440107, 0.25444553, 0.32426073],
           [0.43899357, 0.25739919, 0.32563402],
           [0.44356605, 0.26037396, 0.32698106],
           [0.44811863, 0.26336975, 0.32830312],
           [0.45265142, 0.26638645, 0.32960141],
           [0.45716447, 0.26942402, 0.33087718],
           [0.46165785, 0.27248240, 0.33213157],
           [0.46613158, 0.27556155, 0.33336565],
           [0.47058566, 0.27866147, 0.33458061],
           [0.47502009, 0.28178215, 0.33577743],
           [0.47943481, 0.28492361, 0.33695716],
           [0.48382977, 0.28808588, 0.33812086],
           [0.48820486, 0.29126902, 0.33926948],
           [0.49255998, 0.29447308, 0.34040408],
           [0.49689498, 0.29769815, 0.34152559],
           [0.50120970, 0.30094432, 0.34263504],
           [0.50550395, 0.30421170, 0.34373338],
           [0.50977752, 0.30750041, 0.34482161],
           [0.51403016, 0.31081058, 0.34590073],
           [0.51826162, 0.31414236, 0.34697172],
           [0.52247162, 0.31749589, 0.34803562],
           [0.52665985, 0.32087135, 0.34909344],
           [0.53082599, 0.32426890, 0.35014622],
           [0.53496968, 0.32768874, 0.35119502],
           [0.53909057, 0.33113104, 0.35224093],
           [0.54318825, 0.33459600, 0.35328505],
           [0.54726233, 0.33808383, 0.35432850],
           [0.55131238, 0.34159473, 0.35537246],
           [0.55533796, 0.34512891, 0.35641807],
           [0.55933861, 0.34868658, 0.35746658],
           [0.56331386, 0.35226796, 0.35851921],
           [0.56726322, 0.35587326, 0.35957725],
           [0.57118619, 0.35950269, 0.36064200],
           [0.57508227, 0.36315647, 0.36171479],
           [0.57895093, 0.36683480, 0.36279703],
           [0.58279165, 0.37053790, 0.36389008],
           [0.58660389, 0.37426596, 0.36499544],
           [0.59038712, 0.37801917, 0.36611455],
           [0.59414079, 0.38179772, 0.36724894],
           [0.59786437, 0.38560178, 0.36840018],
           [0.60155731, 0.38943153, 0.36956981],
           [0.60521907, 0.39328711, 0.37075949],
           [0.60884914, 0.39716867, 0.37197082],
           [0.61244698, 0.40107632, 0.37320550],
           [0.61601209, 0.40501019, 0.37446524],
           [0.61954398, 0.40897035, 0.37575173],
           [0.62304216, 0.41295689, 0.37706675],
           [0.62650618, 0.41696986, 0.37841204],
           [0.62993559, 0.42100929, 0.37978937],
           [0.63333000, 0.42507519, 0.38120054],
           [0.63668901, 0.42916755, 0.38264733],
           [0.64001228, 0.43328634, 0.38413153],
           [0.64329947, 0.43743148, 0.38565494],
           [0.64655031, 0.44160291, 0.38721931],
           [0.64976456, 0.44580050, 0.38882643],
           [0.65294199, 0.45002411, 0.39047803],
           [0.65608246, 0.45427358, 0.39217582],
           [0.65918584, 0.45854873, 0.39392149],
           [0.66225206, 0.46284933, 0.39571669],
           [0.66528110, 0.46717513, 0.39756302],
           [0.66827298, 0.47152588, 0.39946203],
           [0.67122776, 0.47590129, 0.40141523],
           [0.67414558, 0.48030102, 0.40342406],
           [0.67702661, 0.48472475, 0.40548989],
           [0.67987107, 0.48917211, 0.40761405],
           [0.68267923, 0.49364273, 0.40979776],
           [0.68545141, 0.49813621, 0.41204218],
           [0.68818801, 0.50265212, 0.41434842],
           [0.69088939, 0.50719006, 0.41671744],
           [0.69355607, 0.51174955, 0.41915022],
           [0.69618852, 0.51633016, 0.42164755],
           [0.69878731, 0.52093142, 0.42421020],
           [0.70135301, 0.52555286, 0.42683883],
           [0.70388624, 0.53019399, 0.42953403],
           [0.70638769, 0.53485434, 0.43229629],
           [0.70885802, 0.53953342, 0.43512603],
           [0.71129796, 0.54423075, 0.43802359],
           [0.71370828, 0.54894583, 0.44098921],
           [0.71608970, 0.55367820, 0.44402308],
           [0.71844312, 0.55842734, 0.44712531],
           [0.72076923, 0.56319284, 0.45029593],
           [0.72306900, 0.56797417, 0.45353491],
           [0.72534319, 0.57277090, 0.45684217],
           [0.72759264, 0.57758260, 0.46021753],
           [0.72981838, 0.58240876, 0.46366081],
           [0.73202118, 0.58724899, 0.46717174],
           [0.73420193, 0.59210289, 0.47075000],
           [0.73636160, 0.59697000, 0.47439526],
           [0.73850113, 0.60184991, 0.47810710],
           [0.74062137, 0.60674226, 0.48188510],
           [0.74272326, 0.61164668, 0.48572879],
           [0.74480773, 0.61656278, 0.48963769],
           [0.74687578, 0.62149019, 0.49361125],
           [0.74892834, 0.62642855, 0.49764891],
           [0.75096632, 0.63137756, 0.50175013],
           [0.75299066, 0.63633687, 0.50591429],
           [0.75500233, 0.64130618, 0.51014078],
           [0.75700229, 0.64628517, 0.51442898],
           [0.75899149, 0.65127354, 0.51877823],
           [0.76097091, 0.65627101, 0.52318787],
           [0.76294152, 0.66127730, 0.52765724],
           [0.76490429, 0.66629214, 0.53218564],
           [0.76686020, 0.67131526, 0.53677239],
           [0.76881024, 0.67634642, 0.54141677],
           [0.77075540, 0.68138536, 0.54611807],
           [0.77269668, 0.68643184, 0.55087556],
           [0.77463509, 0.69148564, 0.55568852],
           [0.77657171, 0.69654651, 0.56055615],
           [0.77850753, 0.70161423, 0.56547773],
           [0.78044355, 0.70668860, 0.57045248],
           [0.78238081, 0.71176943, 0.57547963],
           [0.78432036, 0.71685652, 0.58055840],
           [0.78626330, 0.72194965, 0.58568795],
           [0.78821074, 0.72704862, 0.59086742],
           [0.79016367, 0.73215328, 0.59609604],
           [0.79212314, 0.73726347, 0.60137295],
           [0.79409035, 0.74237899, 0.60669724],
           [0.79606638, 0.74749968, 0.61206802],
           [0.79805223, 0.75262543, 0.61748444],
           [0.80004905, 0.75775607, 0.62294554],
           [0.80205803, 0.76289145, 0.62845032],
           [0.80408010, 0.76803150, 0.63399792],
           [0.80611645, 0.77317607, 0.63958729],
           [0.80816818, 0.77832507, 0.64521741],
           [0.81023626, 0.78347844, 0.65088735],
           [0.81232190, 0.78863606, 0.65659596],
           [0.81442602, 0.79379791, 0.66234226],
           [0.81654968, 0.79896395, 0.66812516],
           [0.81869393, 0.80413413, 0.67394355],
           [0.82085961, 0.80930848, 0.67979640],
           [0.82304785, 0.81448696, 0.68568249],
           [0.82525937, 0.81966965, 0.69160083],
           [0.82749518, 0.82485656, 0.69755021],
           [0.82975599, 0.83004779, 0.70352958],
           [0.83204266, 0.83524341, 0.70953778],
           [0.83435585, 0.84044357, 0.71557373],
           [0.83669628, 0.84564836, 0.72163632],
           [0.83906452, 0.85085798, 0.72772449],
           [0.84146117, 0.85607259, 0.73383715],
           [0.84388667, 0.86129241, 0.73997330],
           [0.84634150, 0.86651765, 0.74613189],
           [0.84882597, 0.87174858, 0.75231199],
           [0.85134042, 0.87698546, 0.75851264],
           [0.85388504, 0.88222860, 0.76473296],
           [0.85646002, 0.88747830, 0.77097209],
           [0.85906543, 0.89273489, 0.77722925],
           [0.86170131, 0.89799874, 0.78350369],
           [0.86436761, 0.90327022, 0.78979473],
           [0.86706424, 0.90854970, 0.79610175],
           [0.86979105, 0.91383758, 0.80242418],
           [0.87254779, 0.91913429, 0.80876154],
           [0.87533424, 0.92444025, 0.81511337],
           [0.87815002, 0.92975588, 0.82147936],
           [0.88099484, 0.93508163, 0.82785915],
           [0.88386822, 0.94041796, 0.83425260],
           [0.88676980, 0.94576529, 0.84065947],
           [0.88969900, 0.95112411, 0.84707976],
           [0.89265545, 0.95649483, 0.85351334]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.sepia', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
