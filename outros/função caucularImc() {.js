function caucularImc() {
    var altura = parseFloat (documento. getElemenbyId ("altura"). valor) / 100;
    var peso = parseFloat (documento. getElemenbyId ("peso"). valor);
    var imc = peso / (altura * altura);

    if (imc > 25){
        alerta(imc + " Cuidado! Voçê precisa diminuir seu peso.");
    } else {
        if (imc < 18) {
            alerta(imc + " Cuidado! Voçê precisa aumentar seu peso.");
        } else {
            alerta (imc + " Parabens voçê está com o peso ideal");
        }
    }
}

    function soma () {

}