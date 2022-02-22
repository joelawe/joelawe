def computepay(h, r):
    if h <= 40:
        pay = h * r
        return pay
    elif h > 40:
        pay = ((h - 40) * (r * 1.5)) + (40 * r)
        return pay


hrs = input('Enter hours:')
hrs = float(hrs)
rate = input('Enter rate:')
rate = float(rate)

print(computepay(hrs, rate))
