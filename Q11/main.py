'''
Desenvolva um sistema para gerenciar veículos de transporte
público em uma cidade inteligente. Crie uma classe abstrata
VeiculoTransporte, com os atributos placa e
capacidadePassageiros, e um método abstrato
calcularCustoOperacional() que retorna o custo por
quilômetro. Crie as subclasses Onibus, com o atributo
consumoPorKm (litros/km), e Metro, com
consumoEnergiaPorKm (kWh/km). Cada uma deve
implementar o cálculo do custo com valores fictícios: R$ 6,00
por litro de diesel e R$ 0,80 por kWh. Na função principal,
permita criar objetos dos dois tipos e exibir os custos
operacionais usando polimorfismo. Implemente tratamento de
exceções para validar os dados de entrada: placa não pode
ser vazia, e os valores numéricos devem ser positivos.
'''