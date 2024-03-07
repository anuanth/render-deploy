from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.zones import ZoneDB
from schemas.zones import Newzone

def Create_zone(db: Session, user_id: int, zone: Newzone):
    try:
        db_zone = ZoneDB(
            user_id=user_id,
            zone_name=zone.zone_name,
            remarks=zone.remarks,
            status=zone.status
        )

        db.add(db_zone)
        db.commit()
        db.refresh(db_zone)
        return db_zone

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
