
# simple backup full
sshpass -p$POSTGRES_PASSWORD pg_dump -h db -p 5432 -U postgres -F c -b -v -f backup app 