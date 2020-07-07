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
           [2.18978444e-04, 1.77540646e-04, 2.55612013e-04],
           [7.68124580e-04, 6.08776467e-04, 9.25389883e-04],
           [1.60743304e-03, 1.24801543e-03, 1.99558151e-03],
           [2.72048166e-03, 2.07363753e-03, 3.47485305e-03],
           [4.09715583e-03, 3.07139249e-03, 5.37786044e-03],
           [5.73018628e-03, 4.23073344e-03, 7.72233034e-03],
           [7.61380934e-03, 5.54335658e-03, 1.05279395e-02],
           [9.74316966e-03, 7.00241938e-03, 1.38160755e-02],
           [1.21139195e-02, 8.60215564e-03, 1.76093743e-02],
           [1.47220226e-02, 1.03375904e-02, 2.19317037e-02],
           [1.75636340e-02, 1.22043364e-02, 2.68082763e-02],
           [2.06349585e-02, 1.41985119e-02, 3.22653727e-02],
           [2.39321803e-02, 1.63166491e-02, 3.83303458e-02],
           [2.74514250e-02, 1.85556037e-02, 4.48143024e-02],
           [3.11887041e-02, 2.09125099e-02, 5.13195203e-02],
           [3.51398654e-02, 2.33847472e-02, 5.78545958e-02],
           [3.93005180e-02, 2.59699639e-02, 6.44243769e-02],
           [4.35416128e-02, 2.86659924e-02, 7.10332953e-02],
           [4.77103734e-02, 3.14708616e-02, 7.76853131e-02],
           [5.18184827e-02, 3.43827896e-02, 8.43839988e-02],
           [5.58674191e-02, 3.74001823e-02, 9.11325837e-02],
           [5.98582631e-02, 4.05203677e-02, 9.79340035e-02],
           [6.37917313e-02, 4.36167095e-02, 1.04790928e-01],
           [6.76681997e-02, 4.66743313e-02, 1.11705782e-01],
           [7.14877210e-02, 4.96957395e-02, 1.18680754e-01],
           [7.52500517e-02, 5.26832389e-02, 1.25718267e-01],
           [7.89545993e-02, 5.56392251e-02, 1.32819807e-01],
           [8.26004715e-02, 5.85660208e-02, 1.39986815e-01],
           [8.61864649e-02, 6.14658124e-02, 1.47221131e-01],
           [8.97110198e-02, 6.43409488e-02, 1.54523749e-01],
           [9.31722230e-02, 6.71938134e-02, 1.61895543e-01],
           [9.65677748e-02, 7.00268571e-02, 1.69337261e-01],
           [9.98949472e-02, 7.28426366e-02, 1.76849496e-01],
           [1.03150569e-01, 7.56440312e-02, 1.84431780e-01],
           [1.06330947e-01, 7.84340173e-02, 1.92083865e-01],
           [1.09431808e-01, 8.12158616e-02, 1.99804968e-01],
           [1.12448240e-01, 8.39931890e-02, 2.07593650e-01],
           [1.15374609e-01, 8.67700585e-02, 2.15447655e-01],
           [1.18204478e-01, 8.95510506e-02, 2.23363720e-01],
           [1.20930510e-01, 9.23413649e-02, 2.31337335e-01],
           [1.23544151e-01, 9.51466855e-02, 2.39363937e-01],
           [1.26035909e-01, 9.79738624e-02, 2.47435348e-01],
           [1.28394603e-01, 1.00830347e-01, 2.55543606e-01],
           [1.30607778e-01, 1.03724978e-01, 2.63676635e-01],
           [1.32661245e-01, 1.06667802e-01, 2.71819724e-01],
           [1.34538696e-01, 1.09670176e-01, 2.79955478e-01],
           [1.36222488e-01, 1.12745301e-01, 2.88059723e-01],
           [1.37692483e-01, 1.15907767e-01, 2.96104969e-01],
           [1.38927508e-01, 1.19173938e-01, 3.04055365e-01],
           [1.39905289e-01, 1.22561419e-01, 3.11868095e-01],
           [1.40603690e-01, 1.26088506e-01, 3.19492294e-01],
           [1.41003278e-01, 1.29773055e-01, 3.26868058e-01],
           [1.41089047e-01, 1.33630747e-01, 3.33929711e-01],
           [1.40854845e-01, 1.37672747e-01, 3.40607651e-01],
           [1.40305823e-01, 1.41903258e-01, 3.46835410e-01],
           [1.39460917e-01, 1.46317501e-01, 3.52556695e-01],
           [1.38352990e-01, 1.50900955e-01, 3.57732791e-01],
           [1.37025891e-01, 1.55630563e-01, 3.62347754e-01],
           [1.35529983e-01, 1.60477450e-01, 3.66409159e-01],
           [1.33916822e-01, 1.65410486e-01, 3.69944837e-01],
           [1.32235244e-01, 1.70399391e-01, 3.72996977e-01],
           [1.30527691e-01, 1.75417337e-01, 3.75615625e-01],
           [1.28830854e-01, 1.80441516e-01, 3.77853384e-01],
           [1.27173815e-01, 1.85454032e-01, 3.79761298e-01],
           [1.25579932e-01, 1.90441170e-01, 3.81386712e-01],
           [1.24066902e-01, 1.95393095e-01, 3.82771914e-01],
           [1.22648951e-01, 2.00302743e-01, 3.83954348e-01],
           [1.21336886e-01, 2.05165450e-01, 3.84966583e-01],
           [1.20138210e-01, 2.09978592e-01, 3.85836410e-01],
           [1.19057929e-01, 2.14741032e-01, 3.86587425e-01],
           [1.18101117e-01, 2.19452059e-01, 3.87240904e-01],
           [1.17268737e-01, 2.24112583e-01, 3.87813587e-01],
           [1.16561858e-01, 2.28723615e-01, 3.88320502e-01],
           [1.15980312e-01, 2.33286606e-01, 3.88774449e-01],
           [1.15522723e-01, 2.37803364e-01, 3.89186215e-01],
           [1.15186690e-01, 2.42275932e-01, 3.89564873e-01],
           [1.14970282e-01, 2.46706094e-01, 3.89919113e-01],
           [1.14868752e-01, 2.51096370e-01, 3.90254789e-01],
           [1.14878812e-01, 2.55448673e-01, 3.90578402e-01],
           [1.14994902e-01, 2.59765462e-01, 3.90894150e-01],
           [1.15212580e-01, 2.64048698e-01, 3.91206811e-01],
           [1.15526272e-01, 2.68300543e-01, 3.91519899e-01],
           [1.15929805e-01, 2.72523197e-01, 3.91836101e-01],
           [1.16417124e-01, 2.76718699e-01, 3.92157945e-01],
           [1.16981917e-01, 2.80889053e-01, 3.92487473e-01],
           [1.17617671e-01, 2.85036219e-01, 3.92826293e-01],
           [1.18317741e-01, 2.89162110e-01, 3.93175634e-01],
           [1.19076055e-01, 2.93268398e-01, 3.93537027e-01],
           [1.19885357e-01, 2.97357037e-01, 3.93910581e-01],
           [1.20738849e-01, 3.01429791e-01, 3.94296559e-01],
           [1.21630402e-01, 3.05488197e-01, 3.94695598e-01],
           [1.22553375e-01, 3.09533904e-01, 3.95107520e-01],
           [1.23501003e-01, 3.13568569e-01, 3.95531708e-01],
           [1.24467728e-01, 3.17593499e-01, 3.95968416e-01],
           [1.25446660e-01, 3.21610353e-01, 3.96416248e-01],
           [1.26432467e-01, 3.25620359e-01, 3.96875003e-01],
           [1.27419088e-01, 3.29624938e-01, 3.97343422e-01],
           [1.28400696e-01, 3.33625444e-01, 3.97820135e-01],
           [1.29372840e-01, 3.37622881e-01, 3.98304750e-01],
           [1.30329586e-01, 3.41618634e-01, 3.98795106e-01],
           [1.31266108e-01, 3.45613805e-01, 3.99289767e-01],
           [1.32178024e-01, 3.49609394e-01, 3.99787373e-01],
           [1.33061023e-01, 3.53606390e-01, 4.00286289e-01],
           [1.33910625e-01, 3.57605824e-01, 4.00784407e-01],
           [1.34722938e-01, 3.61608589e-01, 4.01279843e-01],
           [1.35494318e-01, 3.65615525e-01, 4.01770626e-01],
           [1.36221365e-01, 3.69627414e-01, 4.02254706e-01],
           [1.36900928e-01, 3.73644986e-01, 4.02729961e-01],
           [1.37530108e-01, 3.77668915e-01, 4.03194211e-01],
           [1.38106334e-01, 3.81699803e-01, 4.03645293e-01],
           [1.38627098e-01, 3.85738236e-01, 4.04080848e-01],
           [1.39090229e-01, 3.89784726e-01, 4.04498561e-01],
           [1.39493823e-01, 3.93839728e-01, 4.04896114e-01],
           [1.39836221e-01, 3.97903642e-01, 4.05271174e-01],
           [1.40116049e-01, 4.01976808e-01, 4.05621438e-01],
           [1.40332173e-01, 4.06059516e-01, 4.05944605e-01],
           [1.40483590e-01, 4.10152026e-01, 4.06238307e-01],
           [1.40569586e-01, 4.14254539e-01, 4.06500240e-01],
           [1.40589678e-01, 4.18367210e-01, 4.06728126e-01],
           [1.40543605e-01, 4.22490150e-01, 4.06919716e-01],
           [1.40431329e-01, 4.26623427e-01, 4.07072802e-01],
           [1.40253031e-01, 4.30767068e-01, 4.07185217e-01],
           [1.40009108e-01, 4.34921065e-01, 4.07254839e-01],
           [1.39700185e-01, 4.39085370e-01, 4.07279610e-01],
           [1.39327361e-01, 4.43259858e-01, 4.07257700e-01],
           [1.38891368e-01, 4.47444471e-01, 4.07186940e-01],
           [1.38393443e-01, 4.51639073e-01, 4.07065424e-01],
           [1.37835033e-01, 4.55843500e-01, 4.06891299e-01],
           [1.37217797e-01, 4.60057565e-01, 4.06662773e-01],
           [1.36543781e-01, 4.64281031e-01, 4.06378226e-01],
           [1.35815013e-01, 4.68513680e-01, 4.06035939e-01],
           [1.35033665e-01, 4.72755289e-01, 4.05634193e-01],
           [1.34202277e-01, 4.77005594e-01, 4.05171417e-01],
           [1.33323627e-01, 4.81264321e-01, 4.04646093e-01],
           [1.32400946e-01, 4.85531150e-01, 4.04056888e-01],
           [1.31437279e-01, 4.89805818e-01, 4.03402221e-01],
           [1.30436159e-01, 4.94088020e-01, 4.02680698e-01],
           [1.29401421e-01, 4.98377439e-01, 4.01890977e-01],
           [1.28337274e-01, 5.02673741e-01, 4.01031801e-01],
           [1.27248083e-01, 5.06976611e-01, 4.00101839e-01],
           [1.26138585e-01, 5.11285721e-01, 3.99099811e-01],
           [1.25013922e-01, 5.15600733e-01, 3.98024495e-01],
           [1.23879597e-01, 5.19921307e-01, 3.96874678e-01],
           [1.22741459e-01, 5.24247108e-01, 3.95649132e-01],
           [1.21605832e-01, 5.28577789e-01, 3.94346678e-01],
           [1.20479482e-01, 5.32912999e-01, 3.92966147e-01],
           [1.19369555e-01, 5.37252397e-01, 3.91506323e-01],
           [1.18283611e-01, 5.41595645e-01, 3.89965947e-01],
           [1.17229917e-01, 5.45942375e-01, 3.88343906e-01],
           [1.16217124e-01, 5.50292231e-01, 3.86639005e-01],
           [1.15254373e-01, 5.54644856e-01, 3.84850029e-01],
           [1.14350903e-01, 5.58999935e-01, 3.82975451e-01],
           [1.13517112e-01, 5.63357068e-01, 3.81014218e-01],
           [1.12763541e-01, 5.67715890e-01, 3.78965025e-01],
           [1.12101139e-01, 5.72076034e-01, 3.76826522e-01],
           [1.11541128e-01, 5.76437135e-01, 3.74597246e-01],
           [1.11094762e-01, 5.80798857e-01, 3.72275455e-01],
           [1.10774230e-01, 5.85160774e-01, 3.69859925e-01],
           [1.10591474e-01, 5.89522498e-01, 3.67349070e-01],
           [1.10558450e-01, 5.93883635e-01, 3.64741224e-01],
           [1.10687012e-01, 5.98243782e-01, 3.62034637e-01],
           [1.10988789e-01, 6.02602527e-01, 3.59227460e-01],
           [1.11474655e-01, 6.06959494e-01, 3.56317337e-01],
           [1.12155791e-01, 6.11314204e-01, 3.53302575e-01],
           [1.13042392e-01, 6.15666207e-01, 3.50181003e-01],
           [1.14143895e-01, 6.20015039e-01, 3.46950300e-01],
           [1.15468904e-01, 6.24360221e-01, 3.43607991e-01],
           [1.17025102e-01, 6.28701255e-01, 3.40151435e-01],
           [1.18819198e-01, 6.33037619e-01, 3.36577815e-01],
           [1.20856893e-01, 6.37368772e-01, 3.32884114e-01],
           [1.23142882e-01, 6.41694141e-01, 3.29067103e-01],
           [1.25680878e-01, 6.46013126e-01, 3.25123317e-01],
           [1.28473667e-01, 6.50325094e-01, 3.21049035e-01],
           [1.31523184e-01, 6.54629372e-01, 3.16840260e-01],
           [1.34830613e-01, 6.58925248e-01, 3.12492687e-01],
           [1.38396502e-01, 6.63211960e-01, 3.08001680e-01],
           [1.42220632e-01, 6.67488759e-01, 3.03361206e-01],
           [1.46302855e-01, 6.71754747e-01, 2.98566090e-01],
           [1.50642739e-01, 6.76008961e-01, 2.93610806e-01],
           [1.55239640e-01, 6.80250386e-01, 2.88488963e-01],
           [1.60092832e-01, 6.84478012e-01, 2.83191713e-01],
           [1.65202103e-01, 6.88690628e-01, 2.77711460e-01],
           [1.70567480e-01, 6.92886869e-01, 2.72041195e-01],
           [1.76189592e-01, 6.97065481e-01, 2.66166809e-01],
           [1.82069443e-01, 7.01224734e-01, 2.60082247e-01],
           [1.88209492e-01, 7.05363067e-01, 2.53770047e-01],
           [1.94612256e-01, 7.09478441e-01, 2.47220956e-01],
           [2.01282185e-01, 7.13568785e-01, 2.40417041e-01],
           [2.08225042e-01, 7.17631706e-01, 2.33339800e-01],
           [2.15447556e-01, 7.21664459e-01, 2.25971105e-01],
           [2.22958742e-01, 7.25663971e-01, 2.18287684e-01],
           [2.30769736e-01, 7.29626710e-01, 2.10263187e-01],
           [2.38894054e-01, 7.33548601e-01, 2.01867802e-01],
           [2.47347874e-01, 7.37424919e-01, 1.93067874e-01],
           [2.56153355e-01, 7.41250048e-01, 1.83817223e-01],
           [2.65331947e-01, 7.45017518e-01, 1.74077112e-01],
           [2.74916319e-01, 7.48719349e-01, 1.63784186e-01],
           [2.84939947e-01, 7.52346206e-01, 1.52880519e-01],
           [2.95445971e-01, 7.55886631e-01, 1.41292533e-01],
           [3.06485395e-01, 7.59326660e-01, 1.28940105e-01],
           [3.18119794e-01, 7.62649051e-01, 1.15737789e-01],
           [3.30414817e-01, 7.65833241e-01, 1.01625328e-01],
           [3.43439338e-01, 7.68854899e-01, 8.66041228e-02],
           [3.57251624e-01, 7.71687052e-01, 7.08515709e-02],
           [3.71857810e-01, 7.74305815e-01, 5.50121959e-02],
           [3.87164283e-01, 7.76699935e-01, 4.07292968e-02],
           [4.02910994e-01, 7.78887386e-01, 3.17471713e-02],
           [4.18689590e-01, 7.80922878e-01, 3.10965897e-02],
           [4.34073695e-01, 7.82883423e-01, 3.90365919e-02],
           [4.48766557e-01, 7.84840147e-01, 5.34217397e-02],
           [4.62656859e-01, 7.86838212e-01, 7.02746272e-02],
           [4.75747356e-01, 7.88901491e-01, 8.77386707e-02],
           [4.88113228e-01, 7.91035929e-01, 1.05019902e-01],
           [4.99839881e-01, 7.93241080e-01, 1.21820850e-01],
           [5.11010870e-01, 7.95512991e-01, 1.38059636e-01],
           [5.21703318e-01, 7.97845796e-01, 1.53746905e-01],
           [5.31978461e-01, 8.00234800e-01, 1.68918555e-01],
           [5.41893590e-01, 8.02674049e-01, 1.83630257e-01],
           [5.51488805e-01, 8.05160409e-01, 1.97923374e-01],
           [5.60807871e-01, 8.07688247e-01, 2.11854304e-01],
           [5.69878335e-01, 8.10255346e-01, 2.25456465e-01],
           [5.78730651e-01, 8.12857680e-01, 2.38772161e-01],
           [5.87386390e-01, 8.15493072e-01, 2.51830095e-01],
           [5.95865061e-01, 8.18159345e-01, 2.64656953e-01],
           [6.04184278e-01, 8.20854362e-01, 2.77277374e-01],
           [6.12359929e-01, 8.23576050e-01, 2.89714010e-01],
           [6.20404842e-01, 8.26322940e-01, 3.01984545e-01],
           [6.28327082e-01, 8.29094887e-01, 3.14097666e-01],
           [6.36143480e-01, 8.31888356e-01, 3.26081227e-01],
           [6.43854813e-01, 8.34705264e-01, 3.37929960e-01],
           [6.51476266e-01, 8.37542104e-01, 3.49669941e-01],
           [6.59012358e-01, 8.40399041e-01, 3.61304992e-01],
           [6.66467394e-01, 8.43276210e-01, 3.72838682e-01],
           [6.73850219e-01, 8.46171840e-01, 3.84285252e-01],
           [6.81165558e-01, 8.49085591e-01, 3.95650208e-01],
           [6.88417835e-01, 8.52017132e-01, 4.06938711e-01],
           [6.95611194e-01, 8.54966141e-01, 4.18155608e-01],
           [7.02749517e-01, 8.57932307e-01, 4.29305453e-01],
           [7.09836443e-01, 8.60915331e-01, 4.40392532e-01],
           [7.16875385e-01, 8.63914927e-01, 4.51420880e-01],
           [7.23869544e-01, 8.66930822e-01, 4.62394301e-01],
           [7.30821922e-01, 8.69962760e-01, 4.73316382e-01],
           [7.37735340e-01, 8.73010497e-01, 4.84190507e-01],
           [7.44612445e-01, 8.76073804e-01, 4.95019870e-01],
           [7.51453158e-01, 8.79153679e-01, 5.05800795e-01],
           [7.58261111e-01, 8.82249356e-01, 5.16539340e-01],
           [7.65039480e-01, 8.85360204e-01, 5.27240699e-01],
           [7.71789441e-01, 8.88486500e-01, 5.37904998e-01],
           [7.78509946e-01, 8.91629602e-01, 5.48526441e-01],
           [7.85206578e-01, 8.94787565e-01, 5.59117251e-01],
           [7.91878553e-01, 8.97961553e-01, 5.69672624e-01],
           [7.98526991e-01, 9.01151777e-01, 5.80192976e-01],
           [8.05155731e-01, 9.04357000e-01, 5.90686458e-01],
           [8.11761481e-01, 9.07579669e-01, 6.01141408e-01],
           [8.18351001e-01, 9.10816941e-01, 6.11574531e-01]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.nuclear", N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
