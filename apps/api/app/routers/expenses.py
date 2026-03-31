from fastapi import APIRouter

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.get("/")
async def list_expenses():
    return {"message": "list expenses - coming soon"}

@router.post("/")
async def create_expense():
    return {"message": "create expense - coming soon"}

@router.get("/{expense_id}")
async def get_expense(expense_id: str):
    return {"message": f"get expense {expense_id} - coming soon"}

@router.delete("/{expense_id}")
async def delete_expense(expense_id: str):
    return {"message": f"delete expense {expense_id} - coming soon"}