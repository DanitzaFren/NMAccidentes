create or replace NONEDITIONABLE TRIGGER ACCIDENTE_on_insert
  BEFORE INSERT ON ACCIDENTE
  FOR EACH ROW
BEGIN
  SELECT ACCIDENTE_seCuence.nextval
  INTO :new.id_ACCIDENTE
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER accidenteest_on_insert
  BEFORE INSERT ON accidente
  FOR EACH ROW
BEGIN

  SELECT 1
  INTO :new.id_estado
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER accidentefecha_on_insert
  BEFORE INSERT ON accidente
  FOR EACH ROW
BEGIN

  SELECT sysdate
  INTO :new.fecha
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER administrador_on_insert
  BEFORE INSERT ON administrador
  FOR EACH ROW
BEGIN
  SELECT administrador_sequence.nextval
  INTO :new.id_admin
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER asesoria_on_insert
  BEFORE INSERT ON asesoria
  FOR EACH ROW
BEGIN
  SELECT asesoria_sequence.nextval
  INTO :new.id_asesoria
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER asesoriaes_on_insert
  BEFORE INSERT ON asesoria
  FOR EACH ROW
BEGIN

  SELECT 1
  INTO :new.id_estado
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER capacitacion_on_insert
  BEFORE INSERT ON capacitacion
  FOR EACH ROW
BEGIN
  SELECT capacitacion_sequence.nextval
  INTO :new.nro_capacitacion
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER capacitaciones_on_insert
  BEFORE INSERT ON capacitacion
  FOR EACH ROW
BEGIN

  SELECT 1
  INTO :new.id_estado
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER checklist_on_insert
  BEFORE INSERT ON checklist
  FOR EACH ROW
BEGIN
  SELECT checklist_sequence.nextval
  INTO :new.nro_checklist
  FROM dual;
END;
------

create or replace NONEDITIONABLE TRIGGER checklistEst_on_insert
  BEFORE INSERT ON checklist
  FOR EACH ROW
BEGIN

  SELECT 1
  INTO :new.id_estado
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER condicion_on_insert
  BEFORE INSERT ON condicion
  FOR EACH ROW
BEGIN
  SELECT condicion_sequence.nextval
  INTO :new.id_condicion
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER contrato_servicio_on_insert
  BEFORE INSERT ON contrato_servicio
  FOR EACH ROW
BEGIN
  SELECT contrato_servicio_sequence.nextval
  INTO :new.id_servicio
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER det_checklist_on_insert
  BEFORE INSERT ON det_checklist
  FOR EACH ROW
BEGIN
  SELECT det_checklist_sequence.nextval
  INTO :new.id_detchecklist   
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER ESTADO_ACTIVIDAD_on_insert
  BEFORE INSERT ON ESTADO_ACTIVIDAD
  FOR EACH ROW
BEGIN
  SELECT ESTADO_ACTIVIDAD_SECUENCE.nextval
  INTO :new.id_ESTADO
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER ESTADO_CONTRATO_on_insert
  BEFORE INSERT ON ESTADO_CONTRATO
  FOR EACH ROW
BEGIN
  SELECT ESTADO_CONTRATO_SECUENCE.nextval
  INTO :new.ID_ESTADO_CONTRAT
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER estadopro_on_insert
  BEFORE INSERT ON profesional
  FOR EACH ROW
BEGIN

  SELECT 1
  INTO :new.estado
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER pago_on_insert
  BEFORE INSERT ON pago
  FOR EACH ROW
BEGIN
  SELECT pago_sequence.nextval
  INTO :new.id_pago
  FROM dual;
END;
--
create or replace NONEDITIONABLE TRIGGER RUBRO_on_insert
  BEFORE INSERT ON RUBRO
  FOR EACH ROW
BEGIN
  SELECT RUBRO_SECUENCE.nextval
  INTO :new.id_RUBRO
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER solicitud_asesoria_on_insert
  BEFORE INSERT ON solicitud_asesoria
  FOR EACH ROW
BEGIN
  SELECT solicitud_asesoria_sequence.nextval
  INTO :new.id_solicitud
  FROM dual;
END;
--

create or replace NONEDITIONABLE TRIGGER TIPO_SOLICITUD_on_insert
  BEFORE INSERT ON TIPO_SOLICITUD
  FOR EACH ROW
BEGIN
  SELECT TIPOSOLICITUD_SECUENCE.nextval
  INTO :new.id_TIPOSOLICITUD
  FROM dual;
END;


create or replace NONEDITIONABLE TRIGGER visita_on_insert
  BEFORE INSERT ON visita
  FOR EACH ROW
BEGIN
  SELECT visita_sequence.nextval
  INTO :new.id_visita
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER visitaes_on_insert
  BEFORE INSERT ON visita
  FOR EACH ROW
BEGIN

  SELECT 1
  INTO :new.id_estado
  FROM dual;
END;

---- TRIGGER DE USUARIOS

create or replace TRIGGER Ingresar_usuario_Admin
	AFTER INSERT ON AUTH_USER_GROUPS
BEGIN
UPDATE ADMINISTRADOR
	SET ID_USER = (SELECT a.ID
                   FROM AUTH_USER a 
                   INNER JOIN AUTH_USER_GROUPS b 
                   ON 
                   a.ID = b.USER_ID 
                   INNER JOIN 
                   AUTH_GROUP c 
                   ON 
                   b.GROUP_ID = c.ID WHERE c.NAME = 'Administrador' and a.ID = (SELECT MAX(a.ID)
                   FROM AUTH_USER a 
                   INNER JOIN AUTH_USER_GROUPS b 
                   ON 
                   a.ID = b.USER_ID 
                   INNER JOIN 
                   AUTH_GROUP c 
                   ON 
                   b.GROUP_ID = c.ID WHERE c.NAME = 'Administrador'))
        WHERE ID = (SELECT ID FROM ADMINISTRADOR WHERE ID = (SELECT MAX(ID) FROM ADMINISTRADOR));
END;



create or replace TRIGGER Ingresar_usuario_Cliente
	AFTER INSERT ON AUTH_USER_GROUPS
BEGIN
UPDATE CLIENTE
	SET ID_USER = (SELECT a.ID
                   FROM AUTH_USER a 
                   INNER JOIN AUTH_USER_GROUPS b 
                   ON 
                   a.ID = b.USER_ID 
                   INNER JOIN 
                   AUTH_GROUP c 
                   ON 
                   b.GROUP_ID = c.ID WHERE c.NAME = 'Cliente' and a.ID = (SELECT MAX(a.ID)
                   FROM AUTH_USER a 
                   INNER JOIN AUTH_USER_GROUPS b 
                   ON 
                   a.ID = b.USER_ID 
                   INNER JOIN 
                   AUTH_GROUP c 
                   ON 
                   b.GROUP_ID = c.ID WHERE c.NAME = 'Cliente'))
        WHERE ID = (SELECT ID FROM CLIENTE WHERE ID = (SELECT MAX(ID) FROM CLIENTE));
END;


create or replace TRIGGER Ingresar_usuario_Profesional
	AFTER INSERT ON AUTH_USER_GROUPS
BEGIN
UPDATE PROFESIONAL
	SET ID_USER = (SELECT a.ID
                   FROM AUTH_USER a 
                   INNER JOIN AUTH_USER_GROUPS b 
                   ON 
                   a.ID = b.USER_ID 
                   INNER JOIN 
                   AUTH_GROUP c 
                   ON 
                   b.GROUP_ID = c.ID WHERE c.NAME = 'Profesional' and a.ID = (SELECT MAX(a.ID)
                   FROM AUTH_USER a 
                   INNER JOIN AUTH_USER_GROUPS b 
                   ON 
                   a.ID = b.USER_ID 
                   INNER JOIN 
                   AUTH_GROUP c 
                   ON 
                   b.GROUP_ID = c.ID WHERE c.NAME = 'Profesional'))
        WHERE ID_D = (SELECT ID_D FROM PROFESIONAL WHERE ID_D = (SELECT MAX(ID_D) FROM PROFESIONAL));
END;


CREATE OR REPLACE TRIGGER administrador_on_insert_ID
  BEFORE INSERT ON administrador
  FOR EACH ROW
BEGIN
  SELECT administrador_ID_sequence.nextval
  INTO :new.id
  FROM dual;
END;


CREATE OR REPLACE TRIGGER CLIENTE_on_insert_ID
  BEFORE INSERT ON CLIENTE
  FOR EACH ROW
BEGIN
  SELECT CLIENTE_ID_sequence.nextval
  INTO :new.id
  FROM dual;
END;

CREATE OR REPLACE TRIGGER PROFESIONAL_on_insert_ID
  BEFORE INSERT ON PROFESIONAL
  FOR EACH ROW
BEGIN
  SELECT PROFESIONAL_ID_sequence.nextval
  INTO :new.id_d
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER estadosol_on_insert
  BEFORE INSERT ON solicitud_asesoria
  FOR EACH ROW
BEGIN

  SELECT 1
  INTO :new.id_estado
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER pago_paago
  BEFORE INSERT ON pago
  FOR EACH ROW
BEGIN

  SELECT 0
  INTO :new.pago
  FROM dual;
END;

create or replace NONEDITIONABLE TRIGGER solicitudfecha_on_insert
  BEFORE INSERT ON SOLICITUD_ASESORIA
  FOR EACH ROW
BEGIN

  SELECT sysdate
  INTO :new.fecha
  FROM dual;
END;

create or replace trigger registrar_pago
 after insert
 on cliente
 for each row
 begin
  insert into pago (pago,fecha_pago,fecha_vencimiento,id_cliente,total_pagar) values(0,null,(select add_months(sysdate,1) from dual) ,:new.id_cliente,100000);
 end;
