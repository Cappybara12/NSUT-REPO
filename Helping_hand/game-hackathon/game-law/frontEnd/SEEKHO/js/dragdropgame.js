// en1 = document.getElementById("part1eng")
// en1.addEventListener("click",select)
// hin1 = document.getElementById("part1hindi")
// hin1.addEventListener("click",checkAns)

// en2 = document.getElementById("part2eng")
// en2.addEventListener("click",select)
// hin2 = document.getElementById("part2hindi")
// hin2.addEventListener("click",checkAns)

// en3 = document.getElementById("part3eng")
// en3.addEventListener("click",select)
// hin3 = document.getElementById("part3hindi")
// hin3.addEventListener("click",checkAns)
elCount=3
for(let i =1;i<=elCount;i++){
    enel = document.getElementById("part"+String(i)+"eng")
    hinel = document.getElementById("part"+String(i)+"hindi")
    enel.addEventListener("click",select)
    hinel.addEventListener("click",checkAns)
}

currentSelection = null
correctCount = 0
function checkAns(event){
    console.log(currentSelection)
    console.log(event.target.id)
    en = document.getElementById(currentSelection)
    hin = document.getElementById(event.target.id)
    if(currentSelection != null){
        if(String(currentSelection).slice(0,5)==String(event.target.id).slice(0,5)){
            hin.style.background="#197731"
            en.style.background="#197731"
            setTimeout(()=>{
                en.style.display="none"
                hin.style.display="none"
            },250)
            currentSelection = null;
            correctCount+=1;
            if(correctCount == elCount){
                console.log("2")
                body = document.getElementById("modal-body");
                body.innerHTML=`<h1>Congrats Now you can move to next Level</h1>`
                setTimeout(()=>{
                    window.location.href = "Game%20page.html";
                },500)
            }
        }
        else{
            hin.style.background="#ef5800"
            en.style.background="#ef5800"
            setTimeout(()=>{
                en.style.background=""
                hin.style.background=""
            },250)
            currentSelection = null;
            console.log("first")
        }
    }
    
}
function select(event){
    if(currentSelection!=null){
        currenten = document.getElementById(currentSelection);
        currenten.style.background=""
    }
    en = document.getElementById(event.target.id);
    en.style.background = "#378334";
    currentSelection = event.target.id
    console.log(currentSelection)
}