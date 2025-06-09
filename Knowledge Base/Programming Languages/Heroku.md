```Bash
# push
heroku git:remote -a badr-dashboard
git push heroku ichsanul:main
# logging
heroku logs --tail --app=badr-dashboard
heroku run bash -a badr-dashboard
# database
heroku psql -a badr-dashboard
CREATE EXTENSION IF NOT EXISTS pgcrypto;
select schema_name
from information_schema.schemata;
SELECT * FROM pg_catalog.pg_tables;
\dt
heroku pg:backups:capture -a badr-dashboard
heroku pg:backups:download -a badr-dashboard
```