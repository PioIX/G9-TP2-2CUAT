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
    type:"POST",
    data:{"descripcion": document.getElementById("descripcion").value},

    success: function(success)
  {
    let datos = JSON.parse(response);
      alert(`Tu Descripcion'${document.getElementById("descripcion").value}' se ha añadido correctamente`)
    },
    error: function(error){
      console.log(error)
    }
  });
  
}

function envioAjaxGET()
{
  $.ajax({
   url:"/recepcionAjax",
   type:"GET",
  
   success: function(response){
  
     console.log(response)
     
     vector = JSON.parse(response)
     
     console.log(vector)
    },
    error: function(error){
      console.log(error)
    }
  });
  
}
