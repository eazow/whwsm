/**
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);

*/

drop table if exists locations;
create table locations (
  id integer primary key autoincrement,
  imei text not null,
  lng text not null,
  lat text not null,
  name text not null
);