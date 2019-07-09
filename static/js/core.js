Popup = new Object();

Popup.click = function(element) {
    var a = element.target ? $(this) : $(element);
    var href = a.attr('href') || a.attr('data-href');
    var width = 974;
    var height = '95%';
    href += (href.indexOf('?') == -1) ? '?popup=1' : '&popup=1';
    if (a.hasClass('big')) {width = '85%'; height = '85%';}
    else if (a.hasClass('medium')) {width = 720; height = 540;}
    else if (a.hasClass('form')) {width = 500; height = 400;}
    else if (a.hasClass('bigform')) {width = 540; height = 470;}
    else if (a.hasClass('small')) {width = 320; height = 240;}
    else if(a.is('[class*="x"]') || a.is('[class*="p"]')) {
        var match = a[0].className.match(/([x|p])(\d+)\-(\d+)/);
        if (match){
            if (match[1] == "p"){
                width = match[2] + '%';
                height = match[3] + '%';
            }
            else {
                width = match[2] ;
                height = match[3] ;
            }
        }
    }
    $.colorbox({
                href: href,
                fixed:true,
                transition: 'none',
                opacity: 0.6,
                width: width,
                height: height,
                iframe: true,
                trapFocus: false,
                close: 'close',
                onOpen: function(){$('body').css({ overflow: 'hidden' });},
                onClosed: function(){$('body').css({ overflow: '' });},
                });
    return false;
};


Popup.init = function(elements) {
    if (!elements)
        elements = 'a.popup';
    $(elements).each(function() {
        var a = $(this);
        if (!a.hasClass('hasPopup')) {
            a.addClass('hasPopup');
            a.click(Popup.click);
        }
    });
};

Popup.close = function(refresh=false) {
    parent.$.colorbox.close();
        if (refresh) parent.location.reload();
};

$(document).ready(function() {
    Popup.init();
    $('#colorbox').draggable();
});