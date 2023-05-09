from gensim.models import KeyedVectors
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import re
from . import env, typings

print("INFO: Loading w2v model")
kv = KeyedVectors.load(env.KV_MODEL_PATH, mmap="r")
print("INFO: Test ", kv.most_similar(positive=["かわいい"], negative=["つらい"])[0])
print("INFO: Load compleate")

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
  allow_origins=env.ALLOW_ORIGINS
)


@app.get("/")
async def root():
  return {"msg": "working"}

@app.post("/prompt/")
async def prompt(body: typings.Prompt):
  if (body.positive == []) and (body.negative == []):
    raise HTTPException(422, {"code": 1001, "msg": "prompt is empty"})
  try:
    result = kv.most_similar(positive=body.positive, negative=body.negative)
    return {"result": result}
  except KeyError as e:
    target_word = re.findall(r"'(.*)'", str(e))[0]
    print(target_word)
    raise HTTPException(404, {"code": 1002, "msg": "this key not present in vocabulary", "word": target_word})
