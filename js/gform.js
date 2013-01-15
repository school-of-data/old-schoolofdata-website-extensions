

function gform(fk,name,val) {
    gurl="https://docs.google.com/spreadsheet/formResponse?formkey="+ fk +"&ifq"
    data={"entry.0.single":name,"entry.1.single":val,"submit":"Submit","pageNumber":0,"backupCache":undefined}
    $.post(gurl,data,function(d) {
      console.log("success");
      });
    }

