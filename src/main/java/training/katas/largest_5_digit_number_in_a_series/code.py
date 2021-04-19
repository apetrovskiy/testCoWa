def solution(digits):
    print(digits)
    digits = digits.replace('\n', '').replace(
        ' ', '').replace('\t', '').replace('         ', '')
    print(digits)
    numbers = [int(digits[i:i+5]) for i in range(0, len(digits), 5)]
    numbers.extend([int(digits[i+1:i+6]) for i in range(0, len(digits)-1, 5)])
    numbers.extend([int(digits[i+2:i+7]) for i in range(0, len(digits)-2, 5)])
    numbers.extend([int(digits[i+3:i+8]) for i in range(0, len(digits)-3, 5)])
    numbers.extend([int(digits[i+4:i+9]) for i in range(0, len(digits)-4, 5)])
    return max(numbers)


solution("""73167176531330624919225119674426574742355349194934
         969835203685425063262395783180169848018694788518438
         586156078911294949545950173795833195285320880551112
         540698747158523863050715693290963295227443043557668
         966489504452445231617318564030987111217223831136222
         989342338030813533627661428280644448664523874930358
         907296290491560440772390713810515859307960866701724
         271218839987979087922749219016997208880937766572733
         300105336788122023542180975125454059475224352584907
         711670556013604839586446706324415722155397531234579
         778461740649551492908625693219784686224828397224137
         565705605749026140797296865241453510047482166370484
         403199890008895243450658541227588666881164271714799
         244429282308634656748139191231628245861786645835912
         456652947654568284891288314260769004224219022671055
         626321111109370544217506941658960408071984038509624
         554443629812309878799272442849091888458015616609791
         913387549920052406368991256071760605886116467109405
         077541002256983155200055935729725716362695618826704
         28252483600823257540920752963450""")
