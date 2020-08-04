from pathlib import Path

from invoke import task

BASE_DIR_PATH = Path(__file__).parent
BASE_DIR = str(BASE_DIR_PATH)
SRC_DIR = str(BASE_DIR_PATH / "src")
BUILD_DIR = str(BASE_DIR_PATH / "build")
DOCS_DIR = str(BASE_DIR_PATH / "docs")
DOCS_BUILD_DIR = str(BASE_DIR_PATH / "docs" / "_build")

# Lint
@task()
def black(ctx):
    """Format your code base using black."""

    with ctx.cd(BASE_DIR):
        ctx.run(f"black {BASE_DIR}")


@task
def black_check(ctx):
    """Check if your code base is formatted with black."""
    print("Checking your code with black...")
    with ctx.cd(BASE_DIR):
        ctx.run(f"black --check {BASE_DIR}")


@task()
def flake8_check(ctx):
    """Lint your code using flake8."""
    print("Checking your code with flake8...")
    flake8_includes = ctx.get("flake8", {}).get("includes", "src tests *.py")
    with ctx.cd(BASE_DIR):
        ctx.run(f"flake8 {flake8_includes}")


@task()
def isort(ctx):
    """Sort your imports."""
    # isort is sensitive to where it's run
    with ctx.cd(BASE_DIR):
        ctx.run(f"isort --recursive --skip-glob '*.venv' {BASE_DIR}")


@task()
def isort_check(ctx):
    """Check if your imports have been sorted properly."""
    print("Checking your code with isort...")
    with ctx.cd(BASE_DIR):
        ctx.run(f"isort --recursive --check --quiet --skip-glob '*.venv' {BASE_DIR}")


@task()
def format(ctx):
    """Format your code with black and isort."""
    black(ctx)
    isort(ctx)


@task()
def lint(ctx):
    """Lint your code with flake8 and check the formatting with black and isort."""
    flake8_check(ctx)
    black_check(ctx)
    isort_check(ctx)


# Release
@task()
def clean(ctx):
    """Delete the build directory and other python files that stick around."""
    with ctx.cd(BASE_DIR):
        ctx.run(f"find . -type f -name '*'.pyc -delete")
        ctx.run(f"find . -type f -name '*'.egg-info -delete")
        ctx.run(f"rm -rf .eggs")
        ctx.run(f"rm -rf {BUILD_DIR} ")
        ctx.run(f"rm -rf {DOCS_BUILD_DIR} ")


@task()
def docs(ctx):
    """Regenerate module RST docs and render them to HTML."""
    with ctx.cd(DOCS_DIR):
        ctx.run(f"sphinx-apidoc --module-first --no-toc -f -o {DOCS_DIR} {SRC_DIR}")
        ctx.run(f"make html")


@task(pre=[clean])
def build(ctx):
    """Build a wheel into the build directory."""
    with ctx.cd(BASE_DIR):
        ctx.run(f"python setup.py bdist_wheel -d {BUILD_DIR}")


@task()
def upload(ctx):
    """Upload your wheel to artifactory."""
    with ctx.cd(BASE_DIR):
        ctx.run(f"twine upload {BUILD_DIR}/*.whl")
