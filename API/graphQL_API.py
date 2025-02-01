import strawberry
from strawberry.asgi import GraphQL
from starlette.applications import Starlette
from starlette.routing import Route

@strawberry.type
class MathResponse:
    result: float | None = None
    error: str | None = None

@strawberry.type
class Query:
    @strawberry.field
    def calculate(self, a: float, b: float, operation: str) -> MathResponse:
        if operation == "add":
            return MathResponse(result=a + b)
        elif operation == "subtract":
            return MathResponse(result=a - b)
        elif operation == "multiply":
            return MathResponse(result=a * b)
        elif operation == "divide":
            return MathResponse(result=a / b if b != 0 else None, error="Division by zero" if b == 0 else None)
        return MathResponse(error="Invalid operation")

schema = strawberry.Schema(query=Query)

app = Starlette(routes=[
    Route("/graphql", GraphQL(schema=schema))
])
