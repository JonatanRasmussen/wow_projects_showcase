def to_reddit_table(input_str):
    rows = input_str.strip().split('\n')
    header_row = ['Class'] + rows[0].split(';')[1:]
    data_rows = [row.split(';') for row in rows[1:]]
    reddit_table = '|'.join(header_row) + '\n' + '|'.join(['-' * len(col) for col in header_row]) + '\n'
    for row in data_rows:
        reddit_table += '|'.join(row) + '\n'
    return reddit_table

my_str = """
;Dagger;Fist Weapon;Axe 1h;Mace 1h;Sword 1h;Axe 2h;Mace 2h;Sword 2h;Polearm;Staff;Wand;Off-hand;Shield;Warglaive;Bow;Crossbow;Gun
Monk;0;1;1;1;1;0;0;0;1;1;0;1;0;0;0;0;0
Dh;0;1;1;0;1;0;0;0;0;0;0;0;0;1;0;0;0
Evoker;1;1;1;1;1;1;1;1;1;1;0;1;0;0;0;0;0
Mage;1;0;0;0;1;0;0;0;0;1;1;1;0;0;0;0;0
Priest;1;0;0;1;0;0;0;0;0;1;1;1;0;0;0;0;0
Warlock;1;0;0;0;1;0;0;0;0;1;1;1;0;0;0;0;0
Sham_Int;1;1;1;1;0;1;1;0;0;1;0;1;1;0;0;0;0
Sham_Agi;0;1;1;1;0;0;0;0;0;0;0;0;0;0;0;0;0
Druid_Int;1;1;0;1;0;0;1;0;1;1;0;1;0;0;0;0;0
Druid_Agi;0;0;0;0;0;0;1;0;1;1;0;0;0;0;0;0;0
Outlaw;0;1;1;1;1;0;0;0;0;0;0;0;0;0;0;0;0
Stabby;1;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0
Dk_1h;0;0;1;1;1;1;1;1;1;0;0;0;0;0;0;0;0
Dk_2h;0;0;0;0;0;1;1;1;1;0;0;0;0;0;0;0;0
War_Prot;0;1;1;1;1;0;0;0;0;0;0;0;1;0;0;0;0
War_Fury;0;1;1;1;1;1;1;1;1;1;0;0;0;0;0;0;0
War_Arms;0;0;0;0;0;1;1;1;1;1;0;0;0;0;0;0;0
Pala_Prot;0;0;1;1;1;0;0;0;0;0;0;0;1;0;0;0;0
Pala_Holy;0;0;1;1;1;1;1;1;1;0;0;1;1;0;0;0;0
Pala_Ret;0;0;0;0;0;1;1;1;1;0;0;0;0;0;0;0;0
Hunt_R;0;0;0;0;0;0;0;0;0;0;0;0;0;0;1;1;1
Hunt_M;0;0;0;0;0;1;0;1;1;1;0;0;0;0;0;0;0
"""

print(to_reddit_table(my_str))