"""
You will be given two strings: lamps and drone. lamps represents a row of lamps, currently off, each represented by x. When these lamps are on, they should be represented by o.

The drone string represents the position of the drone T (any better suggestion for character??) and its flight path up until this point =. The drone always flies left to right, and always begins at the start of the row of lamps. Anywhere the drone has flown, including its current position, will result in the lamp at that position switching on.

Return the resulting lamps string. 
"""


import codewars_test as test
from solution import fly_by

@test.describe("Example tests")
def test_group():
    @test.it("example tests")
    def test_case():
        test.assert_equals(fly_by('xxxxxx', '====T'), 'ooooox')
        test.assert_equals(fly_by('xxxxxxxxx', '==T'), 'oooxxxxxx')
        test.assert_equals(fly_by('xxxxxxxxxxxxxxx', '=========T'), 'ooooooooooxxxxx')


def fly_by(lamps, drone):
    line = list(zip(lamps,drone))
    return ''.join(['o' for x in line] + ['x' for i in range(0,len(lamps) - len(drone))])