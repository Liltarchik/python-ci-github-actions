from arit import add

def test_add():
    try:
        assert add(2, 3) == 5
        print("Addition works correctly.")
    except AssertionError:
        print("Addition failed.")    
    try:
        assert add(-1, 1) == 0
        print("Addition works correctly.")    
    except AssertionError:
        print("Addition failed.")
    try:
        assert add(3, 3) == 8
        print("Addition works correctly.")
    except AssertionError:
        print("Addition failed.")

print(test_add())
print("hello world")