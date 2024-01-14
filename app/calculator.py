import app.schemas as schemas, app.models as models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from app.database import get_db
from fastapi.responses import StreamingResponse
import pandas as pd
from fastapi.encoders import jsonable_encoder
router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_calcul(
    db: Session = Depends(get_db), limit: int = 100, page: int = 1, search: str = ""
):
    skip = (page - 1) * limit

    result_calcul_all = (
        db.query(models.Calcul)
        .limit(limit)
        .offset(skip)
        .all()
    )
    return {"Status": "Success", "Results": len(result_calcul_all), "Calcul": result_calcul_all}

@router.post("/calcul", status_code=status.HTTP_201_CREATED)
def create_calcul(calcul: schemas.CalculBaseSchema, db: Session = Depends(get_db)):
    
    answer = calcul_evaluate(calcul.notation)
    print(answer)
    db_calcul= models.Calcul(notation= calcul.notation , resultat=answer)
    db.add(db_calcul)
    db.commit()
    db.refresh(db_calcul)
    return {"Status": "Success", "calcul": db_calcul}


# Get all calcul and resultat to CSV
@router.get("/csv")
def get_csv_data(db: Session = Depends(get_db),skip: int = 0, limit: int = 100):
    
    result_calcul_all = db.query(models.Calcul).offset(skip).limit(limit).all()
    #convert Model in json
    json_data = jsonable_encoder(result_calcul_all)
    #convert Json in dataframe(pandas)
    df = pd.DataFrame(list(json_data))
    
    if not result_calcul_all:
       raise HTTPException(status_code=404, detail='calcul not found')
    #return df in text csv
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=data.csv"}
)

# Get last calcul and resultat 
@router.get("/csvlast/")
def get_csv_data_last(db: Session = Depends(get_db)):
    
    obj = db.query(models.Calcul).order_by(models.Calcul.id.desc()).first()
    return obj

"""
Algo notation polonaise inverse (NPI)

"""
def calcul_evaluate(expression): 
  
  expression = expression.split() 
    
  # stack 
  stack = [] 
    
  # iterating expression 
  for ele in expression: 
      
    # ele is a number 
    if ele not in '/*+-': 
      stack.append(int(ele)) 
      
    # ele is an operator 
    else: 
      # getting operands 
      right = stack.pop() 
      left = stack.pop() 
        
      # performing operation according to operator 
      if ele == '+': 
        stack.append(left + right) 
          
      elif ele == '-': 
        stack.append(left - right) 
          
      elif ele == '*': 
        stack.append(left * right) 
          
      elif ele == '/': 
        stack.append(int(left / right)) 
    
  # return final answer. 
  return stack.pop() 
