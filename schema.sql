drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);


create table location (
  id integer primary key autoincrement,
  imei text not null,
  lng text not null,
  lat text not null
)