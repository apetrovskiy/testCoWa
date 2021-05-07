from src.main.java.training.katas.HumanReadableDurationFormat.solution \
    import format_duration
import pytest


test_data = [
    (1, "1 second"),
    (62, "1 minute and 2 seconds"),
    (120, "2 minutes"),
    (3600, "1 hour"),
    (3662, "1 hour, 1 minute and 2 seconds"),
    (0, "now"),
    (15731080, '182 days, 1 hour, 44 minutes and 40 seconds'),
    (132030240, '4 years, 68 days, 3 hours and 4 minutes'),
    (205851834, '6 years, 192 days, 13 hours, 3 minutes and 54 seconds'),
    (253374061, '8 years, 12 days, 13 hours, 41 minutes and 1 second'),
    (101956166, '3 years, 85 days, 1 hour, 9 minutes and 26 seconds'),
    (7106407, '82 days, 6 hours and 7 seconds'),
    (8601960, '99 days, 13 hours and 26 minutes'),
    (5792789, '67 days, 1 hour, 6 minutes and 29 seconds'),
    (3595920, '41 days, 14 hours and 52 minutes'),
    (2165051, '25 days, 1 hour, 24 minutes and 11 seconds'),
    (8990744, '104 days, 1 hour, 25 minutes and 44 seconds'),
    (1820944, '21 days, 1 hour, 49 minutes and 4 seconds'),
    (4341633, '50 days, 6 hours and 33 seconds'),
    (9979254, '115 days, 12 hours and 54 seconds'),
    (5015292, '58 days, 1 hour, 8 minutes and 12 seconds'),
    (7178033, '83 days, 1 hour, 53 minutes and 53 seconds'),
    (5216422, '60 days, 9 hours and 22 seconds'),
    (7167617, '82 days, 23 hours and 17 seconds')
]


@ pytest.mark.parametrize("seconds,expected_result", test_data)
def test_human_readable_duration_format(seconds: int, expected_result: str):
    assert expected_result == format_duration(seconds)


'''
est.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
'''

'''
Log
242062374
'' should equal '7 years, 246 days, 15 hours, 32 minutes and 54 seconds'
Log
101956166
'' should equal '3 years, 85 days, 1 hour, 9 minutes and 26 seconds'
Log
33243586
'' should equal '1 year, 19 days, 18 hours, 19 minutes and 46 seconds'
Completed in 0.07ms
random tests
Log
3020171
'' should equal '34 days, 22 hours, 56 minutes and 11 seconds'
Log
4779793
'' should equal '55 days, 7 hours, 43 minutes and 13 seconds'
Log
9591925
'' should equal '111 days, 25 minutes and 25 seconds'
Log
4776439
'' should equal '55 days, 6 hours, 47 minutes and 19 seconds'
Log
3757706
'' should equal '43 days, 11 hours, 48 minutes and 26 seconds'
Log
261468
'' should equal '3 days, 37 minutes and 48 seconds'
Log
5896386
'' should equal '68 days, 5 hours, 53 minutes and 6 seconds'
Log
2027348
'' should equal '23 days, 11 hours, 9 minutes and 8 seconds'
Log
751252
'' should equal '8 days, 16 hours, 40 minutes and 52 seconds'
Log
1895728
'' should equal '21 days, 22 hours, 35 minutes and 28 seconds'
Log
127060
'' should equal '1 day, 11 hours, 17 minutes and 40 seconds'
Log
1094858
'' should equal '12 days, 16 hours, 7 minutes and 38 seconds'
Log
7912263
'' should equal '91 days, 13 hours, 51 minutes and 3 seconds'
Log
3244561
'' should equal '37 days, 13 hours, 16 minutes and 1 second'
Log
7445310
'' should equal '86 days, 4 hours, 8 minutes and 30 seconds'
Log
6266551
'' should equal '72 days, 12 hours, 42 minutes and 31 seconds'
Log
8052297
'' should equal '93 days, 4 hours, 44 minutes and 57 seconds'
Log
7328686
'' should equal '84 days, 19 hours, 44 minutes and 46 seconds'
Log
9076545
'' should equal '105 days, 1 hour, 15 minutes and 45 seconds'
Log
3584901
'' should equal '41 days, 11 hours, 48 minutes and 21 seconds'
Log
8194613
'' should equal '94 days, 20 hours, 16 minutes and 53 seconds'
Log
3335077
'' should equal '38 days, 14 hours, 24 minutes and 37 seconds'
Log
2627440
'' should equal '30 days, 9 hours, 50 minutes and 40 seconds'
Log
7282150
'' should equal '84 days, 6 hours, 49 minutes and 10 seconds'
Log
6490478
'' should equal '75 days, 2 hours, 54 minutes and 38 seconds'
Log
3848080
'' should equal '44 days, 12 hours, 54 minutes and 40 seconds'
Log
357100
'' should equal '4 days, 3 hours, 11 minutes and 40 seconds'
Log
9373123
'' should equal '108 days, 11 hours, 38 minutes and 43 seconds'
Log
7903028
'' should equal '91 days, 11 hours, 17 minutes and 8 seconds'
Log
5909922
'' should equal '68 days, 9 hours, 38 minutes and 42 seconds'
Log
4546145
'' should equal '52 days, 14 hours, 49 minutes and 5 seconds'
Log
5045909
'' should equal '58 days, 9 hours, 38 minutes and 29 seconds'
Log
1475517
'' should equal '17 days, 1 hour, 51 minutes and 57 seconds'
Log
6962425
'' should equal '80 days, 14 hours and 25 seconds'
Log
8325991
'' should equal '96 days, 8 hours, 46 minutes and 31 seconds'
Log
223820
'' should equal '2 days, 14 hours, 10 minutes and 20 seconds'
Log
4055921
'' should equal '46 days, 22 hours, 38 minutes and 41 seconds'
Log
7014537
'' should equal '81 days, 4 hours, 28 minutes and 57 seconds'
Log
2145441
'' should equal '24 days, 19 hours, 57 minutes and 21 seconds'
Log
2551276
'' should equal '29 days, 12 hours, 41 minutes and 16 seconds'
Log
7104001
'' should equal '82 days, 5 hours, 20 minutes and 1 second'
Log
2553735
'' should equal '29 days, 13 hours, 22 minutes and 15 seconds'
Log
1753372
'' should equal '20 days, 7 hours, 2 minutes and 52 seconds'
Log
7135859
'' should equal '82 days, 14 hours, 10 minutes and 59 seconds'
Log
1263002
'' should equal '14 days, 14 hours, 50 minutes and 2 seconds'
Log
3932871
'' should equal '45 days, 12 hours, 27 minutes and 51 seconds'
Log
2737901
'' should equal '31 days, 16 hours, 31 minutes and 41 seconds'
Log
1988474
'' should equal '23 days, 21 minutes and 14 seconds'
Log
8439229
'' should equal '97 days, 16 hours, 13 minutes and 49 seconds'
Log
1520664
'' should equal '17 days, 14 hours, 24 minutes and 24 seconds'
Log
9391980
'' should equal '108 days, 16 hours and 53 minutes'
Log
7669155
'' should equal '88 days, 18 hours, 19 minutes and 15 seconds'
Log
9965173
'' should equal '115 days, 8 hours, 6 minutes and 13 seconds'
Log
1102359
'' should equal '12 days, 18 hours, 12 minutes and 39 seconds'
Log
3655412
'' should equal '42 days, 7 hours, 23 minutes and 32 seconds'
Log
7550173
'' should equal '87 days, 9 hours, 16 minutes and 13 seconds'
Log
5452200
'' should equal '63 days, 2 hours and 30 minutes'
Log
6254347
'' should equal '72 days, 9 hours, 19 minutes and 7 seconds'
Log
3124940
'' should equal '36 days, 4 hours, 2 minutes and 20 seconds'
Log
4189781
'' should equal '48 days, 11 hours, 49 minutes and 41 seconds'
Log
3618461
'' should equal '41 days, 21 hours, 7 minutes and 41 seconds'
Log
3469750
'' should equal '40 days, 3 hours, 49 minutes and 10 seconds'
Log
1477283
'' should equal '17 days, 2 hours, 21 minutes and 23 seconds'
Log
2491400
'' should equal '28 days, 20 hours, 3 minutes and 20 seconds'
Log
2185703
'' should equal '25 days, 7 hours, 8 minutes and 23 seconds'
Log
6258333
'' should equal '72 days, 10 hours, 25 minutes and 33 seconds'
Log
997170
'' should equal '11 days, 12 hours, 59 minutes and 30 seconds'
Log
6012984
'' should equal '69 days, 14 hours, 16 minutes and 24 seconds'
Log
905399
'' should equal '10 days, 11 hours, 29 minutes and 59 seconds'
Log
1751731
'' should equal '20 days, 6 hours, 35 minutes and 31 seconds'
Log
5403426
'' should equal '62 days, 12 hours, 57 minutes and 6 seconds'
Log
1065438
'' should equal '12 days, 7 hours, 57 minutes and 18 seconds'
Log
8938334
'' should equal '103 days, 10 hours, 52 minutes and 14 seconds'
Log
4100991
'' should equal '47 days, 11 hours, 9 minutes and 51 seconds'
Log
1574938
'' should equal '18 days, 5 hours, 28 minutes and 58 seconds'
Log
8074070
'' should equal '93 days, 10 hours, 47 minutes and 50 seconds'
Log
3844917
'' should equal '44 days, 12 hours, 1 minute and 57 seconds'
Log
3539859
'' should equal '40 days, 23 hours, 17 minutes and 39 seconds'
Log
8484070
'' should equal '98 days, 4 hours, 41 minutes and 10 seconds'
Log
5872646
'' should equal '67 days, 23 hours, 17 minutes and 26 seconds'
Log
7319499
'' should equal '84 days, 17 hours, 11 minutes and 39 seconds'
Log
8823849
'' should equal '102 days, 3 hours, 4 minutes and 9 seconds'
Log
9396765
'' should equal '108 days, 18 hours, 12 minutes and 45 seconds'
Log
5443026
'' should equal '62 days, 23 hours, 57 minutes and 6 seconds'
Log
1074908
'' should equal '12 days, 10 hours, 35 minutes and 8 seconds'
Log
8105198
'' should equal '93 days, 19 hours, 26 minutes and 38 seconds'
Log
5699215
'' should equal '65 days, 23 hours, 6 minutes and 55 seconds'
Log
434127
'' should equal '5 days, 35 minutes and 27 seconds'
Log
700262
'' should equal '8 days, 2 hours, 31 minutes and 2 seconds'
Log
8781444
'' should equal '101 days, 15 hours, 17 minutes and 24 seconds'
Log
8666486
'' should equal '100 days, 7 hours, 21 minutes and 26 seconds'
Log
8399606
'' should equal '97 days, 5 hours, 13 minutes and 26 seconds'
Log
1978875
'' should equal '22 days, 21 hours, 41 minutes and 15 seconds'
Log
4770163
'' should equal '55 days, 5 hours, 2 minutes and 43 seconds'
Log
8682408
'' should equal '100 days, 11 hours, 46 minutes and 48 seconds'
Log
4339561
'' should equal '50 days, 5 hours, 26 minutes and 1 second'
Log
8901178
'' should equal '103 days, 32 minutes and 58 seconds'
Log
6173494
'' should equal '71 days, 10 hours, 51 minutes and 34 seconds'
Log
3449197
'' should equal '39 days, 22 hours, 6 minutes and 37 seconds'
Log
360841
'' should equal '4 days, 4 hours, 14 minutes and 1 second'
Completed in 8.21ms
'''
