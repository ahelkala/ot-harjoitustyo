from invoke import task

@task 
def start(ctx):
	ctx.run("python3 src/main.py")

@task
def format(ctx):
	ctx.run("autopep8 --in-place --recursive src")

@task
def test(ctx):
	ctx.run("coverage run --branch -m pytest src")

@task(test)
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def lint(ctx):
	ctx.run("pylint src")
