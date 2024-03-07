from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.task_details import Task_detailsDB
from schemas.task_details import Create_Task_details

def create_Task_details(db: Session, user_id: int, task_details: Create_Task_details):
    try:
        db_task_details = Task_detailsDB(
            user_id=user_id,
            task_id=task_details.task_id,
            assigned_to=task_details.assigned_to,
            co_assigned_to=task_details.co_assigned_to,
            correction_action_plan=task_details.correction_action_plan,
            dependent_days=task_details.dependent_days,
            working_days=task_details.working_days,
            start_date=task_details.start_date,
            end_date=task_details.end_date,
            status_progression=task_details.status_progression,
            remarks=task_details.remarks,
            score=task_details.score,
        )

        db.add(db_task_details)
        db.commit()
        db.refresh(db_task_details)
        return db_task_details

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
