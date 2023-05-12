import sparkpi.sparkPi as p
from decimal import Decimal, getcontext



def test_small_thing():
    assert p.calc_pi(2) == Decimal('3.14')
