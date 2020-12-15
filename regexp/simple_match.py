#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = 'ab?'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '[abc]{3}\Z'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = 'sofia\.mp[3|4]\Z'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '(taverna|versus|vera|zveri)\Z'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '[a|b]{3}\Z'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '([a-zA-Z]{2}){3}\Z'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = '([a-zA-Z]{3}\s){2}[a-zA-Z]{3}\Z'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = 'a[a-zA-Z|\.|\-|]*[0|3|]*\Z'
