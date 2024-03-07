from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.tasks import TasksDB
from schemas.tasks import Create_task

def Create_tasks(db: Session, user_id: int, tasks: Create_task):
    try:
        db_tasks = TasksDB(
            user_id=user_id,
            task_name=tasks.task_name,
            evidence_of_compliance=tasks.evidence_of_compliance,
            per_visit=tasks.per_visit,
            staff_availability=tasks.staff_availability,
            awareness_trained=tasks.awareness_trained,
            remarks=tasks.remarks,
        )

        db.add(db_tasks)
        db.commit()
        db.refresh(db_tasks)
        return db_tasks

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
