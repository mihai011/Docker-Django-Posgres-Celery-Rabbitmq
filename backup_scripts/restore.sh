
# simple restore from backup

sshpass -p$POSTGRES_PASSWORD pg_restore -h db -p 5432 -U postgres -d app -v backup