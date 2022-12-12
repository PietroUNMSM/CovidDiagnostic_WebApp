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
window.addEventListener('DOMContentLoaded', (event) => {
  validarFiebre();
  validarDiabetes();
  validarSlider();
});

function validarFiebre(){
  let fiebre = document.querySelector("#fiebre");
  fiebre.addEventListener('change', function(){
    if(fiebre.value<35.3 || fiebre.value>41.3){
        fiebre.nextElementSibling.classList.toggle("show-error");
      }
    else{
      fiebre.nextElementSibling.classList.toggle("show-error");
    }
  });
}
function validarEdad(){
  let edad = document.querySelector("#edad");
  edad.addEventListener('change', function(){
    if(edad.value<10 || edad.value>70){
      edad.nextElementSibling.classList.toggle("show-error");
      }
    else{
      edad.nextElementSibling.classList.toggle("show-error");
    }
  });
}
function validarDiabetes(){
  let diabetes = document.querySelector("#diabetes");
  diabetes.addEventListener('change', function(){
    if(diabetes.value<140 || diabetes.value>215){
      diabetes.nextElementSibling.classList.toggle("show-error");
      }
    else{
      diabetes.nextElementSibling.classList.toggle("show-error");
    }
  });
}
function validarSlider(){
  let sliders = document.querySelectorAll(".slider");
  sliders.forEach(function(slider){
    slider.addEventListener('change', function(){
      if(slider.value>=0.25 && slider.value<=0.75){
        if(slider.classList.contains("high")){
          slider.classList.remove("high");
        }
        slider.classList.add("medium");
      } else if(slider.value>0.75 && slider.value<=1.0){
        if(slider.classList.contains("medium")){
          slider.classList.remove("medium");
        }
        slider.classList.add("high");
      }
      else{
        if(slider.classList.contains("medium")){
          slider.classList.remove("medium");
        }
        if(slider.classList.contains("high")){
          slider.classList.remove("high");
        }
      }
    });
  });
}

function geraSpinner(){

    var formulario = document.getElementById('form_master');

    for(var i=0; i < formulario.elements.length; i++){
      if(formulario.elements[i].value === '' && formulario.elements[i].hasAttribute('required')){
        alert('Alerta... hay campos faltantes');
        return false;
      }
    }
    setTimeout(function () {
        //document.getElementById("conteudo").innerHTML = "";
        //document.getElementById("spinner_desativado").id = "spinner_ativado";
        //document.getElementById("block_desativado").id = "block_ativado";
        document.querySelector(".modal").classList.add('show-modal');
        //document.querySelector(".spinner").classList.add('show-spinner');
    }, 500)
    setTimeout(function () {
  }, 300)
}