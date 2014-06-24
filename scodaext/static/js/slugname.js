
var a=function() {
    var slugify= function(s) 
        {
            return s.toLowerCase().replace(/[^A-Za-z0-9-]/g,"-")
            }
    
    var slugifyName = function()
        {
            document.getElementsByName('slug')[0].value=slugify(this.value);
            }

    document.getElementsByName('name')[0].onkeyup=slugifyName;
    
    if (Markdown) {
        var converter = new Markdown.Converter();
        var editor = new Markdown.Editor(converter);
        editor.run();
        }
    }();

