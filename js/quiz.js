
var form="<h3>{{title}}</h3> \
  <p>{{description}}</p> \
  <form> \
  {{{questions}}} \
  <input type='button' value='submit' class='submit' onclick='check()'/>\
  </form> \
  "
var quiz;

function check() {
  function get_right_answer(a) {
    for (i in a) {
      if (a[i].correct) {
        return a[i].answer;
        }
    }
    return false;
  }
  
  _.each(quiz.questions, function(d,i) {
    var an=$("input:radio[name=q"+i+"]:checked").val();
    console.log(an);
    $("#q"+i+" .answer").remove();
    if (an===get_right_answer(d.answers)) {
      $("#q"+i).append("<div class='answer correct'>correct</div>");
      }
    else {
      $("#q"+i).append("<div class='answer wrong'>incorrect</div>");
      }
    })
  }
function render_mc_answer(q,id)  {
  q.aid=Math.floor(Math.random()*10000);
  q.id=id;
  var tmpl="<li><input type='radio' name='{{id}}' id='{{aid}}' value='{{answer}}'>\
    <label for='{{aid}}'>{{answer}}</label></li>";
  return Mustache.render(tmpl,q);
  }
  
function render_question(q,id) {
  var id="q"+id;
  var tmpl="<div class='question' id='{{id}}' >{{question}}\
        <ul> \
        {{{answers}}}\
        </ul> \
        </div>"

  var view={"question":q.question,
    "id":id};
  view.answers=_.map(q.answers, function(x) {
  return render_mc_answer(x,id);}).join("\n")
  return Mustache.render(tmpl,view);  
  }

function doquiz() {
  var data=document.location.hash.substr(1);
  console.log(data);
  $.getJSON(data,function(d) {
    quiz=d;
    console.log(d);
    var view={"title":d.title,
      "description":d.description};
    view.questions=_.map(d.questions,render_question).join("\n");  
    
    $("#form").append(Mustache.render(form,view));
    })
  }

$(document).ready(doquiz());  
