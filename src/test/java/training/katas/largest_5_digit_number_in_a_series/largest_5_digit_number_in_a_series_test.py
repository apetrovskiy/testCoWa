# import pytest
from src.main.java.training.katas.largest_5_digit_number_in_a_series.code import (
    solution,
)


# @pytest.mark.skip(reason="TODO: no way of currently testing this")
def test_largest_5_digit_number_in_a_series():
    number = """7316717653133062491922511967442657474235534919493496
    98352036854250632623957831801698480186947885184385861560789112
    94949545950173795833195285320880551112540698747158523863050715
    69329096329522744304355766896648950445244523161731856403098711
    12172238311362229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866701724271218
    83998797908792274921901699720888093776657273330010533678812202
    35421809751254540594752243525849077116705560136048395864467063
    24415722155397531234579778461740649551492908625693219784686224
    82839722413756570560574902614079729686524145351004748216637048
    44031998900088952434506585412275886668811642717147992444292823
    08634656748139191231628245861786645835912456652947654568284891
    28831426076900422421902267105562632111110937054421750694165896
    04080719840385096245544436298123098787992724428490918884580156
    16609791913387549920052406368991256071760605886116467109405077
    54100225698315520005593572972571636269561882670428252483600823
    257540920752963450"""
    # actual =
    solution(number)

    # test.expect(actual != 0, 'solution returned zero')
    # test.expect(actual, 'solution did not return a value')
    # test.assert_equals(actual, 99890, 'solution did not
    # return correct value')
    # test.assert_equals(solution('1234567898765'), 98765,
    # 'Failed when max 5 digits is at end of number')
    # assert 1 == 2


# number = "731671765313306249192251196744265747423553491949
# 3496983520368542506326239578318016984801869478851843858615
# 6078911294949545950173795833195285320880551112540698747158
# 5238630507156932909632952274430435576689664895044524452316
# 1731856403098711121722383113622298934233803081353362766142
# 8280644448664523874930358907296290491560440772390713810515
# 8593079608667017242712188399879790879227492190169972088809
# 3776657273330010533678812202354218097512545405947522435258
# 4907711670556013604839586446706324415722155397531234579778
# 4617406495514929086256932197846862248283972241375657056057
# 4902614079729686524145351004748216637048440319989000889524
# 3450658541227588666881164271714799244429282308634656748139
# 1912316282458617866458359124566529476545682848912883142607
# 6900422421902267105562632111110937054421750694165896040807
# 1984038509624554443629812309878799272442849091888458015616
# 6097919133875499200524063689912560717606058861164671094050
# 7754100225698315520005593572972571636269561882670428252483
# 600823257540920752963450"
# actual = solution(number);

# test.expect(actual != 0, 'solution returned zero')
# test.expect(actual, 'solution did not return a value')
# test.assert_equals(actual, 99890, 'solution did not return correct value')
# test.assert_equals(solution('1234567898765'), 98765,
# 'Failed when max 5 digits is at end of number')
