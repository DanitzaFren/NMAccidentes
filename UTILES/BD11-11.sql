DROP TABLE ADMINISTRADOR CASCADE CONSTRAINTS;
DROP TABLE ASESORIA CASCADE CONSTRAINTS;
DROP TABLE CAPACITACION CASCADE CONSTRAINTS;
DROP TABLE CHECKLIST CASCADE CONSTRAINTS;
DROP TABLE CLIENTE CASCADE CONSTRAINTS;
DROP TABLE CONDICION CASCADE CONSTRAINTS;
DROP TABLE CONTRATO_SERVICIO CASCADE CONSTRAINTS;
DROP TABLE DET_CHECKLIST CASCADE CONSTRAINTS;
DROP TABLE PAGO CASCADE CONSTRAINTS;
DROP TABLE PROFESIONAL CASCADE CONSTRAINTS;
DROP TABLE SOLICITUD_ASESORIA CASCADE CONSTRAINTS;
DROP TABLE VISITA CASCADE CONSTRAINTS;
DROP TABLE RUBRO CASCADE CONSTRAINTS;
DROP TABLE ESTADO_ACTIVIDAD CASCADE CONSTRAINTS;
DROP TABLE ESTADO_CONTRATO CASCADE CONSTRAINTS;
DROP TABLE ACCIDENTE CASCADE CONSTRAINTS;
DROP TABLE TIPO_SOLICITUD CASCADE CONSTRAINTS;

CREATE TABLE tipo_solicitud(
    id_tiposolicitud NUMBER(2) NOT NULL,
    nom_solicitud VARCHAR2(50) NOT NULL
);
COMMENT ON COLUMN tipo_solicitud.id_tiposolicitud IS
    '999999999';

ALTER TABLE tipo_solicitud ADD CONSTRAINT tipo_solicitud_pk PRIMARY KEY ( id_tiposolicitud );
CREATE TABLE rubro(
    id_rubro NUMBER(2) NOT NULL,
    nom_rubro VARCHAR2(500) NOT NULL
);

COMMENT ON COLUMN rubro.id_rubro IS
    '999999999';

ALTER TABLE rubro ADD CONSTRAINT rubro_pk PRIMARY KEY ( id_rubro );

CREATE TABLE estado_actividad (
    id_estado    NUMBER(2) NOT NULL,
    nom_est_actividad      VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN estado_actividad.id_estado IS
    '999999999';

ALTER TABLE estado_actividad ADD CONSTRAINT estado_actividad_pk PRIMARY KEY ( id_estado );

CREATE TABLE estado_contrato (
    id_estado_contrat    NUMBER(2) NOT NULL,
    nom_estado_contrato      VARCHAR2(50) NOT NULL
);

COMMENT ON COLUMN estado_contrato.id_estado_contrat IS
    '999999999';

ALTER TABLE estado_contrato ADD CONSTRAINT estado_contrato_pk PRIMARY KEY ( id_estado_contrat );

CREATE TABLE administrador (
    id_admin    NUMBER(8) NOT NULL,
    nombre      VARCHAR2(50) NOT NULL,
    paterno     VARCHAR2(50) NOT NULL,
    materno     VARCHAR2(50),
    ID          NUMBER(8), 
    ID_USER     NUMBER(8),
    RUT_ADMIN   VARCHAR2(50) NOT NULL UNIQUE
);

COMMENT ON COLUMN administrador.id_admin IS
    '999999999';

ALTER TABLE administrador ADD CONSTRAINT administrador_pk PRIMARY KEY ( id_admin );

CREATE TABLE asesoria (
    id_asesoria           NUMBER(3) NOT NULL,
    fecha                 DATE NOT NULL,
    id_solicitud          NUMBER(4) NOT NULL UNIQUE,
    id_estado             NUMBER(1) NOT NULL 
);

ALTER TABLE asesoria ADD CONSTRAINT asesoria_pk PRIMARY KEY ( id_asesoria );

CREATE TABLE capacitacion (
    nro_capacitacion  NUMBER(4) NOT NULL,
    fecha             DATE NOT NULL,
    asistentes        NUMBER(8) NOT NULL,
    id_solicitud      NUMBER NOT NULL UNIQUE,
    descripcion_capa  VARCHAR2(500) NOT NULL,
    id_estado         NUMBER(1) NOT NULL 
);

ALTER TABLE capacitacion ADD CONSTRAINT capacitacion_pk PRIMARY KEY ( nro_capacitacion );

CREATE TABLE checklist (
    nro_checklist      NUMBER(4) NOT NULL,
    descripcion_check  VARCHAR2(500) NOT NULL,
    id_cliente         VARCHAR2(50) NOT NULL,
    id_estado          NUMBER(1) NOT NULL
);

ALTER TABLE checklist ADD CONSTRAINT checklist_pk PRIMARY KEY ( nro_checklist );

CREATE TABLE cliente (
    id_cliente  VARCHAR2(50) NOT NULL,
    direccion   VARCHAR2(50) NOT NULL,
    nombre      VARCHAR2(50) NOT NULL,
    rubro       NUMBER NOT NULL,
    id          NUMBER (8),
    ID_USER     NUMBER (8)
);

COMMENT ON COLUMN cliente.id_cliente IS
    '99999999';

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente );

CREATE TABLE accidente (
    id_accidente NUMBER(8) NOT NULL,
    id_cliente VARCHAR2(50) NOT NULL,
    descripcion VARCHAR2(50) NOT NULL,
    fecha DATE,
    id_estado NUMBER(1) DEFAULT 0
);
COMMENT ON COLUMN accidente.id_accidente IS
    '99999999';

ALTER TABLE accidente ADD CONSTRAINT accidente_pk PRIMARY KEY ( id_accidente);


CREATE TABLE condicion (
    id_condicion   NUMBER(4) NOT NULL,
    nom_condicion  VARCHAR2(500) NOT NULL
);

ALTER TABLE condicion ADD CONSTRAINT condicion_pk PRIMARY KEY ( id_condicion );

CREATE TABLE contrato_servicio (
    id_servicio    NUMBER(4) NOT NULL,
    fecha_inicio   DATE NOT NULL,
    fecha_termino  DATE NOT NULL,
    id_estado_con  NUMBER(1) DEFAULT 1 ,
    id_cliente     VARCHAR2(50) NOT NULL UNIQUE,
    id_profesional VARCHAR2(50) NOT NULL
);

ALTER TABLE contrato_servicio ADD CONSTRAINT contrato_servicio_pk PRIMARY KEY ( id_servicio );

CREATE TABLE det_checklist (
    id_detchecklist            NUMBER(4) NOT NULL,
    estado                   CHAR(1) DEFAULT 0,
    checklist_nro_checklist  NUMBER(4) NOT NULL,
    condicion_id_condicion   NUMBER(4) NOT NULL,
    act_mejora         VARCHAR2(500) NULL
);

ALTER TABLE det_checklist ADD CONSTRAINT det_checklist_pk PRIMARY KEY ( id_detchecklist );

CREATE TABLE pago (
    id_pago            NUMBER(4) NOT NULL,
    pago               NUMBER(6) ,
    fecha_pago         DATE,
    fecha_vencimiento  DATE NOT NULL,
    id_servicio        NUMBER(4) NOT NULL,
    total_pagar        NUMBER(6)
);

COMMENT ON COLUMN pago.pago IS
    '999999';

ALTER TABLE pago ADD CONSTRAINT pago_pk PRIMARY KEY ( id_pago );

CREATE TABLE profesional (
    rut_profesional  VARCHAR2(50) NOT NULL,
    nombre           VARCHAR2(50) NOT NULL,
    paterno          VARCHAR2(50) NOT NULL,
    materno          VARCHAR2(50),
    estado           NUMBER(1) DEFAULT 1 ,
    id_d             NUMBER(8),
    ID_USER          NUMBER(8)

);

ALTER TABLE profesional ADD CONSTRAINT profesional_pk PRIMARY KEY ( rut_profesional );

CREATE TABLE solicitud_asesoria (
    id_solicitud          NUMBER(4) NOT NULL,
    solicitud             VARCHAR2(50) NOT NULL,
    id_cliente            VARCHAR2(50) NOT NULL,
    id_profesional            VARCHAR2(50) NOT NULL,
    tipo_solicitud         NUMBER NOT NULL,
    descripcion_asesoria  VARCHAR2(500) NOT NULL
);

ALTER TABLE solicitud_asesoria ADD CONSTRAINT solicitud_asesoria_pk PRIMARY KEY ( id_solicitud );

CREATE TABLE visita (
    id_visita        NUMBER(4) NOT NULL,
    fecha            DATE NOT NULL,
    id_solicitud     NUMBER NOT NULL UNIQUE,
    descripcion      VARCHAR2(500) ,
    id_estado        NUMBER(1) NOT NULL ,
    nro_checklist    NUMBER NOT NULL
);

ALTER TABLE visita ADD CONSTRAINT visita_pk PRIMARY KEY ( id_visita );

ALTER TABLE visita
    ADD CONSTRAINT visita_solicitud_asesoria_fk FOREIGN KEY ( id_solicitud )
        REFERENCES solicitud_asesoria ( id_solicitud );

ALTER TABLE asesoria
    ADD CONSTRAINT asesoria_solicitud_asesoria_fk FOREIGN KEY ( id_solicitud )
        REFERENCES solicitud_asesoria ( id_solicitud );


ALTER TABLE cliente
    ADD CONSTRAINT cliente_administrador_fk FOREIGN KEY ( id_admin )
        REFERENCES administrador ( id_admin );

ALTER TABLE contrato_servicio
    ADD CONSTRAINT contrato_servicio_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE det_checklist
    ADD CONSTRAINT det_checklist_checklist_fk FOREIGN KEY ( checklist_nro_checklist )
        REFERENCES checklist ( nro_checklist );

ALTER TABLE det_checklist
    ADD CONSTRAINT det_checklist_condicion_fk FOREIGN KEY ( condicion_id_condicion )
        REFERENCES condicion ( id_condicion );

ALTER TABLE pago
    ADD CONSTRAINT pago_contrato_servicio_fk FOREIGN KEY ( id_servicio )
        REFERENCES contrato_servicio ( id_servicio );

ALTER TABLE profesional
    ADD CONSTRAINT profesional_administrador_fk FOREIGN KEY ( id_admin )
        REFERENCES administrador ( id_admin );

ALTER TABLE solicitud_asesoria
    ADD CONSTRAINT solicitud_asesoria_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE solicitud_asesoria
    ADD CONSTRAINT solicitud_asesoria_pro_fk FOREIGN KEY ( id_profesional )
        REFERENCES profesional ( rut_profesional );

ALTER TABLE visita
    ADD CONSTRAINT visita_checklist_fk FOREIGN KEY ( nro_checklist )
        REFERENCES checklist ( nro_checklist );

ALTER TABLE accidente
    ADD CONSTRAINT accidente_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_actividad ( id_estado );

ALTER TABLE accidente
    ADD CONSTRAINT accidente_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE asesoria
    ADD CONSTRAINT asesoria_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_actividad ( id_estado );

ALTER TABLE capacitacion
    ADD CONSTRAINT capacitacion_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_actividad ( id_estado );

ALTER TABLE visita
    ADD CONSTRAINT visita_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_actividad ( id_estado );

ALTER TABLE contrato_servicio
    ADD CONSTRAINT contrato_servicio_es_fk FOREIGN KEY ( id_estado_con )
        REFERENCES estado_contrato ( id_estado_contrat );
ALTER TABLE profesional
    ADD CONSTRAINT profesional_es_fk FOREIGN KEY ( estado )
        REFERENCES estado_contrato ( id_estado_contrat );

ALTER TABLE solicitud_asesoria
    ADD CONSTRAINT solicitud_asesoria_tipo_fk FOREIGN KEY ( tipo_solicitud )
        REFERENCES tipo_solicitud ( id_tiposolicitud );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_rubro_fk FOREIGN KEY ( rubro )
        REFERENCES rubro ( id_rubro );

        
ALTER TABLE contrato_servicio
    ADD CONSTRAINT contrato_servicio_pro_fk FOREIGN KEY ( id_profesional )
        REFERENCES profesional ( rut_profesional );
    
        
ALTER TABLE capacitacion
    ADD CONSTRAINT capacitacion_solicitud_fk FOREIGN KEY ( id_solicitud )
        REFERENCES solicitud_asesoria ( id_solicitud );
        
ALTER TABLE checklist
    ADD CONSTRAINT checklist_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_actividad ( id_estado );        
        
ALTER TABLE checklist
    ADD CONSTRAINT checklist_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );