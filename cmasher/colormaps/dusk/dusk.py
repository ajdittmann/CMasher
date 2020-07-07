# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"


# %% GLOBALS AND DEFINITIONS
# Type of this colormap (according to viscm)
cm_type = "linear"

# RGB-values of this colormap
cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.25036546e-04, 2.28327198e-04, 3.25089265e-04],
           [7.72173553e-04, 7.89716201e-04, 1.18974705e-03],
           [1.58437653e-03, 1.63173767e-03, 2.58887866e-03],
           [2.63486115e-03, 2.73041342e-03, 4.54336709e-03],
           [3.90604117e-03, 4.07008298e-03, 7.08081900e-03],
           [5.38485891e-03, 5.63908610e-03, 1.02329422e-02],
           [7.06082302e-03, 7.42799729e-03, 1.40356337e-02],
           [8.92568441e-03, 9.42907020e-03, 1.85231924e-02],
           [1.09723005e-02, 1.16354901e-02, 2.37332235e-02],
           [1.31941164e-02, 1.40409362e-02, 2.97087555e-02],
           [1.55855170e-02, 1.66396850e-02, 3.64928370e-02],
           [1.81419275e-02, 1.94266828e-02, 4.39721402e-02],
           [2.08581855e-02, 2.23964683e-02, 5.15385255e-02],
           [2.37302706e-02, 2.55442586e-02, 5.91473864e-02],
           [2.67545244e-02, 2.88654859e-02, 6.68034952e-02],
           [2.99262451e-02, 3.23546676e-02, 7.45214572e-02],
           [3.32430526e-02, 3.60080586e-02, 8.22969717e-02],
           [3.66999423e-02, 3.98196426e-02, 9.01472541e-02],
           [4.02948385e-02, 4.36541538e-02, 9.80668135e-02],
           [4.38767569e-02, 4.74163685e-02, 1.06067697e-01],
           [4.73997313e-02, 5.11166730e-02, 1.14152370e-01],
           [5.08691721e-02, 5.47576750e-02, 1.22321125e-01],
           [5.42860749e-02, 5.83400602e-02, 1.30586123e-01],
           [5.76526408e-02, 6.18658127e-02, 1.38947632e-01],
           [6.09704442e-02, 6.53364649e-02, 1.47407743e-01],
           [6.42403438e-02, 6.87529617e-02, 1.55971290e-01],
           [6.74628775e-02, 7.21160974e-02, 1.64642880e-01],
           [7.06382601e-02, 7.54265586e-02, 1.73426842e-01],
           [7.37663729e-02, 7.86849690e-02, 1.82327155e-01],
           [7.68467461e-02, 8.18919398e-02, 1.91347359e-01],
           [7.98785320e-02, 8.50481248e-02, 2.00490460e-01],
           [8.28604694e-02, 8.81542834e-02, 2.09758801e-01],
           [8.57908379e-02, 9.12113538e-02, 2.19153922e-01],
           [8.86657196e-02, 9.42181738e-02, 2.28689570e-01],
           [9.14833705e-02, 9.71777973e-02, 2.38356277e-01],
           [9.42382863e-02, 1.00089470e-01, 2.48166910e-01],
           [9.69262865e-02, 1.02956090e-01, 2.58115676e-01],
           [9.95401630e-02, 1.05778522e-01, 2.68209736e-01],
           [1.02071430e-01, 1.08558652e-01, 2.78453139e-01],
           [1.04510498e-01, 1.11300288e-01, 2.88843233e-01],
           [1.06844018e-01, 1.14006569e-01, 2.99385121e-01],
           [1.09057411e-01, 1.16684386e-01, 3.10070433e-01],
           [1.11130300e-01, 1.19340220e-01, 3.20900320e-01],
           [1.13038378e-01, 1.21984510e-01, 3.31865750e-01],
           [1.14749734e-01, 1.24630199e-01, 3.42958131e-01],
           [1.16225101e-01, 1.27296288e-01, 3.54155589e-01],
           [1.17410887e-01, 1.30006202e-01, 3.65437553e-01],
           [1.18242136e-01, 1.32795304e-01, 3.76752930e-01],
           [1.18629846e-01, 1.35708648e-01, 3.88042191e-01],
           [1.18466390e-01, 1.38810246e-01, 3.99194384e-01],
           [1.17615027e-01, 1.42182052e-01, 4.10056591e-01],
           [1.15924034e-01, 1.45925887e-01, 4.20399185e-01],
           [1.13258155e-01, 1.50150040e-01, 4.29911449e-01],
           [1.09546854e-01, 1.54936741e-01, 4.38247945e-01],
           [1.04848450e-01, 1.60299084e-01, 4.45117162e-01],
           [9.93518341e-02, 1.66160674e-01, 4.50393522e-01],
           [9.33149422e-02, 1.72383599e-01, 4.54142315e-01],
           [8.69971012e-02, 1.78818405e-01, 4.56551516e-01],
           [8.06284456e-02, 1.85338572e-01, 4.57846037e-01],
           [7.44151890e-02, 1.91850174e-01, 4.58235726e-01],
           [6.85554496e-02, 1.98288225e-01, 4.57897553e-01],
           [6.32524141e-02, 2.04609438e-01, 4.56975623e-01],
           [5.87166274e-02, 2.10786270e-01, 4.55585971e-01],
           [5.51602987e-02, 2.16801865e-01, 4.53823282e-01],
           [5.27787066e-02, 2.22646735e-01, 4.51766402e-01],
           [5.17210829e-02, 2.28317008e-01, 4.49481071e-01],
           [5.20647149e-02, 2.33812536e-01, 4.47023718e-01],
           [5.37984241e-02, 2.39136225e-01, 4.44442172e-01],
           [5.68281829e-02, 2.44293002e-01, 4.41777814e-01],
           [6.09994158e-02, 2.49289375e-01, 4.39065993e-01],
           [6.61274729e-02, 2.54132769e-01, 4.36337773e-01],
           [7.20246675e-02, 2.58831681e-01, 4.33617617e-01],
           [7.85187368e-02, 2.63394728e-01, 4.30927282e-01],
           [8.54613781e-02, 2.67830707e-01, 4.28284790e-01],
           [9.27305703e-02, 2.72148422e-01, 4.25704583e-01],
           [1.00228980e-01, 2.76356511e-01, 4.23197933e-01],
           [1.07880596e-01, 2.80463302e-01, 4.20773409e-01],
           [1.15625433e-01, 2.84476567e-01, 4.18439886e-01],
           [1.23419360e-01, 2.88403917e-01, 4.16200834e-01],
           [1.31227867e-01, 2.92252334e-01, 4.14060584e-01],
           [1.39024965e-01, 2.96028366e-01, 4.12022062e-01],
           [1.46791321e-01, 2.99738119e-01, 4.10087001e-01],
           [1.54512753e-01, 3.03387261e-01, 4.08256158e-01],
           [1.62179049e-01, 3.06981034e-01, 4.06529521e-01],
           [1.69783039e-01, 3.10524270e-01, 4.04906478e-01],
           [1.77319519e-01, 3.14021429e-01, 4.03386454e-01],
           [1.84784595e-01, 3.17476648e-01, 4.01969140e-01],
           [1.92177013e-01, 3.20893702e-01, 4.00652200e-01],
           [1.99495076e-01, 3.24276125e-01, 3.99435094e-01],
           [2.06738657e-01, 3.27627159e-01, 3.98316052e-01],
           [2.13908268e-01, 3.30949789e-01, 3.97293125e-01],
           [2.21004410e-01, 3.34246809e-01, 3.96364870e-01],
           [2.28027771e-01, 3.37520831e-01, 3.95529948e-01],
           [2.34979537e-01, 3.40774271e-01, 3.94786606e-01],
           [2.41861066e-01, 3.44009379e-01, 3.94133028e-01],
           [2.48673604e-01, 3.47228284e-01, 3.93567629e-01],
           [2.55418412e-01, 3.50432998e-01, 3.93088828e-01],
           [2.62096519e-01, 3.53625455e-01, 3.92695309e-01],
           [2.68709137e-01, 3.56807478e-01, 3.92385430e-01],
           [2.75257376e-01, 3.59980822e-01, 3.92157543e-01],
           [2.81742123e-01, 3.63147203e-01, 3.92010085e-01],
           [2.88164083e-01, 3.66308311e-01, 3.91941471e-01],
           [2.94523358e-01, 3.69465892e-01, 3.91950556e-01],
           [3.00820499e-01, 3.72621605e-01, 3.92035196e-01],
           [3.07055579e-01, 3.75777172e-01, 3.92193334e-01],
           [3.13227892e-01, 3.78934464e-01, 3.92423285e-01],
           [3.19337115e-01, 3.82095323e-01, 3.92722061e-01],
           [3.25382257e-01, 3.85261766e-01, 3.93086567e-01],
           [3.31361872e-01, 3.88435977e-01, 3.93513132e-01],
           [3.37274731e-01, 3.91620208e-01, 3.93996376e-01],
           [3.43118773e-01, 3.94817002e-01, 3.94530385e-01],
           [3.48892711e-01, 3.98028907e-01, 3.95106331e-01],
           [3.54594859e-01, 4.01258703e-01, 3.95713949e-01],
           [3.60225060e-01, 4.04509006e-01, 3.96338913e-01],
           [3.65784180e-01, 4.07782300e-01, 3.96963964e-01],
           [3.71276142e-01, 4.11080406e-01, 3.97566868e-01],
           [3.76708412e-01, 4.14404168e-01, 3.98121365e-01],
           [3.82093831e-01, 4.17752788e-01, 3.98596778e-01],
           [3.87451425e-01, 4.21123294e-01, 3.98959807e-01],
           [3.92806830e-01, 4.24510080e-01, 3.99176831e-01],
           [3.98191510e-01, 4.27904816e-01, 3.99217093e-01],
           [4.03640262e-01, 4.31296901e-01, 3.99056652e-01],
           [4.09187969e-01, 4.34674398e-01, 3.98680831e-01],
           [4.14865604e-01, 4.38025344e-01, 3.98085909e-01],
           [4.20697226e-01, 4.41339004e-01, 3.97278249e-01],
           [4.26698307e-01, 4.44606804e-01, 3.96272117e-01],
           [4.32875825e-01, 4.47822715e-01, 3.95086469e-01],
           [4.39229391e-01, 4.50983209e-01, 3.93742287e-01],
           [4.45753457e-01, 4.54086800e-01, 3.92259724e-01],
           [4.52438961e-01, 4.57133569e-01, 3.90657301e-01],
           [4.59275329e-01, 4.60124569e-01, 3.88950649e-01],
           [4.66251569e-01, 4.63061412e-01, 3.87152657e-01],
           [4.73356971e-01, 4.65945966e-01, 3.85273868e-01],
           [4.80582007e-01, 4.68780026e-01, 3.83322107e-01],
           [4.87917716e-01, 4.71565387e-01, 3.81304235e-01],
           [4.95356964e-01, 4.74303452e-01, 3.79224592e-01],
           [5.02892830e-01, 4.76995626e-01, 3.77087805e-01],
           [5.10520347e-01, 4.79642797e-01, 3.74896200e-01],
           [5.18234416e-01, 4.82245913e-01, 3.72653063e-01],
           [5.26031604e-01, 4.84805430e-01, 3.70359897e-01],
           [5.33908438e-01, 4.87321819e-01, 3.68018972e-01],
           [5.41862253e-01, 4.89795293e-01, 3.65631999e-01],
           [5.49891220e-01, 4.92225784e-01, 3.63200077e-01],
           [5.57993005e-01, 4.94613376e-01, 3.60725596e-01],
           [5.66166506e-01, 4.96957727e-01, 3.58209669e-01],
           [5.74410627e-01, 4.99258466e-01, 3.55653899e-01],
           [5.82724047e-01, 5.01515284e-01, 3.53060662e-01],
           [5.91106052e-01, 5.03727632e-01, 3.50431905e-01],
           [5.99556401e-01, 5.05894761e-01, 3.47769338e-01],
           [6.08074574e-01, 5.08015988e-01, 3.45075485e-01],
           [6.16660031e-01, 5.10090614e-01, 3.42353320e-01],
           [6.25312560e-01, 5.12117780e-01, 3.39605774e-01],
           [6.34032016e-01, 5.14096568e-01, 3.36836131e-01],
           [6.42818293e-01, 5.16026002e-01, 3.34048068e-01],
           [6.51671301e-01, 5.17905065e-01, 3.31245714e-01],
           [6.60590942e-01, 5.19732699e-01, 3.28433709e-01],
           [6.69577082e-01, 5.21507824e-01, 3.25617267e-01],
           [6.78629973e-01, 5.23229142e-01, 3.22801665e-01],
           [6.87749536e-01, 5.24895450e-01, 3.19993234e-01],
           [6.96934983e-01, 5.26505833e-01, 3.17199875e-01],
           [7.06186451e-01, 5.28058902e-01, 3.14428993e-01],
           [7.15503776e-01, 5.29553355e-01, 3.11689167e-01],
           [7.24885946e-01, 5.30988257e-01, 3.08990861e-01],
           [7.34332513e-01, 5.32362355e-01, 3.06344727e-01],
           [7.43842962e-01, 5.33674377e-01, 3.03762489e-01],
           [7.53415491e-01, 5.34923673e-01, 3.01258452e-01],
           [7.63048828e-01, 5.36109293e-01, 2.98847395e-01],
           [7.72741239e-01, 5.37230498e-01, 2.96545841e-01],
           [7.82490439e-01, 5.38286827e-01, 2.94372215e-01],
           [7.92293494e-01, 5.39278172e-01, 2.92347003e-01],
           [8.02146714e-01, 5.40204864e-01, 2.90492894e-01],
           [8.12047070e-01, 5.41066867e-01, 2.88833444e-01],
           [8.21988159e-01, 5.41866157e-01, 2.87397108e-01],
           [8.31965579e-01, 5.42603596e-01, 2.86212059e-01],
           [8.41971260e-01, 5.43282347e-01, 2.85311557e-01],
           [8.51997117e-01, 5.43905728e-01, 2.84730576e-01],
           [8.62033228e-01, 5.44478371e-01, 2.84507511e-01],
           [8.72067531e-01, 5.45006481e-01, 2.84684415e-01],
           [8.82087007e-01, 5.45497108e-01, 2.85306528e-01],
           [8.92073303e-01, 5.45961142e-01, 2.86425190e-01],
           [9.02006208e-01, 5.46411069e-01, 2.88096311e-01],
           [9.11860107e-01, 5.46863448e-01, 2.90383280e-01],
           [9.21601991e-01, 5.47340447e-01, 2.93358885e-01],
           [9.31190423e-01, 5.47870658e-01, 2.97108001e-01],
           [9.40568830e-01, 5.48494149e-01, 3.01731674e-01],
           [9.49660923e-01, 5.49266053e-01, 3.07351127e-01],
           [9.58360370e-01, 5.50264711e-01, 3.14110122e-01],
           [9.66519027e-01, 5.51601462e-01, 3.22168690e-01],
           [9.73937891e-01, 5.53429722e-01, 3.31669694e-01],
           [9.80385065e-01, 5.55934591e-01, 3.42661497e-01],
           [9.85666111e-01, 5.59282252e-01, 3.54979696e-01],
           [9.89733764e-01, 5.63532400e-01, 3.68215204e-01],
           [9.92724216e-01, 5.68600188e-01, 3.81863166e-01],
           [9.94868638e-01, 5.74316114e-01, 3.95535378e-01],
           [9.96390418e-01, 5.80507321e-01, 4.09015519e-01],
           [9.97461713e-01, 5.87036044e-01, 4.22215116e-01],
           [9.98201891e-01, 5.93804045e-01, 4.35118082e-01],
           [9.98696145e-01, 6.00740825e-01, 4.47731141e-01],
           [9.98998743e-01, 6.07799899e-01, 4.60082683e-01],
           [9.99153904e-01, 6.14944868e-01, 4.72191299e-01],
           [9.99187376e-01, 6.22153195e-01, 4.84087055e-01],
           [9.99119518e-01, 6.29407602e-01, 4.95793441e-01],
           [9.98974103e-01, 6.36690474e-01, 5.07319005e-01],
           [9.98754081e-01, 6.43997318e-01, 5.18694662e-01],
           [9.98474506e-01, 6.51317581e-01, 5.29927838e-01],
           [9.98144762e-01, 6.58644657e-01, 5.41029704e-01],
           [9.97772664e-01, 6.65973374e-01, 5.52010094e-01],
           [9.97361709e-01, 6.73301327e-01, 5.62881436e-01],
           [9.96913236e-01, 6.80627530e-01, 5.73656231e-01],
           [9.96438497e-01, 6.87946003e-01, 5.84333385e-01],
           [9.95933948e-01, 6.95258787e-01, 5.94927812e-01],
           [9.95413397e-01, 7.02559098e-01, 6.05433313e-01],
           [9.94870775e-01, 7.09850530e-01, 6.15865211e-01],
           [9.94311015e-01, 7.17131117e-01, 6.26225491e-01],
           [9.93738226e-01, 7.24399451e-01, 6.36516479e-01],
           [9.93155786e-01, 7.31654600e-01, 6.46740777e-01],
           [9.92566416e-01, 7.38896035e-01, 6.56901204e-01],
           [9.91972263e-01, 7.46123565e-01, 6.67000741e-01],
           [9.91374964e-01, 7.53337280e-01, 6.77042484e-01],
           [9.90775721e-01, 7.60537498e-01, 6.87029601e-01],
           [9.90175356e-01, 7.67724726e-01, 6.96965291e-01],
           [9.89580284e-01, 7.74896988e-01, 7.06847195e-01],
           [9.88995676e-01, 7.82052981e-01, 7.16674126e-01],
           [9.88413220e-01, 7.89197339e-01, 7.26457222e-01],
           [9.87844771e-01, 7.96325863e-01, 7.36188723e-01],
           [9.87289490e-01, 8.03439947e-01, 7.45872533e-01],
           [9.86746123e-01, 8.10541117e-01, 7.55512676e-01],
           [9.86225265e-01, 8.17625962e-01, 7.65102597e-01],
           [9.85720710e-01, 8.24698099e-01, 7.74650490e-01],
           [9.85240620e-01, 8.31755214e-01, 7.84151894e-01],
           [9.84787894e-01, 8.38797213e-01, 7.93606955e-01],
           [9.84355217e-01, 8.45828042e-01, 8.03024317e-01],
           [9.83966419e-01, 8.52839382e-01, 8.12386517e-01],
           [9.83606171e-01, 8.59838354e-01, 8.21708819e-01],
           [9.83278335e-01, 8.66824484e-01, 8.30990329e-01],
           [9.83001151e-01, 8.73791935e-01, 8.40218671e-01],
           [9.82767679e-01, 8.80744494e-01, 8.49401943e-01],
           [9.82580301e-01, 8.87682371e-01, 8.58540626e-01],
           [9.82444525e-01, 8.94604639e-01, 8.67632777e-01],
           [9.82373124e-01, 9.01507807e-01, 8.76670956e-01],
           [9.82369642e-01, 9.08391818e-01, 8.85655118e-01],
           [9.82436783e-01, 9.15256910e-01, 8.94585959e-01],
           [9.82583200e-01, 9.22101229e-01, 9.03459817e-01],
           [9.82819209e-01, 9.28922401e-01, 9.12272134e-01],
           [9.83157556e-01, 9.35717276e-01, 9.21017064e-01],
           [9.83614715e-01, 9.42481486e-01, 9.29686835e-01],
           [9.84213258e-01, 9.49208641e-01, 9.38270660e-01],
           [9.84986752e-01, 9.55888601e-01, 9.46752852e-01],
           [9.85991890e-01, 9.62502887e-01, 9.55111087e-01],
           [9.87362188e-01, 9.68994884e-01, 9.63397871e-01],
           [9.90152568e-01, 9.75015711e-01, 9.70940780e-01],
           [9.92906793e-01, 9.81131369e-01, 9.77966737e-01],
           [9.95422785e-01, 9.87349697e-01, 9.85171861e-01],
           [9.97777892e-01, 9.93642381e-01, 9.92523576e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.dusk", N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
