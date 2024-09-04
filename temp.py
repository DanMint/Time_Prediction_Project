try:
    a = 90
    assert(a == 90), "not 90"

except AssertionError as e:
    exit(e)

print(a)