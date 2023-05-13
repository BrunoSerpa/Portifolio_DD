use Portifolio;
/* Index.html */
create table Ensino(
	key_ensi int auto_increment primary key,
    tit_ensi varchar(200) not null,
    des_ensi varchar(200) not null,
    ano_ensi char(11) not null,
    loc_ensi varchar(200) not null
);
/* Trabalhos.html */
create table Profissao(
	key_prof int auto_increment primary key,
    tit_prof varchar(200) not null,
    dat_prof char(23) not null,
    loc_prof varchar(200) not null
);
create table Voluntariado(
	key_volu int auto_increment primary key,
    tit_volu varchar(200) not null,
    dat_volu char(23) not null,
    loc_volu varchar(200) not null
);
create table Projeto(
	key_proj int auto_increment primary key,
    link_proj varchar(200) not null,
    tit_proj varchar(200) not null,
    dat_proj char(23) not null,
    tec_proj char(200) not null
);