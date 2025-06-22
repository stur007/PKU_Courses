n = int(input())
haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
        'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
tzolkin = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk',
           'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
print(n) ### 做了好几遍AC不了的原因竟然是少了这一句话！！！
for _ in range(n):
    s = input().split()
    haab_date = int(s[0][:-1])
    haab_month = haab.index(s[1])
    haab_year = int(s[2])
    days = haab_year *365 +haab_month *20 + haab_date
    tzolkin_year, reserve_days = divmod(days, 260)
    tzolkin_number = (reserve_days%13)+1
    tzolkin_letter = reserve_days%20
    print(tzolkin_number,tzolkin[tzolkin_letter], tzolkin_year)
