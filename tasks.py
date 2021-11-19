from invoke import task

@task
def test(ctx):
	ctx.run("coverage run --branch -m pytest")

@task(test)
def coverage_report(ctx):
	ctx.run("coverage html")