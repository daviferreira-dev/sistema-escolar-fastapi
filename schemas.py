from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# --- SCHEMAS SIMPLES (PARA O JOIN) ---
class AlunoSimples(BaseModel):
    nome_aluno: str
    class Config: from_attributes = True

class CursoSimples(BaseModel):
    nome_curso: str
    class Config: from_attributes = True

class ProfessorSimples(BaseModel):
    nome_professor: str
    class Config: from_attributes = True

# --- ESTADOS ---
class EstadoBase(BaseModel):
    nome_estado: str
    sigla_estado: str

class EstadoCreate(EstadoBase): pass

class EstadoResponse(EstadoBase):
    cod_estado: int
    class Config: from_attributes = True

# --- CIDADES ---
class CidadeBase(BaseModel):
    nome_cidade: str
    cod_estado: int

class CidadeCreate(CidadeBase): pass

class CidadeResponse(CidadeBase):
    cod_cidade: int
    class Config: from_attributes = True

# --- ALUNOS ---
class AlunoBase(BaseModel):
    nome_aluno: str
    email_aluno: Optional[str] = None
    idade_aluno: Optional[int] = None
    cod_cidade: int
    data_cadastro_aluno: date
    ativo_aluno: bool = True

class AlunoCreate(AlunoBase): pass

class AlunoResponse(AlunoBase):
    cod_aluno: int
    class Config: from_attributes = True

# --- CURSOS ---
class CursoBase(BaseModel):
    nome_curso: str
    carga_horaria_curso: int
    preco_curso: float

class CursoCreate(CursoBase): pass

class CursoResponse(CursoBase):
    cod_curso: int
    class Config: from_attributes = True

# --- PROFESSORES ---
class ProfessorBase(BaseModel):
    nome_professor: str
    email_professor: Optional[str] = None
    salario_professor: float
    cod_regiao: int

class ProfessorCreate(ProfessorBase): pass

class ProfessorResponse(ProfessorBase):
    cod_professor: int
    class Config: from_attributes = True

# --- REGIOES ---
class RegiaoBase(BaseModel):
    nome_regiao: str

class RegiaoCreate(RegiaoBase): pass

class RegiaoResponse(RegiaoBase):
    cod_regiao: int
    class Config: from_attributes = True

# --- MATRICULAS ---
class MatriculaBase(BaseModel):
    cod_aluno: int
    cod_curso: int
    cod_professor: int
    data_matricula: date
    nota_matricula: Optional[float] = None

class MatriculaCreate(MatriculaBase): pass

class MatriculaResponse(MatriculaBase):
    cod_matricula: int
    aluno: AlunoSimples
    curso: CursoSimples
    professor: ProfessorSimples
    class Config: from_attributes = True

# --- MONGODB ---
class RecadoBase(BaseModel):
    autor: str
    mensagem: str
    tags: List[str] = []
    alerta_urgente: bool = False

class RecadoCreate(RecadoBase): pass