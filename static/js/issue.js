var scoda = scoda || {}

scoda.issueBadge = function(element, assertion) {
    OpenBadges.issue(assertion, function(e,s) {
        var text = element.getAttribute("data-success");
        element.innerHTML = text;
        element.setAttribute("href","http://backpack.openbadges.org");
        element.setAttribute("target","_new");
        element.setAttribute("onclick","");
        });
    }
