import unittest
from selfdrive.assets.addon.mapd.lib.geo import vectors, ref_vectors, bearing_to_points, distance_to_points
import numpy as np
from numpy.testing import assert_array_almost_equal
from selfdrive.assets.addon.mapd.test.mock_data import mockNodesData01


class TestMapsdGeoLibrary(unittest.TestCase):
  def test_vectors(self):
    points = mockNodesData01.radians
    expected = np.array([
      [-1.34011951e-05, 1.00776468e-05],
      [-5.83610920e-06, 4.41046897e-06],
      [-7.83348567e-06, 5.94114032e-06],
      [-7.08560788e-06, 5.30408795e-06],
      [-6.57632550e-06, 4.05791838e-06],
      [-1.16077872e-06, 6.91151252e-07],
      [-1.53178098e-05, 9.62215139e-06],
      [-5.76314175e-06, 3.55176643e-06],
      [-1.61124141e-05, 9.86127759e-06],
      [-1.48006628e-05, 8.58192512e-06],
      [-1.72237209e-06, 1.60570482e-06],
      [-8.68985228e-06, 9.22062311e-06],
      [-1.42922812e-06, 1.51494711e-06],
      [-3.39761486e-06, 2.57087743e-06],
      [-2.75467373e-06, 1.28631255e-06],
      [-1.57501989e-05, 5.72309451e-06],
      [-2.52143954e-06, 1.34565295e-06],
      [-1.65278643e-06, 1.28630942e-06],
      [-2.22196114e-05, 1.64360838e-05],
      [-5.88675934e-06, 4.08234746e-06],
      [-1.83673390e-06, 1.46782408e-06],
      [-1.55004206e-06, 1.51843800e-06],
      [-1.20451533e-06, 2.06298011e-06],
      [-1.91801338e-06, 4.64083285e-06],
      [-2.38653483e-06, 5.60076524e-06],
      [-1.65269781e-06, 5.78402290e-06],
      [-3.66908309e-07, 2.75412965e-06],
      [0.00000000e+00, 1.92858882e-06],
      [9.09242615e-08, 2.66162711e-06],
      [3.14490354e-07, 1.53065382e-06],
      [8.66452477e-08, 4.83456208e-07],
      [2.41750593e-07, 1.10828411e-06],
      [7.43745228e-06, 1.27618831e-05],
      [5.59968054e-06, 9.63947367e-06],
      [2.01951467e-06, 2.75413219e-06],
      [4.59952643e-07, 6.42281301e-07],
      [1.74353749e-06, 1.74533121e-06],
      [2.57144338e-06, 2.11185266e-06],
      [1.46893187e-05, 1.11999169e-05],
      [3.84659229e-05, 2.85527952e-05],
      [2.71627936e-05, 1.98727946e-05],
      [8.44632540e-06, 6.15058628e-06],
      [2.29420323e-06, 1.92859222e-06],
      [2.58083439e-06, 3.16952222e-06],
      [3.76373643e-06, 5.14174911e-06],
      [5.32416098e-06, 6.51707770e-06],
      [8.62890928e-06, 1.11998258e-05],
      [1.25762497e-05, 1.65231340e-05],
      [8.90452991e-06, 1.10148240e-05],
      [4.86505726e-06, 4.59023120e-06],
      [3.85545276e-06, 3.39642031e-06],
      [3.48753893e-06, 3.30566145e-06],
      [2.99557303e-06, 2.61276368e-06],
      [2.15496788e-06, 1.87797727e-06],
      [4.10564937e-06, 3.58142649e-06],
      [1.53680853e-06, 1.33866906e-06],
      [4.99540175e-06, 4.35635790e-06],
      [1.37744970e-06, 1.19380643e-06],
      [1.74319821e-06, 1.28456429e-06],
      [9.99931238e-07, 1.14493663e-06],
      [6.42735560e-07, 1.19380547e-06],
      [3.66818436e-07, 1.46782199e-06],
      [5.45413874e-08, 1.83783170e-06],
      [-1.35818548e-07, 1.14842666e-06],
      [-5.50758101e-07, 3.02989178e-06],
      [-4.58785270e-07, 2.66162724e-06],
      [-2.51315555e-07, 1.19031459e-06],
      [-3.91409773e-07, 1.65457223e-06],
      [-2.14525206e-06, 5.67755902e-06],
      [-4.24558096e-07, 1.39102753e-06],
      [-1.46936730e-06, 5.32325561e-06],
      [-1.37632061e-06, 4.59021715e-06],
      [-8.26642899e-07, 4.68097349e-06],
      [-6.42702724e-07, 4.95673534e-06],
      [-3.66796960e-07, 7.25009780e-06],
      [-1.82861669e-07, 8.99542699e-06],
      [4.09564134e-07, 6.11214315e-06],
      [7.80629912e-08, 1.45734993e-06],
      [4.81205526e-07, 7.56076647e-06],
      [2.01036346e-07, 2.42775302e-06]])

    v = vectors(points)
    assert_array_almost_equal(v, expected)

  def test_ref_vectors(self):
    points = mockNodesData01.radians
    expected = np.array([
      [1.59924145e-04, -1.07153714e-04],
      [1.46520873e-04, -9.70788297e-05],
      [1.40683931e-04, -9.26694631e-05],
      [1.32849368e-04, -8.67297434e-05],
      [1.25762852e-04, -8.14268689e-05],
      [1.19185869e-04, -7.73700167e-05],
      [1.18024984e-04, -7.66790438e-05],
      [1.02705711e-04, -6.70592230e-05],
      [9.69420991e-05, -6.35082196e-05],
      [8.08284530e-05, -5.36489556e-05],
      [6.60268961e-05, -4.50685727e-05],
      [6.43043874e-05, -4.34630144e-05],
      [5.56137708e-05, -3.42431117e-05],
      [5.41844341e-05, -3.27282671e-05],
      [5.07866397e-05, -3.01576270e-05],
      [4.80318817e-05, -2.88714948e-05],
      [3.22813286e-05, -2.31493755e-05],
      [2.97598330e-05, -2.18038275e-05],
      [2.81069973e-05, -2.05175815e-05],
      [5.88679032e-06, -4.08230278e-06],
      [0.00000000e+00, 0.00000000e+00],
      [-1.83673390e-06, 1.46782408e-06],
      [-3.38677236e-06, 2.98626574e-06],
      [-4.59127869e-06, 5.04925111e-06],
      [-6.50926460e-06, 9.69009532e-06],
      [-8.89575243e-06, 1.52908806e-05],
      [-1.05483839e-05, 2.10749224e-05],
      [-1.09152548e-05, 2.38290571e-05],
      [-1.09152276e-05, 2.57576459e-05],
      [-1.08242659e-05, 2.84192717e-05],
      [-1.05097542e-05, 2.99499212e-05],
      [-1.04231024e-05, 3.04333762e-05],
      [-1.01813369e-05, 3.15416571e-05],
      [-2.74371711e-06, 4.43034426e-05],
      [2.85599752e-06, 5.39428964e-05],
      [4.87550206e-06, 5.66970360e-05],
      [5.33545066e-06, 5.73393202e-05],
      [7.07897615e-06, 5.90846634e-05],
      [9.65040026e-06, 6.11965396e-05],
      [2.43395796e-05, 7.23966392e-05],
      [6.28046063e-05, 1.00950641e-04],
      [8.99657904e-05, 1.20825635e-04],
      [9.84114021e-05, 1.26977201e-04],
      [1.00705361e-04, 1.28906084e-04],
      [1.03285783e-04, 1.32075942e-04],
      [1.07048835e-04, 1.37218192e-04],
      [1.12372096e-04, 1.43736004e-04],
      [1.20999382e-04, 1.54937080e-04],
      [1.33573053e-04, 1.71462176e-04],
      [1.42475686e-04, 1.82478533e-04],
      [1.47339899e-04, 1.87069658e-04],
      [1.51194707e-04, 1.90466811e-04],
      [1.54681601e-04, 1.93773152e-04],
      [1.57676653e-04, 1.96386513e-04],
      [1.59831239e-04, 1.98264929e-04],
      [1.63936150e-04, 2.01847201e-04],
      [1.65472675e-04, 2.03186195e-04],
      [1.70467147e-04, 2.07543619e-04],
      [1.71844334e-04, 2.08737728e-04],
      [1.73587247e-04, 2.10022678e-04],
      [1.74586922e-04, 2.11167839e-04],
      [1.75229389e-04, 2.12361789e-04],
      [1.75595876e-04, 2.13829694e-04],
      [1.75650001e-04, 2.15667538e-04],
      [1.75513922e-04, 2.16815933e-04],
      [1.74962478e-04, 2.19845700e-04],
      [1.74503092e-04, 2.22507224e-04],
      [1.74251509e-04, 2.23697482e-04],
      [1.73859727e-04, 2.25351966e-04],
      [1.71713202e-04, 2.31029044e-04],
      [1.71288336e-04, 2.32419977e-04],
      [1.69817793e-04, 2.37742908e-04],
      [1.68440467e-04, 2.42332824e-04],
      [1.67612807e-04, 2.47013617e-04],
      [1.66969033e-04, 2.51970213e-04],
      [1.66600674e-04, 2.59220232e-04],
      [1.66415880e-04, 2.68215619e-04],
      [1.66824132e-04, 2.74327850e-04],
      [1.66901881e-04, 2.75785216e-04],
      [1.67381459e-04, 2.83346086e-04],
      [1.67581971e-04, 2.85773882e-04]])

    v = ref_vectors(points[20], points)
    assert_array_almost_equal(v, expected)

  def test_bearing_to_points(self):
    points = mockNodesData01.radians
    expected = np.array([
      2.16112265, 2.15595027, 2.15326799, 2.14916735, 2.14538642,
      2.14657678, 2.14694997, 2.1492257, 2.1507589, 2.15676899,
      2.16973441, 2.1651606, 2.12270237, 2.11416356, 2.10665211,
      2.11201708, 2.19291574, 2.2031069, 2.20136186, 2.17712517,
      0., -0.8965745, -0.84815954, -0.73792895, -0.59150953,
      -0.5269061, -0.46406215, -0.42954043, -0.4008254, -0.36391371,
      -0.33748609, -0.32996807, -0.31223189, -0.06185112, 0.05289544,
      0.08578116, 0.0927833, 0.11924233, 0.15640718, 0.32432622,
      0.55653415, 0.64003094, 0.6593301, 0.66319086, 0.66367982,
      0.66251077, 0.66354137, 0.66302176, 0.66181884, 0.66291139,
      0.66714676, 0.67095594, 0.67367984, 0.6765003, 0.67847961,
      0.68212344, 0.68345356, 0.68762778, 0.68876073, 0.69070183,
      0.69085143, 0.68988665, 0.68753177, 0.68348884, 0.68051081,
      0.67220053, 0.66506824, 0.66177969, 0.65712162, 0.63916951,
      0.6351146, 0.62025347, 0.60741567, 0.59618923, 0.58521935,
      0.57122582, 0.55532475, 0.54636839, 0.54422542, 0.53357655,
      0.53037033])

    v = bearing_to_points(points[20], points)
    assert_array_almost_equal(v, expected)

  def test_distance_to_points(self):
    points = mockNodesData01.radians
    expected = np.array([
      1226.82569068, 1120.13820773, 1073.61121415, 1011.10016574,
      954.81557436, 905.58045038, 896.97734399, 781.7102819,
      738.58271117, 618.26145463, 509.47052142, 494.6403804,
      416.22483123, 403.42108699, 376.42615499, 357.15106681,
      253.15957483, 235.11572972, 221.77439728, 45.65465979,
      0., 14.98414, 28.77606056, 43.49299446,
      74.39463425, 112.74005248, 150.19482607, 167.03665191,
      178.28443483, 193.80834084, 202.28154097, 205.01173833,
      211.22777104, 282.88676739, 344.25957352, 362.66370657,
      367.00206795, 379.23951996, 394.82505328, 486.76073331,
      757.70254732, 960.03439155, 1023.81434529, 1042.49401713,
      1068.53770096, 1109.12696535, 1162.74555108, 1252.847351,
      1385.17179405, 1475.42502599, 1517.57849916, 1549.79838056,
      1580.12405964, 1605.05483058, 1622.98937809, 1657.19268821,
      1669.99157205, 1711.63883132, 1723.09133393, 1736.47655688,
      1746.16073119, 1754.63481838, 1763.34186103, 1772.62691273,
      1777.76189094, 1790.62024447, 1802.11488235, 1807.1040605,
      1813.90756815, 1834.49265566, 1840.00708445, 1861.96087374,
      1880.81678093, 1902.42091191, 1926.37194131, 1963.78301115,
      2011.62679077, 2046.18028824, 2054.37811294, 2097.30347724,
      2111.28586072])

    v = distance_to_points(points[20], points)
    assert_array_almost_equal(v, expected)