from collections import namedtuple
from math import log2
from hm_struct import HMStruct, HMStructInit
from hm_view import HMView
from hm_view_template import HMViewTemplate
from hm_view_logic import HMViewLogic

def main():
    items_list = [HMStructInit(HMStruct(i)).get() for i in range(2, 100)]
    view_template = 'num set_len pairs_len pairs pairs_sum dividers'
    
    hm_view_template = HMViewTemplate()
    hm_view_template.set_template(view_template)
    
    hm_view_logic = HMViewLogic()
    
    hm = HMView(items_list, hm_view_template, hm_view_logic)
    # hm = HMTableView(view_items=items_list, \
    #                  view_template=hm_view_template, \
    #                  view_logic=hm_view_logic)
    hm.view()

    # for i in range(6, 50, 2):
    #     print(f'{i} {sorted(Goldbah(i).get())} <=> {PrimeRange(i).decompose()}')


main()
