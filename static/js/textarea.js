$(document).ready(function() {
    var LANGUAGE_CODE = 'ru';
    var params = {
        selector: "textarea.rich-editor",
        language: LANGUAGE_CODE,
        relative_urls: false,
        convert_urls: false,
        cleanup: false,
        // verify_html : false,
        auto_cleanup_word : true,
        // extended_valid_elements : '+a[*]',
        remove_script_host : false,
        plugins: [
                    "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak spellchecker",
                    "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
                    "table contextmenu directionality emoticons template textcolor paste textcolor images files product",
                    "spellchecker improvedcode imagetools"
        ],
        toolbar1: "paste pastetext | bold italic underline | styleselect | bullist numlist | undo redo removeformat | table images files product media | forecolor backcolor | image link unlink | code fullscreen | fullscreen | spellchecker",
        menubar: false,
        toolbar_items_size: 'small',
        content_css : "/static/css/tiny.css",
        height : "350",
        paste_create_paragraphs : false,
        paste_create_linebreaks : false,
        paste_use_dialog : false,
        paste_auto_cleanup_on_paste : true,
        paste_convert_middot_lists : false,
        paste_unindented_list_class : "unindentedList",
        paste_convert_headers_to_strong : true,
        forced_root_block: false,
        force_br_newlines : false,
        force_p_newlines : false,
        images_path : '/manage/files/images/',
        files_path : '/manage/files/files/',
        products_path: '/manage/content/products/',
	//HTML ImprovedCode
        improvedcode_options : {
            height: 580
            ,indentUnit: 4
            ,tabSize: 4
            ,lineNumbers: true
            ,autoIndent: true
            ,theme: 'monokai'
        },
    spellchecker_languages: "Russian=ru,Ukrainian=uk,English=en",
    spellchecker_rpc_url: "https://speller.yandex.net/services/tinyspell",
    };

    if (!typeof tiny_height === 'undefined') {
        params['height'] = tiny_height;
    };

    if (!typeof tiny_width === 'undefined') {
        params['width'] = tiny_width;
    };
    tinymce.init(params);
});
