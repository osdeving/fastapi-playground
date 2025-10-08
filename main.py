from fastapi import FastAPI, HTTPException, status
from models.curso import Curso

app = FastAPI()


cursos = {
    1: {
        'name': 'Curso de Python',
        'horas': 45,
        'alunos': 323,
    },
    2: {
        'name': 'Curso de Java',
        'horas': 85,
        'alunos': 133,
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{id}')
async def get_curso(id: int):
    try:
        curso = cursos[id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

@app.post('/cursos')
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        #cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Já existe um curso com o id {curso.id}')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)

