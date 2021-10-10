import pathlib
import fastapi
from fastapi import Depends
from sqlalchemy.orm.session import Session

from . import db
from . import schema
from .graphene_schema import schema as graphene_schema

app = fastapi.FastAPI()
current_dir = pathlib.Path(__file__).resolve().parent


@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}


@app.get("/department")
async def get_department(session: Session = Depends(db.get_session)):
    return [
        {
            "departmentNo": elm.department_no,
            "department_name": elm.department_name,
        }
        for elm in session.query(schema.Department).all()
    ]


@app.get("/graphql")
@app.get("/graphql/graphiql")
async def get_graphql_graphiql():
    with open(current_dir / "static" / "graphiql.html") as f:
        return fastapi.responses.HTMLResponse(f.read())


@app.get("/graphql/playground")
async def get_graphql_playground():
    with open(current_dir / "static" / "playground.html") as f:
        return fastapi.responses.HTMLResponse(f.read())


@app.get("/graphql/voyager")
async def get_graphql_voyager():
   with open(current_dir / "static" / "voyager.html") as f:
        return fastapi.responses.HTMLResponse(f.read())


@app.post("/graphql")
async def post_graphql(
    request: fastapi.Request,
    session: Session = Depends(db.get_session),
):
    content_type = request.headers.get("Content-Type", "")

    if "application/json" in content_type:
        data = await request.json()

    elif "application/graphql" in content_type:
        body = await request.body()
        text = body.decode()
        data = {"query": text}

    elif "query" in request.query_params:
        data = request.query_params

    else:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unsupported Media Type",
        )

    if not (q_body := data.get("query")):
        raise fastapi.HTTPException(status_code=400, detail=f"Unsupported method: {q_body}")

    res = graphene_schema.execute(
        q_body,
        context_value={"request": request, "session": session},
    )

    return res.to_dict()
