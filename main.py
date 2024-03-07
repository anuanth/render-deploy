from fastapi import FastAPI
import routers.auth1 as auth1
import routers.domain as domain
import routers.phc_details as phc_details
import routers.phc_domain_details as phc_domain_details
import routers.phc_tbc_code as phc_tbc_code
import routers.phc_tbc_user_details as phc_tbc_user_details
import routers.roles as roles
import routers.specialization as specialization
import routers.task_details as task_details
import routers.tasks as task
import routers.zones as zones


from database.database import Base, engine
app = FastAPI()


Base.metadata.create_all(bind=engine)
app.include_router(auth1.router)
app.include_router(domain.router)
app.include_router(phc_details.router)
app.include_router(phc_domain_details.router)
app.include_router(phc_tbc_code.router)
app.include_router(phc_tbc_user_details.router)
app.include_router(roles.router)
app.include_router(specialization.router)
app.include_router(task_details.router)
app.include_router(task.router)
app.include_router(zones.router)






