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
           [0.00032031, 0.00020876, 0.00015576],
           [0.00115213, 0.00071222, 0.00050933],
           [0.00246632, 0.00145292, 0.00099932],
           [0.00426111, 0.00240248, 0.00159470],
           [0.00654129, 0.00354149, 0.00227479],
           [0.00931453, 0.00485497, 0.00302435],
           [0.01259008, 0.00633067, 0.00383153],
           [0.01637810, 0.00795809, 0.00468676],
           [0.02068947, 0.00972796, 0.00558214],
           [0.02553552, 0.01163194, 0.00651101],
           [0.03092793, 0.01366243, 0.00746771],
           [0.03687870, 0.01581232, 0.00844736],
           [0.04329108, 0.01807499, 0.00944575],
           [0.04970018, 0.02044415, 0.01045917],
           [0.05607744, 0.02291381, 0.01148441],
           [0.06242826, 0.02547822, 0.01251862],
           [0.06875727, 0.02813185, 0.01355932],
           [0.07506844, 0.03086930, 0.01460431],
           [0.08136524, 0.03368535, 0.01565167],
           [0.08765071, 0.03657489, 0.01669973],
           [0.09392754, 0.03953289, 0.01774700],
           [0.10019812, 0.04248851, 0.01879222],
           [0.10646459, 0.04536893, 0.01983431],
           [0.11272888, 0.04818555, 0.02087234],
           [0.11899272, 0.05094021, 0.02190555],
           [0.12525770, 0.05363453, 0.02293331],
           [0.13152527, 0.05626994, 0.02395516],
           [0.13779673, 0.05884770, 0.02497073],
           [0.14407332, 0.06136894, 0.02597979],
           [0.15035614, 0.06383462, 0.02698225],
           [0.15664624, 0.06624561, 0.02797810],
           [0.16294457, 0.06860266, 0.02896747],
           [0.16925203, 0.07090640, 0.02995057],
           [0.17556946, 0.07315739, 0.03092776],
           [0.18189762, 0.07535608, 0.03189947],
           [0.18823726, 0.07750287, 0.03286623],
           [0.19458905, 0.07959805, 0.03382870],
           [0.20095364, 0.08164185, 0.03478764],
           [0.20733163, 0.08363445, 0.03574389],
           [0.21372359, 0.08557593, 0.03669841],
           [0.22013006, 0.08746634, 0.03765228],
           [0.22655154, 0.08930565, 0.03860667],
           [0.23298852, 0.09109380, 0.03956286],
           [0.23944144, 0.09283065, 0.04052097],
           [0.24591073, 0.09451600, 0.04146142],
           [0.25239679, 0.09614964, 0.04239527],
           [0.25890000, 0.09773126, 0.04332440],
           [0.26542072, 0.09926052, 0.04425071],
           [0.27195929, 0.10073705, 0.04517610],
           [0.27851612, 0.10216029, 0.04610242],
           [0.28509144, 0.10352983, 0.04703172],
           [0.29168551, 0.10484515, 0.04796603],
           [0.29829858, 0.10610566, 0.04890741],
           [0.30493089, 0.10731073, 0.04985793],
           [0.31158270, 0.10845962, 0.05081968],
           [0.31825437, 0.10955144, 0.05179469],
           [0.32494588, 0.11058558, 0.05278533],
           [0.33165741, 0.11156121, 0.05379388],
           [0.33838918, 0.11247734, 0.05482253],
           [0.34514146, 0.11333282, 0.05587349],
           [0.35191413, 0.11412692, 0.05694939],
           [0.35870733, 0.11485850, 0.05805261],
           [0.36552140, 0.11552606, 0.05918537],
           [0.37235602, 0.11612887, 0.06035055],
           [0.37921149, 0.11666531, 0.06155047],
           [0.38608774, 0.11713411, 0.06278785],
           [0.39298465, 0.11753398, 0.06406542],
           [0.39990243, 0.11786308, 0.06538571],
           [0.40684070, 0.11812026, 0.06675174],
           [0.41379968, 0.11830340, 0.06816610],
           [0.42077900, 0.11841110, 0.06963182],
           [0.42777857, 0.11844140, 0.07115178],
           [0.43479835, 0.11839213, 0.07272887],
           [0.44183779, 0.11826176, 0.07436631],
           [0.44889692, 0.11804763, 0.07606698],
           [0.45597537, 0.11774759, 0.07783407],
           [0.46307262, 0.11735955, 0.07967086],
           [0.47018828, 0.11688094, 0.08158056],
           [0.47732206, 0.11630887, 0.08356643],
           [0.48447342, 0.11564059, 0.08563184],
           [0.49164167, 0.11487339, 0.08778027],
           [0.49882616, 0.11400421, 0.09001524],
           [0.50602619, 0.11302981, 0.09234030],
           [0.51324096, 0.11194681, 0.09475911],
           [0.52046957, 0.11075165, 0.09727541],
           [0.52771103, 0.10944063, 0.09989300],
           [0.53496423, 0.10800987, 0.10261578],
           [0.54222828, 0.10645458, 0.10544773],
           [0.54950158, 0.10477099, 0.10839295],
           [0.55678265, 0.10295467, 0.11145561],
           [0.56407005, 0.10100050, 0.11463998],
           [0.57136221, 0.09890294, 0.11795046],
           [0.57865683, 0.09665778, 0.12139144],
           [0.58595251, 0.09425758, 0.12496762],
           [0.59324637, 0.09169820, 0.12868351],
           [0.60053647, 0.08897198, 0.13254399],
           [0.60781996, 0.08607290, 0.13655381],
           [0.61509391, 0.08299424, 0.14071783],
           [0.62235528, 0.07972847, 0.14504098],
           [0.62960086, 0.07626735, 0.14952833],
           [0.63682690, 0.07260321, 0.15418475],
           [0.64402945, 0.06872768, 0.15901515],
           [0.65120429, 0.06463189, 0.16402435],
           [0.65834703, 0.06030595, 0.16921717],
           [0.66545273, 0.05574060, 0.17459807],
           [0.67251615, 0.05092618, 0.18017123],
           [0.67953179, 0.04585268, 0.18594053],
           [0.68649408, 0.04050791, 0.19190990],
           [0.69339656, 0.03501827, 0.19808181],
           [0.70023310, 0.02974032, 0.20445918],
           [0.70699677, 0.02473108, 0.21104325],
           [0.71368081, 0.02004735, 0.21783521],
           [0.72027805, 0.01575128, 0.22483488],
           [0.72678121, 0.01190847, 0.23204104],
           [0.73318299, 0.00858729, 0.23945145],
           [0.73947609, 0.00585900, 0.24706262],
           [0.74565328, 0.00379723, 0.25486974],
           [0.75170751, 0.00247734, 0.26286660],
           [0.75763201, 0.00197573, 0.27104565],
           [0.76342035, 0.00236912, 0.27939796],
           [0.76906659, 0.00373375, 0.28791328],
           [0.77456531, 0.00614457, 0.29658016],
           [0.77991170, 0.00967453, 0.30538600],
           [0.78510166, 0.01439382, 0.31431727],
           [0.79013176, 0.02036922, 0.32335963],
           [0.79499936, 0.02766356, 0.33249813],
           [0.79970258, 0.03633527, 0.34171740],
           [0.80424028, 0.04610137, 0.35100187],
           [0.80861206, 0.05593074, 0.36033595],
           [0.81281824, 0.06575513, 0.36970423],
           [0.81685977, 0.07556701, 0.37909164],
           [0.82073820, 0.08536045, 0.38848361],
           [0.82445563, 0.09513050, 0.39786621],
           [0.82801462, 0.10487292, 0.40722623],
           [0.83141814, 0.11458394, 0.41655122],
           [0.83466964, 0.12426002, 0.42582926],
           [0.83777258, 0.13389850, 0.43505012],
           [0.84073089, 0.14349659, 0.44420371],
           [0.84354864, 0.15305194, 0.45328109],
           [0.84622995, 0.16256264, 0.46227431],
           [0.84877908, 0.17202698, 0.47117623],
           [0.85120054, 0.18144313, 0.47998013],
           [0.85349849, 0.19081025, 0.48868085],
           [0.85567734, 0.20012720, 0.49727347],
           [0.85774150, 0.20939307, 0.50575378],
           [0.85969539, 0.21860703, 0.51411817],
           [0.86154321, 0.22776871, 0.52236389],
           [0.86328918, 0.23687774, 0.53048865],
           [0.86493759, 0.24593368, 0.53849050],
           [0.86649243, 0.25493655, 0.54636825],
           [0.86795766, 0.26388635, 0.55412108],
           [0.86933714, 0.27278325, 0.56174857],
           [0.87063488, 0.28162708, 0.56925039],
           [0.87185473, 0.29041795, 0.57662667],
           [0.87299987, 0.29915672, 0.58387836],
           [0.87407470, 0.30784267, 0.59100548],
           [0.87508176, 0.31647731, 0.59800984],
           [0.87602545, 0.32505984, 0.60489185],
           [0.87690829, 0.33359164, 0.61165350],
           [0.87773379, 0.34207284, 0.61829617],
           [0.87850545, 0.35050356, 0.62482133],
           [0.87922592, 0.35888478, 0.63123109],
           [0.87989827, 0.36721697, 0.63752735],
           [0.88052548, 0.37550059, 0.64371209],
           [0.88111058, 0.38373605, 0.64978738],
           [0.88165635, 0.39192396, 0.65575540],
           [0.88216538, 0.40006502, 0.66161845],
           [0.88264034, 0.40815983, 0.66737883],
           [0.88308383, 0.41620898, 0.67303885],
           [0.88349837, 0.42421311, 0.67860087],
           [0.88388658, 0.43217272, 0.68406723],
           [0.88425089, 0.44008842, 0.68944031],
           [0.88459352, 0.44796098, 0.69472256],
           [0.88491674, 0.45579107, 0.69991638],
           [0.88522277, 0.46357936, 0.70502418],
           [0.88551386, 0.47132645, 0.71004831],
           [0.88579260, 0.47903263, 0.71499109],
           [0.88606054, 0.48669904, 0.71985498],
           [0.88631967, 0.49432634, 0.72464230],
           [0.88657273, 0.50191463, 0.72935531],
           [0.88682100, 0.50946512, 0.73399636],
           [0.88706656, 0.51697833, 0.73856771],
           [0.88731166, 0.52445464, 0.74307157],
           [0.88755748, 0.53189523, 0.74751019],
           [0.88780677, 0.53930002, 0.75188571],
           [0.88806029, 0.54667042, 0.75620029],
           [0.88832077, 0.55400637, 0.76045604],
           [0.88858898, 0.56130917, 0.76465503],
           [0.88886751, 0.56857881, 0.76879932],
           [0.88915723, 0.57581648, 0.77289087],
           [0.88946027, 0.58302245, 0.77693169],
           [0.88977801, 0.59019749, 0.78092369],
           [0.89011184, 0.59734231, 0.78486874],
           [0.89046385, 0.60445719, 0.78876876],
           [0.89083498, 0.61154309, 0.79262552],
           [0.89122688, 0.61860051, 0.79644080],
           [0.89164127, 0.62562987, 0.80021639],
           [0.89207922, 0.63263202, 0.80395396],
           [0.89254218, 0.63960749, 0.80765517],
           [0.89303193, 0.64655664, 0.81132175],
           [0.89354946, 0.65348027, 0.81495521],
           [0.89409613, 0.66037894, 0.81855714],
           [0.89467341, 0.66725312, 0.82212908],
           [0.89528268, 0.67410333, 0.82567258],
           [0.89592507, 0.68093022, 0.82918904],
           [0.89660188, 0.68773430, 0.83267991],
           [0.89731440, 0.69451609, 0.83614660],
           [0.89806405, 0.70127602, 0.83959053],
           [0.89885189, 0.70801470, 0.84301299],
           [0.89967918, 0.71473262, 0.84641529],
           [0.90054714, 0.72143026, 0.84979872],
           [0.90145701, 0.72810810, 0.85316454],
           [0.90241007, 0.73476657, 0.85651399],
           [0.90340743, 0.74140617, 0.85984825],
           [0.90445031, 0.74802735, 0.86316849],
           [0.90553992, 0.75463054, 0.86647585],
           [0.90667746, 0.76121615, 0.86977146],
           [0.90786415, 0.76778459, 0.87305641],
           [0.90910120, 0.77433626, 0.87633178],
           [0.91038981, 0.78087154, 0.87959861],
           [0.91173124, 0.78739078, 0.88285793],
           [0.91312673, 0.79389433, 0.88611074],
           [0.91457758, 0.80038249, 0.88935803],
           [0.91608500, 0.80685562, 0.89260074],
           [0.91765039, 0.81331396, 0.89583983],
           [0.91927511, 0.81975775, 0.89907623],
           [0.92096059, 0.82618722, 0.90231088],
           [0.92270830, 0.83260254, 0.90554466],
           [0.92451964, 0.83900395, 0.90877841],
           [0.92639632, 0.84539150, 0.91201305],
           [0.92834008, 0.85176524, 0.91524947],
           [0.93035272, 0.85812518, 0.91848857],
           [0.93243609, 0.86447132, 0.92173117],
           [0.93459223, 0.87080356, 0.92497815],
           [0.93682359, 0.87712161, 0.92823055],
           [0.93913266, 0.88342515, 0.93148937],
           [0.94152187, 0.88971391, 0.93475546],
           [0.94399458, 0.89598719, 0.93803021],
           [0.94655427, 0.90224421, 0.94131502],
           [0.94920436, 0.90848425, 0.94461125],
           [0.95194957, 0.91470593, 0.94792118],
           [0.95479468, 0.92090786, 0.95124737],
           [0.95774485, 0.92708839, 0.95459314],
           [0.96080631, 0.93324527, 0.95796364],
           [0.96398446, 0.93937648, 0.96136518],
           [0.96728521, 0.94547938, 0.96480785],
           [0.97071125, 0.95155233, 0.96830475],
           [0.97426122, 0.95759472, 0.97187464],
           [0.97792404, 0.96360932, 0.97554077],
           [0.98167361, 0.96960465, 0.97932802],
           [0.98546619, 0.97559672, 0.98325573],
           [0.98924336, 0.98160914, 0.98732439],
           [0.99294687, 0.98766807, 0.99150675],
           [0.99653673, 0.99379467, 0.99575160],
           [1.00000000, 1.00000000, 1.00000000]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.flamingo', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
