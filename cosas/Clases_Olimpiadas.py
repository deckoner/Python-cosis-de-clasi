from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Integer, Column, String, ForeignKey, PrimaryKeyConstraint, create_engine

Base = declarative_base()

# CREAR LA CLASE DEPORTE******************************************************************
class Deporte(Base):
    __tablename__ = 'Deporte'
    id_deporte = Column(Integer, primary_key=True)
    nombre = Column(String)


# CREAR LA CLASE DEPORTISTA******************************************************************
class Deportista(Base):
    __tablename__ = 'Deportista'
    id_deportista = Column(Integer, primary_key=True)
    nombre = Column(String)
    sexo = Column(String)
    peso = Column(Integer)
    altura = Column(Integer)



# CREAR LA CLASE EQUIPO******************************************************************
class Equipo(Base):
    __tablename__ = 'Equipo'
    id_Equipo = Column(Integer, primary_key=True)
    nombre = Column(String)
    Iniciales = Column(String)


# CREAR LA CLASE OLIMPIADA******************************************************************
class Olimpiada(Base):
    __tablename__ = 'Olimpiada'
    id_olimpiada = Column(Integer, primary_key=True)
    nombre = Column(String)
    anio = Column(Integer)
    temporada = Column(String)
    ciudad = Column(String)


# CREAR LA CLASE EVENTO******************************************************************
class Evento(Base):
    __tablename__ = 'Evento'
    id_evento = Column(Integer, primary_key=True)
    nombre = Column(String)

    id_olimpiada = Column(Integer, ForeignKey(Olimpiada.id_olimpiada))
    olimpiada = relationship("Olimpiada", back_populates="eventos")

    id_deporte = Column(Integer, ForeignKey(Deporte.id_deporte))
    deporte = relationship("Deporte", back_populates="eventos")

# CREAR LA CLASE PARTICIPACION******************************************************************
class Participacion(Base):
    __tablename__ = 'Participacion'

    id_deportista = Column(Integer, ForeignKey(Deportista.id_deportista))
    deportista = relationship("Deportista", back_populates="participaciones")

    id_evento = Column(Integer, ForeignKey(Evento.id_evento))
    evento = relationship("Evento", back_populates="participaciones")

    __table_args__ = (
        PrimaryKeyConstraint('id_deportista', 'id_evento'),
        {},
    )
    id_equipo = Column(Integer, ForeignKey(Equipo.id_Equipo))
    equipo = relationship("Equipo", back_populates="participaciones")

    edad = Column(Integer)
    medalla = Column(String)


# RELACIONES**************************************************************************************

#----RELACIONES EVENTO
Olimpiada.eventos = relationship("Evento", back_populates="olimpiada")
Deporte.eventos = relationship("Evento", back_populates="deporte")

#----RELACIONES PARTICIPACION
Deportista.participaciones = relationship("Participacion", back_populates="deportista")
Evento.participaciones = relationship("Participacion", back_populates="evento")
Equipo.participaciones = relationship("Participacion", back_populates="equipo")

# # PRUEBAS MAPEO*****************************************************************************************
# lista = sesion.query(Participacion).all()
# for e in lista:
#     print(e.deportista.nombre)
# sesion.close()




# EJERCICIO*******************************************************************************************
class Ejercicio1:
    def menu(self):
        num = (int)(input("""Hola, ¿qué quieres hacer hoy?
        1-Listado de deportistas participantes
        2-Modificar medalla deportista
        3-Añadir deportista/participación
        4-Eliminar participación
        0-Salir del programa
    
        """))


        if num == 1:
            self.metodo1()
        elif num == 2:
            self.metodo2()
        elif num == 3:
            self.metodo3()
        elif num == 4:
            self.metodo4()
        else:
            print("Adio")

#--------------------EJERCICIO1--------------------
    def metodo1(self):
        # Elegir tipo de base de datos
        print("""Elige uno atraves del numero de la izquierda
        1.-MySQL
        2.-SQLite
        """)
        bbdd = 7
        while (bbdd != 2 and bbdd != 1):
            bbdd = (int)(input())
        engine=elegirBBDD(bbdd)
        Session = sessionmaker(bind=engine)
        sesion = Session()
        if(bbdd==2):
            sesion.execute("pragma foreign_keys=on")


        # Elegir temporada para listar
        temporada = ""
        while (temporada != "w" and temporada != "s"):
            temporada = input("""Elige temporada por la letra a su izquierda
            w.-Invierno
            s.-Verano""")

        if temporada == "w":
            temporada = "Winter"
        else:
            temporada = "Summer"

        #aplicar el primer filtro
        listaOlimpiadas = sesion.query(Olimpiada).filter(Olimpiada.temporada==temporada).all()
        cont=0
        for e in listaOlimpiadas:
            cont += 1
            print(cont,".-",e.nombre)
        opc=0
        while opc<1 or opc>cont:
            opc=(int)(input("Elige uno"))
        olimpiadaElegida=listaOlimpiadas.__getitem__(opc-1)
        # Sacar deportes y su eleccion
        listaDeportes=sacarDeportePorOlimpiada(olimpiadaElegida,sesion)
        cont=0
        print("Escribe el numero del dfepote que quieres")
        for e in listaDeportes:
            cont+=1
            print(cont,".-",e.nombre)
        opc=(int)(input())
        deporteSeleccionado=listaDeportes.__getitem__(opc-1)
        listaDeportesEventosPosibles=sacarEventoporDeporteyOlimpiada(deporteSeleccionado,olimpiadaElegida,sesion)
        cont=0
        print("elige un numero")
        for e in listaDeportesEventosPosibles:
            cont+=1
            print(cont,".-",e.nombre)
        opc=(int)(input())
        eventoElegido=listaDeportesEventosPosibles.__getitem__(opc-1)
        print("RESUMEN DE TODA LA INFORMACION DEL EVENTO SELECCIONADO")
        olimpiada=sacarOlimpiadaPorEvento(eventoElegido,sesion)
        print(olimpiada.temporada,"--",olimpiada.nombre,"--",deporteSeleccionado.nombre,"--",eventoElegido.nombre)
        print("Y ESTOS SON LOS PARTICIPANTES")
        listParticipaciones=sacarParticipacionDesdeEvento(eventoElegido,sesion)
        for e in listParticipaciones:
            medalla=e.medalla
            edad=e.edad
            deportista=sacarDeportistasPorParticipacion(e,sesion)
            equipo=sacarEquiposPorParticipacion(e,sesion)
            print(" ",deportista.nombre,"--",deportista.peso,"--",deportista.altura,"--",edad,"--",equipo.nombre,"--",medalla)

# --------------------EJERCICIO2--------------------
    def metodo2(self):
        # ----------CON MYSQL----------
        engine = create_engine('mysql+pymysql://admin:password@localhost/olimpiadas')
        Session = sessionmaker(bind=engine)
        sesion = Session()

        nombre = input("""introduzce un texto para buscar al deportista por el nombre
        """)

        listDeportistas = sacarDeportistasPorTexto(nombre, sesion)
        print("Elige uno atraves del numero de alado")
        cont=0
        for e in listDeportistas:
            cont+=1
            print(cont,".-",e.nombre)
        opc=(int)(input())
        deportistaElegido=listDeportistas.__getitem__(opc-1)

        listParticipaciones=sacarParticipacionPorDeprtista(deportistaElegido,sesion)
        cont=0
        print("Elige uno atraves del numero de alado")
        listAux=[]
        for e in listParticipaciones:
            cont+=1
            evento=sacarEventoPorParticipacion(e,deportistaElegido,sesion)
            listAux.append(evento)
            print(cont,".-",evento.nombre)
        opc = (int)(input())
        eventoElegido=listAux.__getitem__(opc-1)
        medallanueva=input("A QUE MEDALLA QUIERES CAMBIAR ESA PARTICIPACION")
        participacionElegida = sesion.query(Participacion).filter(deportistaElegido.id_deportista == Participacion.id_deportista, eventoElegido.id_evento == Participacion.id_evento ).one()
        participacionElegida.medalla=medallanueva
        id_d=deportistaElegido.id_deportista
        id_v=eventoElegido.id_evento
        sesion.commit()
        # ----------CON SQLite----------
        engine = create_engine('sqlite:///olimpiadas.db')
        Session = sessionmaker(bind=engine)
        sesion = Session()
        sesion.execute("pragma foreign_keys=on")

        participacionElegida = sesion.query(Participacion).filter(id_d== Participacion.id_deportista,
                                                                  id_v == Participacion.id_evento ).one()
        participacionElegida.medalla=medallanueva
        sesion.commit()

# --------------------EJERCICIO3--------------------
    def metodo3(self):
        nuevo=0
        # ----------CON MYSQL----------
        engine = create_engine('mysql+pymysql://admin:password@localhost/olimpiadas')
        Session = sessionmaker(bind=engine)
        sesion = Session()

        nombre = input("""introduzce un texto para buscar al deportista por el nombre
             """)

        listDeportistas = sacarDeportistasPorTexto(nombre, sesion)
        print("Elige uno atraves del numero de alado")
        cont = 0
        for e in listDeportistas:
            cont += 1
            print(cont, ".-", e.nombre)
        cont += 1
        print(cont, ".-Crear uno con este nombre")
        opc = (int)(input())
        nombre=""
        peso=0
        altura=0
        if opc!=cont:
            deportistaElegido = listDeportistas.__getitem__(opc - 1)
            nombre=deportistaElegido.nombre
            sexo=deportistaElegido.sexo
            peso=deportistaElegido.peso
            altura=deportistaElegido.altura
        else:
            nombre = input("¿Nombre?")
            print("""Elige atraves de la letra
            M-Masculino
            F-Femenino""")
            sexo = ""
            while (sexo != "M" and sexo != "F"):
                sexo = input()
            peso = (int)(input("¿Peso?"))
            altura = (int)(input("¿Altura?"))
            deportistaElegido=crearDeportista(nombre,sexo,peso,altura,sesion)
            nuevo=1

        print("""Elige uno mediante la letra
        w - Winter
        s - Summer""")
        opc=""
        while opc!="w" and opc!="s":
            opc=input()
        if(opc=="w"):
            temporadaElegida="Winter"
        else:
            temporadaElegida="Summer"

        listaOlimpiadas = sesion.query(Olimpiada).filter(Olimpiada.temporada == temporadaElegida).all()
        cont = 0
        for e in listaOlimpiadas:
            cont += 1
            print(cont, ".-", e.nombre)
        opc = 0
        while opc < 1 or opc > cont:
            opc = (int)(input("Elige uno"))
        olimpiadaElegida = listaOlimpiadas.__getitem__(opc - 1)


        listDeporte=sacarDeportePorOlimpiada(olimpiadaElegida,sesion)
        cont=0
        print("Elige uno mediante el numero")
        for e in listDeporte:
            cont+=1
            print(cont,".-",e.nombre)
        opc=(int)(input())
        deporteElegido=listDeporte.__getitem__(opc-1)


        listEventos=sacarEventoporDeporteyOlimpiada(deporteElegido,olimpiadaElegida,sesion)
        cont = 0
        print("Elige uno mediante el numero")
        for e in listEventos:
            cont += 1
            print(cont, ".-", e.nombre)
        opc = (int)(input())
        eventoElegido=listEventos.__getitem__(opc-1)

        listequipo = sesion.query(Equipo).all()
        print("Elige un equipo atraves del numero")
        for e in listequipo:
            print(e.id_Equipo, ".-", e.nombre)
        opc = (int)(input())
        equipo=listequipo.__getitem__(opc-1)
        edad = input("¿Edad?")
        medalla = input("¿Medalla?")

        crearParticipacion(deportistaElegido,eventoElegido,equipo,edad,medalla,sesion)
        print(deportistaElegido.id_deportista)
        id_d=deportistaElegido.id_deportista
        id_v=eventoElegido.id_evento
        id_e=equipo.id_Equipo
        sesion.commit()
        # ----------CON SQLite----------
        engine = create_engine('sqlite:///olimpiadas.db')
        Session = sessionmaker(bind=engine)
        sesion = Session()
        sesion.execute("pragma foreign_keys=on")

        deporti=Deportista()
        if nuevo==1:
            deporti.nombre= nombre
            deporti.sexo=sexo
            deporti.peso=peso
            deporti.altura=altura
            sesion.add(deporti)
            sesion.commit()
            id_d=deporti.id_deportista


        parti=Participacion()
        parti.id_deportista=id_d
        parti.id_evento=id_v
        parti.id_equipo=id_e
        parti.edad=edad
        parti.medalla=medalla
        sesion.add(parti)
        sesion.commit()

# --------------------EJERCICIO4--------------------
    def metodo4(self):
        # ----------CON MYSQL----------
        engine = create_engine('mysql+pymysql://admin:password@localhost/olimpiadas')
        Session = sessionmaker(bind=engine)
        sesion = Session()

        nombre = input("""introduzce un texto para buscar al deportista por el nombre
             """)

        listDeportistas = sacarDeportistasPorTexto(nombre, sesion)
        print("Elige uno atraves del numero de alado")
        cont = 0
        for e in listDeportistas:
            cont += 1
            print(cont, ".-", e.nombre)
        opc = (int)(input())
        deportistaElegido = listDeportistas.__getitem__(opc - 1)

        listParticipaciones = sacarParticipacionPorDeprtista(deportistaElegido, sesion)
        cont = 0
        print("Elige uno atraves del numero de alado")
        listAux = []
        for e in listParticipaciones:
            cont += 1
            evento = sacarEventoPorParticipacion(e, deportistaElegido, sesion)
            listAux.append(evento)
            print(cont, ".-", evento.nombre)
        opc = (int)(input())
        eventoElegido = listAux.__getitem__(opc - 1)
        listPart=sesion.query(Participacion).filter(deportistaElegido.id_deportista==Participacion.id_deportista,
                                                    eventoElegido.id_evento==Participacion.id_evento).all()
        cont=0
        for e in listPart:
            cont+=1
            sesion.delete(e)
        if(cont==1):
           sesion.delete(deportistaElegido)
        sesion.commit()
        id_v=eventoElegido.id_evento
        id_d=deportistaElegido.id_deportista
        # ----------CON SQLite----------
        engine = create_engine('sqlite:///olimpiadas.db')
        Session = sessionmaker(bind=engine)
        sesion = Session()
        sesion.execute("pragma foreign_keys=on")

        deportistaElegido=sesion.query(Deportista).filter(Deportista.id_deportista==id_d).one()
        listPart = sesion.query(Participacion).filter(id_d == Participacion.id_deportista,
                                                       id_v  == Participacion.id_evento).all()
        cont=0
        for e in listPart:
            cont+=1
            sesion.delete(e)
        if (cont==1):
            sesion.delete(deportistaElegido)
        sesion.commit()


# ********************METODOS EJERCICIO1********************
def elegirBBDD(tipo):
    if tipo==1:
        engine = create_engine('mysql+pymysql://admin:password@localhost/olimpiadas')
    else:
        engine = create_engine('sqlite:///olimpiadas.db')
    return engine


def sacarDeportePorOlimpiada(olimpiada,sesion):
    listaOlimpiadas = sesion.query(Evento).filter(Evento.id_olimpiada == olimpiada.id_olimpiada).all()
    cont=0
    listaDeportes=[]
    for e in listaOlimpiadas:
        cont += 1
        dep = sesion.query(Deporte).filter(Deporte.id_deporte==e.id_deporte).one()
        if not listaDeportes.__contains__(dep):
            listaDeportes.append(dep)
    return listaDeportes


def sacarEventoporDeporteyOlimpiada(deporte,olimpiada,sesion):
    listaEventos= sesion.query(Evento).filter(Evento.id_olimpiada == olimpiada.id_olimpiada, Evento.id_deporte == deporte.id_deporte).all()
    return listaEventos
def sacarOlimpiadaPorEvento(evento,sesion):
    olimpiada=sesion.query(Olimpiada).filter(evento.id_olimpiada == Olimpiada.id_olimpiada).one()
    return olimpiada

def sacarParticipacionDesdeEvento(evento,sesion):
    participaciones=sesion.query(Participacion).filter(Participacion.id_evento == evento.id_evento).all()
    return participaciones
def sacarDeportistasPorParticipacion(participacion,sesion):
    deportistas=sesion.query(Deportista).filter(participacion.id_deportista == Deportista.id_deportista).one()
    return deportistas
def sacarEquiposPorParticipacion(participacion,sesion):
    equipos=sesion.query(Equipo).filter(participacion.id_equipo == Equipo.id_Equipo).one()
    return equipos



# ********************METODOS EJERCICIO2********************
def sacarDeportistasPorTexto(nombre,sesion):
    deportistas=sesion.query(Deportista).filter(Deportista.nombre.contains(nombre)).all()
    return deportistas

def sacarParticipacionPorDeprtista(deportista,sesion):
    participaciones=sesion.query(Participacion).filter(deportista.id_deportista == Participacion.id_deportista).all()
    return participaciones

def sacarEventoPorParticipacion(participacion,deportista,sesion):
    eventos=sesion.query(Evento).filter(participacion.id_evento == Evento.id_evento, deportista.id_deportista == participacion.id_deportista).one()
    return eventos


# ********************METODOS EJERCICIO3********************

def crearDeportista(nombre,sexo,peso,altura,sesion):

    deportista=Deportista()
    deportista.nombre=nombre
    deportista.sexo=sexo
    deportista.peso=peso
    deportista.altura=altura
    sesion.add(deportista)
    sesion.commit()
    return deportista

def crearParticipacion(deportista,evento,equipo,edad,medalla,sesion):
    Parti=Participacion()

    Parti.id_deportista=deportista.id_deportista
    Parti.id_evento=evento.id_evento
    Parti.id_equipo=equipo.id_Equipo
    Parti.edad=edad
    Parti.medalla=medalla
    sesion.add(Parti)
    sesion.commit()


# ********************METODOS EJERCICIO4********************




ej1=Ejercicio1()
ej1.menu()
# for e in lista:
#     print(e.nombre)