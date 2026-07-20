'''
Implemente em Python um sistema para uma plataforma de
cursos online que utilize herança e polimorfismo,
armazenando os dados em uma lista. Crie uma classe base
chamada Participante, com os atributos nome e email, e um
método emitirCertificado() que retorna uma mensagem
genérica. Em seguida, crie as subclasses Aluno, com o
atributo curso, e Instrutor, com o atributo especialidade,
ambas sobrescrevendo o método emitirCertificado() com
mensagens específicas: o aluno recebe um certificado de
conclusão do curso e o instrutor um certificado de participação
como palestrante. O programa deve conter um menu com as
opções: 1) Cadastrar participante, 2) Listar participantes, 3)
Emitir certificados, e 0) Sair. O usuário deve escolher entre
cadastrar um aluno ou instrutor, e os dados devem ser
armazenados em uma lista de objetos do tipo Participante. O
método emitirCertificado() deve ser chamado de forma
polimórfica para cada participante cadastrado.
'''