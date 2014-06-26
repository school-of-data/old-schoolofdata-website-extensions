
var $=CMS.$;

$(document).ready(function() {
    var slugify= function(s) 
        {
            return s.toLowerCase().replace(/[^A-Za-z0-9-]/g,"-")
            }
    
    $("input[name='name']").on("keyup",function()
        {   
            
            $("input[name='slug']").val(slugify(this.value));
            });
    
    if (Markdown) {
        var suffixes=["","-1"]
        for (i in suffixes) {
            var converter = new Markdown.Converter();
            var editor = new Markdown.Editor(converter,suffixes[i]);
            editor.run();
        }
        }
    });

