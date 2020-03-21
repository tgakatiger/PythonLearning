from utils import DefaultParams
from collections import namedtuple
from hm_view_template import HMViewTemplate
from hm_view_logic import HMViewLogic

class HMView:
    def __init__(self, items_list, hm_view_template, hm_view_logic, *args, **kwargs):
        self.answer = items_list
        self.hmvt = hm_view_template
        self.hmvl = hm_view_logic
        
    def view(self):
        for item in self.answer:
            self.hmvt.set_object(item)
            if self.hmvl.check(item):
                print(self.hmvt.get_instance())
                

class HMTableView(DefaultParams):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default('view_items', vtype=list)
        self.default('view_temlate', vtype=HMViewTemplate)
        self.default('view_logic', vtype=HMViewLogic)
        self.view_items_meta = self.get_view_items_meta()

    def view(self):
        for item in self.default('view_items_meta'):
            self.default('view_template').set_object(item)
            if self.default('view_logic').check(item):
                print(self.default('view_template').get_instance())

        
    def get_view_items_meta(self):
        VIMetaObject = namedtuple('VIMetaObject', 'item data_name data_len data')
        out = []
        for item in self.default('view_items'):
            for data_name in dir(item):
                if not data_name.startswith('_'):
                    data = item.__getattribute__(data_name)
                    # print(data)
                    data_len = len(str(data))
                    out.append(VIMetaObject(item.num, data_name, data_len, data))
        return out
