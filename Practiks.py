# guests = ['ms.Tikhanovskaya','msr.Chaliy','msr.Bykov','msr.Armen','msr.Georgiy']
# #guest_person = guests[3]
# invite_text_intro = 'Dear '
# invite_text_body = '! I invite you to lounch!'
# #print(f'{invite_text_intro}{guest_person}{invite_tetxt_body}')
# print(f'{invite_text_intro}{guests[0]}{invite_text_body}')
# print(f'{invite_text_intro}{guests[1]}{invite_text_body}')
# print(f'{invite_text_intro}{guests[2]}{invite_text_body}')
# print(f'{invite_text_intro}{guests[3]}{invite_text_body}')
# print(f'{invite_text_intro}{guests[4]}{invite_text_body}')

import keyword
kw_list = keyword.kwlist
for kw in kw_list:
    print(kw)