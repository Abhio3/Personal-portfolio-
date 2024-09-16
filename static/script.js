var tabtitles=document.getElementsByClassName("tab-title")
var tabcontents=document.getElementsByClassName("tab-contents")
function opentab(tabname){
    for( tabtitle of tabtitles){
        tabtitle.classList.remove("active-link")
    }
    for( tabcontent of tabcontents){
        tabcontent.classList.remove("active-tab")
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab")

}
var sidemenu = document.getElementById("side-menu");
function openmenu(){
    sidemenu.style.left ="10px";
}
function closemenu(){
    sidemenu.style.left="-200px";
}
function done (){
    var span = document.getElementById("msg")
    span.textContent="Thank you Your response has been submitted "
}
