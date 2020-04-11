from invoke import task


def simple_task(name: str, commands: str):
    def caller(c):
        c.run(f"echo running {name}")
        c.run(commands)

    return task(caller, name=name)


make_setup = simple_task(name="make-setup", commands="dephell deps convert")

format = simple_task(name="format", commands="inv black isort")
black = simple_task(name="black", commands="black -q .")
isort = simple_task(name="isort", commands="isort -rc .")

flake8 = simple_task(name="flake8", commands="flake8 src")

test = simple_task(name="test", commands="pytest")

check = simple_task(name="check", commands="inv format make-setup test flake8")
