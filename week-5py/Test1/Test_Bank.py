from Banky import Luckydraw
def test_luck():
            assert Luckydraw("Hello")==100
            assert Luckydraw("Hi")==20
            assert Luckydraw("hi")==20
            assert Luckydraw("What's up")==0

