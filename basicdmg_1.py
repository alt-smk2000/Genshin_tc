import numpy as np
import pandas as pd
import matplotlib as mpl

# defining variables
base_ATK = 0
percent_ATK = 0
flat_ATK = 0
DEF = 0
EM = 0
crate = 0.05
cdmg = 0.5
talent_mul = 1
dmg_bonus = 0

# Add all params to lists


# non-crit damage not taking enemy level into consideration
def gen_damage_calc(base_ATK, percent_ATK, flat_ATK, talent_mul, dmg_bonus):
    net_ATK = base_ATK*(1+(percent_ATK/100)) + flat_ATK
    return net_ATK*(talent_mul/100)*(1+(dmg_bonus/100))

def crit_damage_calc(cdmg, base_ATK, percent_ATK, flat_ATK, talent_mul, dmg_bonus):
    non_crit = gen_damage_calc(base_ATK, percent_ATK, flat_ATK, talent_mul, dmg_bonus)
    return non_crit*(1+cdmg/100)

def main():
    base_ATK, percent_ATK, flat_ATK, talent_mul, dmg_bonus, cdmg = [float(x) for x in input('''Hi. Please type in the following info to estimate outgoing damage:\n Base ATK\n Percent ATK\n Flat ATK\n Talent Multiplier\n Damage bonus\n Crit Damage\n''').split()]
    print()
    print("Estimated non-CRIT damage is: ", gen_damage_calc(base_ATK, percent_ATK, flat_ATK, talent_mul, dmg_bonus))
    print("Estimated CRIT damage is: ", crit_damage_calc(cdmg, base_ATK, percent_ATK, flat_ATK, talent_mul, dmg_bonus))

if __name__ == "__main__":
    main()