from fastapi import HTTPException, Header, Query, APIRouter, status, Depends
from sqlalchemy.orm import Session
from schemas.zones import Zoneresponse, Newzone
from database.database import get_db
from models.zones import ZoneDB
from routers.auth1 import get_current_user
from repository.zones import create_zones, read_zone, read_zones

router = APIRouter(prefix='/zones', tags=['zones'])

@router.post("/zones/")
async def Create_zones(zone: Newzone, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        create_zones.Create_zone(db, user_id, zone)

        return {"message": "zone created successfully"}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/zones/{zones_id}", response_model=Zoneresponse)
async def Read_zone(zone_id: str, token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        zones = read_zone.read_zone_by_id(db, zone_id, user_id)

        if zones:
            return zones
        raise HTTPException(status_code=404, detail="Zone not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/zones/", response_model=list[Zoneresponse])
async def Read_zones(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        user_info = get_current_user(token)
        user_id = user_info['id']

        zones_list = read_zones.read_zones(db, user_id)

        return zones_list

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
