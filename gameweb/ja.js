var col=6,row=6,colm = 6,rowm = 6
var cd = 37;

var lll = document.getElementById("khung")
document.getElementById("col").addEventListener("change",()=>{
    col = document.getElementById("col").value
    if(col>=colm){
      console.log(col)
      for(let y = colm;y<col;y++){
        for(let nb = 1;nb<=row;nb++){
          var them = document.createElement("div")
          them.id = cd;
          // them.innerText = cd
          cd++;
          them.classList.add("o")
          lll.style.gridTemplateColumns = `repeat(${col},1fr)`
          them.onclick = function(){
            chon(this)
          }
          lll.appendChild(them);
        }
      }
      colm = col
    }
    else{
      col = colm
    }
})

document.getElementById("row").addEventListener("change",()=>{
  row = document.getElementById("row").value
  console.log(row)
    for(let y = rowm;y<row;y++){
      for(let nb = 1;nb<=col;nb++){
        var them = document.createElement("div")
        them.id = cd;
        // them.innerText = cd
        cd++;
        them.classList.add("o")
        lll.style.gridTemplateRows = `repeat(${row},1fr)`
        them.onclick = function(){
          chon(this)
        }
        lll.appendChild(them);
      }
    }
    rowm = row
})

var m = 0;
function chon(element){
  if(!element.textContent.trim()){
   if(m%2==0){
     element.innerText = 'x';
    //  element.style.background = "white"
     element.style.color = "black"
     m++;
   }
   else{
     element.innerText = 'o'
     element.style.color = "white"
    //  element.style.background = "black"
     m++;
   }
  }
}

var k = document.getElementById("but")

k.addEventListener('click',()=>{
    location.reload()
})

var q = 1;
var a = []
for(let i = 0;i<row;i++){
  a[i] = []
  for(let j = 0;j<col;j++){
    a[i][j] = document.getElementById(`${q++}`)
    a[i][j].addEventListener("click",(a11)=>{
      console.log(`toa do : (${i}:${j})`)
      let a111 = a11.target.innerHTML
      if(a111 === "x"){
        console.log(true)
      }
      else{
        console.log(false)
      }
    })
  }
}

