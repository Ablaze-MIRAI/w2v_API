import os

KV_MODEL_PATH = os.environ.get("MODEL_PATH", "model/wikipedia_ja_w2v.model.kv")
ALLOW_ORIGINS = [os.environ.get("ALLOW_ORIGINS", "*")]
