drop database if exists chart;
create database chart default character set utf8 collate utf8_spanish_ci;
use chart;

-- Table

drop table if exists records;
create table if not exists records
(
	id int primary key auto_increment not null ,
    value int not null,
    time datetime not null default now()
)engine = innodb character set utf8 collate utf8_spanish_ci;


insert into records (value) values (80);
insert into records (value) values (95);
insert into records (value) values (103);
insert into records (value) values (79);