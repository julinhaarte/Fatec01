let lampada=document.getElementById("lampada");
function ligar(){
    lampada.src="lampadaLiga.png";
}

function desligar(){
    lampada.setAttribute("src", "lampadaDesligada.png");
}

function alternar(){
    if(lampada.getAttribute("src")=="lampadaLiga.png"){
    desligar();
    }

    else if (lampada.getAttribute("src")=="lampadaDesligada.png") 
    {ligar();
    }
}

function sumir(){
    lampada.hidden = true ;
}

function aparecer(){
    lampada.hidden = false ;
}
document.getElementById("titulo").style.color="pink";

function piscar(){
    alternar()
}
setInterval(piscar, 500);