Conta classe:
    limiteChequeEspecial = 1000,0

    def __init__ (self, numero, saldo):
        auto. numero = numero
        auto.  saldo = saldo

    def __str__(self):
        retorno f"Conta {self. numero}: R$ {self. saldo}. Limite: {self. limiteChequeEspecial})"

    debitar def (self, valor):
        auto. saldo = self. saldo - valor

    def creditar (self, valor):
        auto. saldo = self. saldo + valor

    def modificadoLimite(valor):
        se valor > Conta. limiteChequeEspecial:
            Conta, o que está por fazer. limiteChequeEspecial = valor

classe Banco:
    def __init__(self):
        auto. contas = {}

    def cadastrarConta (self, conta):
        auto. contas [conta. numero] = conta

    def relatorioContas(self):
        impressão (self. contas)

    def transferencia (self, numeroOrigem, numeroDestino, valor):
        contaOrigem = self. contas[numeroOrigem]
        constestino = self. contas[numeroDestino]
        
        se contaOrigem. saldo >= valor:
            contaOrigem. débito (valor)
            contaDestino. creditar (valor)
            impressão("Valor transferido: ", valor)
        outra coisa:
            se abs (contaOrigem. saldo - valor) <= contaOrigem. limiteChequeEspecial:
                contaOrigem. débito (valor)
                contaDestino. creditar (valor)
                impressão("Valor transferido: ", valor)
            outra coisa:
                imprimir(f"A conta {numeroOrigem} excedeu o limite do cheque especial.")
            

c1 = Conta("123-4", 100,0)
c2 = Conta("678-9",500,0)

Conta, o que está por fazer. modificarLimite(2.0)

impressão(c1)
imprimir(c2)

bancoDoBrasil = Banco()
caixa = Banco()

#bancoDoBrasil.relatorioContas

bancoDoBrasil. cadastrarConta(c1))

Caixa. cadastrarConta(c2))

#bancoDoBrasil.relatorioContas
bancoDoBrasil. transferencia ("123-4", "678-9" , 10000,0)

bancoDoBrasil. transferencia ("123-4", "678-9", 1.0)
bancoDoBrasil. transferencia ("123-4", "678-9", 50.0)
bancoDoBrasil. transferencia ("123-4", "678-9", 100.0)
bancoDoBrasil. transferencia ("123-4", "678-9", 10.0)
bancoDoBrasil. transferencia ("123-4", "678-9" , 1000,0)

impressão(c1)
impressão(c2)