# 🏛️Sistema Bancário
O projeto consiste em criar um sistema bancario com as operações: sacar, depositar e visualizar extrato.

## Linguagem utilizada
![Python](https://img.shields.io/badge/Python-000?style=for-the-badge&logo=python)

## 💰Operação de depósito
Deve ser possível depositar valores positivos. O projeto trabalha apenas com 1 usuário, dessa forma não precisa identificar número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibir na operação de extrato.

## 💸Operação de saque
O sistema deve permitir realizar 3 saques diários com limete máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informndo que não é possivel sacar o dinheiro por falta de saldo. Todos saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## 📜Operação de extrato
Essa operação lista todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores são exibidos utilizando o formato R$ xxx.xx.

## 🚹Operação de criação de usuarios
Essa operação pode criar usuarios, informando os valores: nome completo, data de nascimento e endereço. O codigo ainda não vinculada as demais operaçoes com o usuario. Um cpf so pode ter um usuario.

## 📜Operação de listar usuarios
Essa operação lista todos os usuario cadastrados.

## 📧Operação de criação de contas
Essa operação pode criar contas, verifica o cpf, se existir o cpf cadastrado será possivel criar a conta. O codigo ainda não vinculada as demais operaçoes com a conta. Um cpf pode ter mais de uma conta.

## 📜Operação de listar contas
Essa operação lista todos os contas cadastrados.