const elementoNome = document.getElementById('digimon'); /* Cria a variável elementoNome e coloca o elemento com o id nome nela */
const elementoSituacao = document.querySelector('#nível'); /* Cria a variável elementoSituacao e coloca o elemento com o id situacao nela */
const elementoImg = document.querySelector('#imagem') /* Cria a variável elementoImg e coloca o elemento com o id imagem nela */
let elementoBtn = document.querySelector('#alterar') /* Cria a variável elementoBtn e coloca o elemento com o id alterar nela */

/* Adiciona o evento de click no elementoBtn e executa a função anonima (arrow function) */
elementoBtn.addEventListener('click', () =>{
    /* Verifica se o valour do botão é 'primeiro', se for troque de humor para o Hulk */
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './assets/img/agumon.png' /* Troca a imagem do personagem */
        elementoNome.innerText = 'Agumon' /* Altera o texto do elemento nome */
        elementoSituacao.innerText = 'Nível: criança' /* Altera o texto do elemento situação */
        elementoBtn.innerText = 'Digivolve para ...'
        elementoBtn.value = 'segundo' /* Altera valor do botão */
    } else if(elementoBtn.value == 'segundo') { /* Verifica se o valour do botão é 'segundo', se for troque de humor para o Dr. Hulk */
        elementoImg.src = './assets/img/graymon.png'  /* Troca a imagem do personagem */
        elementoNome.innerText = 'Graymon' /* Altera o texto do elemento nome */
        elementoSituacao.innerText = 'Nível: adulto' /* Altera o texto do elemento situação */
        elementoBtn.innerText = 'Digivolve para ...'
        elementoBtn.value = 'terceiro'  /* Altera valor do botão */
    } else if(elementoBtn.value == 'terceiro') { /* Verifica se o valour do botão é 'segundo', se for troque de humor para o Dr. Hulk */
    elementoImg.src = './assets/img/metalgreymon.png'  /* Troca a imagem do personagem */
    elementoNome.innerText = 'MetalGreymon' /* Altera o texto do elemento nome */
    elementoSituacao.innerText = 'Nível: perfeito' /* Altera o texto do elemento situação */
    elementoBtn.innerText = 'Digivolve para ...'
    elementoBtn.value = 'quarto'  /* Altera valor do botão */
    } else if(elementoBtn.value == 'quarto') { /* Verifica se o valour do botão é 'segundo', se for troque de humor para o Dr. Hulk */
    elementoImg.src = './assets/img/wargreymon.png'  /* Troca a imagem do personagem */
    elementoNome.innerText = 'WarGreymon' /* Altera o texto do elemento nome */
    elementoSituacao.innerText = 'Nível: final' /* Altera o texto do elemento situação */
    elementoBtn.innerText = 'Voltar'
    elementoBtn.value = 'quinto'  /* Altera valor do botão */
    } else { /* Se os valores do botão não forem, 'primeiro' nem 'segundo' mude para o Dr. Banner */
        elementoImg.src = './assets/img/koromon.png' /* Troca a imagem do personagem */
        elementoNome.innerText = 'Koromon' /* Altera o texto do elemento nome */
        elementoSituacao.innerText = 'Nível: bebê' /* Altera o texto do elemento situação */
        elementoBtn.innerText = 'Digivolve para ...'
        elementoBtn.value = 'primeiro' /* Altera valor do botão */
    }
})