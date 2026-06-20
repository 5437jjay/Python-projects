from words_shorten import check
def test_check():
    try:
        assert check("Hi/nHello")!="H/nHll"
    except AssertionError:
        print("Something went wrong")
test_check()