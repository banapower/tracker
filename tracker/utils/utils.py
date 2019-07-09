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
