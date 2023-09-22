db.auth('root', 'password123')
default_db = db.getSiblingDB('dev')
default_db.createUser({
    user: 'test',
    pwd: 'test',
    roles: [
        {
            role: 'dbOwner',
            db: 'dev',
        },
        {
            role: 'dbOwner',
            db: 'cerebro',
        },
    ],
});

