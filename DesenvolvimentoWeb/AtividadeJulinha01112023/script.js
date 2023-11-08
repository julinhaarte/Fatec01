comboValue = 0

function Calcular() {

    let checkboxes=0;
    let adicionais=0;

    let nome = document.getElementById("nome").value;
    let telefone = document.getElementById("telefone").value;
    let comboValue = parseFloat(document.querySelector("#lanches select").value);
  
     checkboxes = document.querySelectorAll("input[name='adicionais']");

    let descricaoAdicionais = "";

    for (i=0; i< checkboxes.length ; i++) {
      if (checkboxes[i].checked) {
        adicionais += 2;
        descricaoAdicionais = descricaoAdicionais+ checkboxes[i].textContent;
      }
    } 

    let entregaValue =0;
     entregaValue = parseFloat(document.querySelector('input[name="gridRadios"]:checked').value);
  

    let total = comboValue + adicionais + entregaValue;
    let descricao = `Seu combo custará ${comboValue} reais`;
  
    if (adicionais > 0) {
      descricao += ` com ${adicionais} reais de adicionais ${descricaoAdicionais}`;
    }
  
    descricao += ` e ${entregaValue} reais de taxa de entrega`;
  

    document.getElementById("floatingInputDisabled").value = `Total para ${nome} (${telefone}): R$ ${total.toFixed(2)}`;
  

    document.getElementById("floatingTextarea2Disabled").value = descricao;


}
    
  
