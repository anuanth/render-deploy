from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.zones import ZoneDB

def read_zone_by_id(db: Session, zone_id: str, user_id: int):
    try:
        zone = db.query(ZoneDB).filter(
            ZoneDB.id == zone_id,
            ZoneDB.user_id == user_id
        ).first()
        return zone

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
