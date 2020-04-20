import graphene
import json


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "world"


schema = graphene.Schema(query=Query)

result = schema.execute(
    """
    {
      hello
    }
    """
)
# get in odict format
print(result.data.items())

# just get the return value
print(result.data["hello"])

# get in plain json format
dictResult = dict(result.data.items())
print(json.dumps(dictResult))

# get in json indent format
print(json.dumps(dictResult, indent=2))
