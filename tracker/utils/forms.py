from django.forms import widgets


class Textarea(widgets.Textarea):
    class Media:
        js = ('js/tinymce/tinymce.min.js', 'js/textarea.js')

    def __init__(self, attrs=None):
        if not attrs:
            attrs = {'class': 'rich-editor'}
        else:
            attrs['class'] = "%s %s " % ('text-input', attrs.get('class', ''))
        super(Textarea, self).__init__(attrs)
