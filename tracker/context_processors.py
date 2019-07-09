

def variables(request):
    is_popup = getattr(request, 'is_popup', False)
    base_template = 'popup.html' if is_popup else 'core.html'
    return {'is_popup': is_popup,
            'base_template': base_template
            }
