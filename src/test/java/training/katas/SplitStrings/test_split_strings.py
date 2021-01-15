from src.main.java.training.katas.SplitStrings.split_strings import solution
from typing import List
import pytest


test_data = [
    ('abc', ['ab', 'c_']),
    ('abcdef', ['ab', 'cd', 'ef']),
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
    ("ulnckdcoygljbbkrjxmxmdxafyippuflgwaquathcrswadnbjglszozwtarkjtuojnamzzntnxpznjyrmjlskkkwmuzgyyxkju", ['ul', 'nc', 'kd', 'co', 'yg', 'lj', 'bb', 'kr', 'jx', 'mx', 'md', 'xa', 'fy', 'ip', 'pu', 'fl',
                                                                                                            'gw', 'aq', 'ua', 'th', 'cr', 'sw', 'ad', 'nb', 'jg', 'ls', 'zo', 'zw', 'ta', 'rk', 'jt', 'uo', 'jn', 'am', 'zz', 'nt', 'nx', 'pz', 'nj', 'yr', 'mj', 'ls', 'kk', 'kw', 'mu', 'zg', 'yy', 'xk', 'ju']),
    ("whugsw", ['wh', 'ug', 'sw']),
    ("coamiagcohvpavjynitnjyaqzhmmtpmgtcpgebftxfrhwymhacmhouzumbbl", ['co', 'am', 'ia', 'gc', 'oh', 'vp', 'av', 'jy', 'ni', 'tn',
                                                                      'jy', 'aq', 'zh', 'mm', 'tp', 'mg', 'tc', 'pg', 'eb', 'ft', 'xf', 'rh', 'wy', 'mh', 'ac', 'mh', 'ou', 'zu', 'mb', 'bl']),
    ("totcmbfekgqgsltdlxtofeqmpmhblxetzovltijrqpztjrgmvnflunbbtnhvydwuudrsrgpylhcrhri", ['to', 'tc', 'mb', 'fe', 'kg', 'qg', 'sl', 'td', 'lx', 'to', 'fe', 'qm', 'pm',
                                                                                         'hb', 'lx', 'et', 'zo', 'vl', 'ti', 'jr', 'qp', 'zt', 'jr', 'gm', 'vn', 'fl', 'un', 'bb', 'tn', 'hv', 'yd', 'wu', 'ud', 'rs', 'rg', 'py', 'lh', 'cr', 'hr', 'i_']),
    ("sfteoemjgyziwhickxjtxrrhjmzpywfkjxyxlvhplnd", ['sf', 'te', 'oe', 'mj', 'gy', 'zi', 'wh',
                                                     'ic', 'kx', 'jt', 'xr', 'rh', 'jm', 'zp', 'yw', 'fk', 'jx', 'yx', 'lv', 'hp', 'ln', 'd_']),
    ("ltwtthafxxqtghfvwwmvfyxyyekypglqsejmivxytwufiewiczgzvyjezhasdjqbeglmwrcxgwgvtuiyjoghpofdfjhwvok", ['lt', 'wt', 'th', 'af', 'xx', 'qt', 'gh', 'fv', 'ww', 'mv', 'fy', 'xy', 'ye', 'ky', 'pg', 'lq',
                                                                                                         'se', 'jm', 'iv', 'xy', 'tw', 'uf', 'ie', 'wi', 'cz', 'gz', 'vy', 'je', 'zh', 'as', 'dj', 'qb', 'eg', 'lm', 'wr', 'cx', 'gw', 'gv', 'tu', 'iy', 'jo', 'gh', 'po', 'fd', 'fj', 'hw', 'vo', 'k_']),
    ("lpdrbuwhoohiiagjsopchwuannfrfupsznxbgbwqgnfbdqenhgwpofrcmfvptbinwxrjhdtfanczc", ['lp', 'dr', 'bu', 'wh', 'oo', 'hi', 'ia', 'gj', 'so', 'pc', 'hw', 'ua', 'nn',
                                                                                       'fr', 'fu', 'ps', 'zn', 'xb', 'gb', 'wq', 'gn', 'fb', 'dq', 'en', 'hg', 'wp', 'of', 'rc', 'mf', 'vp', 'tb', 'in', 'wx', 'rj', 'hd', 'tf', 'an', 'cz', 'c_']),
    ("ateikmopkqrsnodfbizjqvyttancjxaomsjlwznopcdoxsjzdjthnnuszvnhrrscfvu", ['at', 'ei', 'km', 'op', 'kq', 'rs', 'no', 'df', 'bi', 'zj', 'qv',
                                                                             'yt', 'ta', 'nc', 'jx', 'ao', 'ms', 'jl', 'wz', 'no', 'pc', 'do', 'xs', 'jz', 'dj', 'th', 'nn', 'us', 'zv', 'nh', 'rr', 'sc', 'fv', 'u_']),
    ("nlxikxqyhjttmovhdwguztwposwisfzbxzmyaxxjtffiklbmgnrfspcjemcfrpfkmbiewhcyytxfcrwu", ['nl', 'xi', 'kx', 'qy', 'hj', 'tt', 'mo', 'vh', 'dw', 'gu', 'zt', 'wp', 'os',
                                                                                          'wi', 'sf', 'zb', 'xz', 'my', 'ax', 'xj', 'tf', 'fi', 'kl', 'bm', 'gn', 'rf', 'sp', 'cj', 'em', 'cf', 'rp', 'fk', 'mb', 'ie', 'wh', 'cy', 'yt', 'xf', 'cr', 'wu']),
    ("igdiavqsfbdfptqrvcpkoavztvkxzyed", [
     'ig', 'di', 'av', 'qs', 'fb', 'df', 'pt', 'qr', 'vc', 'pk', 'oa', 'vz', 'tv', 'kx', 'zy', 'ed']),
    ("ohuyfrdrmujpghhwftxitzbtakizfzvockvraymvawbbyfmdapdxutks", ['oh', 'uy', 'fr', 'dr', 'mu', 'jp', 'gh', 'hw', 'ft',
                                                                  'xi', 'tz', 'bt', 'ak', 'iz', 'fz', 'vo', 'ck', 'vr', 'ay', 'mv', 'aw', 'bb', 'yf', 'md', 'ap', 'dx', 'ut', 'ks']),
    ("jgrpcmnfzizy", ['jg', 'rp', 'cm', 'nf', 'zi', 'zy']),
    ("gpmwiyaqnydmbilityhzmexgyrpq", [
     'gp', 'mw', 'iy', 'aq', 'ny', 'dm', 'bi', 'li', 'ty', 'hz', 'me', 'xg', 'yr', 'pq']),
    ("jiavwuvizxrycmlucxtihpsglggxhmfzxoakcrdcavbpg", ['ji', 'av', 'wu', 'vi', 'zx', 'ry', 'cm',
                                                       'lu', 'cx', 'ti', 'hp', 'sg', 'lg', 'gx', 'hm', 'fz', 'xo', 'ak', 'cr', 'dc', 'av', 'bp', 'g_']),
    ("whekvncjntetndmqmndyhdjeekrgbepifvvsmoxmbldwneik", ['wh', 'ek', 'vn', 'cj', 'nt', 'et', 'nd', 'mq',
                                                          'mn', 'dy', 'hd', 'je', 'ek', 'rg', 'be', 'pi', 'fv', 'vs', 'mo', 'xm', 'bl', 'dw', 'ne', 'ik']),
    ("rtcgobkejfxbilgitvexzmlqdwjkvjhfpcwaqjlmujujwjh", ['rt', 'cg', 'ob', 'ke', 'jf', 'xb', 'il', 'gi',
                                                         'tv', 'ex', 'zm', 'lq', 'dw', 'jk', 'vj', 'hf', 'pc', 'wa', 'qj', 'lm', 'uj', 'uj', 'wj', 'h_']),
    ("ryolejzthujgrpynsxkejjxnkzhkpcjbvehtnwoijgquqokyazeqjgvmjr", ['ry', 'ol', 'ej', 'zt', 'hu', 'jg', 'rp', 'yn', 'sx',
                                                                    'ke', 'jj', 'xn', 'kz', 'hk', 'pc', 'jb', 've', 'ht', 'nw', 'oi', 'jg', 'qu', 'qo', 'ky', 'az', 'eq', 'jg', 'vm', 'jr']),
    ("adyzbvtwrmqnwkutry", ['ad', 'yz', 'bv',
                            'tw', 'rm', 'qn', 'wk', 'ut', 'ry']),
    ("vvtys", ['vv', 'ty', 's_'])
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_split_strings(input: str, expected_result: List[str]):
    assert expected_result == solution(input)


'''
test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
'''
