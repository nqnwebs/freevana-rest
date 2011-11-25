from djangorestframework.views import ListModelView, InstanceModelView

class MyListModelView(ListModelView):
    def get(self, *args, **kwargs):
        import ipdb;ipdb.set_trace()
        if self.args[0]:
            return qs.filter(name__icontains=self.args[0])
        else:
            return qs
