x1, y1, z1, s1 = [int(input()) for i in range(4)]
x2, y2, z2, s2 = [int(input()) for i in range(4)]


if x2 > x1+s1 or y2 > y1+s1 or z2 > z1+s1:
  print(0)
else:
  xstart = max(x1, x2)
  xend = min(x1+s1, x2+s2)
  ystart = max(y1, y2)
  yend = min(y1+s1, y2+s2)
  zstart = max(z1, z2)
  zend = min(z1+s1, z2+s2)

  print((xend - xstart) * (yend - ystart) * (zend - zstart))


