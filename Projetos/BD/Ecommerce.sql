-- Criando BD
create database ecommerce;
use ecommerce;

-- Criar tabela Cliente
create table clients(
	idClient int auto_increment primary key,
    Fname varchar(10),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Address varchar(30),
    constraint unique_cpf_client unique (CPF)
);
alter table clients auto_increment=1;

-- Criar tabela Produto
create table product(
	idProduct int auto_increment primary key,
    Pname varchar(10) not null,
    classification_kids bool default false,
    category enum('Eletronico', 'Vestimenta','Brinquedos', 'Alimentos','Moveis') not null,
    avaliacao float default 0,
    dimensao varchar(10),
    constraint unique_cpf_client unique (CPF)
);
alter table product auto_increment=1;

-- Criar tabela pedido
create table orders(
	idOrder int auto_increment primary key,
    idOrderClient int,
    orderStatus enum('Cancelado', 'Confirmado', 'Em processamento') default 'Em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    paymentCash bool default false,
    
    constraint fk_orders_client foreign key (idOrderClient) references clients(idClient)
);
alter table orders auto_increment=1;

-- Criar tabela pagamento TODO termine de implentar a tabela e crie a conexão com as tabelas necessarias
-- Alem disso, reflita essa modificaçao no diagrama esquema relaciona
-- criar constraints relacionadas ao pagamento
create table payments(
	idClient int,
    idpayment int,
    typePayment enum('Boleto', 'Cartão', 'Dois Cartões'),
    limitAvailable float,
    primary key (idClient, idpayment)
);

-- Cria tabela estoque
create table productStorage(
	idProdStrorage int auto_increment primary key,
    storageLocation varchar (255),
    quantity int default 0
);
alter table productStorage auto_increment=1;

-- Cria tabela Fornecedor
create table supplier(
	idSupplier int auto_increment primary key,
    SocialName varchar (255) not null,
    CNPJ char(15) not null,
    contact varchar(11) not null,
    constraint unique_supplier unique (CNPJ)
);
alter table supplier auto_increment=1;

-- Cria tabela Vendedor
create table seller(
	idSeller int auto_increment primary key,
    SocialName varchar (255) not null,
    abstName varchar(255),
    CNPJ char(15),
    CPF char(9),
    location varchar(255),
    contact varchar(11) not null,
    constraint unique_seller unique (CNPJ),
    constraint unique_seller unique (CPF)
);
alter table seller auto_increment=1;

create table productSeller(
	idPSeller int,
    idProduct int,
	prodQuantity int default 1,
    primary key (idPSeller, idProduct),
    constraint fk_product_seller foreign key (idPSeller) references seller(idSeller),
    constraint fk_product_product foreign key (idProduct) references product(idProduct)
);

create table productOrder(
	idPOproduct int,
    idPOorder int,
    poQuantity int default 1,
    poStatus enum('Disponivel', 'Sem estoque') default 'Disponivel',
    primary key(idPOproduct, idPOorder),
    constraint fk_orderProduct foreign key (idPOproduct) references product(idProduct),
    constraint fk_orderId foreign key (idPOorder) references orders(idOrder)
);

create table storageLocation(
	idLproduct int,
    idLstorage int,
    location varchar(255) not null,
    primary key(idLproduct, idLstorage),
    constraint fk_idProductLoc foreign key (idLproduct) references product(idProduct),
    constraint fk_orderId foreign key (idLstorage) references productStorage(idProdStrorage)
);

insert into clients (Fname, Minit, Lname, CPF, Address)
		values ('João', 'J', 'Silva', 123456789, 'Rua algum lugar 10, Centro - Lugar nenhum'),
			   ('Maria', 'M', 'Silva', 987654321, 'Rua algum lugar 25, Centro - Lugar nenhum'),
               ('Tiago', 'M', 'Tanaka', 147258369, 'Rua algum lugar 54, Centro - Lugar nenhum'),
               ('Pâmela', 'P', 'Castro', 369258147, 'Rua algum lugar 54, Centro - Lugar nenhum'),
               ('Ricardo', 'F', 'Cruz', 741852963, 'Rua algum lugar 105, Centro - Lugar nenhum'),
               ('Julia', 'S', 'França', 963852741, 'Rua algum lugar 156, Centro - Lugar nenhum');
select * from clients;
        
insert into product (Pname, classification_kids_, category, avaliacao, dimensao)
		values ('Mouse', false, 'Eletronico', '4', null),
			   ('Microfone', false, 'Eletronico', '5', null),
               ('Barbie', false, 'Brinquedos', '3', null),
               ('Cama', false, 'Moveis', '4', '12x138x188'),
               ('Achocolatado', false, 'Alimentos', '2', null),
               ('Calça Jeans', false, 'Vestimenta', '5', null),
               ('Camisa', false, 'Vestimenta', '4', null);
select * from product;
               
insert into orders (idOrderClient, orderStatus, orderDescription, sendValue, paymentCash)
		values (1, null, 'Compra via aplicativo', null, 1),
			   (2, null, 'Compra via aplicativo', null, 50.0),
               (3, 'Confirmado',null, null, 1),
               (4, null, 'Compra via web site', null, 150.0);
select * from orders;

insert into productOrder (idPOproduct, idPOorder, poQuantity, poStatus)
			values (1, 1, 2, null),
				   (2, 1, 1, null),
                   (3, 2, 1, null);
select * from clients;
                   
insert into productStorage (storageLocation, quantify)
			values ('Paraná',1000),
				   ('São Paulo',500),
                   ('Rio de Janeiro',100),
                   ('Minas Gerais',300),
                   ('Paraná',10),
                   ('Paraná',50);
select * from productStorage;
                   
insert into storageLocation (idLproduct, idLstorage, location)
			values (1,2, 'SP'),
				   (2, 1, 'PR');
select * from storageLocation;
                   
insert into supplier (SocialName, CNPJ, contact)
			values ('Eletronicos Tanaka', 123456789123456, '74185296'),
				   ('Eletronicos Castro', 987654321987654, '14725836'),
                   ('Almeida e filhos', 147258369147258, '12365478');
select * from supplier;
                   
insert into productSupplier (idPsSupplier, idPsProduct, quantity)
			values (1,1,500),
				   (1,2,400),
                   (2,4,633),
                   (3,3,5),
                   (2,5,10);
select * from productSupplier;
            
insert into seller (SocialName, AbstName, CNPJ, CPF, location, contact)
			values ('Tech eltronics', null, 123456789456321, null, 'Rio de Janeiro', 21346578),
				   ('Botique Durgas', null, null, 123456789, 'Rio de Janeiro', 98746532),
                   ('Kids World', null, 123456789456321, null, 'São Paulo', 15975326);
select * from seller;
            
insert into productSeller (idPseller, idPproduct, ProdQuantity)
			values (1,6,80),
				   (2,7,10);
select * from productSeller;