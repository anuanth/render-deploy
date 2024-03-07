from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,Text,ForeignKey,func
from sqlalchemy.orm import relationship

class Phc_domain_detailsDB(Base):
    __tablename__ = "phc_domain_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    phc_detail_ID = Column(String(36),ForeignKey("phc_details.id"), default =None)
    Domain_ID = Column(String(36),ForeignKey("domains.id"), default=None)
    remarks = Column(Text, nullable=True)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    user = relationship("UsersDB", back_populates="phc_domain_details")
    
    domains = relationship("DomainDB", back_populates="phc_domain_details")
    
    phc_details = relationship("Phc_detailsDB", back_populates="phc_domain_details")
    









    # phc_detail = relationship("Phc_detailsDB", back_populates="user_details")
    # ,ForeignKey("phc_details.id")
    