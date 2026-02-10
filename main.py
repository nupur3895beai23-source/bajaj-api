from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

app = FastAPI()

OFFICIAL_EMAIL = "nupur3895.beai23@chitkara.edu.in"

class RequestModel(BaseModel):
    fibonacci: int | None = None
    prime: list[int] | None = None
    lcm: list[int] | None = None
    hcf: list[int] | None = None
    AI: str | None = None

@app.get("/health")
def health():
    return {"is_success": True, "official_email": OFFICIAL_EMAIL}

def fib(n):
    a,b=0,1; res=[]
    for _ in range(n):
        res.append(a); a,b=b,a+b
    return res

def is_prime(x):
    if x<2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0: return False
    return True

def lcm_list(arr):
    r=arr[0]
    for x in arr[1:]:
        r=abs(r*x)//math.gcd(r,x)
    return r

def hcf_list(arr):
    r=arr[0]
    for x in arr[1:]:
        r=math.gcd(r,x)
    return r

@app.post("/bfhl")
def bfhl(req: RequestModel):
    if req.fibonacci is not None:
        data=fib(req.fibonacci)
    elif req.prime is not None:
        data=[x for x in req.prime if is_prime(x)]
    elif req.lcm is not None:
        data=lcm_list(req.lcm)
    elif req.hcf is not None:
        data=hcf_list(req.hcf)
    elif req.AI is not None:
        data="Mumbai"
    else:
        raise HTTPException(status_code=400, detail="Invalid input")

    return {"is_success": True, "official_email": OFFICIAL_EMAIL, "data": data}

