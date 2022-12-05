// function show_valueHViaje(x)
// {
//  document.getElementById("slider_value_HistViaje").innerHTML=x;
// }

// function add_one()
// {
//   document.f.histviaje.value=parseInt(document.f.histviaje.value)+0.01;
//   show_valueHViaje(document.f.histviaje.value);
// }

// function subtract_one()
// {
//   document.f.histviaje.value=parseInt(document.f.histviaje.value)-0.01;
//   show_valueHViaje(document.f.histviaje.value);
// }

function geraSpinner(){

    var formulario = document.getElementById('form_master');

    for(var i=0; i < formulario.elements.length; i++){
      if(formulario.elements[i].value === '' && formulario.elements[i].hasAttribute('required')){
        alert('Alerta... hay campos faltantes');
        return false;
      }
    }
    setTimeout(function () {
        document.getElementById("conteudo").innerHTML = "";
        document.getElementById("spinner_desativado").id = "spinner_ativado";
        document.getElementById("block_desativado").id = "block_ativado";
    }, 300)
}