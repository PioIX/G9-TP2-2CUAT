function filtrado(display)
{
  
  let zapatillas = document.getElementsByClassName('zapatillas');
  for (let i = 0; i < zapatillas.length; i++) {
    zapatillas[i].style.display = display ;  
  }

  let pantalones = document.getElementsByClassName('pantalones');
  for (let i = 0; i < pantalones.length; i++) {
    pantalones[i].style.display = display ;  
  }

  
  let buzos = document.getElementsByClassName('buzos');
  for (let i = 0; i < buzos.length; i++) {
    buzos[i].style.display = display ;  
  }

  
  let remeras = document.getElementsByClassName('remeras');
  for (let i = 0; i < remeras.length; i++) {
    remeras[i].style.display = display ;  
  }
  
} 

function filtrarProductos(producto) 
{
  filtrado("none");
  let array = document.getElementsByClassName(producto);
  for (let i = 0; i < array.length; i++) {
    array[i].style.display = '' ;  
  }
}

function filtrar() {
  let valor = document.getElementById('selectFiltros').value;

  if (valor == "todo") {
    filtrado('')
  }
  else{
    filtrarProductos(valor)
  }
}

//ARREGLAR PEDIDO POST DESCRIPCION
function envioAjaxPOST() 
{
  $.ajax({
    url:"/recepcionAjax",
    type:"PUT",
    data:{"descripcion": document.getElementById("descripcion").value,
          "producto":document.getElementById("snk-nombre").inner
  },

    success: function(success)
  {
    let datos = JSON.parse(response);
      alert(`Tu Descripcion'${document.getElementById("descripcion").value}' se ha añadido correctamente`)
    document.getElementById("descripcion").innerHTML = document.getElementById("descripcion").value;
    },
    error: function(error){
      console.log(error)
    }
  });
  
}