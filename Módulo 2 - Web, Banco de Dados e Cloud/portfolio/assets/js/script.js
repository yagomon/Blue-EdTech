  
/* Cria a variável inputNome e coloca nela o elemento que possui o id nome */
let inputNome = document.querySelector('#nome')

/* Só posso utilziar a arrow function (=>) quando a função não tiver nome */
inputNome.addEventListener('keyup', () => { 
   if(inputNome.value.length < 4){
      inputNome.style.borderColor = 'red'
   } else {
      inputNome.style.borderColor = 'green'
   }
})

