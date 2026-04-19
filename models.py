from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Numeric
from database import Base
from sqlalchemy.orm import relationship 

class Estado(Base):
    __tablename__ = "tb_estados"
    cod_estado = Column(Integer, primary_key=True, index=True)
    nome_estado = Column(String(50), nullable=False)
    sigla_estado = Column(String(2), nullable=False)

class Cidade(Base):
    __tablename__ = "tb_cidades"
    cod_cidade = Column(Integer, primary_key=True, index=True)
    nome_cidade = Column(String(100), nullable=False)
    cod_estado = Column(Integer, ForeignKey("tb_estados.cod_estado"), nullable=False)

class Regiao(Base):
    __tablename__ = "tb_regioes"
    cod_regiao = Column(Integer, primary_key=True, index=True)
    nome_regiao = Column(String(30), nullable=False)

class Aluno(Base):
    __tablename__ = "tb_alunos"
    cod_aluno = Column(Integer, primary_key=True, index=True)
    nome_aluno = Column(String(100), nullable=False)
    email_aluno = Column(String(100), nullable=True)
    idade_aluno = Column(Integer, nullable=True) 
    cod_cidade = Column(Integer, ForeignKey("tb_cidades.cod_cidade"), nullable=False)
    data_cadastro_aluno = Column(Date, nullable=False)
    ativo_aluno = Column(Boolean, default=True)
    matriculas = relationship("Matricula", back_populates="aluno")

class Curso(Base):
    __tablename__ = "tb_cursos"
    cod_curso = Column(Integer, primary_key=True, index=True)
    nome_curso = Column(String(100))
    carga_horaria_curso = Column(Integer) 
    preco_curso = Column(Numeric(10,2))
    matriculas = relationship("Matricula", back_populates="curso")

class Professor(Base):
    __tablename__ = "tb_professores"
    cod_professor = Column(Integer, primary_key=True, index=True)
    nome_professor = Column(String(100), nullable=False)
    email_professor = Column(String(100), nullable=True)
    salario_professor = Column(Numeric(10,2), nullable=False)
    cod_regiao = Column(Integer, ForeignKey("tb_regioes.cod_regiao"))
    matriculas = relationship("Matricula", back_populates="professor")

class Matricula(Base):
    __tablename__ = "tb_matriculas"
    cod_matricula = Column(Integer, primary_key=True, index=True)
    cod_aluno = Column(Integer, ForeignKey("tb_alunos.cod_aluno"), nullable=False)
    cod_curso = Column(Integer, ForeignKey("tb_cursos.cod_curso"), nullable=False)
    cod_professor = Column(Integer, ForeignKey("tb_professores.cod_professor"), nullable=False)
    data_matricula = Column(Date, nullable=False)
    nota_matricula = Column(Numeric(4,1), nullable=True)
    
    aluno = relationship("Aluno", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")
    professor = relationship("Professor", back_populates="matriculas")