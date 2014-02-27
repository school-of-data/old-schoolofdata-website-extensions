var scoda = scoda || {}

scoda.issueBadge = function(element, assertion) {
    OpenBadges.issue(assertion, function(e,s) {
        var text = element.getAttribute("data-success");
        element.innerHTML = text;
        element.setAttribute("href","http://backpack.openbadges.org");
        element.setAttribute("target","_new");
        element.setAttribute("onclick","");
        });
    while (document.getElementsByTagName("iframe").length == 0) {
        console.log("waiting");
        };
    var i = document.getElementsByTagName("iframe")[0]
    i.style['width']="90%";
    i.style['left']="5%";
    i.style['margin-left']="0px";
    }
