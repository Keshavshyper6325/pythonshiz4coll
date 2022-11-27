s = "Hello World"
s = s.encode("utf-8")
print(type(s))
print(s)
print(b'\xE2\x9C\x85'.decode("utf-8"))