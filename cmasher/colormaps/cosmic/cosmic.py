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
           [0.00022254, 0.00017671, 0.00025009],
           [0.00078387, 0.00060500, 0.00090179],
           [0.00164763, 0.00123817, 0.00193717],
           [0.00280144, 0.00205342, 0.00336061],
           [0.00423939, 0.00303533, 0.00518202],
           [0.00595880, 0.00417200, 0.00741444],
           [0.00795875, 0.00545370, 0.01007259],
           [0.01023937, 0.00687218, 0.01317220],
           [0.01280170, 0.00842008, 0.01673051],
           [0.01564747, 0.01009067, 0.02076595],
           [0.01877857, 0.01187795, 0.02529699],
           [0.02219739, 0.01377623, 0.03034346],
           [0.02590682, 0.01577996, 0.03592673],
           [0.02990978, 0.01788399, 0.04202298],
           [0.03420930, 0.02008340, 0.04820472],
           [0.03880874, 0.02237336, 0.05439934],
           [0.04358445, 0.02474908, 0.06061196],
           [0.04832042, 0.02720564, 0.06684805],
           [0.05302794, 0.02973858, 0.07311083],
           [0.05771012, 0.03234333, 0.07940403],
           [0.06236976, 0.03501524, 0.08573111],
           [0.06700933, 0.03774971, 0.09209532],
           [0.07163105, 0.04054044, 0.09849968],
           [0.07623693, 0.04327934, 0.10494709],
           [0.08082877, 0.04595941, 0.11144026],
           [0.08540827, 0.04858162, 0.11798198],
           [0.08997690, 0.05114686, 0.12457468],
           [0.09453596, 0.05365588, 0.13122062],
           [0.09908671, 0.05610920, 0.13792216],
           [0.10363029, 0.05850720, 0.14468161],
           [0.10816775, 0.06085010, 0.15150121],
           [0.11270017, 0.06313785, 0.15838356],
           [0.11722839, 0.06537049, 0.16533065],
           [0.12175321, 0.06754789, 0.17234460],
           [0.12627538, 0.06966979, 0.17942753],
           [0.13079560, 0.07173582, 0.18658154],
           [0.13531450, 0.07374552, 0.19380872],
           [0.13983264, 0.07569829, 0.20111112],
           [0.14435069, 0.07759327, 0.20849123],
           [0.14886940, 0.07942918, 0.21595220],
           [0.15338885, 0.08120569, 0.22349476],
           [0.15790940, 0.08292181, 0.23112093],
           [0.16243170, 0.08457592, 0.23883387],
           [0.16695619, 0.08616646, 0.24663627],
           [0.17148270, 0.08769287, 0.25452854],
           [0.17601191, 0.08915275, 0.26251464],
           [0.18054395, 0.09054460, 0.27059648],
           [0.18507865, 0.09186716, 0.27877510],
           [0.18961684, 0.09311710, 0.28705556],
           [0.19415775, 0.09429396, 0.29543682],
           [0.19870231, 0.09539359, 0.30392490],
           [0.20324973, 0.09641511, 0.31251899],
           [0.20780042, 0.09735485, 0.32122351],
           [0.21235420, 0.09821004, 0.33004063],
           [0.21691053, 0.09897843, 0.33897132],
           [0.22146970, 0.09965550, 0.34802028],
           [0.22603124, 0.10023806, 0.35718935],
           [0.23059455, 0.10072284, 0.36648009],
           [0.23515923, 0.10110562, 0.37589528],
           [0.23972479, 0.10138193, 0.38543762],
           [0.24429061, 0.10154697, 0.39510979],
           [0.24885596, 0.10159568, 0.40491433],
           [0.25341998, 0.10152262, 0.41485371],
           [0.25798164, 0.10132206, 0.42493024],
           [0.26253975, 0.10098790, 0.43514603],
           [0.26709296, 0.10051368, 0.44550301],
           [0.27163969, 0.09989258, 0.45600280],
           [0.27617812, 0.09911739, 0.46664673],
           [0.28070701, 0.09817741, 0.47743992],
           [0.28522342, 0.09706670, 0.48837993],
           [0.28972520, 0.09577455, 0.49946960],
           [0.29420947, 0.09429133, 0.51070913],
           [0.29867327, 0.09260527, 0.52210001],
           [0.30311267, 0.09070667, 0.53363982],
           [0.30752387, 0.08858214, 0.54532909],
           [0.31190255, 0.08621737, 0.55716750],
           [0.31624329, 0.08360013, 0.56915082],
           [0.32054033, 0.08071586, 0.58127560],
           [0.32478720, 0.07754942, 0.59353712],
           [0.32897683, 0.07408316, 0.60593109],
           [0.33310058, 0.07030445, 0.61844686],
           [0.33714920, 0.06619871, 0.63107428],
           [0.34111255, 0.06174960, 0.64380328],
           [0.34497874, 0.05694953, 0.65661652],
           [0.34873478, 0.05179404, 0.66949545],
           [0.35236629, 0.04628711, 0.68241857],
           [0.35585736, 0.04044955, 0.69535960],
           [0.35919048, 0.03450248, 0.70828712],
           [0.36234671, 0.02894281, 0.72116432],
           [0.36530584, 0.02392884, 0.73395112],
           [0.36804648, 0.01964477, 0.74659946],
           [0.37054659, 0.01629018, 0.75905887],
           [0.37278395, 0.01408742, 0.77127140],
           [0.37473691, 0.01326930, 0.78317727],
           [0.37638521, 0.01407636, 0.79471435],
           [0.37771093, 0.01674823, 0.80582046],
           [0.37869941, 0.02151387, 0.81643596],
           [0.37934000, 0.02858112, 0.82650669],
           [0.37962694, 0.03812858, 0.83598519],
           [0.37955939, 0.04951968, 0.84483436],
           [0.37914154, 0.06144082, 0.85302802],
           [0.37838226, 0.07366794, 0.86055174],
           [0.37729438, 0.08604353, 0.86740266],
           [0.37589428, 0.09845369, 0.87358820],
           [0.37420030, 0.11081496, 0.87912536],
           [0.37223249, 0.12306544, 0.88403831],
           [0.37001170, 0.13515937, 0.88835682],
           [0.36755886, 0.14706339, 0.89211456],
           [0.36489450, 0.15875385, 0.89534754],
           [0.36203830, 0.17021480, 0.89809281],
           [0.35900949, 0.18143572, 0.90038753],
           [0.35582553, 0.19241145, 0.90226812],
           [0.35250263, 0.20314042, 0.90376962],
           [0.34905654, 0.21362321, 0.90492566],
           [0.34550110, 0.22386312, 0.90576779],
           [0.34184894, 0.23386511, 0.90632553],
           [0.33811203, 0.24363489, 0.90662650],
           [0.33430129, 0.25317905, 0.90669631],
           [0.33042661, 0.26250480, 0.90655861],
           [0.32649697, 0.27161973, 0.90623512],
           [0.32252050, 0.28053167, 0.90574576],
           [0.31850454, 0.28924853, 0.90510876],
           [0.31445576, 0.29777822, 0.90434077],
           [0.31038061, 0.30612826, 0.90345722],
           [0.30628532, 0.31430588, 0.90247243],
           [0.30217392, 0.32231916, 0.90139844],
           [0.29805278, 0.33017428, 0.90024789],
           [0.29392464, 0.33787908, 0.89903036],
           [0.28979522, 0.34543927, 0.89775663],
           [0.28566704, 0.35286192, 0.89643473],
           [0.28154364, 0.36015310, 0.89507278],
           [0.27742935, 0.36731812, 0.89367887],
           [0.27332615, 0.37436312, 0.89225902],
           [0.26923690, 0.38129344, 0.89081940],
           [0.26516428, 0.38811418, 0.88936560],
           [0.26111077, 0.39483025, 0.88790274],
           [0.25707865, 0.40144635, 0.88643542],
           [0.25307008, 0.40796697, 0.88496784],
           [0.24908704, 0.41439642, 0.88350381],
           [0.24513141, 0.42073882, 0.88204676],
           [0.24120493, 0.42699810, 0.88059982],
           [0.23730925, 0.43317804, 0.87916579],
           [0.23344590, 0.43928225, 0.87774724],
           [0.22961633, 0.44531416, 0.87634645],
           [0.22582190, 0.45127709, 0.87496549],
           [0.22206389, 0.45717419, 0.87360621],
           [0.21834349, 0.46300848, 0.87227029],
           [0.21466236, 0.46878272, 0.87095954],
           [0.21102119, 0.47449978, 0.86967506],
           [0.20742080, 0.48016236, 0.86841794],
           [0.20386210, 0.48577303, 0.86718919],
           [0.20034666, 0.49133403, 0.86599021],
           [0.19687454, 0.49684789, 0.86482134],
           [0.19344637, 0.50231688, 0.86368323],
           [0.19006344, 0.50774301, 0.86257688],
           [0.18672570, 0.51312849, 0.86150244],
           [0.18343350, 0.51847533, 0.86046025],
           [0.18018787, 0.52378532, 0.85945104],
           [0.17698826, 0.52906048, 0.85847458],
           [0.17383532, 0.53430249, 0.85753132],
           [0.17072887, 0.53951311, 0.85662124],
           [0.16766875, 0.54469402, 0.85574432],
           [0.16465509, 0.54984675, 0.85490071],
           [0.16168705, 0.55497296, 0.85409003],
           [0.15876483, 0.56007400, 0.85331248],
           [0.15588710, 0.56515145, 0.85256749],
           [0.15305387, 0.57020657, 0.85185517],
           [0.15026358, 0.57524082, 0.85117488],
           [0.14751579, 0.58025541, 0.85052658],
           [0.14480878, 0.58525167, 0.84990960],
           [0.14214173, 0.59023075, 0.84932376],
           [0.13951263, 0.59519388, 0.84876836],
           [0.13692028, 0.60014214, 0.84824310],
           [0.13436243, 0.60507669, 0.84774724],
           [0.13183741, 0.60999854, 0.84728036],
           [0.12934276, 0.61490877, 0.84684171],
           [0.12687634, 0.61980834, 0.84643072],
           [0.12443548, 0.62469823, 0.84604664],
           [0.12201756, 0.62957937, 0.84568878],
           [0.11961967, 0.63445266, 0.84535639],
           [0.11723878, 0.63931897, 0.84504866],
           [0.11487170, 0.64417916, 0.84476479],
           [0.11251507, 0.64903403, 0.84450394],
           [0.11016531, 0.65388437, 0.84426522],
           [0.10781885, 0.65873094, 0.84404775],
           [0.10547170, 0.66357448, 0.84385054],
           [0.10312014, 0.66841567, 0.84367273],
           [0.10075970, 0.67325523, 0.84351320],
           [0.09838664, 0.67809378, 0.84337110],
           [0.09599597, 0.68293198, 0.84324519],
           [0.09358395, 0.68777038, 0.84313463],
           [0.09114522, 0.69260963, 0.84303810],
           [0.08867599, 0.69745020, 0.84295474],
           [0.08617051, 0.70229269, 0.84288313],
           [0.08362511, 0.70713753, 0.84282243],
           [0.08103357, 0.71198527, 0.84277110],
           [0.07839237, 0.71683626, 0.84272829],
           [0.07569525, 0.72169103, 0.84269246],
           [0.07293844, 0.72654989, 0.84266263],
           [0.07011617, 0.73141325, 0.84263735],
           [0.06722404, 0.73628145, 0.84261542],
           [0.06425764, 0.74115477, 0.84259561],
           [0.06121130, 0.74603356, 0.84257635],
           [0.05808247, 0.75091799, 0.84255664],
           [0.05486570, 0.75580838, 0.84253483],
           [0.05155846, 0.76070488, 0.84250968],
           [0.04815913, 0.76560763, 0.84247998],
           [0.04466405, 0.77051685, 0.84244395],
           [0.04107468, 0.77543259, 0.84240043],
           [0.03741096, 0.78035490, 0.84234809],
           [0.03385282, 0.78528385, 0.84228537],
           [0.03043137, 0.79021949, 0.84221065],
           [0.02716948, 0.79516171, 0.84212275],
           [0.02409051, 0.80011044, 0.84202021],
           [0.02122047, 0.80506559, 0.84190153],
           [0.01858815, 0.81002699, 0.84176524],
           [0.01622412, 0.81499451, 0.84160961],
           [0.01416537, 0.81996783, 0.84143342],
           [0.01245080, 0.82494667, 0.84123518],
           [0.01112317, 0.82993067, 0.84101341],
           [0.01022949, 0.83491944, 0.84076663],
           [0.00982139, 0.83991250, 0.84049339],
           [0.00995551, 0.84490931, 0.84019224],
           [0.01069215, 0.84990934, 0.83986145],
           [0.01210010, 0.85491187, 0.83949971],
           [0.01425466, 0.85991610, 0.83910577],
           [0.01723795, 0.86492117, 0.83867832],
           [0.02113724, 0.86992620, 0.83821555],
           [0.02605147, 0.87493010, 0.83771618],
           [0.03209157, 0.87993158, 0.83717944],
           [0.03937186, 0.88492950, 0.83660298],
           [0.04753062, 0.88992218, 0.83598667],
           [0.05607917, 0.89490805, 0.83532877],
           [0.06500234, 0.89988525, 0.83462804],
           [0.07428800, 0.90485162, 0.83388399],
           [0.08393083, 0.90980477, 0.83309565],
           [0.09393285, 0.91474203, 0.83226231],
           [0.10430211, 0.91966031, 0.83138359],
           [0.11505191, 0.92455607, 0.83045962],
           [0.12619999, 0.92942531, 0.82949010],
           [0.13776962, 0.93426332, 0.82847628],
           [0.14978894, 0.93906464, 0.82741934],
           [0.16229169, 0.94382285, 0.82632213],
           [0.17531808, 0.94853039, 0.82518803],
           [0.18891548, 0.95317821, 0.82402273],
           [0.20313976, 0.95775546, 0.82283421],
           [0.21805616, 0.96224898, 0.82163430],
           [0.23374218, 0.96664270, 0.82043899],
           [0.25028497, 0.97091692, 0.81927329],
           [0.26778032, 0.97504765, 0.81817391],
           [0.28632927, 0.97900591, 0.81719338],
           [0.30601898, 0.98275811, 0.81640936],
           [0.32689118, 0.98626848, 0.81593233],
           [0.34888332, 0.98950593, 0.81591102],
           [0.37176267, 0.99245625, 0.81652140]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.cosmic', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
