var GCP_ACTIVE_CITIES=["Mekn\u00e8s","K\u00e9nitra","Tanger","Oujda"];
function gcpRunFilter(btn){
  var form=btn;
  while(form&&!(form.classList&&form.classList.contains("frm-show-form")))form=form.parentElement;
  var city =(form?form.querySelector('[id^="field_y68yj"]')||{}:{}).value||"";
  var type =(form?form.querySelector('[id^="field_um9ky"]')||{}:{}).value||"";
  var rooms=(form?form.querySelector('[id^="field_qfq1i"]')||{}:{}).value||"";
  city =city.trim(); type=type.trim(); rooms=rooms.replace(/\u00a0/g," ").trim();
  var cards=document.querySelectorAll(".gcp-pc");
  var cs=document.getElementById("gcp-coming-soon");
  var nr=document.getElementById("gcp-no-results");
  if(cs)cs.style.display="none";
  if(nr)nr.style.display="none";
  cards.forEach(function(c){c.style.display="";});
  if(city&&GCP_ACTIVE_CITIES.indexOf(city)===-1){
    cards.forEach(function(c){c.style.display="none";});
    if(cs)cs.style.display="block";
    return;
  }
  var visible=0;
  cards.forEach(function(card){
    var cc=card.getAttribute("data-city")||"";
    var ct=card.getAttribute("data-type")||"";
    var cr=(card.getAttribute("data-rooms")||"").replace(/\u00a0/g," ").trim();
    var cok=!city||cc===city;
    var tok=!type||ct===type;
    var rok=true;
    if(rooms){
      if(rooms==="5+ pi\u00e8ces"){var m=cr.match(/(\d+)/);rok=m?parseInt(m[1])>=5:false;}
      else rok=cr===rooms;
    }
    if(cok&&tok&&rok){card.style.display="";visible++;}
    else card.style.display="none";
  });
  if(visible===0&&nr)nr.style.display="block";
}
console.log("Syntax is OK");
