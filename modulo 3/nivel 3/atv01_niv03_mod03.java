/**- Considerando a solução apresentada no Hipertexto 5, aplique o padrão de projeto Strategy para criar uma simples calculadora. 
- Os requisitos para avaliar o projeto são:
- implementar uma interface Strategy com o método abstrato execute(). Deve haver três classes concretas que implementam a Strategy 
- para realizar as operações de Soma, Subtração e Multiplicação de números inteiros;
- o método execute() deve receber dois números inteiros como parâmetros e retornar o resultado também como número inteiro;
- como input do usuário, a aplicação deve receber o primeiro valor, depois o segundo e, por último, a operação matemática que deve realizar;
- no final, a aplicação deve definir qual Strategy será usada, com base na operação informada, e imprimir o resultado da operação.*/

var readlinesync = require('readline-sync')

ESTRATÉGIA DE INTERFACE
Estratégia de interface {
    execute(numero1: número, numero2: número):  número
}

ESTRATÉGIA CONCRETA SOMA
classe Soma implementa Estratégia {
    execução pública(numero1: número, numero2: número):  número {
       return parseInt(numero1. toString()) + parseFloat(numero2. toString())
    }
}

ESTRATÉGIA CONCRETA SUBTRAÇÃO
classe Subtracao implementa estratégia {
    execução pública(numero1: número, numero2: número):  número {
        retorno numero1 - numero2 
    }
}

ESTRATÉGIA DE MULTIPLICAÇÃO CONCRETA
classe Multiplicacao implementa Estratégia {
    execução pública(numero1: número, numero2: número):  número {
        retorno numero1 * numero2 
    }
}


CLASSE DE CONTEXTO
classe Calculadora {

    calcular(operacao: Estratégia) {
        retorno operacao. executar(num1, num2)
    }
}


CÓDIGO DO CLIENTE

let num1: number = readlinesync. question('insira o primeiro numero: \n')
let num2: number = readlinesync. question('insira o segundo numero: \n')
let operadorMatematico: string = readlinesync. question('informe a operacao que deseja realizar: [+] [-] [x]: \n')

const fazerConta = nova Calculadora()

if (operadorMatematico == '+') {
    console. log('${num1} + ${num2} = ${fazerConta. calcular(new Soma())}')
} else if (operadorMatematico == '-') {
    console. log('${num1} - ${num2} = ${fazerConta. calcular(novo Subtracao())}')
} else if (operadorMatematico == 'x') {
    console. log('${num1} x ${num2} = ${fazerConta. calcular(new Multiplicacao())}')
} mais {
    throw Error('ERR04 - Operação inválida')
}