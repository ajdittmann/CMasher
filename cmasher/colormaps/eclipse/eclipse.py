from matplotlib.colors import ListedColormap

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.07517779e-04, 2.10625536e-04, 2.64510973e-04],
           [7.12572983e-04, 7.30616561e-04, 9.49475382e-04],
           [1.46225238e-03, 1.51423381e-03, 2.03025033e-03],
           [2.43078526e-03, 2.54181697e-03, 3.50650496e-03],
           [3.60049565e-03, 3.80143028e-03, 5.38381777e-03],
           [4.95755524e-03, 5.28496381e-03, 7.67078602e-03],
           [6.49035251e-03, 6.98659933e-03, 1.03776726e-02],
           [8.18873039e-03, 8.90205203e-03, 1.35155309e-02],
           [1.00433115e-02, 1.10281313e-02, 1.70967670e-02],
           [1.20455163e-02, 1.33624891e-02, 2.11335767e-02],
           [1.41869468e-02, 1.59034314e-02, 2.56396198e-02],
           [1.64596956e-02, 1.86498138e-02, 3.06280164e-02],
           [1.88558519e-02, 2.16009470e-02, 3.61129347e-02],
           [2.13676021e-02, 2.47565410e-02, 4.20617974e-02],
           [2.39873080e-02, 2.81166597e-02, 4.80627202e-02],
           [2.67069926e-02, 3.16816869e-02, 5.40526568e-02],
           [2.95188193e-02, 3.54523020e-02, 6.00356007e-02],
           [3.24148583e-02, 3.94294588e-02, 6.60149067e-02],
           [3.53869306e-02, 4.34930157e-02, 7.19937137e-02],
           [3.84265262e-02, 4.75122439e-02, 7.79750343e-02],
           [4.14989566e-02, 5.15002703e-02, 8.39609823e-02],
           [4.44830679e-02, 5.54602832e-02, 8.99533252e-02],
           [4.73835605e-02, 5.93952090e-02, 9.59537413e-02],
           [5.02006572e-02, 6.33077506e-02, 1.01963641e-01],
           [5.29342578e-02, 6.72004215e-02, 1.07984186e-01],
           [5.55839615e-02, 7.10755733e-02, 1.14016310e-01],
           [5.81490844e-02, 7.49354200e-02, 1.20060722e-01],
           [6.06286734e-02, 7.87820574e-02, 1.26117919e-01],
           [6.30214480e-02, 8.26174854e-02, 1.32188302e-01],
           [6.53256077e-02, 8.64436390e-02, 1.38272478e-01],
           [6.75397075e-02, 9.02623363e-02, 1.44369837e-01],
           [6.96617777e-02, 9.40753514e-02, 1.50480037e-01],
           [7.16889981e-02, 9.78844578e-02, 1.56603387e-01],
           [7.36190695e-02, 1.01691322e-01, 1.62738785e-01],
           [7.54490307e-02, 1.05497609e-01, 1.68885480e-01],
           [7.71754873e-02, 1.09304969e-01, 1.75042662e-01],
           [7.87948940e-02, 1.13115022e-01, 1.81209047e-01],
           [8.03036966e-02, 1.16929338e-01, 1.87382731e-01],
           [8.16969235e-02, 1.20749588e-01, 1.93562797e-01],
           [8.29703096e-02, 1.24577330e-01, 1.99746748e-01],
           [8.41188593e-02, 1.28414153e-01, 2.05932186e-01],
           [8.51370063e-02, 1.32261664e-01, 2.12116530e-01],
           [8.60187661e-02, 1.36121473e-01, 2.18296777e-01],
           [8.67577246e-02, 1.39995188e-01, 2.24469467e-01],
           [8.73470284e-02, 1.43884412e-01, 2.30630638e-01],
           [8.77787186e-02, 1.47790818e-01, 2.36776295e-01],
           [8.80448203e-02, 1.51716015e-01, 2.42901410e-01],
           [8.81372411e-02, 1.55661541e-01, 2.49000050e-01],
           [8.80454594e-02, 1.59629144e-01, 2.55066899e-01],
           [8.77603171e-02, 1.63620295e-01, 2.61094511e-01],
           [8.72710666e-02, 1.67636539e-01, 2.67075325e-01],
           [8.65661085e-02, 1.71679383e-01, 2.73001015e-01],
           [8.56333894e-02, 1.75750226e-01, 2.78862211e-01],
           [8.44605366e-02, 1.79850313e-01, 2.84648432e-01],
           [8.30350472e-02, 1.83980686e-01, 2.90348045e-01],
           [8.13435237e-02, 1.88142252e-01, 2.95948608e-01],
           [7.93731525e-02, 1.92335569e-01, 3.01436341e-01],
           [7.71113447e-02, 1.96560864e-01, 3.06796447e-01],
           [7.45475527e-02, 2.00817801e-01, 3.12012837e-01],
           [7.16726081e-02, 2.05105560e-01, 3.17068727e-01],
           [6.84809116e-02, 2.09422603e-01, 3.21946586e-01],
           [6.49714972e-02, 2.13766617e-01, 3.26628626e-01],
           [6.11494128e-02, 2.18134471e-01, 3.31097341e-01],
           [5.70305993e-02, 2.22521888e-01, 3.35335907e-01],
           [5.26414914e-02, 2.26923791e-01, 3.39329357e-01],
           [4.80243681e-02, 2.31334157e-01, 3.43065188e-01],
           [4.32424215e-02, 2.35746085e-01, 3.46534261e-01],
           [3.83798926e-02, 2.40152156e-01, 3.49731583e-01],
           [3.37984938e-02, 2.44544656e-01, 3.52656783e-01],
           [2.97201953e-02, 2.48915920e-01, 3.55314297e-01],
           [2.62539025e-02, 2.53258676e-01, 3.57713187e-01],
           [2.34976830e-02, 2.57566347e-01, 3.59866603e-01],
           [2.15359752e-02, 2.61833292e-01, 3.61790985e-01],
           [2.04380729e-02, 2.66054952e-01, 3.63505107e-01],
           [2.02578619e-02, 2.70227903e-01, 3.65029081e-01],
           [2.10346112e-02, 2.74349826e-01, 3.66383447e-01],
           [2.27950431e-02, 2.78419345e-01, 3.67588674e-01],
           [2.55540526e-02, 2.82436041e-01, 3.68664108e-01],
           [2.93179724e-02, 2.86400143e-01, 3.69628189e-01],
           [3.40854546e-02, 2.90312539e-01, 3.70497557e-01],
           [3.98500389e-02, 2.94174501e-01, 3.71287591e-01],
           [4.62492145e-02, 2.97987645e-01, 3.72012071e-01],
           [5.29305048e-02, 3.01753828e-01, 3.72683209e-01],
           [5.98083087e-02, 3.05475062e-01, 3.73311722e-01],
           [6.68134863e-02, 3.09153447e-01, 3.73906943e-01],
           [7.38946896e-02, 3.12791059e-01, 3.74477788e-01],
           [8.10148710e-02, 3.16390080e-01, 3.75030712e-01],
           [8.81461312e-02, 3.19952561e-01, 3.75572797e-01],
           [9.52687878e-02, 3.23480577e-01, 3.76109045e-01],
           [1.02368299e-01, 3.26976111e-01, 3.76644254e-01],
           [1.09434150e-01, 3.30441082e-01, 3.77182595e-01],
           [1.16458874e-01, 3.33877334e-01, 3.77727627e-01],
           [1.23437283e-01, 3.37286637e-01, 3.78282372e-01],
           [1.30365908e-01, 3.40670682e-01, 3.78849383e-01],
           [1.37242567e-01, 3.44031081e-01, 3.79430802e-01],
           [1.44065521e-01, 3.47369387e-01, 3.80028950e-01],
           [1.50834563e-01, 3.50687060e-01, 3.80645001e-01],
           [1.57549585e-01, 3.53985498e-01, 3.81280318e-01],
           [1.64210630e-01, 3.57266051e-01, 3.81936269e-01],
           [1.70818564e-01, 3.60529978e-01, 3.82613490e-01],
           [1.77374190e-01, 3.63778495e-01, 3.83312706e-01],
           [1.83878117e-01, 3.67012787e-01, 3.84034815e-01],
           [1.90331831e-01, 3.70233932e-01, 3.84779818e-01],
           [1.96736401e-01, 3.73442994e-01, 3.85548056e-01],
           [2.03092964e-01, 3.76640991e-01, 3.86339728e-01],
           [2.09402524e-01, 3.79828914e-01, 3.87155067e-01],
           [2.15666528e-01, 3.83007674e-01, 3.87993788e-01],
           [2.21886200e-01, 3.86178165e-01, 3.88855717e-01],
           [2.28062758e-01, 3.89341242e-01, 3.89740590e-01],
           [2.34197412e-01, 3.92497728e-01, 3.90648041e-01],
           [2.40291366e-01, 3.95648413e-01, 3.91577611e-01],
           [2.46345677e-01, 3.98794074e-01, 3.92528881e-01],
           [2.52361572e-01, 4.01935434e-01, 3.93501164e-01],
           [2.58340279e-01, 4.05073186e-01, 3.94493676e-01],
           [2.64282962e-01, 4.08208002e-01, 3.95505592e-01],
           [2.70190779e-01, 4.11340526e-01, 3.96536001e-01],
           [2.76064627e-01, 4.14471414e-01, 3.97584153e-01],
           [2.81905789e-01, 4.17601239e-01, 3.98648830e-01],
           [2.87715544e-01, 4.20730549e-01, 3.99728732e-01],
           [2.93494829e-01, 4.23859916e-01, 4.00822810e-01],
           [2.99244881e-01, 4.26989846e-01, 4.01929646e-01],
           [3.04967119e-01, 4.30120784e-01, 4.03047559e-01],
           [3.10662356e-01, 4.33253252e-01, 4.04175417e-01],
           [3.16332345e-01, 4.36387592e-01, 4.05311073e-01],
           [3.21978116e-01, 4.39524239e-01, 4.06453067e-01],
           [3.27601320e-01, 4.42663495e-01, 4.07599257e-01],
           [3.33203276e-01, 4.45805694e-01, 4.08747819e-01],
           [3.38785749e-01, 4.48951058e-01, 4.09896437e-01],
           [3.44350231e-01, 4.52099830e-01, 4.11043086e-01],
           [3.49898778e-01, 4.55252117e-01, 4.12185145e-01],
           [3.55432984e-01, 4.58408074e-01, 4.13320528e-01],
           [3.60955215e-01, 4.61567680e-01, 4.14446349e-01],
           [3.66467454e-01, 4.64730941e-01, 4.15560217e-01],
           [3.71972103e-01, 4.67897745e-01, 4.16659362e-01],
           [3.77471722e-01, 4.71067902e-01, 4.17740947e-01],
           [3.82968697e-01, 4.74241210e-01, 4.18802473e-01],
           [3.88466015e-01, 4.77417298e-01, 4.19840897e-01],
           [3.93966549e-01, 4.80595766e-01, 4.20853483e-01],
           [3.99473191e-01, 4.83776154e-01, 4.21837677e-01],
           [4.04989247e-01, 4.86957863e-01, 4.22790622e-01],
           [4.10517954e-01, 4.90140251e-01, 4.23709771e-01],
           [4.16062508e-01, 4.93322623e-01, 4.24592849e-01],
           [4.21626396e-01, 4.96504171e-01, 4.25437437e-01],
           [4.27213005e-01, 4.99684045e-01, 4.26241456e-01],
           [4.32825654e-01, 5.02861358e-01, 4.27003111e-01],
           [4.38467666e-01, 5.06035168e-01, 4.27720782e-01],
           [4.44142309e-01, 5.09204494e-01, 4.28393060e-01],
           [4.49852673e-01, 5.12368353e-01, 4.29018883e-01],
           [4.55601648e-01, 5.15525762e-01, 4.29597525e-01],
           [4.61392001e-01, 5.18675733e-01, 4.30128447e-01],
           [4.67226238e-01, 5.21817310e-01, 4.30611444e-01],
           [4.73106594e-01, 5.24949576e-01, 4.31046603e-01],
           [4.79035021e-01, 5.28071664e-01, 4.31434279e-01],
           [4.85013203e-01, 5.31182764e-01, 4.31775040e-01],
           [4.91042495e-01, 5.34282139e-01, 4.32069698e-01],
           [4.97123949e-01, 5.37369130e-01, 4.32319252e-01],
           [5.03258359e-01, 5.40443151e-01, 4.32524790e-01],
           [5.09446155e-01, 5.43503721e-01, 4.32687620e-01],
           [5.15687509e-01, 5.46550442e-01, 4.32809101e-01],
           [5.21982361e-01, 5.49583000e-01, 4.32890610e-01],
           [5.28330458e-01, 5.52601153e-01, 4.32933478e-01],
           [5.34731194e-01, 5.55604785e-01, 4.32939203e-01],
           [5.41183841e-01, 5.58593840e-01, 4.32909156e-01],
           [5.47687646e-01, 5.61568302e-01, 4.32844459e-01],
           [5.54241534e-01, 5.64528275e-01, 4.32746382e-01],
           [5.60844315e-01, 5.67473930e-01, 4.32616089e-01],
           [5.67494897e-01, 5.70405444e-01, 4.32454376e-01],
           [5.74192037e-01, 5.73323070e-01, 4.32262010e-01],
           [5.80934247e-01, 5.76227164e-01, 4.32039852e-01],
           [5.87720377e-01, 5.79118019e-01, 4.31788135e-01],
           [5.94549029e-01, 5.81996029e-01, 4.31507217e-01],
           [6.01418623e-01, 5.84861679e-01, 4.31197512e-01],
           [6.08328284e-01, 5.87715267e-01, 4.30858363e-01],
           [6.15276179e-01, 5.90557417e-01, 4.30490163e-01],
           [6.22261289e-01, 5.93388530e-01, 4.30092107e-01],
           [6.29282179e-01, 5.96209168e-01, 4.29663755e-01],
           [6.36337580e-01, 5.99019868e-01, 4.29204284e-01],
           [6.43426268e-01, 6.01821182e-01, 4.28712645e-01],
           [6.50546961e-01, 6.04613713e-01, 4.28187674e-01],
           [6.57698296e-01, 6.07398119e-01, 4.27628114e-01],
           [6.64879350e-01, 6.10174945e-01, 4.27031927e-01],
           [6.72088311e-01, 6.12945066e-01, 4.26397983e-01],
           [6.79324489e-01, 6.15709012e-01, 4.25723436e-01],
           [6.86586244e-01, 6.18467674e-01, 4.25006375e-01],
           [6.93872020e-01, 6.21221959e-01, 4.24244452e-01],
           [7.01180410e-01, 6.23972766e-01, 4.23434749e-01],
           [7.08510362e-01, 6.26720910e-01, 4.22573411e-01],
           [7.15859670e-01, 6.29467675e-01, 4.21657651e-01],
           [7.23226493e-01, 6.32214276e-01, 4.20683620e-01],
           [7.30608763e-01, 6.34962078e-01, 4.19647116e-01],
           [7.38004125e-01, 6.37712627e-01, 4.18543568e-01],
           [7.45409863e-01, 6.40467692e-01, 4.17368028e-01],
           [7.52822812e-01, 6.43229309e-01, 4.16115164e-01],
           [7.60239908e-01, 6.45999594e-01, 4.14778244e-01],
           [7.67656489e-01, 6.48781395e-01, 4.13351526e-01],
           [7.75067194e-01, 6.51577984e-01, 4.11828743e-01],
           [7.82467197e-01, 6.54392615e-01, 4.10200764e-01],
           [7.89848176e-01, 6.57230076e-01, 4.08461919e-01],
           [7.97202842e-01, 6.60095015e-01, 4.06602145e-01],
           [8.04520280e-01, 6.62993736e-01, 4.04614613e-01],
           [8.11788251e-01, 6.65933371e-01, 4.02491542e-01],
           [8.18992031e-01, 6.68922348e-01, 4.00226044e-01],
           [8.26113886e-01, 6.71970614e-01, 3.97813235e-01],
           [8.33132772e-01, 6.75089739e-01, 3.95251373e-01],
           [8.40024726e-01, 6.78292725e-01, 3.92542031e-01],
           [8.46761842e-01, 6.81594244e-01, 3.89694935e-01],
           [8.53314455e-01, 6.85009619e-01, 3.86726375e-01],
           [8.59651987e-01, 6.88554169e-01, 3.83662475e-01],
           [8.65745779e-01, 6.92241759e-01, 3.80538152e-01],
           [8.71571891e-01, 6.96083354e-01, 3.77395989e-01],
           [8.77113987e-01, 7.00085649e-01, 3.74282589e-01],
           [8.82365297e-01, 7.04250314e-01, 3.71242784e-01],
           [8.87328591e-01, 7.08574087e-01, 3.68317382e-01],
           [8.92015211e-01, 7.13049652e-01, 3.65536210e-01],
           [8.96442460e-01, 7.17666887e-01, 3.62920433e-01],
           [9.00631157e-01, 7.22414262e-01, 3.60480779e-01],
           [9.04603566e-01, 7.27279735e-01, 3.58221818e-01],
           [9.08381333e-01, 7.32252004e-01, 3.56139118e-01],
           [9.11985382e-01, 7.37320105e-01, 3.54228653e-01],
           [9.15433981e-01, 7.42474841e-01, 3.52478848e-01],
           [9.18743621e-01, 7.47707899e-01, 3.50879063e-01],
           [9.21929804e-01, 7.53011369e-01, 3.49421661e-01],
           [9.25004192e-01, 7.58379699e-01, 3.48091716e-01],
           [9.27978539e-01, 7.63807005e-01, 3.46881019e-01],
           [9.30861574e-01, 7.69289179e-01, 3.45777107e-01],
           [9.33662251e-01, 7.74821809e-01, 3.44772498e-01],
           [9.36388081e-01, 7.80401282e-01, 3.43859117e-01],
           [9.39044540e-01, 7.86025118e-01, 3.43026985e-01],
           [9.41638102e-01, 7.91690163e-01, 3.42270957e-01],
           [9.44172811e-01, 7.97394647e-01, 3.41582527e-01],
           [9.46652148e-01, 8.03137054e-01, 3.40954052e-01],
           [9.49079897e-01, 8.08915648e-01, 3.40380104e-01],
           [9.51460984e-01, 8.14728035e-01, 3.39858564e-01],
           [9.53795301e-01, 8.20574615e-01, 3.39378975e-01],
           [9.56088241e-01, 8.26452703e-01, 3.38942047e-01],
           [9.58340089e-01, 8.32362423e-01, 3.38540041e-01],
           [9.60552113e-01, 8.38303320e-01, 3.38167899e-01],
           [9.62728332e-01, 8.44273459e-01, 3.37825789e-01],
           [9.64869193e-01, 8.50272818e-01, 3.37508378e-01],
           [9.66975327e-01, 8.56301253e-01, 3.37211242e-01],
           [9.69048080e-01, 8.62358233e-01, 3.36931587e-01],
           [9.71088583e-01, 8.68443333e-01, 3.36666655e-01],
           [9.73097773e-01, 8.74556226e-01, 3.36413723e-01],
           [9.75076400e-01, 8.80696674e-01, 3.36170099e-01],
           [9.77025044e-01, 8.86864522e-01, 3.35933113e-01],
           [9.78944121e-01, 8.93059690e-01, 3.35700119e-01],
           [9.80833901e-01, 8.99282165e-01, 3.35468483e-01],
           [9.82694509e-01, 9.05531996e-01, 3.35235583e-01],
           [9.84528415e-01, 9.11808090e-01, 3.35002383e-01],
           [9.86334645e-01, 9.18111039e-01, 3.34764988e-01],
           [9.88111987e-01, 9.24441528e-01, 3.34519366e-01],
           [9.89860091e-01, 9.30799810e-01, 3.34262892e-01],
           [9.91583502e-01, 9.37183820e-01, 3.34000024e-01],
           [9.93278187e-01, 9.43595566e-01, 3.33723115e-01],
           [9.94942662e-01, 9.50035812e-01, 3.33428313e-01]]

test_cm = ListedColormap(cm_data, name="eclipse")
