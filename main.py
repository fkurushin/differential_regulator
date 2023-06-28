from fastapi import FastAPI
from regulator import DifferentialRegulator
app = FastAPI()

# http://localhost:8000/process?arg1=value1&arg2=value2&arg3=value3&arg4=value4


@app.get('/differential_regulator')
def process_data(t0: float, T0: float, t1: float, T1: float):
    regulator = DifferentialRegulator(100, 90)
    regulator.time0 = t0
    regulator.temp0 = T0
    regulator.time1 = t1
    regulator.temp1 = T1
    res = regulator.regulate()
    return {"result": f"{res}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
