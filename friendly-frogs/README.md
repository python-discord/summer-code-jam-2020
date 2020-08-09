# Friendly Frogs

This is the default README of your team's project. Please replace this by a README with more information on your project. At the very least, your README should contain information on how to set-up and run your project.

1. Create virtualenv
`make env`
2. Activate virtual env
`source venv/bin/activate`
3. Create .env file in project root like as example_env.
4. Export env vars.
`set -o allexport; source .env; set +o allexport;`
5. Install depedencies
`make packages`
6. Open new terminal and run postgres
`make up postgres`
7. Make migration
`make migrate`
8. Run django
`make run`
