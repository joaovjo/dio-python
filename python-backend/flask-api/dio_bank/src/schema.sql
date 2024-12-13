DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post; -- Remove a tabela 'post' se ela existir

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- Cria uma coluna 'id' como chave primária com incremento automático
  username TEXT UNIQUE NOT NULL, -- Cria uma coluna 'username' que deve ser única e não pode ser nula
  password TEXT NOT NULL -- Cria uma coluna 'password' que não pode ser nula
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- Cria uma coluna 'id' como chave primária com incremento automático
  author_id INTEGER NOT NULL, -- Cria uma coluna 'author_id' que não pode ser nula
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Cria uma coluna 'created' com timestamp padrão como o horário atual
  title TEXT NOT NULL, -- Cria uma coluna 'title' que não pode ser nula
  body TEXT NOT NULL, -- Cria uma coluna 'body' que não pode ser nula
  FOREIGN KEY (author_id) REFERENCES user (id) -- Define 'author_id' como chave estrangeira referenciando 'id' na tabela 'user'
);