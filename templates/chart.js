//Resultado
var nega = document.querySelector(".negativo").dataset.chart;
var cuarentena = document.querySelector(".cuarentena").dataset.chart;
var positivo = document.querySelector(".positivo").dataset.chart;
//Datos fiebre
var fiebre_baja = document.querySelector(".fiebre-baja").dataset.chart;
var fiebre_media = document.querySelector(".fiebre-media").dataset.chart;
var fiebre_alta = document.querySelector(".fiebre-alta").dataset.chart;
var fiebre_text = document.querySelector(".fiebre-title").textContent;
//Datos Edad
var edad_baja = document.querySelector(".edad-menor").dataset.chart;
var edad_media = document.querySelector(".edad-entre").dataset.chart;
var edad_alta = document.querySelector(".edad-mayor").dataset.chart;
var edad_text = document.querySelector(".edad-title").textContent;

//Datos Glucosa
var glucosa_baja = document.querySelector(".glucosa-baja").dataset.chart;
var glucosa_media = document.querySelector(".glucosa-media").dataset.chart;
var glucosa_alta = document.querySelector(".glucosa-alta").dataset.chart;
var glucosa_text = document.querySelector(".glucosa-title").textContent;
//Datos Viajero
var viajero_baja = document.querySelector(".viajero-no").dataset.chart;
var viajero_media = document.querySelector(".viajero-moderado").dataset.chart;
var viajero_alta = document.querySelector(".viajero-infectado").dataset.chart;
var viajero_text = document.querySelector(".viajero-title").textContent;

//Datos Garganta
var garganta_baja = document.querySelector(".gargantea-baja").dataset.chart;
var garganta_media = document.querySelector(".gargantea-medio").dataset.chart;
var garganta_alta = document.querySelector(".gargantea-alta").dataset.chart;
var garganta_text = document.querySelector(".gargantea-title").textContent;

//Datos Tos
var tos_baja = document.querySelector(".tos-bajo").dataset.chart;
var tos_media = document.querySelector(".tos-medio").dataset.chart;
var tos_alta = document.querySelector(".tos-alta").dataset.chart;
var tos_text = document.querySelector(".tos-title").textContent;

//Datos Olfato
var olfato_baja = document.querySelector(".olfato-bajo").dataset.chart;
var olfato_media = document.querySelector(".olfato-medio").dataset.chart;
var olfato_alta = document.querySelector(".olfato-alta").dataset.chart;
var olfato_text = document.querySelector(".olfato-title").textContent;

//Datos Respiratorio
var respiratorio_baja = document.querySelector(".respiratorio-bajo").dataset.chart;
var respiratorio_media = document.querySelector(".respiratorio-medio").dataset.chart;
var respiratorio_alta = document.querySelector(".respiratorio-alta").dataset.chart;
var respiratorio_text = document.querySelector(".respiratorio-title").textContent;

//Datos Respiratorio
var pecho_baja = document.querySelector(".pecho-bajo").dataset.chart;
var pecho_media = document.querySelector(".pecho-medio").dataset.chart;
var pecho_alta = document.querySelector(".pecho-alta").dataset.chart;
var pecho_text = document.querySelector(".pecho-title").textContent;

//Resultados
var xValues = ["Negativo", "Cuarentena", "Positivo"];
var yValues = [nega,cuarentena,positivo];

//Datos fiebre
var xValuesFiebre = ["Fiebre Baja", "Fiebre Media", "Fiebre Alta"];
var yValuesFiebre = [fiebre_baja,fiebre_media,fiebre_alta];

//Datos edad
var xValuesEdad = ["Edad menor a 40", "Edad entre 40 y 50", "Edad mayor a 50"];
var yValuesEdad = [edad_baja,edad_media,edad_alta];

//Datos glucosa
var xValuesGlucosa = ["Diabetes bajo", "Diabetes medio", "Diabetes alto"];
var yValuesGlucosa = [glucosa_baja,glucosa_media,glucosa_alta];

//Datos viajero
var xValuesViajero = ["NO contacto con infectado(s)", "Duda de contacto", "Contacto infectado(s)"];
var yValuesViajero = [viajero_baja,viajero_media,viajero_alta];

//Datos Garganta
var xValuesGarganta = ["Dolor garganta bajo", "Dolor garganta medio", "Dolor garganta alto"];
var yValuesGarganta = [garganta_baja,garganta_media,garganta_alta];


//Datos Tos
var xValuesTos = ["Tos bajo", "Tos medioo", "Tos alto"];
var yValuesTos = [tos_baja,tos_media,tos_alta];

//Datos Olfato
var xValuesOlfato = ["Perdida de olfato y gusto bajo", "Perdida de olfato y gusto medio", "Perdida de olfato y gusto alto"];
var yValuesOlfato = [olfato_baja,olfato_media,olfato_alta];

//Datos Respiratorios
var xValuesRespiratorio = ["Problema respiratorio bajo", "Problema respiratorio medio", "Problema respiratorio alto"];
var yValuesRespiratorio = [respiratorio_baja,respiratorio_media,respiratorio_alta];

//Datos Pecho
var xValuesPecho = ["Dolor en el pecho bajo", "Dolor en el pecho medio", "Dolor en el pecho alto"];
var yValuesPecho = [respiratorio_baja,respiratorio_media,respiratorio_alta];


var barColors = ['#ffd2d2','#fdf9cd','#ccfddb'];


new Chart("chartResultado", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Grado de pertenencia"
    },
    scales: {
        xAxes: [{
            barPercentage: 0.4
        }]
    }
  }
});

new Chart("chartFiebre", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesFiebre,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesFiebre
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + fiebre_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartEdad", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesEdad,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesEdad
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + edad_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartGlucosa", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesGlucosa,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesGlucosa
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + glucosa_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartViajero", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesViajero,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesViajero
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + viajero_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartGarganta", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesGarganta,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesGarganta
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + garganta_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartTos", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesTos,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesTos
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + tos_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartOlfato", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesOlfato,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesOlfato
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + olfato_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartRespiratorio", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesRespiratorio,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesRespiratorio
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + respiratorio_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });
  new Chart("chartPecho", {
    type: "horizontalBar",
    indexAxis: 'y',
    data: {
      labels: xValuesPecho,
      datasets: [{
        backgroundColor: barColors,
        data: yValuesPecho
      }]
    },
    options: {
        legend: {display: false},
        title: {
            display: true,
            text: "Grado de pertenencia de " + pecho_text
        },
        scales: {
            xAxes: [{
                barPercentage: 0.4
            }]
        }
    }
  });