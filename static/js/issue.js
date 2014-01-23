scoda = scoda || {}

scoda.issue_badge = function(element, assertion) {
    OpenBadges.issue(assertion, function(e,s) {
        console.log(this);
        }
    }
