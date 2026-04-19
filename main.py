from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import engine, get_db, colecao_recados

# Cria as tabelas no banco de dados se não existirem
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Sistema Escolar - Versão Final",
    description="Sistema híbrido SQL/NoSQL para gestão de alunos e professores."
)

# Configuração de CORS para permitir acesso do Hoppscotch/Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# ROTAS: ESTADOS
# ==========================================
@app.get("/estados/", response_model=List[schemas.EstadoResponse], tags=["Estados"])
def listar_estados(db: Session = Depends(get_db)):
    return db.query(models.Estado).all()

@app.post("/estados/", response_model=schemas.EstadoResponse, status_code=201, tags=["Estados"])
def criar_estado(estado: schemas.EstadoBase, db: Session = Depends(get_db)):
    novo = models.Estado(**estado.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.put("/estados/{cod_estado}", response_model=schemas.EstadoResponse, tags=["Estados"])
def atualizar_estado(cod_estado: int, estado_novo: schemas.EstadoBase, db: Session = Depends(get_db)):
    estado = db.query(models.Estado).get(cod_estado)
    if not estado: raise HTTPException(status_code=404, detail="Estado não encontrado.")
    estado.nome_estado = estado_novo.nome_estado
    estado.sigla_estado = estado_novo.sigla_estado
    db.commit()
    return estado

@app.delete("/estados/{cod_estado}", status_code=204, tags=["Estados"])
def deletar_estado(cod_estado: int, db: Session = Depends(get_db)):
    estado = db.query(models.Estado).get(cod_estado)
    if not estado: raise HTTPException(status_code=404, detail="Estado inexistente.")
    db.delete(estado)
    db.commit()
    return None

# ==========================================
# ROTAS: CIDADES
# ==========================================
@app.get("/cidades/", response_model=List[schemas.CidadeResponse], tags=["Cidades"])
def listar_cidades(db: Session = Depends(get_db)):
    return db.query(models.Cidade).all()

@app.get("/cidades/{cod_cidade}/alunos", response_model=List[schemas.AlunoResponse], tags=["Cidades"])
def buscar_alunos_por_cidade(cod_cidade: int, db: Session = Depends(get_db)):
    return db.query(models.Aluno).filter(models.Aluno.cod_cidade == cod_cidade).all()

@app.post("/cidades/", response_model=schemas.CidadeResponse, status_code=201, tags=["Cidades"])
def criar_cidade(cidade: schemas.CidadeBase, db: Session = Depends(get_db)):
    nova = models.Cidade(**cidade.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.delete("/cidades/{cod_cidade}", status_code=204, tags=["Cidades"])
def deletar_cidade(cod_cidade: int, db: Session = Depends(get_db)):
    cidade = db.query(models.Cidade).get(cod_cidade)
    if not cidade: raise HTTPException(status_code=404, detail="Cidade não encontrada.")
    db.delete(cidade)
    db.commit()
    return None

# ==========================================
# ROTAS: ALUNOS
# ==========================================
@app.get("/alunos/", response_model=List[schemas.AlunoResponse], tags=["Alunos"])
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(models.Aluno).all()

@app.get("/alunos/{cod_aluno}", response_model=schemas.AlunoResponse, tags=["Alunos"])
def buscar_aluno_especifico(cod_aluno: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).get(cod_aluno)
    if not aluno: raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return aluno

@app.post("/alunos/", response_model=schemas.AlunoResponse, status_code=201, tags=["Alunos"])
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    novo = models.Aluno(**aluno.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.put("/alunos/{cod_aluno}", response_model=schemas.AlunoResponse, tags=["Alunos"])
def atualizar_aluno(cod_aluno: int, aluno_novo: schemas.AlunoCreate, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).get(cod_aluno)
    if not aluno: raise HTTPException(status_code=404, detail="Aluno não existe.")
    for key, value in aluno_novo.model_dump().items():
        setattr(aluno, key, value)
    db.commit()
    return aluno

@app.delete("/alunos/{cod_aluno}", status_code=204, tags=["Alunos"])
def deletar_aluno(cod_aluno: int, db: Session = Depends(get_db)):
    aluno = db.query(models.Aluno).get(cod_aluno)
    if not aluno: raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    db.delete(aluno)
    db.commit()
    return None

# ==========================================
# ROTAS: CURSOS
# ==========================================
@app.get("/cursos/", response_model=List[schemas.CursoResponse], tags=["Cursos"])
def listar_cursos(db: Session = Depends(get_db)):
    return db.query(models.Curso).all()

@app.get("/cursos/{cod_curso}", response_model=schemas.CursoResponse, tags=["Cursos"])
def buscar_curso_especifico(cod_curso: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).get(cod_curso)
    if not curso: raise HTTPException(status_code=404, detail="Curso não existe.")
    return curso

@app.post("/cursos/", response_model=schemas.CursoResponse, status_code=201, tags=["Cursos"])
def criar_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    novo = models.Curso(**curso.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.delete("/cursos/{cod_curso}", status_code=204, tags=["Cursos"])
def deletar_curso(cod_curso: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).get(cod_curso)
    if not curso: raise HTTPException(status_code=404, detail="Curso não encontrado.")
    db.delete(curso)
    db.commit()
    return None

# ==========================================
# ROTAS: PROFESSORES E REGIÕES
# ==========================================
@app.get("/professores/", response_model=List[schemas.ProfessorResponse], tags=["Professores"])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()

@app.get("/regioes/{cod_regiao}", response_model=schemas.RegiaoResponse, tags=["Regiões"])
def buscar_regiao_por_id(cod_regiao: int, db: Session = Depends(get_db)):
    regiao = db.query(models.Regiao).get(cod_regiao)
    if not regiao:
        raise HTTPException(status_code=404, detail="Região não encontrada.")
    return regiao

@app.get("/regioes/{cod_regiao}/professores", response_model=List[schemas.ProfessorResponse], tags=["Regiões"])
def listar_professores_por_regiao(cod_regiao: int, db: Session = Depends(get_db)):
    return db.query(models.Professor).filter(models.Professor.cod_regiao == cod_regiao).all()

# post professores
@app.post("/professores/", response_model=schemas.ProfessorResponse, status_code=201, tags=["Professores"])
def criar_professor(prof: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    # Opcional: Verificar se a região existe antes de cadastrar
    regiao = db.query(models.Regiao).get(prof.cod_regiao)
    if not regiao:
        raise HTTPException(status_code=404, detail="Região informada não existe.")
        
    novo_professor = models.Professor(**prof.model_dump())
    db.add(novo_professor)
    db.commit()
    db.refresh(novo_professor)
    return novo_professor

@app.delete("/professores/{cod_professor}", status_code=204, tags=["Professores"])
def deletar_professor(cod_professor: int, db: Session = Depends(get_db)):
    prof = db.query(models.Professor).get(cod_professor)
    if not prof: raise HTTPException(status_code=404, detail="Professor não encontrado.")
    db.delete(prof)
    db.commit()
    return None

# ==========================================
# ROTAS: MATRÍCULAS
# ==========================================
@app.get("/matriculas/", response_model=List[schemas.MatriculaResponse], tags=["Matrículas"])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(models.Matricula).all()

@app.post("/matriculas/", response_model=schemas.MatriculaResponse, status_code=201, tags=["Matrículas"])
def criar_matricula(mat: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    nova = models.Matricula(**mat.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.put("/matriculas/{cod_matricula}", response_model=schemas.MatriculaResponse, tags=["Matrículas"])
def atualizar_matricula(cod_matricula: int, mat_nova: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    item = db.query(models.Matricula).get(cod_matricula)
    if not item: raise HTTPException(status_code=404, detail="Matrícula não existe.")
    for key, value in mat_nova.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@app.delete("/matriculas/{cod_matricula}", status_code=204, tags=["Matrículas"])
def deletar_matricula(cod_matricula: int, db: Session = Depends(get_db)):
    item = db.query(models.Matricula).get(cod_matricula)
    if not item: raise HTTPException(status_code=404, detail="Matrícula não encontrada.")
    db.delete(item)
    db.commit()
    return None

# ==========================================
# ROTAS: MONGODB (MURAL DE RECADOS)
# ==========================================
@app.post("/recados-mongodb/", status_code=201, tags=["Mural MongoDB"])
def postar_recado(recado: schemas.RecadoCreate):
    resultado = colecao_recados.insert_one(recado.model_dump())
    return {"id": str(resultado.inserted_id), "status": "Recado publicado!"}

@app.get("/recados-mongodb/", tags=["Mural MongoDB"])
def ler_recados():
    recados = list(colecao_recados.find({}))
    for r in recados: r["_id"] = str(r["_id"])
    return recados