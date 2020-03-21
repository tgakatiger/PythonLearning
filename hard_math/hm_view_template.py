class HMTemplateBase:
    def __init__(self, template='', *args, **kwargs):
        self.template = template

    def set_template(self, template):
        self.template = template
        
    def get_template(self):
        return self.template

    def __repr__(self):
        return self.template
        
        
class HMViewTemplate(HMTemplateBase):
    def __init__(self, obj=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj = obj
        
    def set_object(self, obj=None):
        if obj is not None:
            self.obj = obj

    def get_object(self):
        return self.obj
        
    def get_instance(self):
        attr_list = [i for i in dir(self.get_object()) if not i.startswith('_')]
        out = ''
        for t_word in self.get_template().split():
            if t_word in attr_list:
                attr = self.get_object().__getattribute__(t_word)
                if isinstance(attr, int):
                    out += f'{attr:02} '
                else:
                    out += str(attr)
        return out.strip()    


class HMTableViewTemplate(HMViewTemplate):
    def __init__(self, obj=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj = obj

    def get_instance(self):
        return self.get_object()
