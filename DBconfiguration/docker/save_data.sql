-- Insertar datos en la tabla usuarios
INSERT INTO usuarios (nombre, correo, telefono, fecha_nacimiento)VALUES
('Juan Pérez', 'juan.perez1@example.com', '1234567890', '1985-01-15'),
('Ana Gómez', 'ana.gomez2@example.com', '1234567891', '1990-03-22'),
('Luis Martínez', 'luis.martinez3@example.com', '1234567892', '1988-07-10'),
('María López', 'maria.lopez4@example.com', '1234567893', '1992-11-05'),
('Carlos Ruiz', 'carlos.ruiz5@example.com', '1234567894', '1980-06-25'),
-- Insertar datos en la tabla credenciales
INSERT INTO credenciales (id_usuario, username, password_hash)VALUES
(1, 'juan.perez1', 'hash_juan_perez'),
(2, 'ana.gomez2', 'hash_ana_gomez'),
