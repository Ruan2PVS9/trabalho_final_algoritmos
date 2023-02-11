O trabalho final do CCR Algoritmos e Programação é uma agenda de compromissos. A agenda deverá conter a data e hora do compromisso, descrição e duração (em horas) do mesmo. Exemplo: Data: 24/12/2022 Hora: 19:00 Duração: 3.5 Descrição: Jantar de Natal no Palácio do Alvorada

A agenda deverá permitir a inclusão, exclusão, consulta e alteração de compromissos cadastrados. A consulta deverá ser por data (aparecem todos os eventos na data informada) ou por data e hora, aparecem todos os eventos cadastrados na data e hora informados. Deverá existir um menu para o usuário escolher a ação sobre a agenda. Por exemplo:

Incluir Consultar Alterar Excluir Listar todos Sair

Descrição das opções:

Incluir: permite que um compromisso seja incluído na agenda. Verificar se já existe um compromisso agendado para a mesma data e horário.

Consultar: permite fazer consultas de duas formas: pela data e pela data e hora. No caso de apenas pela data, listar todos os compromissos naquela data. Para data e hora, apenas o compromisso agendado para a data e hora informados. Apresentar a mensagem “Agenda Vazia” caso não existam compromissos para a consulta realizada.

Alterar: permite alterar a descrição e a duração de um compromisso. O usuário digita a data e hora do compromisso a ser alterado. Apresentar a mensagem “Compromisso não encontrado” caso não exista compromisso para a data e hora informados.

Excluir: permite excluir um compromisso. A implementação é similar ao da opção Alterar, exceto que o compromisso é excluído da lista.

Listar todos: lista todos os compromissos da agenda.

Sair: finaliza o programa.