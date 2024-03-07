from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,Text,ForeignKey,func
from sqlalchemy.orm import relationship

class Phc_tbc_user_detailsDB(Base):
    __tablename__ = 'phc_tbc_user_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    phc_detail_ID = Column(String(36),ForeignKey("phc_details.id"),default=None)
    user_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    tbc_code_ID= Column(String(36),ForeignKey("phc_tbc_code.id"), default=None)
    name= Column(String(255), nullable=False)
    specialization_id = Column(String(36),ForeignKey("specializations.id"), default=None)
    remarks = Column(Text, nullable=True)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    user = relationship("UsersDB", back_populates="phc_tbc_user_details")
    
    phc_tbc_code = relationship("Phc_tbc_codeDB", back_populates="phc_tbc_user_details")
    
    phc_details = relationship("Phc_detailsDB", back_populates="phc_tbc_user_details")
    
    specializations = relationship("SpecializationDB", back_populates="phc_tbc_user_details")


