let valorPacote = 0;
let totalAdicionais;

function CalcularTotalViagem(){
    CalcularPacote();
    CalcularAdicionais();
    let totalFinal = totalAdicionais + valorPacote;
    
    document.getElementsByName("TotalFinal").innerHTML 
 }

 function CalcularPacote(){
    let qtdPacotes = document.querySelectorAll("input[name='pacotes']").length;
    console.log(qtdPacotes);

    let pacotes = document.querySelectorAll("input[name='pacotes']");
    
    console.log(pacotes);
    for(var i=0; i < qtdPacotes; i++)
    {
        if( pacotes[i].checked == true )
        {
            console.log(pacotes[i].value);
            valorPacote = Number(pacotes[i].value);
            break;
        }
    }
 }

 function CalcularAdicionais(){
    totalAdicionais=0;
    let adicionais = document.querySelectorAll("input[type='checkbox']");
    console.log(adicionais);
    for (let i=0; i < adicionais.length; i++){
        if (adicionais[i].checked == true) {
            totalAdicionais = totalAdicionais + parseFloat(adicionais[i].value);
        }
    }
    
 }