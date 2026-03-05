def increase_by(pct):
    return pct*1.05

print("increase 100 by 5%", increase_by(100))

anon_increase = lambda p: p * 1.05

print(type(anon_increase),"increase 100 by 5%", anon_increase(100))