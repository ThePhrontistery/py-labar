import logging

import uvicorn

# Init Logger for this Class
from app.common.core import get_global_settings
from app.common.core.configuration import get_log_config
from app.common.infra.sql_adaptors import init_db_entities, get_db_settings

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # import entities to init
    from app.domain.users.models import user
    from app.domain.topics.models import topic, vote 
    from app.domain.groups.models import group 
    init_db_entities(get_db_settings())
    uvicorn.run("app.api:api", host="localhost", port=get_global_settings().port, log_config=get_log_config(), reload=True)