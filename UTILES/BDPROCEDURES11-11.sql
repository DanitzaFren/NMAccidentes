create or replace NONEDITIONABLE procedure agregar_asesoria(
	v_1 in date,
    v_2 in number,
    v_salida out number)
is
begin
	insert into asesoria(fecha,id_solicitud)
	values(v_1,v_2);
    update solicitud_asesoria set id_estado=2 where id_solicitud=v_2;
	commit;
    v_salida:=1; 

    exception

    when others then 
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure agregar_capacitacion(
	v_1 in date,
    v_2 in number,
      v_4 in number,
           v_3 in VARCHAR2,
    v_salida out number)
is
begin
	insert into capacitacion(fecha,asistentes,id_solicitud,descripcion_capa)
	values(v_1,v_2,v_4,v_3);
    update solicitud_asesoria set id_estado=2 where id_solicitud=v_4;
	commit;
    v_salida:=1; 

    exception

    when others then
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure agregar_cliente(
	v_2 in VARCHAR2,
    v_3 in VARCHAR2,
    v_4 in varchar2,
    v_5 in number,
    v_salida out number)
is
begin
	insert into cliente(id_cliente,direccion,nombre,rubro)
	values(v_2, v_3,v_4,v_5);
	commit;
    v_salida:=1; 

    exception

    when others then 
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure agregar_condicion(
    v_3 in VARCHAR2,
    v_salida out number)
is
begin
	insert into condicion(nom_condicion)
	values(v_3);
	commit;
    v_salida:=1; 

    exception

    when others then
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure agregar_contrato(
    v_1 in contrato_servicio.fecha_inicio%type,
    v_2 in contrato_servicio.fecha_termino%type,
    v_4 in VARCHAR2,
    v_5 in VARCHAR2,
    v_salida out number)
is
begin
	insert into contrato_servicio(fecha_inicio, fecha_termino, id_cliente, id_profesional)
	values(v_1,v_2,v_4,v_5);
	commit;
    v_salida:=1; 

    exception

    when others then
        v_salida:=0;
end; 

create or replace NONEDITIONABLE procedure agregar_solicitud(
    v_2 in VARCHAR2,
    v_4 in VARCHAR2,
    v_5 in number,
    v_3 in VARCHAR2,
    v_salida out number)
is
begin
	insert into solicitud_asesoria( id_cliente, id_profesional,tipo_solicitud,descripcion_asesoria)
	values(v_2,v_4,v_5,v_3);
	commit;
    v_salida:=1; 

    exception 

    when others then
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure agregar_visita(
	v_1 in date,
    v_2 in number,
     v_3 in VARCHAR2,
      v_4 in number,
    v_salida out number)
is
begin
	insert into visita(fecha,id_solicitud,descripcion,nro_checklist)
	values(v_1,v_2,v_3,v_4);
    update solicitud_asesoria set id_estado=2 where id_solicitud=v_2;
	commit;
    v_salida:=1; 

    exception
 
    when others then
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure checklisto(v_1 in number, v_salida out number) 
IS
BEGIN
    update checklist set id_estado = 2
    where nro_checklist = v_1 ;
    v_salida:=1;
    exception
    when others then
        v_salida:= 0;
END;

create or replace NONEDITIONABLE procedure clientes(
clientes out 
sys_refcursor) 
IS
BEGIN
open clientes for SELECT 
* FROM cliente;

END;

create or replace NONEDITIONABLE procedure crear_checklist(
	v_1 in varchar2, v_2 in number,
    v_salida out number)
is
begin
	insert into checklist(descripcion_check,id_cliente)
	values(v_1, v_2);
	commit;
    v_salida:=1; 

    exception

    when others then
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure  eliminar_detalle(v_3 in number, v_salida out number) 
IS
BEGIN
    DELETE
    FROM
        DET_CHECKLIST
    WHERE
        DET_checklist.CHECKLIST_NRO_CHECKLIST = v_3 ;
    v_salida:=1;

    exception

    when others then
        v_salida:= 0;
END;

create or replace NONEDITIONABLE procedure listado_checklistCliente(v_id in number,
checklist out 
sys_refcursor) 
IS
BEGIN
open checklist for SELECT nro_checklist, cliente.nombre,checklist.id_estado FROM checklist, cliente 
where checklist.id_cliente = cliente.id_cliente and cliente.id_user= v_id ;

END;

create or replace NONEDITIONABLE procedure listado_clienteprofesional( v_1 in number,
cliente out 
sys_refcursor) 
IS 
BEGIN
open cliente for 
SELECT cliente.id_cliente,cliente.nombre FROM cliente, profesional,contrato_servicio where contrato_servicio.id_cliente=cliente.id_cliente
and contrato_servicio.id_profesional=profesional.rut_profesional and profesional.id_user=v_1;

END;

create or replace NONEDITIONABLE procedure listado_detallescliente(
v_id in number,
det_checklist out
sys_refcursor) 
IS
BEGIN
open det_checklist for Select  det_checklist.id_detchecklist, condicion.nom_condicion, det_checklist.estado, det_checklist.act_mejora
        FROM det_checklist, condicion
        where condicion.id_condicion= det_checklist.condicion_id_condicion
        and det_checklist.checklist_nro_checklist=v_id;
        commit;
END;

create or replace NONEDITIONABLE procedure profesionales(
profesionales out 
sys_refcursor) 
IS
BEGIN
open profesionales for SELECT * FROM profesional;

END;

create or replace NONEDITIONABLE procedure rubros(
rubros out 
sys_refcursor) 
IS
BEGIN
open rubros for SELECT id_rubro, nom_rubro FROM rubro;

END;

create or replace NONEDITIONABLE procedure sp_accidentibilidad(
profesional out 
sys_refcursor) 
IS
BEGIN
open profesional for Select profesional.rut_profesional,profesional.nombre || ' '|| profesional.paterno , count(accidente.id_accidente)*100/
        (select DISTINCT count(id_cliente) from contrato_servicio )|| '%' as 
        FROM accidente, profesional, contrato_servicio, cliente
        WHERE contrato_servicio.id_cliente=cliente.id_cliente
        and contrato_servicio.id_profesional=profesional.rut_profesional
        and accidente.id_cliente=cliente.id_cliente
        group by profesional.rut_profesional, profesional.nombre || ' '||profesional.paterno, ' ', profesional.paterno, 
profesional.nombre || ' '|| profesional.paterno order by profesional.rut_profesional;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_act_cliente( v_1 in number,
actividades out 
sys_refcursor) 
IS
BEGIN
open actividades for SELECT asesoria.id_asesoria, asesoria.fecha, asesoria.id_estado, 'Asesoria' from asesoria, cliente,solicitud_asesoria 
                where asesoria.id_solicitud=solicitud_asesoria.id_solicitud and solicitud_asesoria.id_cliente=cliente.id_cliente
                and cliente.id_user=v_1
                UNION
                SELECT  capacitacion.nro_capacitacion, capacitacion.fecha,capacitacion.id_estado, 'Capacitación' from capacitacion, cliente, solicitud_asesoria
                where capacitacion.id_solicitud=solicitud_asesoria.id_solicitud and solicitud_asesoria.id_cliente=cliente.id_cliente
                and cliente.id_user=v_1
                UNION
                SELECT  visita.id_visita, visita.fecha,visita.id_estado, 'visita' from visita, cliente, solicitud_asesoria
                where visita.id_solicitud=solicitud_asesoria.id_solicitud and solicitud_asesoria.id_cliente=cliente.id_cliente
                and cliente.id_user=v_1;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_actualizarpago(v_1 in pago.pago%TYPE, v_2 in pago.fecha_pago%TYPE, v_3 in number, v_salida out number) 
IS
BEGIN
    update pago set pago = v_1, fecha_pago = v_2 
    where id_pago = v_3 ;
    v_salida:=1;

    exception

    when others then
        v_salida:= 0;
END;

create or replace NONEDITIONABLE procedure sp_agregar_detcheck(
	v_nrocheck in number,
    v_nrocond in number,
    v_salida out number)
is
begin
	insert into det_checklist(checklist_nro_checklist,condicion_id_condicion)
	values(v_nrocheck, v_nrocond);
	commit;
    v_salida:=1; 
    
    exception
    
    when others then
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure sp_atrasos( 
atrasos out 
sys_refcursor) 
IS
BEGIN
open atrasos for select pago.id_pago,contrato_servicio.id_cliente, cliente.nombre ,fecha_vencimiento,auth_user.email from pago, contrato_servicio,cliente,auth_user where pago.id_servicio=contrato_servicio.id_servicio
and cliente.id_cliente=contrato_servicio.id_cliente and cliente.id_user = auth_user.id and fecha_vencimiento < sysdate and pago <=0;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_completar_check(v_1 in det_checklist.act_mejora%TYPE, v_2 in det_checklist.estado%TYPE, v_3 in number, v_salida out number) 
IS
BEGIN
    update det_checklist set act_mejora = v_1, estado = v_2 
    where id_detchecklist = v_3 ;
    v_salida:=1;

    exception

    when others then
        v_salida:= 0;
END;

create or replace NONEDITIONABLE procedure sp_count_det(v_id in number,
v_1 out 
sys_refcursor) 
IS
BEGIN
open v_1 for SELECT count(id_detchecklist) FROM det_checklist where checklist_nro_checklist=v_id;

END;

create or replace NONEDITIONABLE procedure sp_lista_checklist(v_id in number,
checklist out 
sys_refcursor) 
IS
BEGIN
open checklist for SELECT nro_checklist FROM checklist where nro_checklist = v_id ;

END;


create or replace NONEDITIONABLE procedure sp_listar_accidente(
v_id in number, 
accidente out 
sys_refcursor) 
IS
BEGIN
open accidente for Select accidente.id_accidente, cliente.nombre, accidente.descripcion, accidente.fecha,accidente.id_estado
        FROM accidente, profesional, contrato_servicio, cliente
        WHERE contrato_servicio.id_cliente=cliente.id_cliente
        and contrato_servicio.id_profesional=profesional.rut_profesional
        and accidente.id_cliente=cliente.id_cliente
        and profesional.id_user=v_id
        order by id_accidente;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_listar_asesoria(v_1 in number,
asesoria out 
sys_refcursor) 
IS
BEGIN
open asesoria for SELECT asesoria.id_asesoria,asesoria.id_solicitud, solicitud_asesoria.descripcion_asesoria, cliente.nombre, asesoria.fecha, asesoria.id_estado
FROM asesoria,solicitud_asesoria,cliente ,profesional
where asesoria.id_solicitud=solicitud_asesoria.id_solicitud and solicitud_asesoria.tipo_solicitud = 1
and cliente.id_cliente=solicitud_asesoria.id_cliente and solicitud_asesoria.id_profesional=profesional.rut_profesional 
and profesional.id_user=v_1 ; 

END;

create or replace NONEDITIONABLE procedure sp_listar_check(v_1 in det_checklist.act_mejora%TYPE, v_2 in det_checklist.estado%TYPE, v_3 out number) 
IS
BEGIN
update det_checklist set act_mejora = v_1, estado = v_2
where checklist_nro_checklist = v_3;
END;

create or replace NONEDITIONABLE procedure sp_listar_checklist(
checklist out 
sys_refcursor) 
IS
BEGIN
open checklist for SELECT max(nro_checklist) FROM checklist ORDER BY nro_checklist DESC ;

END;

create or replace NONEDITIONABLE procedure sp_listar_condiciones(
condicion out 
sys_refcursor) 
IS
BEGIN
open condicion for Select * from condicion;

END;

create or replace NONEDITIONABLE procedure sp_listar_det(
v_id in number,
det_checklist out 
sys_refcursor) 
IS
BEGIN
open det_checklist for Select condicion.id_condicion, condicion.nom_condicion, det_checklist.id_detchecklist, det_checklist.estado, det_checklist.act_mejora, checklist.nro_checklist
        FROM det_checklist, checklist, condicion 
        where det_checklist.checklist_nro_checklist=checklist.nro_checklist
        and det_checklist.condicion_id_condicion=condicion.id_condicion
        and det_checklist.checklist_nro_checklist=v_id;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_listar_detalles(
v_id in number,
det_checklist out
sys_refcursor) 
IS
BEGIN
open det_checklist for Select  det_checklist.id_detchecklist, condicion.nom_condicion, det_checklist.estado, det_checklist.act_mejora, det_checklist.checklist_nro_checklist
        FROM det_checklist, condicion
        where condicion.id_condicion= det_checklist.condicion_id_condicion
        and det_checklist.checklist_nro_checklist=v_id;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_listarpago(v_id in number,
pago out 
sys_refcursor) 
IS
BEGIN
open pago for SELECT * FROM pago where id_pago = v_id ;

END;

create or replace NONEDITIONABLE procedure sp_listarpagos(
v_id in number, 
PAGO out 
sys_refcursor) 
IS
BEGIN
open PAGO for Select *
        FROM pago, contrato_servicio,cliente
        WHERE pago.id_servicio = contrato_servicio.id_servicio
        AND contrato_servicio.id_cliente = cliente.id_cliente
        AND cliente.id_cliente=v_id
        order by pago.id_pago;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_misclientes( v_1 in number,
cliente out 
sys_refcursor) 
IS
BEGIN
open cliente for select cliente.id_cliente, cliente.nombre, rubro.nom_rubro, cliente.direccion from cliente, contrato_servicio,profesional, rubro
where cliente.id_cliente=contrato_servicio.id_cliente and rubro.id_rubro=cliente.rubro
and profesional.rut_profesional=contrato_servicio.id_profesional and profesional.id_user=v_1;
        commit;
END;

create or replace NONEDITIONABLE procedure sp_report_accident(
	v_nrocliente in number, v_2 in varchar2, v_salida out number
    )
is
begin
	insert into accidente(id_cliente,descripcion)
	values(v_nrocliente, v_2);
	commit;
    v_salida:=1; 

    exception

    when others then
        v_salida:=0;
end;

create or replace NONEDITIONABLE procedure spactividadesadmin( 
actividades out 
sys_refcursor) 
IS
BEGIN
open actividades for SELECT asesoria.id_asesoria, asesoria.FECHA, 'Asesoria'  as tipo, cliente.nombre 
    FROM ASESORIA, solicitud_asesoria,cliente 
    where asesoria.id_solicitud=solicitud_asesoria.id_solicitud and solicitud_asesoria.id_cliente=cliente.id_cliente
UNION
SELECT capacitacion.NRO_CAPACITACION, capacitacion.FECHA, 'Capacitacion', cliente.nombre FROM CAPACITACION, cliente,solicitud_asesoria 
where capacitacion.id_solicitud=solicitud_asesoria.id_solicitud and solicitud_asesoria.id_cliente=cliente.id_cliente; 
        commit;
END;


create or replace NONEDITIONABLE procedure tipoasesoria(v_1 in number,
tiposolicitud out 
sys_refcursor) 
IS
BEGIN
open tiposolicitud for SELECT solicitud_asesoria.id_solicitud, cliente.nombre FROM tipo_solicitud,solicitud_asesoria,cliente,profesional
where tipo_solicitud.id_tiposolicitud=solicitud_asesoria.tipo_solicitud
and cliente.id_cliente=solicitud_asesoria.id_cliente  and solicitud_asesoria.id_estado=1 and solicitud_asesoria.tipo_solicitud=1
and solicitud_asesoria.id_profesional=profesional.rut_profesional and profesional.id_user=v_1 ;
END;

create or replace NONEDITIONABLE procedure tipocapacitacion(v_1 in number,
tiposolicitud out 
sys_refcursor) 
IS
BEGIN
open tiposolicitud for SELECT solicitud_asesoria.id_solicitud, cliente.nombre FROM tipo_solicitud,solicitud_asesoria,cliente, profesional
where tipo_solicitud.id_tiposolicitud=solicitud_asesoria.tipo_solicitud
and cliente.id_cliente=solicitud_asesoria.id_cliente  and solicitud_asesoria.id_estado=1 and solicitud_asesoria.tipo_solicitud=2
and solicitud_asesoria.id_profesional=profesional.rut_profesional and profesional.id_user=v_1 ;
END;

create or replace NONEDITIONABLE procedure tipomodificar(v_1 in number,
tiposolicitud out 
sys_refcursor) 
IS
BEGIN
open tiposolicitud for SELECT solicitud_asesoria.id_solicitud, cliente.nombre FROM tipo_solicitud,solicitud_asesoria,cliente 
where tipo_solicitud.id_tiposolicitud=solicitud_asesoria.tipo_solicitud
and cliente.id_cliente=solicitud_asesoria.id_cliente and solicitud_asesoria.id_estado=1 and solicitud_asesoria.tipo_solicitud=4
and solicitud_asesoria.id_profesional=v_1 ;
END;

create or replace NONEDITIONABLE procedure tiposolicitud(
tiposolicitud out 
sys_refcursor) 
IS
BEGIN
open tiposolicitud for SELECT * FROM tipo_solicitud;

END;

create or replace NONEDITIONABLE procedure tipovisita(v_1 in number,
tiposolicitud out 
sys_refcursor) 
IS
BEGIN
open tiposolicitud for SELECT solicitud_asesoria.id_solicitud, cliente.nombre,
checklist.nro_checklist
FROM tipo_solicitud,solicitud_asesoria,cliente, checklist, profesional
where tipo_solicitud.id_tiposolicitud=solicitud_asesoria.tipo_solicitud
and cliente.id_cliente=solicitud_asesoria.id_cliente  
and solicitud_asesoria.tipo_solicitud=3 
and solicitud_asesoria.id_estado=1
and checklist.id_cliente=cliente.id_cliente
and solicitud_asesoria.id_profesional=profesional.rut_profesional and profesional.id_user=v_1 ;
END;


create or replace NONEDITIONABLE procedure sp_listar_capacitacion(v_1 in number,
capacitacion out 
sys_refcursor) 
IS
BEGIN
open capacitacion for SELECT capacitacion.nro_capacitacion,capacitacion.fecha, capacitacion.asistentes, cliente.nombre, capacitacion.id_estado
FROM capacitacion,cliente,profesional,solicitud_asesoria where capacitacion.id_solicitud=solicitud_asesoria.id_solicitud
and cliente.id_cliente=solicitud_asesoria.id_cliente
and profesional.rut_profesional=solicitud_asesoria.id_profesional
and profesional.id_user=v_1;

END;


create or replace NONEDITIONABLE procedure sp_listar_visita(v_1 in number,
visita out 
sys_refcursor) 
IS
BEGIN
open visita for SELECT visita.id_visita,visita.fecha, visita.descripcion, visita.id_estado, cliente.nombre, profesional.rut_profesional
FROM visita,cliente,profesional,solicitud_asesoria where visita.id_solicitud=solicitud_asesoria.id_solicitud
and cliente.id_cliente=solicitud_asesoria.id_cliente
and profesional.rut_profesional=solicitud_asesoria.id_profesional
and profesional.id_user=v_1;
END;

create or replace NONEDITIONABLE procedure contratoprocli(
v_id in number, 
contrato_servicio out 
sys_refcursor) 
IS
BEGIN
open contrato_servicio for Select contrato_servicio.id_profesional, contrato_servicio.id_cliente
        FROM profesional, contrato_servicio, cliente
        WHERE contrato_servicio.id_cliente=cliente.id_cliente
        and contrato_servicio.id_profesional=profesional.rut_profesional
        and cliente.id_user=v_id;
        commit;
END;

create or replace NONEDITIONABLE procedure list_solicitudcliente(v_id in number,
solicitud_asesoria out 
sys_refcursor) 
IS
BEGIN
open solicitud_asesoria for SELECT solicitud_asesoria.id_solicitud, solicitud_asesoria.tipo_solicitud,solicitud_asesoria.descripcion_asesoria,solicitud_asesoria.id_estado
 FROM solicitud_asesoria, cliente 
where solicitud_asesoria.id_cliente = cliente.id_cliente and cliente.id_user= v_id ;

END;

----------ESTE ES PARA MOSTRAR LAS ACTIVIDADES DEL PROFESIONAL, FALTA MODIFICARlo en el codigo
create or replace NONEDITIONABLE procedure sp_act_profesional( v_1 in number,
actividades out 
sys_refcursor) 
IS
BEGIN
open actividades for SELECT asesoria.id_asesoria, asesoria.fecha, estado_actividad.nom_est_actividad, 'Asesoria',cliente.nombre
                from asesoria, profesional,solicitud_asesoria, estado_actividad,cliente
                where asesoria.id_solicitud=solicitud_asesoria.id_solicitud 
                and estado_actividad.id_estado=asesoria.id_estado
                and solicitud_asesoria.id_solicitud=asesoria.id_solicitud
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional
                and profesional.id_user=v_1
                UNION
             SELECT  capacitacion.nro_capacitacion, capacitacion.fecha, estado_actividad.nom_est_actividad,'Capacitación',cliente.nombre 
                from capacitacion, profesional, solicitud_asesoria, estado_actividad,cliente
                where capacitacion.id_solicitud=solicitud_asesoria.id_solicitud
                and estado_actividad.id_estado=capacitacion.id_estado
                and solicitud_asesoria.id_solicitud=capacitacion.id_solicitud
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional
                and profesional.id_user=v_1
                UNION
                SELECT  visita.id_visita, visita.fecha, estado_actividad.nom_est_actividad,'visita',cliente.nombre 
                from visita, profesional, solicitud_asesoria, estado_actividad,cliente
                where visita.id_solicitud=solicitud_asesoria.id_solicitud 
                and estado_actividad.id_estado=visita.id_estado
                and solicitud_asesoria.id_solicitud=visita.id_solicitud
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional
                and profesional.id_user=v_1
                UNION 
                SELECT  solicitud_asesoria.id_solicitud, solicitud_asesoria.fecha, estado_actividad.nom_est_actividad,'Solicitud' ||' '|| tipo_solicitud.nom_solicitud ,cliente.nombre 
                from  profesional, solicitud_asesoria, estado_actividad,cliente,tipo_solicitud
                where estado_actividad.id_estado=solicitud_asesoria.id_estado
                 and solicitud_asesoria.id_estado=1 
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional
                 and solicitud_asesoria.tipo_solicitud=tipo_solicitud.id_tiposolicitud
                and profesional.id_user=v_1;
        commit;
END;

----------ESTE ES PARA MOSTRAR LAS ACTIVIDADES DEL admin, FALTA MODIFICARlo en el codigo
create or replace NONEDITIONABLE procedure SPACTIVIDADESADMIN(
actividades out 
sys_refcursor) 
IS
BEGIN
open actividades for SELECT  solicitud_asesoria.id_solicitud,cliente.nombre,profesional.nombre ||' '|| profesional.paterno, solicitud_asesoria.fecha ,
                estado_actividad.nom_est_actividad, 'Solicitud' ||' '|| tipo_solicitud.nom_solicitud 
                from solicitud_asesoria,estado_actividad,tipo_solicitud, cliente,profesional
                where estado_actividad.id_estado=solicitud_asesoria.id_estado 
                and solicitud_asesoria.id_estado=1 
                and solicitud_asesoria.tipo_solicitud=tipo_solicitud.id_tiposolicitud
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional
                UNION
                SELECT  visita.id_visita, cliente.nombre,profesional.nombre ||' '|| profesional.paterno, visita.fecha,estado_actividad.nom_est_actividad, 'visita' 
                from visita,estado_actividad, cliente,profesional,solicitud_asesoria
                where estado_actividad.id_estado=visita.id_estado
                and solicitud_asesoria.id_solicitud=visita.id_solicitud
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional
                UNION

                SELECT  capacitacion.nro_capacitacion, cliente.nombre,profesional.nombre ||' '|| profesional.paterno,capacitacion.fecha,estado_actividad.nom_est_actividad, 'Capacitación' 
                from capacitacion,estado_actividad, cliente,profesional,solicitud_asesoria
                where estado_actividad.id_estado=capacitacion.id_estado 
                and solicitud_asesoria.id_solicitud=capacitacion.id_solicitud
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional
                
                UNION

                SELECT asesoria.id_asesoria, cliente.nombre,profesional.nombre ||' '|| profesional.paterno,asesoria.fecha, estado_actividad.nom_est_actividad, 'Asesoria' from asesoria,estado_actividad, cliente,profesional,solicitud_asesoria
                where estado_actividad.id_estado=asesoria.id_estado 
                and solicitud_asesoria.id_solicitud=asesoria.id_solicitud
                and cliente.id_cliente=solicitud_asesoria.id_cliente
                and profesional.rut_profesional=solicitud_asesoria.id_profesional

                UNION
                SELECT accidente.id_accidente, cliente.nombre,profesional.nombre ||' '|| profesional.paterno,accidente.fecha, estado_actividad.nom_est_actividad, 'Accidente' from accidente,estado_actividad, cliente,profesional,contrato_servicio
                where estado_actividad.id_estado=accidente.id_estado 
                and contrato_servicio.id_cliente=accidente.id_cliente
                and cliente.id_cliente=contrato_servicio.id_cliente
                and profesional.rut_profesional=contrato_servicio.id_profesional
                ;


        commit;
END;
