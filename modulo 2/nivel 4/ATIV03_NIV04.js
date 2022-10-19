const polignos = ['circulo', 'quadrado','triangulo'];

function listarpolignos() {
    for (const e of polignos){
        console.log(e);
    }
}

listarpolignos();
console.log();

var compuador = {
    marca:'acer',
    modelo:'aspire ES 15',
    processador:'I3'
};

function listarpolignos(){
    for (const propriedade in compuador) {
        console.log(`${propriedade}: ${compuador[propriedade]}`);
    }
}

listarpolignos();