s = input()
r = ""
c = 1
for i in range(len(s)):
  if i + 1 < len(s) and s[i] == s[i + 1]:
    c += 1
  else:
    r += s[i]
    if c > 1: r += str(c)
    c = 1
print(r)
