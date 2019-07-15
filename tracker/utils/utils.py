from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect, render


def close_view(request, url, args=None, timeout=0, restore=False, getargs=None):
    if request.is_popup:
        return render(request, 'popup_done.html', {'timeout': timeout})
    else:
        url = reverse(url, args=args)
        args = []
        if restore:
            args.append('restore')
        if getargs:
            args.extend(getargs)
        if args:
            url = url + '?' + '&'.join(args)
        if url.startswith('/'):
            url = '%s://%s%s' % (settings.SCHEME, settings.DOMAIN, url)
        return redirect(url)


def cmp_to_text(cmps):
    result = []
    for item in cmps.keys():
        result.append(u'%s: %s -> %s' % (item, cmps[item][0] or '""', cmps[item][1]) or '""')
    return result


def compare(first, second, fields=[], exclude=[]):
    """
        порівнює поля двох об'єктів типу dict або class
    """
    def get_value(value, key):
        return value.__dict__[key] if getattr(value, '__dict__', None) else value[key] if key in value else None

    assert(type(first) == type(second))
    result = {}

    sets = set(first.__dict__.keys() if getattr(first, '__dict__', None) else first.keys())
    sets = sets.union(set(second.__dict__.keys() if getattr(second, '__dict__', None) else second.keys()))

    sets = sets & set(fields) if fields else sets
    sets = sets - set(exclude) if exclude else sets

    for item in sets:
        i = get_value(first, item)
        j = get_value(second, item)
        if not i and j:
            result[item] = (None, j)
        elif not j and i:
            result[item] = (i, None)
        elif not i == j and i and j:
            result[item] = (i, j)
    return result
